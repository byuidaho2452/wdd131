// Store the selectors in variables
const mainnav = document.querySelector('.navigation');
const hambutton = document.querySelector('#menu');

// Add a click event listener to the hamburger button
hambutton.addEventListener('click', () => {
    mainnav.classList.toggle('show');
    hambutton.classList.toggle('show');
});

/* 
Note: In your CSS, you can use the #menu.show::before 
syntax to change the ≡ to an X icon.
*/