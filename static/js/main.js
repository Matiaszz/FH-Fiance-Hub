
const navbar = document.querySelector('.navbar');
const themeSwitcherLink = document.getElementById('theme-switcher-link');
const themeIcon = document.getElementById('theme-icon');
const content = document.querySelector('.content');

function switcher() {
    
    console.log("Botão clicado!"); 
    
    if (document.body.classList.contains('dark')) {
        document.body.classList.remove('dark');
        document.body.classList.add('light');
        themeIcon.classList.remove('fa-sun');
        themeIcon.classList.add('fa-moon');
    } else {
        document.body.classList.remove('light');
        document.body.classList.add('dark');
        themeIcon.classList.remove('fa-moon');
        themeIcon.classList.add('fa-sun');
    }
    
}

navbar.addEventListener('mouseenter', () => {
    const texts = document.querySelectorAll('.text');
    texts.forEach(text => {
        text.style.display = 'inline';
    });
});

navbar.addEventListener('mouseleave', () => {
    const texts = document.querySelectorAll('.text');
    texts.forEach(text => {
        text.style.display = 'none';
    });
});