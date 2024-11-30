const navbar = document.querySelector('.navbar');

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