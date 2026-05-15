import face_recognition
import cv2
import numpy as np
from scipy.spatial import distance as dist

# 1. Helper function to calculate Eye Aspect Ratio (EAR)
def calculate_ear(eye_points):
    # Vertical distances
    A = dist.euclidean(eye_points[1], eye_points[5])
    B = dist.euclidean(eye_points[2], eye_points[4])
    # Horizontal distance
    C = dist.euclidean(eye_points[0], eye_points[3])
    # The EAR formula
    return (A + B) / (2.0 * C)

# 2. Setup: Load your "Authorized" photo
# MAKE SURE you have a file named 'my_id_photo.jpg' in the same folder!
print("Loading authorized profile...")
try:
    authorized_image = face_recognition.load_image_file("my_id_photo.jpg")
    authorized_encoding = face_recognition.face_encodings(authorized_image)[0]
    print("Profile loaded successfully.")
except Exception as e:
    print(f"Error: Could not load 'my_id_photo.jpg'. {e}")
    exit()

# 3. Initialize Camera and Blink Tracking
video_capture = cv2.VideoCapture(0)
blink_counter = 0
eye_closed = False

print("Starting Camera... Press 'q' to quit.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert the image from BGR (OpenCV style) to RGB (face_recognition style)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Find all facial landmarks in the current frame
    face_landmarks_list = face_recognition.face_landmarks(rgb_frame)

    for landmarks in face_landmarks_list:
        left_eye = landmarks['left_eye']
        right_eye = landmarks['right_eye']
        
        # Calculate EAR for both eyes
        ear = (calculate_ear(left_eye) + calculate_ear(right_eye)) / 2.0
        
        # Blink Logic: If EAR is low, the eye is closed
        if ear < 0.20:
            if not eye_closed:
                eye_closed = True
                blink_counter += 1
                print(f"Blink detected! Count: {blink_counter}")
        else:
            eye_closed = False

    # Once 3 blinks are recorded, check the identity
    if blink_counter >= 3:
        print("Liveness confirmed! Verifying identity...")
        current_encodings = face_recognition.face_encodings(rgb_frame)
        
        if current_encodings:
            match = face_recognition.compare_faces([authorized_encoding], current_encodings[0])
            if match[0]:
                print("--- ACCESS GRANTED: Welcome to RedmanFinance ---")
                # Add a label to the screen
                cv2.putText(frame, "VERIFIED", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                print("--- ACCESS DENIED: Face does not match ID ---")
                cv2.putText(frame, "UNAUTHORIZED", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Reset counter after an attempt
        blink_counter = 0

    # Display the result
    cv2.imshow('RedmanFinance Biometric Login', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video_capture.release()
cv2.destroyAllWindows()