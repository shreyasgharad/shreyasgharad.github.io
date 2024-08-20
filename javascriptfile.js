// scripts.js
document.addEventListener('DOMContentLoaded', function() {
    // Example animation: Fade in the main content
    const mainContent = document.querySelector('main');
    mainContent.style.opacity = 0;
    setTimeout(() => {
        mainContent.style.transition = 'opacity 1s';
        mainContent.style.opacity = 1;
    }, 100);
});