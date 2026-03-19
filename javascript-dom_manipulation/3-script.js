document.addEventListener('DOMContentLoaded', () => {
  const toggleHeader = document.getElementById('toggle_header');
  const header = document.querySelector('header');
    
  toggleHeader.addEventListener('click', () => {
    if(header.classList.contains('green')) {
      header.classList.replace('green', 'red');
    } else {
      header.classList.replace('red', 'green');
    }
  });
});