document.addEventListener('DOMContentLoaded', () => {
    const helloDiv = document.getElementById('hello'); // grab the element

    fetch('https://hellosalut.stefanbohacek.com/?lang=fr') // fetch the API
        .then(response => response.json())                // parse JSON
        .then(data => {
            helloDiv.textContent = data.hello;           // set the translation
        })
        .catch(error => console.error('Error fetching hello:', error));
});