// scripts.js for Marabo Waste Learning

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // 1. Loading Animation
    initLoadingAnimation();
    
    // 2. Smooth Scrolling for Anchor Links
    initSmoothScrolling();
    
    // 3. Animate Elements on Scroll
    initScrollAnimations();
    
    // 4. Interactive Card Hover Effects
    initCardInteractions();
    
    // 5. Mobile Menu Toggle
    initMobileMenu();
    
    // 6. Form Validation (if forms exist)
    initFormValidation();
});

// ======================
// 1. Loading Animation
// ======================
function initLoadingAnimation() {
    // Create loading overlay
    const loadingOverlay = document.createElement('div');
    loadingOverlay.className = 'loading-overlay';
    loadingOverlay.innerHTML = `
        <div class="loading-spinner">
            <div class="spinner-border text-success" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-3">Loading Marabo Waste Learning...</p>
        </div>
    `;
    document.body.prepend(loadingOverlay);
    
    // Remove loader when page is fully loaded
    window.addEventListener('load', function() {
        setTimeout(function() {
            loadingOverlay.style.opacity = '0';
            setTimeout(function() {
                loadingOverlay.remove();
                document.body.classList.add('loaded');
            }, 500);
        }, 1000); // Minimum 1 second loading time
    });
}

// ======================
// 2. Smooth Scrolling
// ======================
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ======================
// 3. Scroll Animations
// ======================
function initScrollAnimations() {
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.animate-on-scroll');
        
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementPosition < windowHeight - 100) {
                element.classList.add('animated');
            }
        });
    };
    
    // Set up observer for modern browsers
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });
        
        document.querySelectorAll('.animate-on-scroll').forEach(element => {
            observer.observe(element);
        });
    } else {
        // Fallback for older browsers
        window.addEventListener('scroll', animateOnScroll);
        animateOnScroll(); // Run once on load
    }
}

// ======================
// 4. Card Interactions
// ======================
function initCardInteractions() {
    const cards = document.querySelectorAll('.card');
    
    cards.forEach(card => {
        // Add hover class on mouseenter
        card.addEventListener('mouseenter', function() {
            this.classList.add('hover');
        });
        
        // Remove hover class on mouseleave
        card.addEventListener('mouseleave', function() {
            this.classList.remove('hover');
        });
        
        // Handle click/tap for mobile
        card.addEventListener('click', function() {
            window.location = this.querySelector('a').href;
        });
    });
}

// ======================
// 5. Mobile Menu Toggle
// ======================
function initMobileMenu() {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', function() {
            navbarCollapse.classList.toggle('show');
            this.setAttribute('aria-expanded', navbarCollapse.classList.contains('show'));
        });
        
        // Close menu when clicking a link
        document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
            link.addEventListener('click', function() {
                if (navbarCollapse.classList.contains('show')) {
                    navbarToggler.click();
                }
            });
        });
    }
}

// ======================
// 6. Form Validation
// ======================
function initFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            let isValid = true;
            const inputs = this.querySelectorAll('input[required], textarea[required]');
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('is-invalid');
                    
                    // Remove invalid class when user starts typing
                    input.addEventListener('input', function() {
                        if (this.value.trim()) {
                            this.classList.remove('is-invalid');
                        }
                    });
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                this.querySelector('.is-invalid').focus();
            }
        });
    });
}

// ======================
// Utility Functions
// ======================
function debounce(func, wait = 100) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => {
            func.apply(this, args);
        }, wait);
    };
}


//About page functionality //

// Document ready function
document.addEventListener('DOMContentLoaded', function() {
    // Set current year in footer
    document.getElementById('currentYear').textContent = new Date().getFullYear();

    // Smooth scrolling for anchor links
    document.querySelectorAll('a.scroll-to').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Newsletter form submission
    const newsletterForm = document.getElementById('newsletterForm');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const emailInput = this.querySelector('input[type="email"]');
            const email = emailInput.value.trim();
            
            if (email) {
                // Here you would typically send the data to your server
                console.log('Subscribing email:', email);
                alert('Thank you for subscribing to our newsletter!');
                this.reset();
            }
        });
    }

    // Login button functionality
    const loginBtn = document.getElementById('loginBtn');
    if (loginBtn) {
        loginBtn.addEventListener('click', function() {
            // Redirect to login page or show modal
            window.location.href = '/login';
        });
    }

    // Initialize any other core functionality here
});