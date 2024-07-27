# **Checking with Playbook**
You must create a playbook that verifies a specific configuration vulnerability. The playbook should only verify the vulnerability, and if found, suggest a possible remedy. If you want to create a playbook for a specific system, it must be done in the directory referring to the type of system, in the directory intended to contribute to the tasks (tasks). 

# Guide to Create and Manage Check Playbooks

## 1. Abstract and Global Design

When creating your playbook, it is crucial to establish a layout that is reusable and easy to manage. Follow these key points:

### Global Variables

**Global variables** allow configurations to be easily modified and adapted. These variables are defined in the `vars` directory of the common role (`common`). Some useful global variables could be:

- **Common Package Names:** Defines once common package names to be used across multiple playbooks.
- **Common Commands:** Commands that can be used in various playbooks.
- **Common Paths:** Common file paths and directories for different playbooks.
- **Common Remedies:** General solutions for common vulnerabilities.
- **Configuration Parameters:** General settings that may vary depending on the system.

### Reusable Tasks

- **Creation of Generic Tasks:** Tasks should be as generic as possible to facilitate their reuse in multiple playbooks.
- **Minimal Modifications:** Design the tasks and variables so that they require the minimum of modifications to adapt to different systems.

## 2. Creation of the Playbook

When creating your playbook, be sure to follow these steps:

- **Vulnerability Check:** The playbook must check for the presence of vulnerabilities in specific system configurations. **Do not perform automatic changes** on the system apart from this check.
- **Remediation Suggestions:** If a vulnerability is detected, the playbook should provide suggestions on how to fix it, **without applying the solutions automatically**.

## 3. Structure of the Playbooks

- **Specific Directory by System Type:** Places the playbook in the directory corresponding to the type of system it verifies. This makes it easier to organize and access specific playbooks for each system.
- **Tasques:** Locate the tasks in the directory designed for tasks (`tasks`).

## 4. New Type of System

If you want to contribute playbooks for a system that does not have a dedicated directory, follow these steps:

### Open an Issue

- **Report the Need:** Open an issue in the project management platform (such as GitHub) to report the need to create a directory for this new type of system. Include details about the system and the type of playbooks you want to add.

### Create a New Role

- **Role Name:** The role name must match the name of the operating system distribution, as provided by `distro.name()`.
- **Command:** Use the following command to create a new role for this system:

  		ansible-galaxy init roles/sysname

> **Note** Replace **system_name** with the specific name of the operating system or system type you are adding.
#
>### Additional notes
>
>- **Style Consistency:** Make sure to use a consistent style for headings and lists to maintain clarity.
>- **Clear Details:** Provides clear and detailed instructions so that users can follow the steps without confusion.

This guide should help users clearly understand how to create and manage playbooks that checks the configurations's system in search of vulnerabilities, as well as contribute to include new types of systems to be tracted.
