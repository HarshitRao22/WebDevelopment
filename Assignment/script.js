// Smooth scroll navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Navbar background on scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 5px 20px rgba(0, 0, 0, 0.2)';
    } else {
        navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
    }
});

// Form submission
const orderForm = document.querySelector('.order-form form');
if (orderForm) {
    orderForm.addEventListener('submit', (e) => {
        e.preventDefault();
        alert('Thank you for your order! We will process it shortly.');
        orderForm.reset();
    });
}

// Newsletter form
const newsletterForm = document.querySelector('.newsletter-form');
if (newsletterForm) {
    newsletterForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = newsletterForm.querySelector('input[type="email"]');
        if (email.value) {
            alert(`Thank you for subscribing with ${email.value}!`);
            email.value = '';
        }
    });
    
    // Make newsletter button clickable
    const newsletterBtn = document.querySelector('.newsletter .btn');
    if (newsletterBtn) {
        newsletterBtn.addEventListener('click', () => {
            const email = document.querySelector('.newsletter-form input[type="email"]');
            if (email.value) {
                alert(`Thank you for subscribing with ${email.value}!`);
                email.value = '';
            } else {
                alert('Please enter your email address');
            }
        });
    }
}

// Add animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

document.querySelectorAll('.feature-card, .review-card, .location-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'all 0.6s ease';
    observer.observe(el);
});
