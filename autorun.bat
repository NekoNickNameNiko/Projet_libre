@echo off
python.exe -m pip install --upgrade pip
pip install pygame

python.exe "%~dp0\run.py"

pause
