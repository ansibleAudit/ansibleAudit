# **Results analysis**

## **Results by Console**

When it runs a playbook, results will be displayed in the console indicating the status of the security checks:

   - <span style="color: green;">**OK**</span>: Indicates that the playbook has not detected any vulnerability in the system.
   - <span style="color: red;">**FAILED**</span>: Indicates that a vulnerability has been detected in the system. The application will show possible remedies to mitigate the vulnerability. This way, users can proactively take corrective actions to strengthen system security.

## **Generated Reports**

In addition to console results, the application generates detailed reports in PDF and HTML formats. These reports are stored in the reports directory and contain the following elements:

 - **Playbook Name**: Identification of the specific playbook that has been executed.
 - **Obtained Date/Time, System Type and Version**: Timestamp indicating when the results were obtained, along with the system type and its version.
 - **Status**: Can be <span style="color: green;">**OK**</span> or <span style="color: red;">**FAILED**</span>, depending on whether vulnerabilities were detected or not.
 - **Severity Score**: Level of severity of the vulnerability found, classified as: <span style="background-color: gray;">**None**</span>, <span style="background-color: green;">**Low**</span>, <span style="background-color: yellow;">**Medium**</span>, <span style="background-color: orange;">**High**</span>, <span style="background-color: red;">**Critical**</span>.
 -  **Description**: Details about the specific configuration being verified.
 -  **Rationale**: Explanation or justification of why the vulnerability represents a risk to the system.
 -  **Remediation**: Detailed instructions on how to mitigate the detected vulnerability.
