import os
import datetime
from jinja2 import Template
import pdfkit

def playbook_already_exists(html_file, playbook):
        """
        Checks if a specific playbook already exists in an HTML file.

        Args:
           html_file (str): The path of the HTML file to verify.
           playbook (str): The name of the playbook to search within the HTML file.

        Returns:
           bool: Returns True if the playbook is found in the content of the HTML file,
              otherwise it returns False.
        """
        with open(html_file) as f:
             content = f.read()
             return playbook in content

def get_rating(score):
    """
    Determines the severity rating based on a given score.

    Args:
        score (float): The score to evaluate (CVSS score).

    Returns:
        str: The severity rating corresponding to the score:
             - "None" for a score of 0.0.
             - "Low" for scores between 0.1 and 3.9.
             - "Medium" for scores between 4.0 and 6.9.
             - "High" for scores between 7.0 and 8.9.
             - "Critical" for scores between 9.0 and 10.0.
             - "Invalid score" for any other score outside the valid range.
    """
    if score == 0.0:
        return "None"
    elif 0.1 <= score and score <= 3.9:
        return "Low"
    elif 4.0 <= score and score <= 6.9:
        return "Medium"
    elif 7.0 <= score and score <= 8.9:
        return "High"
    elif 9.0 <= score and score <= 10.0:
        return "Critical"
    else:
        return "Invalid score"


def generate_report(playbook, system_name, system_version, state, remediations, metadata_info):
        description, rationale, cvss_score = metadata_info
        actual_path = os.getcwd()
        report = system_name.lower() + system_version
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H")
        report_name = "report_" + system_name.lower() + "_" + system_version + "_" + timestamp
        rating = get_rating(cvss_score)
        params = {
              'playbook': playbook,
              'date': datetime.datetime.now().strftime("%Y/%m/%d"),
              'hour': datetime.datetime.now().strftime("%H:%M:%S"),
              'system_name': system_name,
              'system_version': system_version,
              'description': description,
              'rationale': rationale,
              'cvss_score': rating,
              'state': state,
              'remediation': remediations
        }
        report_template_path = os.path.join(actual_path, 'templates', 'report_template.html')
        html_output_file = os.path.join(actual_path, 'reports', f'{report_name}.html')
        pdf_output_file = os.path.join(actual_path, 'reports', f'{report_name}.pdf')
                   
        with open(report_template_path) as file:
                   template = Template(file.read())
                   html_content = template.render(params)
       
        if os.path.exists(html_output_file):
              if playbook_already_exists(html_output_file, playbook):
                  return
              else:
                  with open(html_output_file, 'a') as f:
                     f.write(html_content)
        else:
              with open(html_output_file, 'w') as f:
                   f.write(html_content)
              
        pdfkit.from_file(html_output_file, pdf_output_file)
