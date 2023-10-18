const form = document.querySelector('form');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const email = document.querySelector('#email').value;
  const password = document.querySelector('#password').value;
  // Aquí puedes agregar la lógica para hacer la verificación del usuario en la base de datos
  console.log(`Email: ${email}, Password: ${password}`);
});
