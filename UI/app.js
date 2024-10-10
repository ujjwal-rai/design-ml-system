const express = require('express');
const multer = require('multer');
const { exec } = require('child_process');
const path = require('path');
const app = express();

// Set up static files to serve HTML
app.use(express.static('public'));

// Set up multer for file uploads
const upload = multer({ dest: 'uploads/' });

// Route to handle file upload
app.post('/upload', upload.fields([{ name: 'dataset' }, { name: 'features' }]), (req, res) => {
    const datasetPath = req.files['dataset'][0].path;
    const featuresPath = req.files['features'][0].path;

    // Execute the Python script for logistic regression
    exec(`python logistic_regression.py ${datasetPath} ${featuresPath}`, (error, stdout, stderr) => {
        if (error) {
            return res.status(500).send(`Error: ${stderr}`);
        }
        res.send(`<h3>Logistic Regression Results:</h3><pre>${stdout}</pre>`);
    });
});

// Start server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
