@echo off

python --version | find "3.12.1" > nul
if errorlevel 1 (
    echo Python 3.12.1 is not installed. Please install Python 3.12.1 and run this script again.
    exit /b 1
)

pip install -r requirements.txt

echo @echo off > start.bat
echo python main.py >> start.bat

echo Installation and setup completed successfully.
exit /b 0