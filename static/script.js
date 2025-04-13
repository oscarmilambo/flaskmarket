document.getElementById('loginForm').addEventListener('submit', function(event) {
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();

    if (!username || !email || !password) {
        event.preventDefault();
        alert('All fields are required!');
            return;
    }
    
        alert('login successfully!');
    });