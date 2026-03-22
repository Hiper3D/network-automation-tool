# 💻 Automated Fleet Management Tool: Source Code

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Bash](https://img.shields.io/badge/GNU%20Bash-4EAA25?style=for-the-badge&logo=GNU%20Bash&logoColor=white)

# Network Automation Tool

A Python-based SSH automation tool that connects to Linux systems using key-based authentication, executes commands remotely, and stores outputs in structured log files.

## Features
- SSH key-based authentication
- Multi-device support through a config file
- Automated command execution
- Per-device logging
- Clean and scalable project structure

## Tech Stack
- Python 3
- Paramiko
- Linux / WSL

## Project Structure
- `src/` — application code
- `config/` — device and command files
- `logs/` — command outputs
- `requirements.txt` — Python dependencies

## Usage
1. Create and activate a virtual environment
2. Install dependencies
3. Add your machine details to `config/devices.local.txt`
4. Add commands to `config/commands.txt`
5. Run:

```bash
python src/main.py

##Security
Uses SSH key authentication
Real device details are ignored by Git using .gitignore
#Author

Priyanshu Patra
