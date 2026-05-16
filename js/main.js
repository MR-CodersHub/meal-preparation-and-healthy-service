// FuelUp Advanced Frontend Features

document.addEventListener('DOMContentLoaded', () => {
    // 1. Theme Toggle Logic
    const themeToggle = document.createElement('div');
    themeToggle.className = 'theme-controls';
    themeToggle.innerHTML = `
        <button id="theme-btn" aria-label="Toggle Dark/Light Mode"><i class="fas fa-moon"></i></button>
    `;
    const navBtns = document.querySelector('.nav-btns');
    if (navBtns) navBtns.prepend(themeToggle);

    const themeBtn = document.getElementById('theme-btn');
    const html = document.documentElement;

    const setTheme = (theme) => {
        html.setAttribute('data-theme', theme);
        if (themeBtn) themeBtn.innerHTML = theme === 'dark' ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
        localStorage.setItem('theme', theme);
    };

    setTheme(localStorage.getItem('theme') || 'dark');

    if (themeBtn) themeBtn.addEventListener('click', () => setTheme(html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark'));

    // 2. Profile Dropdown Logic
    const initProfileDropdowns = () => {
        const containers = document.querySelectorAll('.profile-dropdown');
        
        containers.forEach(container => {
            const btn = container.querySelector('.profile-btn');
            const menu = container.querySelector('.dropdown-menu');
            
            if (!btn || !menu) return;

            btn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                
                // Close others
                document.querySelectorAll('.dropdown-menu').forEach(m => {
                    if (m !== menu) m.classList.remove('active');
                });

                menu.classList.toggle('active');
            });

            // Close on item click
            menu.querySelectorAll('.dropdown-item').forEach(item => {
                item.addEventListener('click', () => menu.classList.remove('active'));
            });
        });

        // Close all on outside click
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.profile-dropdown')) {
                document.querySelectorAll('.dropdown-menu').forEach(m => m.classList.remove('active'));
            }
        });
    };

    initProfileDropdowns();

    // 3. Form Validation Logic
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            let isValid = true;
            const inputs = form.querySelectorAll('input[required], textarea[required]');
            inputs.forEach(input => {
                const existingError = input.parentElement.querySelector('.error-msg');
                if (existingError) existingError.remove();
                if (!input.value.trim()) {
                    isValid = false;
                    showError(input, 'This field is required');
                }
            });
            if (!isValid) e.preventDefault();
        });
    });

    function showError(input, msg) {
        input.style.borderColor = '#ff4d4d';
        const error = document.createElement('span');
        error.className = 'error-msg';
        error.style.color = '#ff4d4d';
        error.style.fontSize = '0.75rem';
        error.innerText = msg;
        input.parentElement.appendChild(error);
    }

    // 4. Skeleton Loading Simulation (only on first load of specific pages)
    const dynamicSections = document.querySelectorAll('.meal-grid, .blog-grid');
    if (dynamicSections.length > 0) {
        dynamicSections.forEach(section => {
            const originalContent = section.innerHTML;
            section.innerHTML = '';
            for (let i = 0; i < 3; i++) {
                const skel = document.createElement('div');
                skel.className = 'meal-card skeleton-card';
                skel.innerHTML = `
                    <div class="skeleton" style="height: 200px; margin-bottom: 20px;"></div>
                    <div class="skeleton" style="height: 20px; width: 70%; margin-bottom: 10px;"></div>
                    <div class="skeleton" style="height: 15px; width: 40%;"></div>
                `;
                section.appendChild(skel);
            }
            setTimeout(() => { section.innerHTML = originalContent; }, 1200);
        });
    }

    // 5. Header Scroll Effect
    const header = document.getElementById('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) header?.classList.add('scrolled');
        else header?.classList.remove('scrolled');
    });

    // 6. AOS Init
    if (typeof AOS !== 'undefined') AOS.init({ duration: 800, once: true });

    // 7. Global Cart Logic
    const initCart = () => {
        const cart = JSON.parse(localStorage.getItem('cart') || '[]');
        const count = cart.reduce((acc, item) => acc + item.quantity, 0);
        document.querySelectorAll('.cart-count').forEach(el => el.innerText = count);
    };

    window.addToCart = (id, name, price, image, desc) => {
        let cart = JSON.parse(localStorage.getItem('cart') || '[]');
        const existingItem = cart.find(item => item.id === id);

        if (existingItem) {
            existingItem.quantity += 1;
        } else {
            cart.push({ id, name, price, image, desc, quantity: 1 });
        }

        localStorage.setItem('cart', JSON.stringify(cart));
        initCart();

        // Show Toast Notification
        showToast(`${name} added to cart!`);
    };

    function showToast(msg) {
        const toast = document.createElement('div');
        toast.className = 'glass';
        toast.style.cssText = `
            position: fixed; bottom: 30px; right: 30px; 
            padding: 15px 30px; border-radius: 12px; 
            border: 1px solid var(--primary); z-index: 3000;
            animation: slideIn 0.3s ease-out; background: var(--bg-card);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        `;
        toast.innerHTML = `<i class="fas fa-check-circle" style="color: #4caf50; margin-right: 10px;"></i> ${msg}`;
        document.body.appendChild(toast);

        setTimeout(() => {
            toast.style.animation = 'slideOut 0.3s ease-in forwards';
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }

    // Add styles for toast animations
    const style = document.createElement('style');
    style.innerHTML = `
        @keyframes slideIn { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
        @keyframes slideOut { from { transform: translateX(0); opacity: 1; } to { transform: translateX(100%); opacity: 0; } }
    `;
    document.head.appendChild(style);

    // 8. Mobile Menu Toggle (Robust Version)
    const initMobileMenu = () => {
        const menuToggle = document.querySelector('.menu-toggle');
        const navLinks = document.querySelector('.nav-links');

        if (menuToggle && navLinks) {
            menuToggle.addEventListener('click', (e) => {
                e.stopPropagation();
                navLinks.classList.toggle('active');
                const icon = menuToggle.querySelector('i');
                if (icon) {
                    icon.classList.toggle('fa-bars');
                    icon.classList.toggle('fa-times');
                }
            });

            // Close menu when clicking outside
            document.addEventListener('click', (e) => {
                if (navLinks.classList.contains('active') && !navLinks.contains(e.target) && !menuToggle.contains(e.target)) {
                    navLinks.classList.remove('active');
                    const icon = menuToggle.querySelector('i');
                    if (icon) {
                        icon.classList.add('fa-bars');
                        icon.classList.remove('fa-times');
                    }
                }
            });

            // Close menu when clicking links (mobile)
            navLinks.querySelectorAll('a').forEach(link => {
                link.addEventListener('click', () => {
                    navLinks.classList.remove('active');
                    const icon = menuToggle.querySelector('i');
                    if (icon) {
                        icon.classList.add('fa-bars');
                        icon.classList.remove('fa-times');
                    }
                });
            });
        }
    };

    initMobileMenu();

    // 9. Dashboard Sidebar Toggle
    const dashToggle = document.querySelector('.dash-toggle');
    const sidebar = document.querySelector('.sidebar');
    const sidebarOverlay = document.querySelector('.sidebar-overlay');

    if (dashToggle && sidebar) {
        const toggleSidebar = (e) => {
            if (e) e.stopPropagation();
            sidebar.classList.toggle('active');
            sidebarOverlay?.classList.toggle('active');
        };

        dashToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            toggleSidebar();
        });

        sidebarOverlay?.addEventListener('click', toggleSidebar);

        // Close on link click (mobile)
        sidebar.querySelectorAll('.nav-item').forEach(item => {
            item.addEventListener('click', () => {
                if (window.innerWidth <= 992) toggleSidebar();
            });
        });
    }

    initCart();
});
