import paramiko

def run_commands(host, user, password):
    commands = ["uname -a", "uptime", "whoami"]

    try:
        print(f"\nConnecting to {host}...")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(host, username=user, password=password)

        print(f"Connected to {host}")

        output_file = f"logs/{host}.txt"

        with open(output_file, "w") as file:
            for cmd in commands:
                stdin, stdout, stderr = ssh.exec_command(cmd)
                output = stdout.read().decode()

                print(f"[{host}] {cmd}:\n{output}")
                file.write(f"\n--- {cmd} ---\n{output}")

        ssh.close()
        print(f"Saved output to {output_file}")

    except Exception as e:
        print(f"Error on {host}: {e}")


def main():
    with open("devices.txt", "r") as f:
        devices = f.readlines()

    for device in devices:
        host, user, password = device.strip().split(",")
        run_commands(host, user, password)


if __name__ == "__main__":
    main()
