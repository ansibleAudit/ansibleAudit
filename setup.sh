#!/bin/bash

# Function to print messages
print_message() {
    echo "==================================="
    echo $1
    echo "==================================="
}

# Install Ansible
print_message "Installing Ansible..."
pip3 install ansible
pip3 install ansible-core==2.13.9

# Run the setup_config.yml playbook
print_message "Running the install_packages.yml playbook..."
ansible-playbook install_packages.yml

print_message "Setup completed."
