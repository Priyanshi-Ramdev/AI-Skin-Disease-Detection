/* app/static/js/script.js */

const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const previewImg = document.getElementById('preview-img');
const promptText = document.getElementById('drop-zone-prompt');
const analyzeBtn = document.getElementById('analyze-btn');
const resultsSection = document.getElementById('results-section');
const loader = document.getElementById('loader');
const downloadBtn = document.getElementById('download-btn');

let currentPredictionData = null;

// Elements for Results
const resDisease = document.getElementById('res-disease');
const resDesc = document.getElementById('res-desc');
const resConf = document.getElementById('res-conf');
const confFill = document.getElementById('conf-fill');
const resMedicated = document.getElementById('res-medicated');
const resHerbal = document.getElementById('res-herbal');
const resLifestyle = document.getElementById('res-lifestyle');
const resSkinAdvice = document.getElementById('res-skin-advice');

// Trigger file input on click
dropZone.addEventListener('click', () => fileInput.click());

// Drag & Drop handling
dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('active');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('active');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('active');
    const files = e.dataTransfer.files;
    if (files.length) handleFile(files[0]);
});

fileInput.addEventListener('change', () => {
    if (fileInput.files.length) handleFile(fileInput.files[0]);
});

let selectedFile = null;

function handleFile(file) {
    if (!file.type.startsWith('image/')) {
        alert('Please upload an image file.');
        return;
    }

    selectedFile = file;
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImg.src = e.target.result;
        previewImg.style.display = 'block';
        promptText.style.display = 'none';
        analyzeBtn.disabled = false;
    };
    reader.readAsDataURL(file);
}

analyzeBtn.addEventListener('click', async () => {
    if (!selectedFile) return;

    const skinType = document.getElementById('skin-type').value;
    const formData = new FormData();
    formData.append('file', selectedFile);
    formData.append('skin_type', skinType);

    // Reset UI
    resultsSection.style.display = 'none';
    loader.style.display = 'block';
    analyzeBtn.disabled = true;

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        if (data.error) throw new Error(data.error);

        displayResults(data);
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        loader.style.display = 'none';
        analyzeBtn.disabled = false;
    }
});

function displayResults(data) {
    currentPredictionData = data; // Store for PDF generation
    resDisease.innerText = data.disease;
    resDesc.innerText = data.description;
    resConf.innerText = data.confidence;
    confFill.style.width = data.confidence;
    
    // Clear lists
    resMedicated.innerHTML = '';
    resHerbal.innerHTML = '';

    data.medicated.forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `<i class="fas fa-check" style="color: #ff00cc; margin-right: 10px;"></i> ${item}`;
        resMedicated.appendChild(li);
    });

    data.herbal.forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `<i class="fas fa-check" style="color: #ff00cc; margin-right: 10px;"></i> ${item}`;
        resHerbal.appendChild(li);
    });

    resLifestyle.innerText = data.lifestyle;
    resSkinAdvice.innerText = data.skin_advice;

    // Show results with animation
    resultsSection.style.display = 'flex';
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}

downloadBtn.addEventListener('click', async () => {
    if (!currentPredictionData) return;

    try {
        const response = await fetch('/download_report', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(currentPredictionData)
        });

        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `DermAI_Report_${new Date().getTime()}.pdf`;
            document.body.appendChild(a);
            a.click();
            a.remove();
        } else {
            alert('Failed to generate report.');
        }
    } catch (error) {
        alert('Error: ' + error.message);
    }
});
