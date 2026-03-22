from pathlib import Path

def load_devices(path: str):
    devices = []
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"Device file not found: {path}")

    for line in file_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        parts = [part.strip() for part in line.split(",")]
        if len(parts) != 2:
            raise ValueError(f"Invalid device line: {line}")

        host, username = parts
        devices.append({
            "host": host,
            "username": username
        })

    return devices


def load_commands(path: str):
    commands = []
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"Command file not found: {path}")

    for line in file_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        commands.append(line)

    return commands
