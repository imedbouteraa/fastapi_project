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
        document.getElementById('result').innerHTML = JSON.stringify(result, null, 2);
    } catch (error) {
        console.error("There was an error processing the image!", error);
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
};
