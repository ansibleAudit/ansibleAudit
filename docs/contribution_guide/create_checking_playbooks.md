# Check Playbook
You must create a playbook that verifies a specific configuration vulnerability. The playbook should only verify the vulnerability, and if found, suggest a possible remedy. If you want to create a playbook for a specific system, it must be done in the directory referring to the type of system, in the directory intended to contribute to the tasks (tasks). 

In the event that you want to contribute playbooks for a type of system that does not have a directory, one must be created to make the specific contributions for that type of system. Although before doing that, you need to open an issue reporting it. To create a new role to be able to add a new type of system to the application, you must do:
	
	ansible-galaxy init roles/new_role

> **Steps to follow**
> 1. Abstract and global design
Global variables: Use global variables in the vars directory of the role common, which can be easily modified to adapt to different systems. The use of global variables allows you to define values ​​that can be performed in many tasks and playbooks, facilitating the management and maintenance of the configuration. Here are some examples of global variables you could use:

>	1. Names of common packages
>
>	2. Common orders
>
>	3. Common routes
>
>	4. Common remedies
>
>	5. Configuration parameters

Reusable tasks: Create tasks that are as generic as possible so they can be used in many playbooks.
Minimal modifications: Try to make tasks and variables so that they require minimal modifications to adapt to different systems.

> **2.-Creation of the Playbook**
>Vulnerability verification: The playbook must verify a vulnerability on some specific configuration. Just verify, >without making any changes to the system.
>Remediation Suggestion: If the vulnerability is found, a possible remedy must be shown. Just show it, without making any changes to the system.

> **3.-Structure of the Playbooks**
>Directory specific to system type: If the playbook is specific to a system type, it must be located in the directory corresponding to that type of system. 
>Tasks: Place the tasks in the directory intended for them

> **4.- New type of system**
>If you want to contribute playbooks for a system that does not have a specific directory:
>
>• **Open an Issue**: Open an issue informing about the need to add a directory for a new type of >system.
>
>• **Create a new role**:
>The name of the role you want to create must be the same as the name of the operating system distribution (distro.name()).
>
	Ansible-galaxy init roles/system_name


