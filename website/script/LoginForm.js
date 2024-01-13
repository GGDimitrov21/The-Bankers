document.getElementById('registerForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const registerUsername = document.getElementById('registerUsername').value;
  const registerPassword = document.getElementById('registerPassword').value;

  const existingData = localStorage.getItem('fileData') || 'Usernames:\tPasswords:\n';

  if (existingData.includes(registerUsername)) {
    alert('This data already exists.');
  } else {
    const newData = `${existingData}${registerUsername}\t${registerPassword}\n`;
    localStorage.setItem('fileData', newData);
    alert('Registration was successful.');
  }
});

document.getElementById('loginForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const loginUsername = document.getElementById('loginUsername').value;
  const loginPassword = document.getElementById('loginPassword').value;

  const existingData = localStorage.getItem('fileData') || 'Usernames:\tPasswords:\n';
  const users = existingData.split('\n').slice(1).map(row => row.split('\t'));

  let found = false;
  for (const user of users) {
    if (user[0] === loginUsername && user[1] === loginPassword) {
      found = true;
      break;
    }
  }

  if (found) {
    alert('Login successful!');
    window.location.href = '/profilePage.html';
  } else {
    alert('Wrong username or password.');
  }
});