#!/bin/bash

# Define the list of nodes
nodes=("deployer" "node1" "node2" "node3")

public_key= "yourpubkeyhere" 
# Define the SSH directory creation command
create_ssh_dir="if [ ! -d /root/.ssh ]; then sudo mkdir /root/.ssh; fi"

# Define the command to run on each node
command="
sudo sed -i 's/^#PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
sudo passwd root && \
echo \"$public_key\" | sudo tee /root/.ssh/authorized_keys && \
sudo chmod 700 /root/.ssh && \
sudo chmod 600 /root/.ssh/authorized_keys && \
sudo sed -i 's/^PermitRootLogin yes/PermitRootLogin prohibit-password/' /etc/ssh/sshd_config && \
sudo systemctl restart ssh*
"

# Execute the command on each node (use ssh or a similar tool to run this remotely)


# Loop through each node and execute the command
for node in "${nodes[@]}"; do
		ip=$(nslookup "$node" | grep 'Address:' | awk '{print $2}' | grep -v '^127.0.0.53$')

		read -p "Enter username for $ip: " username

    echo "Running command on $node as $username"
    ssh -t "$username@$node" "$command"
done
