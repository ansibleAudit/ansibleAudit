#!/bin/bash

# Function to print messages
print_message() {
    echo "==================================="
    echo $1
    echo "==================================="
}

# Function to install Python packages
install_python_package() {
    package=$1
    print_message "Installing Python package: $package..."
    pip3 install "$package" || { echo "Failed to install $package"; exit 1; }
}

# Install Ansible
install_python_package ansible
install_python_package ansible-core==2.13.9
install_python_package ansible-runner
install_python_package alive-progress
install_python_package ansible-lint
install_python_package rich
install_python_package pdfkit
install_python_package jinja2
install_python_package distro
install_python_package matplotlib
install_python_package pdfplumber

# Install wkhtmltopdf and its dependencies
print_message "Installing wkhtmltopdf..."
sudo apt-get install -y wkhtmltopdf 

print_message "Installation completed!"