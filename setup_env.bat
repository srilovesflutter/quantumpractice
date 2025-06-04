@echo off
echo Setting up virtual environment for Quantum Practice project...

REM Check if Python is installed
python --version > nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
echo Installing required packages...
pip install -r requirements.txt

echo.
echo Setup complete! The virtual environment is now activated.
echo To run the example, type: python examples/deutsch_jozsa.py
echo.
echo When you're done, type 'deactivate' to exit the virtual environment.
echo. 