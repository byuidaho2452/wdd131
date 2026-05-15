const bioDisplay = document.querySelector('#user-bio');
const inputField = document.querySelector('#hacker-input');
const attackBtn = document.querySelector('#attack-btn');
const secureBtn = document.querySelector('#secure-btn');

// --- THE DANGEROUS WAY (Vulnerable to XSS) ---
attackBtn.addEventListener('click', () => {
    const dataFromDatabase = inputField.value;
    
    // innerHTML tells the browser: "Execute any code found in this string!"
    bioDisplay.innerHTML = dataFromDatabase;
});

// --- THE BEST PRACTICE WAY (Secure) ---
secureBtn.addEventListener('click', () => {
    const dataFromDatabase = inputField.value;
    
    // textContent tells the browser: "Just draw these symbols. Do NOT execute them."
    bioDisplay.textContent = dataFromDatabase;
});