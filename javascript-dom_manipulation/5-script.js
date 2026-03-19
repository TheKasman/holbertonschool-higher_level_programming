document.addEventListener('DOMContentLoaded', () => {
  const header = document.getElementById('update_header');
  
  header.addEventListener('click', () => {
    header.textContent = 'New Header!!!';
  });
});