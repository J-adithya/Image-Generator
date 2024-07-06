async function generateImage() {
    const prompt = document.getElementById('prompt').value;

    // Show loader and hide previous image
    document.getElementById('loader').style.display = 'block';
    const generatedImage = document.getElementById('generated-image');
    generatedImage.style.display = 'none';

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
        generatedImage.src = imageUrl;
        generatedImage.style.display = 'block';

        // Update download button behavior
        const downloadBtn = document.getElementById('download-btn');
        downloadBtn.onclick = () => downloadImage(imageBlob);
    } else {
        alert('Failed to generate image');
    }

    // Hide loader
    document.getElementById('loader').style.display = 'none';
}

function downloadImage(blob) {
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'generated_image.png';
    link.click();
}

function clearPrompt() {
    document.getElementById('prompt').value = '';
    document.getElementById('generated-image').style.display = 'none';
}
