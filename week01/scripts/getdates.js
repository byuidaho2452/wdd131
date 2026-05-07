// --- 1. SET CURRENT YEAR ---
// This grabs the current date from your computer/device
const yearSpan = document.querySelector("#currentyear");
const today = new Date();

// This puts the 4-digit year into the HTML
yearSpan.innerHTML = today.getFullYear();


// --- 2. SET LAST MODIFIED DATE ---
// This built-in property tells us when the file was last saved/uploaded
const lastModSpan = document.querySelector("#lastModified");
lastModSpan.innerHTML = document.lastModified;

// --- 3. CONSOLE LOG TEST ---
// This shows up in your browser's 'Inspect' tool under the 'Console' tab
console.log("Date logic loaded successfully.");

// This creates a clock that updates every 1 second
setInterval(() => {
    const now = new Date();
    // Assuming you add an id="clock" somewhere in your HTML
    const clockElement = document.querySelector("#clock");
    if(clockElement) {
        clockElement.textContent = now.toLocaleTimeString();
    }
}, 1000);