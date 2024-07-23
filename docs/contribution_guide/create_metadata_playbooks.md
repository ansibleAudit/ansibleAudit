# Metadata Playbook

A **Metadata Playbook** provides additional information about the vulnerabilities verified by the playbook, including supported systems and versions, as well as details about the vulnerability. Here's how to create and structure this metadata file:

## **Creation of the Metadata File**

### **File name**

- **YAML file:** Create a YAML file that contains the metadata related to the playbook you have created. The file name must be the same as the playbook, but must end with `_metadata.yml`. For example, if your playbook is called `check_security.yml`, the metadata file should be called `check_security_metadata.yml`.

### **Metadata File Contents**

The `metadata.yml` file must include the following information:

- **Compatible Systems and Versions:** Specifies the operating systems and versions that are compatible with the verification carried out by the playbook. If there are multiple systems or versions, list them in as much detail as possible. If you discover that a system or version is missing, other collaborators can add them later.

- **Description:** Provides a detailed description of the vulnerability that the playbook checks for. You can obtain this information directly from relevant databases or benchmarks. If the description is long, you can summarize it for clarity.

- **Justification (Rationale):** Explains why the vulnerability represents a risk to the system. This justification can also be obtained from databases or benchmarks. If it is not available, you will need to create one manually that clearly describes the associated risk.

- **Vulnerability Score:** Includes the vulnerability score based on the CVE (Common Vulnerabilities and Exposures) calculator. This score helps evaluate the severity of the vulnerability found and its potential impact on the system.



>## **Additional considerations**
>
>    - **Information Gathering**: Use reliable sources such as vulnerability databases and benchmarks to obtain the description and justification. Make sure the information is accurate and relevant.
>
>    - **Summary of Extensive Information**: If the information is very extensive, make a summary that maintains the most important aspects without losing clarity.
>
>    - **Continuous Update**: Make sure to keep the metadata updated as new vulnerabilities are discovered or supported system versions are updated.


