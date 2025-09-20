// Alterna o ícone do menu e a barra de navegação
let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menuIcon.onclick = () => {
    menuIcon.classList.toggle('fa-xmark'); // Opcional: muda o ícone para um 'X'
    navbar.classList.toggle('active');
};

// Destaca o link ativo ao rolar a página
window.onscroll = () => {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('header nav a');

    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150; // Deslocamento para acionar o destaque mais cedo
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if (top >= offset && top < offset + height) {
            navLinks.forEach(link => {
                link.classList.remove('active');
            });
            // Usa um seletor mais específico para evitar erros
            const activeLink = document.querySelector(`header nav a[href*=${id}]`);
            if (activeLink) {
                activeLink.classList.add('active');
            }
        }
    });

    // Remove o ícone e a barra de navegação ao clicar em um link (para rolagem suave)
    menuIcon.classList.remove('fa-xmark');
    navbar.classList.remove('active');
};

// Executa o código quando o DOM estiver totalmente carregado
document.addEventListener('DOMContentLoaded', function() {

    // --- Lógica para Navegação e Links ---
    const links = document.querySelectorAll('a[href^="#"]');
    for (const link of links) {
        link.addEventListener('click', function(e) {
            // Lógica para lidar com a classe ativa no clique para feedback imediato
            const navLinks = document.querySelectorAll('header nav a');
            navLinks.forEach(navLink => navLink.classList.remove('active'));
            
            // Verifica se o link clicado está na barra de navegação antes de adicionar a classe ativa
            if(Array.from(navLinks).includes(this)){
                this.classList.add('active');
            }
        });
    }

    // --- Lógica para Animações com ScrollReveal ---
    const sr = ScrollReveal({
        distance: '60px', // Uma distância um pouco menor
        duration: 1000, // Animação mais rápida (1 segundo)
        delay: 100,      // Atraso menor
        reset: true
    });

    // Anima a Seção de Início
    sr.reveal('.hero-content', { origin: 'top' });

    // Anima os Títulos das Seções
    sr.reveal('.section-title', { origin: 'top' });
    sr.reveal('.section-subtitle', { origin: 'bottom' });

    // Anima Competências, Experiência e Formação
    sr.reveal('.skills-columns-container', { origin: 'left' });
    sr.reveal('.experience-item', { origin: 'right' });
    sr.reveal('.education-content', { origin: 'left' });

    // Anima os Cards de Projeto (com atraso entre eles)
    sr.reveal('.project-card', { origin: 'bottom', interval: 200 });

    // Anima a Seção de Contato
    sr.reveal('.contact-links', { origin: 'bottom' });
});

