# Setup Instructions for Quantum Practice Project

## Installing Python

1. Download Python from the [official website](https://www.python.org/downloads/)
   - Choose the latest version (3.10+ recommended)
   - During installation, ensure to check "Add Python to PATH"

2. Verify installation by opening a new PowerShell window and running:
   ```
   python --version
   ```

## Setting up a Virtual Environment

After Python is installed, open a PowerShell window in the project directory and run:

```powershell
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\Activate

# Install requirements
pip install -r requirements.txt
```

## Running the Example

With the virtual environment activated, run:

```powershell
python examples/deutsch_jozsa.py
```

## Deactivating the Environment

When you're done, you can deactivate the virtual environment:

```powershell
deactivate
```

## Troubleshooting

If you encounter issues with PowerShell execution policy, try:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

If Python commands aren't recognized after installation, restart your PowerShell or command prompt. 