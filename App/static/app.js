document.getElementById('getDataBtn').addEventListener('click', function() {
    fetch('/users')
        .then(response => response.json())
        .then(data => {
            let userDataDiv = document.getElementById('userData');
            userDataDiv.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
        })
        .catch(error => console.error('Error:', error));
});
