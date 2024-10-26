// Smooth scroll for the 'Explore Features' button
document.querySelector('.hero-button').addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector('#features').scrollIntoView({
        behavior: 'smooth'
    });
});
