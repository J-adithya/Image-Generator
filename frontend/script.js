async function generateImage() {
    const prompt = document.getElementById('prompt').value;
    const response = await fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: prompt }),
    });

    if (response.ok) {
        const imageBlob = await response.blob();
        const imageUrl = URL.createObjectURL(imageBlob);
        document.getElementById('image-container').innerHTML = `<img src="${imageUrl}" alt="Generated Image">`;

        // Display the download button
        const downloadBtn = document.getElementById('download-btn');
        downloadBtn.style.display = 'block';
        downloadBtn.onclick = () => downloadImage(imageBlob);
    } else {
        alert('Failed to generate image');
    }
}

function downloadImage(blob) {
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'generated_image.png';
    link.click();
}

function clearPrompt() {
    document.getElementById('prompt').value = '';
}
