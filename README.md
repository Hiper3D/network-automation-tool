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

* **Programming Language:** Python 3
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
```

## ▶️ Deployment & Execution Guide
1. Repository Initialization
Clone the production branch to your local workstation:
```text
Bash
```
```text
git clone git@github.com:Hiper3D/network-automation-tool.git
cd network-automation-tool
```
2. Environment Isolation
Establish a local venv [Virtual Environment: A tool to create isolated Python environments] to ensure dependency hermeticity and prevent conflicts with global system packages:
```text
Bash
```
```text
python3 -m venv env
source env/bin/activate
```
3. Dependency Management
Install the requisite cryptographic and networking libraries via pip [Pip Installs Packages: The standard package manager for Python]:
```text
Bash
```
```text
pip install -r requirements.txt
```
4. Fleet Inventory Configuration
Initialize your local node registry. This inventory is excluded from VC [Version Control: A system that records changes to a file or set of files over time] to maintain infrastructure obfuscation. Ensure your RSA [Rivest-Shamir-Adleman: A widely used public-key cryptosystem for secure data transmission] or Ed25519 [Edwards-curve Digital Signature Algorithm: A fast and highly secure public-key signature system] public key is present in the```~/.ssh/authorized_keys``` file on all target nodes.

Create ``` config/devices.local.txt: ```
```text
Plaintext
```
```text
# Schema: [IP_ADDRESS], [REMOTE_USER]
          192.168.1.10, admin
              10.0.0.5, root
```
5. Payload Definition
Define the automated directives (idempotent commands) within config/commands.txt:
```text
Bash
```
```text
uname -a
uptime
whoami
```
6. Execution Pipeline
Trigger the main orchestration sequence:
```text
Bash
```
```text
python src/main.py
```
## 📊 Telemetry & Audit Trails
Upon execution completion, the tool generates structured log artifacts within the logs/ directory. Each artifact is dynamically indexed by the target IP [Internet Protocol: A set of rules governing the format of data sent over the internet or local network] address ```(e.g., logs/192.168.1.10.txt)```.

These logs provide a high-fidelity audit trail, including:

Temporal Metadata: Precise timestamps for execution start and end.

Command Echoing: Clear mapping of inputs to outputs.

Standard Streams: Full capture of remote shell responses.

## 🔐 Security Posture
Zero-Trust Authentication: Strictly enforces key-based authentication; interactive password prompts are programmatically rejected to mitigate brute-force risks.

Secret Obfuscation: The```.gitignore``` policy ensures that sensitive PII [Personally Identifiable Information: Information that can be used to identify a specific individual] and internal network topologies never enter the public domain.

Identity Management: Leverages existing SSH [Secure Shell: A cryptographic network protocol for operating network services securely over an unsecured network] configurations for seamless integration with enterprise identity providers.

## 💼 Enterprise Use Cases

SRE/DevOps Seamless integration into CI/CD pipelines for post-deployment health checks.


Cloud Operations: Fleet-wide configuration management and patch verification across ephemeral instances.


Systems Administration: Automated resource monitoring and rapid incident response across distributed data centers.


### 👨‍💻 Author
Priyanshu Patra

Software & Network/Cloud Engineer
