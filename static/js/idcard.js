document.getElementById('ocr-form').onsubmit = async function(e) {
    e.preventDefault();
    document.getElementById('loading').style.display = 'block';

    const formData = new FormData();
    formData.append("image", document.getElementById('image').files[0]);

    try {
        const response = await fetch('/api/ocr/idcard/', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        document.getElementById('result').innerHTML = formatResultAsTable(result);
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

