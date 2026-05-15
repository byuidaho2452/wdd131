const video = document.querySelector('#webcam');
const snap = document.querySelector('#snap');
const canvas = document.querySelector('#canvas');

// Start the camera
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => video.srcObject = stream);

snap.addEventListener('click', () => {
    const context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, 320, 240);
    const imageData = canvas.toDataURL('image/png'); // This is your image "data"
    // Now you would send 'imageData' to your Python server!
});