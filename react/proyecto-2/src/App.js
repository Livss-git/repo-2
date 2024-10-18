document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('error-message');

    errorMessage.style.display = 'none'; // Ocultar mensaje de error anterior

    if (username === '' || password === '') {
        errorMessage.textContent = 'Por favor, complete todos los campos.';
        errorMessage.style.display = 'block';
    } else {
        // Aquí puedes agregar lógica para autenticar al usuario
        alert(`Bienvenido, ${username}!`);
    }
});