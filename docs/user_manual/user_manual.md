# **User manual**
This manual is designed for users who wish to use the application to verify vulnerabilities in their system configurations. If you are interested in contributing to the development of the application, please consult the Contribution Manual.

## Prerequisites:

- Python 3.x or 2.x installed on the system

- Git installed

- Pip installed


> ### **1. Steps for installing the app:**
>
> 1. Go to the [Github repository](https://github.com/ansibleAudit/ansibleAudit)
>
> 2. Download the **.zip** file of the code by clicking on the "**Code**" button and then on "**Download ZIP**".
>
> 3. Unzip the **.zip** file


> ### **2. Create and activate a virtual environment**
>
>1. Open a terminal and navigate to the directory where the code has been unzipped
>
>2. Create a virtual environment by executing the following command:		
>               
        python -m venv .
>		
> 3. Activate the virtual environment
>		
        source ./bin/activate
>	
> ### **3. Install dependencies**
> Once the virtual environment is activated, run the **setup.sh** file that will install all the necessary packages:
>	
        ./setup.sh
>
> **Note:** Make sure the **setup.sh** file has execute permissions. If not, grant it permissions by running:
>
        chmod +x install setup.sh

> ### **4. Run the application**
> With all dependencies installed, run the application with the following command:
>	
        python run.py
		
The application will start running and perform a check of rules compatible with the user's system and version to identify possible vulnerabilities in the configurations. Running the application from the terminal console will display important information about the playbooks that are running and their status. This tool is designed to provide real-time feedback on systems configuration and potential vulnerabilities detected. During execution, the application will display the names of the playbooks that are being executed to indicate which tasks are currently being performed.

