# 🚀 Enterprise Network Automation Pipeline

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

## 📌 System Overview

This repository contains a modular, Python-driven network automation pipeline designed to streamline the administration of distributed infrastructure. By leveraging cryptographic SSH [Secure Shell: A cryptographic network protocol for operating network services securely over an unsecured network] key-based authentication, the tool securely connects to multiple Linux environments to execute automated system commands. 

This project demonstrates real-world automation patterns heavily utilized in modern DevOps, Cloud Engineering, and System Administration workflows, replacing manual CLI [Command-Line Interface: A text-based user interface used to interact with software and operating systems] operations with a scalable, code-driven approach.

## ⚙️ Core Engineering Features

* **Zero-Trust Authentication:** Implements secure SSH [Secure Shell: A cryptographic network protocol for operating network services securely over an unsecured network] key-based authentication, entirely eliminating the need for hardcoded or plaintext passwords.
* **Decoupled Infrastructure as Code:** Supports multi-device targeting via an external configuration matrix (`config/devices.local.txt`), ensuring the core codebase remains independent of the deployment environment.
* **Modular Execution Engine:** Dynamically ingests target commands from `config/commands.txt`, enabling rapid pivoting of operational tasks without altering script logic.
* **Structured Telemetry & Auditing:** Features a per-device logging subsystem that captures standard output, timestamps, and execution metadata, providing an immutable audit trail for all remote operations.

## 🛠️ Technology Stack & Environment

* **Programming Language:** Python 3.x
* **Core Libraries:** Paramiko (Provides native Python bindings for the SSH2 [Secure Shell 2: The second, more secure version of the SSH network protocol] protocol)
* **Operating Environment:** Linux / WSL [Windows Subsystem for Linux: A compatibility layer for running Linux binary executables natively on Windows]
* **Version Control:** Git & GitHub

## 📂 Project Architecture

```text
network-automation-tool/
├── src/
│   ├── main.py              # Application entry point and orchestrator
│   ├── ssh_runner.py        # Core logic for SSH connections and remote execution
│   └── config_loader.py     # File I/O operations for parsing inventory and commands
├── config/
│   ├── devices.example.txt  # Template for fleet inventory setup
│   └── commands.txt         # Execution payload definitions
├── logs/                    # Centralized directory for structured telemetry
├── requirements.txt         # Python dependency definitions
├── .gitignore               # Excludes sensitive logs, configs, and environments
└── README.md                # Project documentation
