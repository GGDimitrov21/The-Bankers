const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirm-password");
const showPassword = document.getElementById("show-password");

/* A button in the right end of the password text box. When pressed it shows/hides the password(input) in the text box */
showPassword.addEventListener('click', (event) => {
  if (password.type == 'password')
  {
    password.type = "text";
    confirmPassword.type = "text";
    showPassword.innerText = 'hide';
    showPassword.setAttribute('aria-label', 'hide password');
    showPassword.setAttribute('aria-checked', 'true');
  }
  else
  {
    password.type = "password";
    confirmPassword.type = "password";
    showPassword.innerText = 'show';
    showPassword.setAttribute('aria-label', 'show password');
    showPassword.setAttribute('aria-checked', 'false');
  }
});

/* Validating the password(input) */
confirmPassword.addEventListener("blur", (event) => {
  const value = event.target.value
  
  if (value.length && value != password.value)
    matchPassword.classList.remove('hidden');
  else
    matchPassword.classList.add('hidden');
});

/* Password(input) requirements */
password.addEventListener("input", (event) => {
  const value = event.target.value;
  updateRequirement('length', value.length >= 8);
  updateRequirement('lowercase', [a-z].test(value));
  updateRequirement('uppercase', [A-Z].test(value));
  updateRequirement('number', d.test(value));
  updateRequirement('characters', ["#", "?", "!", "@", "$", "%", "^", "&", "*", "-"].test(value));
});

let first = document.getElementById("firstName");
let last = document.getElementById("lastName");