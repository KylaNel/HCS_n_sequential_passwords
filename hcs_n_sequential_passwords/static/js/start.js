let startTime, endTime;
let currentStep = 0;
const errorMessages = document.getElementById('errorMessages');
const passwordInputDiv = document.getElementById('passwordInput');
const pinInputDiv = document.getElementById('pinInput');
const patternInputDiv = document.getElementById('patternInput');
const timerDisplay = document.getElementById('timer');
const setPasswordBtn = document.getElementById('setPasswordBtn');
const setPinBtn = document.getElementById('setPinBtn');
const setPatternBtn = document.getElementById('setPatternBtn');
const passwordSubmitBtn = document.getElementById('passwordSubmitBtn');
const pinSubmitBtn = document.getElementById('pinSubmitBtn');
const startTimerBtn = document.getElementById('startTimerBtn');

setPasswordBtn.addEventListener('click', () => {
  const newPassword = prompt("Enter the new password:");
  if (newPassword) {
    localStorage.setItem('password', newPassword);
  }
});

setPinBtn.addEventListener('click', () => {
  const newPin = prompt("Enter the new PIN:");
  if (newPin) {
    localStorage.setItem('pin', newPin);
  }
});

startTimerBtn.addEventListener('click', () => {
  startTimerBtn.style.display = 'none';
  showStep(currentStep);
  startTime = new Date().getTime();
});

passwordSubmitBtn.addEventListener('click', () => {
  const enteredPassword = document.getElementById('passwordField').value.trim();
  const correctPassword = localStorage.getItem('password') || "password123";
  if (enteredPassword === correctPassword) {
    currentStep++;
    showStep(currentStep);
  } else {
    errorMessages.textContent = "Incorrect password. Please try again.";
  }
});

pinSubmitBtn.addEventListener('click', () => {
  const enteredPin = document.getElementById('pinField').value.trim();
  const correctPin = localStorage.getItem('pin') || "1234";
  if (enteredPin === correctPin) {
    currentStep++;
    showStep(currentStep);
  } else {
    errorMessages.textContent = "Incorrect PIN. Please try again.";
  }
});


function showStep(step) {
  switch (step) {
    case 0:
      passwordInputDiv.style.display = 'block';
      break;
    case 1:
      passwordInputDiv.style.display = 'none';
      pinInputDiv.style.display = 'block';
      break;
    case 2:
      pinInputDiv.style.display = 'none';
      patternInputDiv.style.display = 'block';
      break;
  }
}

function displayTime(milliseconds) {
  const minutes = Math.floor(milliseconds / 60000);
  const seconds = ((milliseconds % 60000) / 1000).toFixed(2);
  timerDisplay.innerHTML = `Elapsed Time: ${minutes}:${(seconds < 10 ? '0' : '')}${seconds}`;
  timerDisplay.style.display = 'block';
}
