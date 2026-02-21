@echo off
REM Batch script to create Windows executable for BPM Repitch Calculator
REM Requires PyInstaller to be installed: pip install pyinstaller

SET script_name=bpm_repitch_calculator.py
SET output_name=BPM_Repitch_Calculator_win

ECHO Creating Windows executable...
pyinstaller --onefile --windowed --name "%output_name%" --icon=NONE %script_name%

ECHO.
ECHO Windows executable created: dist\%output_name%.exe
ECHO.
PAUSE