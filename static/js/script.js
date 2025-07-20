// Custom JavaScript for Disease Prediction System

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add loading animation to buttons
    function addLoadingToButton(button) {
        const originalText = button.innerHTML;
        button.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Processing...';
        button.disabled = true;
        
        return function() {
            button.innerHTML = originalText;
            button.disabled = false;
        };
    }

    // Tooltip initialization
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
        alerts.forEach(alert => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Add animation classes to elements when they come into view
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, observerOptions);

    // Observe all cards and feature elements
    document.querySelectorAll('.card, .feature-card').forEach(el => {
        observer.observe(el);
    });

    // Back to top button
    const backToTopButton = createBackToTopButton();
    
    function createBackToTopButton() {
        const button = document.createElement('button');
        button.innerHTML = '<i class="fas fa-chevron-up"></i>';
        button.className = 'btn btn-primary position-fixed';
        button.style.cssText = `
            bottom: 20px;
            right: 20px;
            z-index: 1000;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: none;
            box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3);
        `;
        
        button.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
        
        document.body.appendChild(button);
        return button;
    }

    // Show/hide back to top button
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });

    // Enhanced form validation
    function validateForm(form) {
        let isValid = true;
        const requiredFields = form.querySelectorAll('[required]');
        
        requiredFields.forEach(field => {
            if (!field.value.trim()) {
                isValid = false;
                field.classList.add('is-invalid');
                
                // Remove invalid class after user starts typing
                field.addEventListener('input', function() {
                    this.classList.remove('is-invalid');
                }, { once: true });
            }
        });
        
        return isValid;
    }

    // Add form validation to all forms
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
                showNotification('Please fill in all required fields.', 'warning');
            }
        });
    });

    // Notification system
    function showNotification(message, type = 'info', duration = 5000) {
        const notification = document.createElement('div');
        notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
        notification.style.cssText = `
            top: 20px;
            right: 20px;
            z-index: 1050;
            max-width: 300px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        `;
        
        notification.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        
        document.body.appendChild(notification);
        
        // Auto remove after duration
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, duration);
    }

    // Local storage helpers
    const storage = {
        set: function(key, value) {
            try {
                localStorage.setItem(key, JSON.stringify(value));
            } catch (e) {
                console.warn('Local storage not available');
            }
        },
        
        get: function(key) {
            try {
                const item = localStorage.getItem(key);
                return item ? JSON.parse(item) : null;
            } catch (e) {
                console.warn('Local storage not available');
                return null;
            }
        },
        
        remove: function(key) {
            try {
                localStorage.removeItem(key);
            } catch (e) {
                console.warn('Local storage not available');
            }
        }
    };

    // Save user preferences
    function saveUserPreferences() {
        const preferences = {
            lastSymptoms: getSelectedSymptoms(),
            timestamp: new Date().getTime()
        };
        storage.set('userPreferences', preferences);
    }

    // Load user preferences
    function loadUserPreferences() {
        const preferences = storage.get('userPreferences');
        if (preferences && preferences.lastSymptoms) {
            // Check if preferences are less than 24 hours old
            const oneDay = 24 * 60 * 60 * 1000;
            if (new Date().getTime() - preferences.timestamp < oneDay) {
                return preferences.lastSymptoms;
            }
        }
        return [];
    }

    // Get selected symptoms
    function getSelectedSymptoms() {
        const checkboxes = document.querySelectorAll('input[name="symptoms"]:checked');
        return Array.from(checkboxes).map(cb => cb.value);
    }

    // Enhanced search functionality
    function enhancedSymptomSearch() {
        const searchInput = document.getElementById('symptomSearch');
        if (!searchInput) return;

        let searchTimeout;
        
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                const searchTerm = this.value.toLowerCase().trim();
                filterSymptoms(searchTerm);
            }, 300); // Debounce search
        });
    }

    function filterSymptoms(searchTerm) {
        const symptomsContainer = document.getElementById('symptomsContainer');
        if (!symptomsContainer) return;

        const symptomItems = symptomsContainer.querySelectorAll('.symptom-item');
        let visibleCount = 0;
        
        symptomItems.forEach(item => {
            const label = item.querySelector('label');
            if (!label) return;
            
            const labelText = label.textContent.toLowerCase();
            const isVisible = !searchTerm || labelText.includes(searchTerm);
            
            item.style.display = isVisible ? 'flex' : 'none';
            if (isVisible) visibleCount++;
        });

        // Show "no results" message if needed
        showNoResultsMessage(visibleCount === 0 && searchTerm);
    }

    function showNoResultsMessage(show) {
        const symptomsContainer = document.getElementById('symptomsContainer');
        if (!symptomsContainer) return;

        let noResultsMsg = symptomsContainer.querySelector('.no-results-message');
        
        if (show && !noResultsMsg) {
            noResultsMsg = document.createElement('div');
            noResultsMsg.className = 'no-results-message text-center text-muted py-3';
            noResultsMsg.innerHTML = '<i class="fas fa-search me-2"></i>No symptoms found matching your search.';
            symptomsContainer.appendChild(noResultsMsg);
        } else if (!show && noResultsMsg) {
            noResultsMsg.remove();
        }
    }

    // Initialize enhanced search
    enhancedSymptomSearch();

    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + Enter to submit form
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
            const activeForm = document.querySelector('form:focus-within');
            if (activeForm) {
                const submitButton = activeForm.querySelector('button[type="submit"]');
                if (submitButton) {
                    submitButton.click();
                }
            }
        }
        
        // Escape to clear search
        if (e.key === 'Escape') {
            const searchInput = document.getElementById('symptomSearch');
            if (searchInput && document.activeElement === searchInput) {
                searchInput.value = '';
                filterSymptoms('');
            }
        }
    });

    // Performance monitoring
    if ('performance' in window) {
        window.addEventListener('load', function() {
            setTimeout(function() {
                const perfData = performance.getEntriesByType('navigation')[0];
                if (perfData) {
                    console.log('Page load time:', Math.round(perfData.loadEventEnd - perfData.fetchStart), 'ms');
                }
            }, 0);
        });
    }

    // Error handling for fetch requests
    window.fetchWithErrorHandling = function(url, options = {}) {
        return fetch(url, {
            ...options,
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .catch(error => {
            console.error('Fetch error:', error);
            showNotification('Network error. Please check your connection.', 'danger');
            throw error;
        });
    };

    // Print functionality
    window.printResults = function() {
        const resultsSection = document.getElementById('resultsSection');
        if (!resultsSection || resultsSection.style.display === 'none') {
            showNotification('No results to print. Please make a prediction first.', 'warning');
            return;
        }

        const printWindow = window.open('', '_blank');
        const styles = Array.from(document.querySelectorAll('link[rel="stylesheet"], style'))
            .map(link => link.outerHTML || `<style>${link.innerHTML}</style>`)
            .join('');

        printWindow.document.write(`
            <!DOCTYPE html>
            <html>
            <head>
                <title>Disease Prediction Results</title>
                ${styles}
                <style>
                    body { background: white !important; }
                    .btn, .navbar, footer { display: none !important; }
                    @media print {
                        .no-print { display: none !important; }
                    }
                </style>
            </head>
            <body>
                <div class="container mt-4">
                    <h1 class="text-center mb-4">Disease Prediction Results</h1>
                    ${resultsSection.innerHTML}
                    <div class="text-center mt-4">
                        <small class="text-muted">Generated on ${new Date().toLocaleString()}</small>
                    </div>
                </div>
            </body>
            </html>
        `);
        
        printWindow.document.close();
        printWindow.focus();
        
        setTimeout(() => {
            printWindow.print();
            printWindow.close();
        }, 500);
    };

    // Export functionality
    window.exportResults = function(format = 'json') {
        const resultsSection = document.getElementById('resultsSection');
        if (!resultsSection || resultsSection.style.display === 'none') {
            showNotification('No results to export. Please make a prediction first.', 'warning');
            return;
        }

        // This would need to be implemented based on the last prediction data
        showNotification('Export functionality coming soon!', 'info');
    };

    console.log('Disease Prediction System initialized successfully!');
});

// Global utility functions
window.utils = {
    debounce: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    throttle: function(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    },
    
    formatDate: function(date) {
        return new Intl.DateTimeFormat('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        }).format(new Date(date));
    }
};
