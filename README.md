# Keylogger-Using-Python
This tool is intended for controlled environments only (e.g., lab machines, personal VMs, consented testing). Always follow local laws and get proper authorization before deploying keylogging tools.

# 🔐 Python Keylogger (Educational)

A basic keylogger written in Python using the `pynput` library. This script listens for keyboard events, logs keystrokes to a local file, and stops recording when a specific key (F12) is pressed.

> ⚠️ **Disclaimer**: This project is for **educational and ethical testing** purposes only. Do not use it on any system without **explicit authorization**. Misuse of this tool is strictly discouraged and may be illegal depending on your jurisdiction.

## 🔧 Features

- Logs all keystrokes (alphanumeric and special keys)
- Saves to `keylog.txt` in the current directory
- Cleanly stops logging when `F12` is pressed
- Logs the stop time for auditing
- Lightweight and runs from the terminal

## 🧪 Use Cases

- Information Security Labs
- Cyber Forensics Practice
- Keylogging Research & Demonstration
- Red Team Educational Scenarios

## 🚀 Getting Started

```bash
pip install pynput
python keylogger.py
