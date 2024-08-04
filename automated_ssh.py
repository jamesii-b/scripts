import subprocess

def get_server_details():
    servers = []
    while True:
        ip = input("Enter server IP address (or type 'done' to finish): ")
        if ip.lower() == 'done':
            break
        username = input(f"Enter username for {ip}: ")
        password = input(f"Enter password for {ip}: ")
        port = input(f"Enter port for {ip} (default 22): ") or "22"
        servers.append((ip, username, password, port))
    return servers

def get_command():
    return input("Enter the command to run on all hosts: ")

def connect_to_server(ip, username, password, port, command):
    try:
        # Construct the SSH command with port
        ssh_command = f'sshpass -p {password} ssh -o StrictHostKeyChecking=no -p {port} {username}@{ip} "{command}"'
        print(f"Connecting to {ip} on port {port} and executing command: {command}")
        
        result = subprocess.run(ssh_command, shell=True, text=True, capture_output=True)
        
        if result.returncode == 0:
            print(f"Output from {ip}:\n{result.stdout}")
        else:
            print(f"Error connecting to {ip}:\n{result.stderr}")
    except Exception as e:
        print(f"An error occurred with {ip}: {e}")

def main():
    servers = get_server_details()
    command = get_command()
    for ip, username, password, port in servers:
        connect_to_server(ip, username, password, port, command)

if __name__ == "__main__":
    main()
