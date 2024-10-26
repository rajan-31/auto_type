## Depencecies

> If you want, use python virtual environment (in a dev folder)
> 
> `python -m venv .venev`

## Setup

Create a file `code.txt` in which you will put text that you want to auto type.

### Ubuntu

- `sudo apt-get install python3-tk python3-dev`
- Switch to Xorg/X11 
    - OR execute `xhost +SI:localuser:$(whoami)`

## Run

(The time you have to point your cursor where you want to type, after executing auto_type.py is 5 seconds, you can change it by changing `delay` variable)

### Windows (Powershell)

```bash
./.venv/scripts/activate.ps1

pip install pyautogui   # only once

python auto_type.py
```

### Ubuntu

```bash
source ./.venv/bin/activate

pip install pyautogui # only once

python3 auto_type.py
```

---

## Convert Python file to Executable (optional)

### Windows

`pyinstaller --onefile auto_type.py`

gives `auto_type.exe` (check ./dist directory)

double click `auto_type.txt`

### Ubuntu

Noting extra just add shebang notation and make auto_type.py executable

Add this to top (if not already present)

`#!/usr/bin/env python3`

`./auto_type.py`