from pathlib import Path
import argparse

from config_loader import load_devices, load_commands
from ssh_runner import run_commands


def parse_args():
    parser = argparse.ArgumentParser(description="SSH-based network automation tool")
    parser.add_argument(
        "--devices",
        default="config/devices.local.txt",
        help="Path to devices file"
    )
    parser.add_argument(
        "--commands",
        default="config/commands.txt",
        help="Path to commands file"
    )
    parser.add_argument(
        "--logs",
        default="logs",
        help="Directory to store logs"
    )
    parser.add_argument(
        "--key",
        default="~/.ssh/id_ed25519",
        help="Path to SSH private key"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    devices_file = Path(args.devices)
    commands_file = Path(args.commands)

    devices = load_devices(str(devices_file))
    commands = load_commands(str(commands_file))

    for device in devices:
        try:
            run_commands(
                host=device["host"],
                username=device["username"],
                key_path=args.key,
                commands=commands,
                logs_dir=args.logs
            )
        except Exception as e:
            print(f"Error on {device['host']}: {e}")


if __name__ == "__main__":
    main()
