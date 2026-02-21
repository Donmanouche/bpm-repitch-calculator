# BPM Repitch Calculator - Executables

This folder contains pre-built executables for the BPM Repitch Calculator application.

## Available Executables

### Linux (x86_64)
- **File**: `dist/BPM_Repitch_Calculator`
- **Status**: ✅ Built and tested
- **Usage**: `chmod +x BPM_Repitch_Calculator && ./BPM_Repitch_Calculator`

### macOS (Universal)
- **File**: `dist/BPM_Repitch_Calculator_mac`
- **Status**: ✅ Built (from Linux, may need testing on actual macOS)
- **Note**: For best results, build on actual macOS machine

### Windows (x86_64)
- **File**: `dist/BPM_Repitch_Calculator_win.exe`
- **Status**: ✅ Built using Wine (cross-compiled from Linux)
- **Size**: 10.3 MB
- **Usage**: Double-click or run from command prompt
- **Note**: Built with Wine, should work on Windows 10/11

## How to Build Windows Executable

To create a Windows executable, you have two options:

### Option 1: Build on Windows Machine

1. Install Python 3.6+ on Windows
2. Install PyInstaller: `pip install pyinstaller`
3. Run the batch script: `build_windows_executable.bat`
4. The executable will be created in the `dist/` folder

### Option 2: Cross-compile from Linux (Advanced)

1. Install Wine: `sudo apt install wine`
2. Install PyInstaller in Wine Python environment
3. Run: `wine pyinstaller --onefile --windowed --name "BPM_Repitch_Calculator_win" bpm_repitch_calculator.py`

## Building from Source

If you want to rebuild any executable:

```bash
# Install requirements
python3 -m venv venv
source venv/bin/activate
pip install pyinstaller

# Build for current platform
pyinstaller --onefile --windowed --name "BPM_Repitch_Calculator" bpm_repitch_calculator.py

# Build for macOS (universal)
pyinstaller --onefile --windowed --name "BPM_Repitch_Calculator_mac" --target-arch universal2 bpm_repitch_calculator.py
```

## Requirements

- Python 3.6+
- PyInstaller 6.0+
- Tkinter (usually included with Python)

## Notes

- The Linux and macOS executables are built on Linux and should work on their respective platforms
- For Windows, it's recommended to build on an actual Windows machine
- All executables are single-file, no additional dependencies needed
- The application uses Tkinter for GUI, which should be available on all platforms