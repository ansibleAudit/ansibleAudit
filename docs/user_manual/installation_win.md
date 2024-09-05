# Installation Manual for Windows

This section explains the installation manual for Windows, providing detailed instructions for properly configuring the system.

## Step 1: Install WSL

1. **Open PowerShell as Administrator**: Right-click on the Start menu and select "Windows PowerShell (Administrator)".
2. **Enable WSL**: In the PowerShell window, execute the following command:

    ```powershell
    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
    ```

3. **Restart the computer**: Once the installation is complete, it's necessary to restart the computer to apply the changes.

## Step 2: Install Ubuntu 22.04 LTS

1. **Open Microsoft Store**: Open Microsoft Store from the Start menu.
2. **Search and install Ubuntu 22.04**:
    - In the search bar of Microsoft Store, type **Ubuntu 22.04 LTS** and press Enter.
    - Select **Ubuntu 22.04 LTS** from the search results.
    - Click **Get** or **Install** to download and install the distribution (sign-in to the store is not required for this installation).

3. **Launch Ubuntu 22.04**: Once the installation is complete, open **Ubuntu 22.04** from the Start menu.
4. **Configure Ubuntu 22.04**: Upon starting Ubuntu for the first time, you will be asked to create a username and password. This will create a local user account.
5. **Update Ubuntu software packages**: Once logged into Ubuntu, open the terminal (if it doesn't open automatically) and run the following command to update all software packages:

    ```bash
    sudo apt update && sudo apt upgrade -y
    ```

    This command will update the list of available packages and upgrade all installed packages to the latest versions.

## Step 3: Create a User and Add to the Administrators Group Using PowerShell

1. **Open PowerShell as Administrator**: To begin, open PowerShell with administrator privileges. Right-click on the Windows Start button and select "Windows PowerShell (Administrator)" or "PowerShell (Administrator)". This ensures you have the necessary permissions to make changes to the system.

2. **Create a New User**: Next, create a new user named **"ansible"**. Use the following command to create the user with a specific password and set the password to never expire:

    ```powershell
    New-LocalUser -Name "ansible" -FullName "ansible" -Description "ansible user" -Password (ConvertTo-SecureString "SuperSecurePassword123@" -AsPlainText -Force) -PasswordNeverExpires
    ```

3. **Add the User to the Administrators Group**: To add the **"ansible"** user to the Administrators group, first list the local groups to confirm the exact name of the Administrators group:

    ```powershell
    Get-LocalGroup
    ```

    This command will display all local groups on the system, including the name and description of each group. Look for the group corresponding to administrators, which is typically **"Administrators"**. Once confirmed, add the **"ansible"** user to the Administrators group with the following command:

    ```powershell
    Add-LocalGroupMember -Group "Administrators" -Member "ansible"
    ```
    
## Step 4: Verify PowerShell and .NET

1. **Verify PowerShell Version**: To ensure that the PowerShell version is appropriate, use the following command:

    ```powershell
    Get-Host | Select-Object Version
    ```

    This command will display the current version of PowerShell installed on the system. Verify this version, as WinRM requires a specific version of PowerShell for proper compatibility and operation.

2. **Verify .NET Version**: To check the version of the .NET framework installed, use the following command:

    ```powershell
    Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP' -Recurse | Get-ItemProperty -Name version -EA 0 | Where { $_.PSChildName -Match '^(?!S)\p{L}' } | Select PSChildName, version
    ```

    This command accesses the Windows registry to retrieve information about the installed .NET framework versions.

3. **Verify WinRM is Not Configured**: To confirm if WinRM (Windows Remote Management) is configured on the system, use the following command:

    ```powershell
    winrm get winrm/config/Service
    ```

## Step 5: Configure WinRM

To prepare WinRM (Windows Remote Management) to accept remote connections, follow these specific steps in PowerShell. These steps configure the service to allow connections through WinRM, which is necessary for remote management and automation with tools like Ansible.

1. **Open PowerShell as Administrator**: To begin, open PowerShell with administrator privileges. Right-click on the Windows Start button and select "Windows PowerShell (Administrator)" or "PowerShell (Administrator)".

2. **Configure WinRM**: Execute the following commands in PowerShell:

    (a) **Initialize Basic WinRM Configuration**:

        ```powershell
        winrm quickconfig
        ```

       This command initializes the basic configuration of WinRM. If WinRM is not enabled, this command configures it to accept connections and sets the default configurations.

    (b) **Allow Basic Authentication**:

        ```powershell
        winrm set winrm/config/service/auth '@{Basic="true"}'
        ```

       Basic authentication allows credentials to be transmitted in plain text. This option can be useful for testing environments but is not recommended for production environments without proper encryption.

    (c) **Allow Unencrypted Connections**:

        ```powershell
        winrm set winrm/config/service '@{AllowUnencrypted="true"}'
        ```

       This allows unencrypted connections, which can be a vulnerability in production environments. In such cases, it is advisable to use Kerberos for more robust security. Using Kerberos requires additional configuration, including domain configuration, ticket generation for authentication, configuring WinRM to use Kerberos, and managing keys and security policies.


## Step 6: Download and Run the Script to Configure WinRM for Ansible

To complete the WinRM configuration for use with Ansible, follow these additional steps:

1. **Ensure PowerShell Uses TLS 1.2**: To ensure secure connections with Ansible, make sure PowerShell uses TLS 1.2. Execute the following command in PowerShell:

    ```powershell
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    ```

2. **Download the Configuration Script**: Download the script provided by Ansible that configures WinRM for use with Ansible. Use the following commands to download and execute the script:

    ```powershell
    $url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
    $file = "$env:temp\ConfigureRemotingForAnsible.ps1"
    (New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)
    ```

3. **Run the Configuration Script**: Once the script is downloaded, the final step is to execute it to configure WinRM. Use the following command to run the script with the appropriate options:

    ```powershell
    powershell.exe -ExecutionPolicy ByPass -File $file
    ```

    The `-ExecutionPolicy ByPass` option allows the script to run without the usual PowerShell execution policy restrictions, ensuring that the script can execute correctly.

## Verify WinRM Configuration

To ensure that WinRM (Windows Remote Management) is configured correctly on a system, it is important to check various aspects of its configuration.

1. **Verify Current WinRM Configuration**: Use the following command to get detailed information about the current WinRM service configuration. This includes aspects such as authentication, encryption, and connection options:

    ```powershell
    winrm get winrm/config/Service
    ```

2. **Verify Windows Remote Shell (WinRS) Configuration**: This command provides information about the configuration of WinRS, the component that allows remote command execution. Check the timeouts and remote execution options:

    ```powershell
    winrm get winrm/config/Winrs
    ```


3. **Verify Configured WinRM Listeners**: Use the following command to show the listeners configured for WinRM, and ensure they are correctly configured with the expected ports and protocols:

    ```powershell
    winrm enumerate winrm/config/Listener
    ```

## Inventory File

To run Ansible on Windows from a Windows Subsystem for Linux (WSL) environment on Ubuntu, you first need to configure an inventory file. Begin by creating a file named `inventory` in the directory where you work with Ansible. This file specifies the necessary information to connect to the Windows machines.

Inside this file, define a group of machines named `windows`, and in this case, add a machine named `windows10` with the IP address `X.X.X.X`. This IP address corresponds to the Windows machine where Ansible will be executed.

The inventory file contains a section of variables for the `windows` group, configuring crucial details for the connection. These variables include:

1. **ansible_user and ansible_password**: Specifies the username and password required to authenticate to the Windows machine. This allows Ansible to perform remote operations with the appropriate access rights.

    ```ini
    ansible_user: username
    ansible_password: password
    ```

2. **ansible_port**: Defines the port used for the WinRM connection. The default port for secure WinRM is 5986.

    ```ini
    ansible_port: 5986
    ```

3. **ansible_connection**: Specifies the type of connection. For WinRM, it is set to `winrm`.

    ```ini
    ansible_connection: winrm
    ```

4. **ansible_winrm_transport**: Configures the transport method for the WinRM connection. In this case, it is set to `basic`, which uses basic authentication.

    ```ini
    ansible_winrm_transport: basic
    ```

5. **ansible_winrm_server_cert_validation**: Defines server certificate validation. In this case, it is set to `ignore` to disable server certificate validation.

    ```ini
    ansible_winrm_server_cert_validation: ignore
    ```

## win_ping.yml File

To verify that Ansible can run correctly on Windows machines from the WSL environment on Ubuntu, create and run a test playbook. This playbook will help confirm that the configuration of your inventory file is correct and that Ansible can communicate with the Windows machines as expected.

First, create a file named `win_ping.yml`. This file is an Ansible playbook that contains instructions for Ansible to execute on the machines defined in the inventory file. The content of the `win_ping.yml` file is as follows:

```
---
- name: win_ping module demo
  hosts: windows
  become: false
  gather_facts: false
  tasks:
    - name: test connection
      ansible.windows.win_ping:
```

## Run the Playbook

To verify that Ansible can communicate correctly with the Windows machines, execute the `win_ping.yml` playbook using the appropriate command. Run the following command in the WSL environment on Ubuntu:

```
ansible-playbook -i inventory win_ping.yml
```

