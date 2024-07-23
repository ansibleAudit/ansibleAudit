# **Contribution Guide**
Thank you for your interest in contributing to our open source vulnerability checker with **Ansible**! This guide will help you understand how to contribute to the project by adding new vulnerability checks and helping to grow this application. First of all, it should be noted that this application is intended for users who know how to program and have knowledge with **Ansible**. Our goal is to create a tool that helps users identify potential vulnerabilities in their system configurations without making any changes to the system. In addition, in the event that a vulnerability is detected, information will be provided on how to mitigate it. It should also be noted that this application focuses on checking for vulnerabilities in system configurations.

To contribute to the project, it is necessary to clone the "[ansibleAudit](https://github.com/ansibleAudit/ansibleAudit)" repository on your local machine. Below are the steps to do this using both the HTTPS URL and the SSH URL.

# **Clone with HTTPS URL**
1.- Open a terminal

2.- Run the following command to clone the repository using the HTTPS URL:

        git clone https://github.com/ansibleAudit/ansibleAudit.git

# **Clone with SSH URL**
If you prefer to use an SSH URL to clone the repository, follow these steps:

> 1. **Generate an SSH key**: It is necessary to generate an SSH key if you do not have one. 
> 2. **Add SSH key** to your Github account
> 3. **Clone the repository**
>
> After adding your SSH key to your Github account. Clone the repository using the SSH URL:
>
        git clone git@github.com:ansibleAudit/ansibleAudit.git

##
>
> **Note:**
>
> • Git configuration: Make sure you have your username and email configured in Git before making contributions:
>	
        git config –global user.name “your_username”
>
        git config –global user.email your_email@example.com

With these steps, you can clone the repository and start contributing to the project. 
##
# **Best practices for naming branches**
Before following the steps on how you can contribute, it is recommended to follow a series of good practices while naming the branches you will work with. First, it is recommended to use the separators “_”, to improve the readability of the name.

> **Note:**
> It is recommended that the branch name begins with a category name, which indicates the type of work being carried out in the branch. Some of the most used categories are:

| Category Type | Meaning                                                              |
|---------------|----------------------------------------------------------------------|
| Hotfix        | To quickly fix critical issues, usually with a temporary solution    |
| Bugfix        | To correct an error                                                  |
| Feature       | To add, remove, or modify a feature                                  |
| Test          | To experiment with something that is not a problem                   |
| Wip           | Work in progress                                                     |


If the following steps are performed it will be easier to identify the task and track its progress:

## 1.- Concatenate the category type with the issue ID:

- Select the category to which the task belongs (feature, bugfix, hotfix, etc.).
       
- Find the issue ID on GitHub that corresponds to the task.

>**Note:**
>
> For example, if you are working on a new feature and the issue ID is 42, you concatenate feature and 42 with an underscore: ***feature_42***.

## 2.- Add a brief description of the task:

- Add a brief description of the task to be performed.
	
- This description should be informative but brief, and should be separated by another underscore.

>**Note:**
>
>Following the previous example, if the task is to add a new role for CentOS, the branch would be called: ***feature_42_add_new_role_CentOS***.

## Reason for this convention:
>
>    - **Ease of identification**: This naming convention allows anyone viewing the branch to understand what the task is about and what issue it is linked to without needing to delve into the details.
>    - **Progress Tracking**: Facilitates monitoring the progress of each task and its relationship with the issues registered in the problem tracking system.
##
>**Tips:**
>
> • **Avoid using only numbers**: It causes confusion and errors
>
> • **Avoid long branch names**: The branch name must be informative, precise and short. If the names are long they may not be so readable or efficient.
>


## **Steps for Contributing**
>
> 1. [Find vulnerabilities](find_vulnerabilities.md)
>
> 2. Create Ansible Playbooks
>
	> 2.1 [Create verification playbooks](create_checking_playbooks.md)
	>
	> 2.2 [Create metadata playbooks](create_metadata_playbooks.md)
>
> 3.- [Test contributions](test_playbooks.md)
>
> 4.- [Create a Pull Request](create_pull_request.md)
>
> 5.- Fork the repository (optional)
>
> 6.- [Future improvements of the application](future_improvements.md)
>
> 7.- Structure of the project
>

