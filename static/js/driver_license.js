document.getElementById('ocr-form').onsubmit = async function(e) {
    e.preventDefault();
    document.getElementById('loading').style.display = 'block';

    const formData = new FormData();
    const fileInput = document.getElementById('image');
    console.log('Selected file:', fileInput.files[0]);

    formData.append("image", fileInput.files[0]);

    try {
        const response = await fetch('/api/ocr/driver_license/', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const result = await response.json();
            console.log('API response:', result);
            document.getElementById('result').innerHTML = formatResultAsTable(result);
        } else {
            console.error('Server error:', response.statusText);
            alert('There was an error processing your request. Please try again.');
        }
    } catch (error) {
        console.error("There was an error processing the image!", error);
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
};

function formatResultAsTable(data) {
    let table = '<table class="result-table">';
    table += '<tr><th>Field</th><th>Value</th></tr>';
    for (const key in data) {
        if (data.hasOwnProperty(key)) {
            table += `<tr><td>${key.replace('_', ' ').toUpperCase()}</td><td>${data[key]}</td></tr>`;
        }
    }
    table += '</table>';
    return table;
}
