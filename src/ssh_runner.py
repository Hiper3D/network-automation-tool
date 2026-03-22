from pathlib import Path
from datetime import datetime
import paramiko


def run_commands(host: str, username: str, key_path: str, commands: list[str], logs_dir: str):
    logs_path = Path(logs_dir)
    logs_path.mkdir(parents=True, exist_ok=True)

    log_file = logs_path / f"{host}.txt"
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        print(f"\nConnecting to {host}...")

        ssh.connect(
            hostname=host,
            username=username,
            key_filename=str(Path(key_path).expanduser()),
            timeout=10
        )

        print(f"Connected to {host}")

        with log_file.open("w", encoding="utf-8") as f:
            f.write(f"Host: {host}\n")
            f.write(f"User: {username}\n")
            f.write(f"Started: {datetime.now().isoformat()}\n")

            for cmd in commands:
                stdin, stdout, stderr = ssh.exec_command(cmd)

                output = stdout.read().decode(errors="replace")
                error = stderr.read().decode(errors="replace")
                exit_code = stdout.channel.recv_exit_status()

                print(f"[{host}] {cmd}:")
                print(output)

                f.write(f"\n--- {cmd} ---\n")
                f.write(f"Exit code: {exit_code}\n")
                f.write(output)

                if error.strip():
                    f.write("\n[ERROR]\n")
                    f.write(error)

        print(f"Saved output to {log_file}")

    finally:
        ssh.close()
