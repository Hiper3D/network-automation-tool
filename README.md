# 💻 Automated Fleet Management Tool: Source Code

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Bash](https://img.shields.io/badge/GNU%20Bash-4EAA25?style=for-the-badge&logo=GNU%20Bash&logoColor=white)

## 📋 Project Overview

This repository contains the source code for a robust, Python-driven network automation utility. To demonstrate backend scripting proficiency and infrastructure control, I designed and built a tool that connects to distributed target nodes via the SSH [Secure Shell: A network protocol that gives users a secure way to access a computer over an unsecured network] protocol to execute system commands automatically.

The application behaves as a scalable CLI [Command-Line Interface: A text-based user interface used to interact with software and operating systems] utility. It maps standard output from remote executions into structured, device-specific log files, ensuring clean telemetry, highly auditable records, and simplified debugging for network administrators.

## 🛠️ Backend Architecture & System Design

### 1. Remote Execution Pipeline

* **Cryptographic Bindings:** Utilizes the Paramiko library to establish secure, programmatic connections to multiple target devices via SSH [Secure Shell: A network protocol that gives users a secure way to access a computer over an unsecured network].
* **Automation:** Allows for the bulk execution of system commands across an entire network fleet simultaneously, heavily reducing manual configuration overhead.

### 2. Decoupled Configuration Management

* **External Inventory:** Uses an external `devices.txt` configuration file structured as a CSV [Comma-Separated Values: A text file format that uses commas to separate data fields] to manage fleet credentials and routing.
* **Scalability:** This decoupled approach allows administrators to add or remove target IP [Internet Protocol: A set of rules governing the format of data sent over the internet or local network] addresses dynamically without requiring any core codebase modifications.

### 3. Structured Telemetry & Auditing

* **Automated Logging:** Engineered to automatically isolate and route execution outputs into dedicated, timestamped log files per device node.
* **State Tracking:** Provides an immutable record of state changes, errors, and queries within a centralized `logs/` directory.

---

## 🚀 Deployment & Execution Environment

### 1. Initialization & Environment Isolation

Clone the repository and spin up a secure venv [Virtual Environment: A tool to create isolated Python environments] to prevent system dependency conflicts:

```bash
git clone git@github.com:Hiper3D/network-automation-tool.git
cd network-automation-tool
python3 -m venv env
source env/bin/activate
2. Dependency Management
Install the required cryptographic and network libraries:

Bash
pip install paramiko
3. Fleet Configuration
Edit the devices.txt file to define your target infrastructure. Ensure your network permits inbound traffic from your host machine to the target nodes:

Code snippet
# Format: IP,username,password
192.168.1.10,admin,secure_password
10.0.0.5,root,another_password
4. Execution
Trigger the automation sequence:

Bash
python main.py
Note: For production environments, it is strongly recommended to refactor the authentication flow to utilize RSA/Ed25519 SSH [Secure Shell: A network protocol that gives users a secure way to access a computer over an unsecured network] key pairs rather than plaintext passwords.

👤 Author
Priyanshu Patra
Aspiring Software & Cloud Network Engineer focused on AI-Augmented Development and scalable cloud infrastructure.


