document.getElementById('signup-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    alert(`Thank you for signing up, ${email}!`);
    // Here you can add code to handle form submission to your backend
});
