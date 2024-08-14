// health/static/js/script.js
document.getElementById('mentalHealthForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const mood = document.getElementById('mood').value;
    const comments = document.getElementById('comments').value;

    fetch('{% url "submit_form" %}', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: new URLSearchParams({
            'mood': mood,
            'comments': comments
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('responseMessage').innerText = data.message || 'Submission received';
        document.getElementById('mentalHealthForm').reset();
    })
    .catch(error => console.error('Error:', error));
});
