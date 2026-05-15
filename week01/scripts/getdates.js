const yearSpan = document.querySelector("#currentyear");

const today = new Date();


yearSpan.innerHTML = today.getFullYear();



const lastModSpan = document.querySelector("#lastModified");
lastModSpan.innerHTML = document.lastModified;


console.log("Date logic loaded successfully.");


setInterval(() => {
    const now = new Date();
    
    const clockElement = document.querySelector("#clock");
    if(clockElement) {
        clockElement.textContent = now.toLocaleTimeString();
    }
}, 1000);