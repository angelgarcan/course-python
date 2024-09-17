# Python 3 Installation and Virtual Environment Setup

## Installing Python 3

### For Windows:
1. **Download Python:**
   - Go to the [official Python website](https://www.python.org/downloads/) and download the latest version of Python 3 for Windows.

2. **Run the Installer:**
   - Open the downloaded file (`python-3.x.x.exe`).
   - On the first installation screen, check the box **"Add Python to PATH"** (this is very important!).
   - Click **"Install Now"** to install with default settings, or choose **"Customize Installation"** for advanced options (the default settings are fine for most users).

3. **Verify the Installation:**
   - Open the **Command Prompt** by pressing `Win + R`, typing `cmd`, and hitting **Enter**.
   - In the Command Prompt, type:
     ```bash
     python --version
     ```
     - You should see the installed Python version (e.g., `Python 3.x.x`).

### For macOS:
1. **Check If Python 3 is Pre-Installed:**
   - Open **Terminal** by pressing `Cmd + Space` and searching for "Terminal."
   - In Terminal, type:
     ```bash
     python3 --version
     ```
     - If Python 3 is already installed, you will see the version number.

2. **Install Python (if not already installed):**
   - If Python 3 is not installed, go to the [official Python website](https://www.python.org/downloads/) and download the installer for macOS.
   - Run the installer and follow the instructions.

3. **Verify the Installation:**
   - In the Terminal, type:
     ```bash
     python3 --version
     ```
     - You should see the installed Python version (e.g., `Python 3.x.x`).

---

## Setting Up a Virtual Environment

Virtual environments are useful for managing dependencies for different projects independently.

### Step 1: Install `venv` (if not already installed)

On both Windows and macOS, `venv` comes bundled with Python 3. If it's not installed, you can install it manually:

- On Windows and macOS:
  ```bash
  python3 -m ensurepip --upgrade
