# Define the virtual environment name
$venvName = "venv"

# Check if virtual environment exists
if (Test-Path $venvName) {
    Write-Host "Virtual environment already exists. Activating..."
} else {
    # Create virtual environment if not exists
    python -m venv $venvName
    Write-Host "Virtual environment created."
}

# Activate virtual environment
$activateScript = Join-Path $venvName "Scripts\Activate"
Write-Host "Activating virtual environment..."
& $activateScript

# Install dependencies from requirements.txt
Write-Host "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

Write-Host "Setup completed. Virtual environment activated."
