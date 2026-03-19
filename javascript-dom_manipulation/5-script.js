document.addEventListener('DOMContentLoaded', () => {
  const div = document.getElementById('update_header'); // the clickable div
  const header = document.querySelector('header');      // the header to update

  div.addEventListener('click', () => {
    header.textContent = 'New Header!!!';
  });
});