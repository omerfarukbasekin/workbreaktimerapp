@echo off

REM Install dependencies using pip
start /B cmd /C "pip install -r requirements.txt"

REM Start main.py
start /B cmd /C "python main.py"

exit
