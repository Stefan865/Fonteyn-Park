const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const loginForm = document.querySelector('.form-box.login');
const registerForm = document.querySelector('.form-box.register');

registerLink.addEventListener('click', () => {
    wrapper.classList.add('active');
    loginForm.style.opacity = '0';
    loginForm.style.visibility = 'hidden';
    
    registerForm.style.opacity = '1';
    registerForm.style.visibility = 'visible';
});

loginLink.addEventListener('click', () => {
    wrapper.classList.remove('active');
    loginForm.style.opacity = '1';
    loginForm.style.visibility = 'visible';
    
    registerForm.style.opacity = '0';
    registerForm.style.visibility = 'hidden';
});

