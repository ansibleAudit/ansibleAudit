# Metadata Playbook
The user must create a yaml file that will represent the metadata, which must be named the same as the playbook you created in the previous step but must end with "_metadata.yml". In this file are defined the systems and versions supported by the check, along with a description, justification, and the vulnerability score based on the CVE calculator. 
 
At the beginning of the metadata.yml file, the compatible systems and versions must be specified. As there may be several, we must try to specify as much as possible which ones they are. If any are missing, the other contributors will be responsible for adding them if necessary. 

The description and rationale: This information can be obtained directly from the databases or benchmarks mentioned above. If the description and rationale are very long, you can summarize them. In the event that this information is not provided, it will have to be created manually explaining the description and the rationale.
In our project, the vulnerability score is a crucial aspect to evaluate the severity of insecure configurations. Here it explain how to treat it:


