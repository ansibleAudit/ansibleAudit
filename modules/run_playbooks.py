import os
import distro
import yaml
import shutil
import platform
import subprocess
import re
from modules.report_generator import generate_report
from rich.console import Console
from modules.generate_pdf_dashboards import create_pdf_with_dashboards
from modules.is_compatible import is_compatible
from modules.run_playbook import run_playbook
from modules.handle_results import handle_results
from modules.get_rating_counts import get_rating_types_counts

console = Console()

def get_system_name_for_compatibility(system_name):
    """
    Maps system names to the format used in metadata.
    
    Args:
        system_name (str): The system name returned by distro.name().
        
    Returns:
        str: A standardized system name for compatibility checks.
    """
    system_map = {
        'Fedora Linux': 'Fedora',
        'Ubuntu': 'Ubuntu',
    }
    return system_map.get(system_name, system_name)

def get_windows_distro_name():
    """
    Gets the distribution name of Windows. If running in WSL, retrieves the Windows version.
    
    Returns:
        str: The name of the Windows distribution or version.
    """
    if is_wsl():
        # Retrieve Windows version information using Windows command
        try:
            output = subprocess.check_output("cmd.exe /c ver", shell=True, stderr=subprocess.STDOUT).decode()
            match = re.search(r"Microsoft Windows \[Versión \d+\.\d+\.\d+\.\d+\]", output)
            if match:
                return match.group(0)
            else:
                return "No se pudo encontrar la versión de Windows en la salida."
        except subprocess.CalledProcessError as e:
            return f"Failed to retrieve Windows version: {e}"
  
            
            
def is_wsl():
    """
    Detects if the script is running on WSL (Windows Subsystem for Linux).
    
    Returns:
        bool: True if running on WSL, False otherwise.
    """
    # Check if the environment contains 'Microsoft' which indicates WSL
    if 'microsoft' in platform.uname().release.lower():
        return True
    else: 
        return False

def load_metadata(file_path):
    """
    Loads and returns the contents of a metadata file in YAML format.

    Args:
        file_path (str): The path of the YAML file containing the metadata.

    Returns:
        dict: A dictionary that represents the content of the YAML file.
    """
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
        
        
def obtain_metadata_info(metadata):
    """
    Extracts and returns specific information from the provided metadata.

    Args:
        metadata (dict): A dictionary containing metadata information.

    Returns:
        tuple: A tuple containing the description, rationale, and CVSS score extracted from the metadata.
               If any key is not present, an empty list is returned for that key.
    """
    description = metadata.get('description', [])
    rationale = metadata.get('rationale', [])
    cvss_score = metadata.get('cvss_score', [])
    return description, rationale, cvss_score
    
    
def run_playbooks(roles_dir):
    """
    Runs playbooks associated with roles that contain metadata files compatible with the current system.
    Generate reports and a PDF with dashboard at the end of the execution.

    Args:
        roles_dir (str): Directory containing the role directories.

    Returns:
        None
    """
    # Current system and version
    current_system = get_system_name_for_compatibility(distro.name())
    current_version = distro.version()
    rating_counts = {"None": 0,"Low": 0,"Medium": 0,"High": 0,"Critical": 0,"Invalid score": 0}
    if is_wsl():
       windows_distro = get_windows_distro_name()
       match = re.search(r"(Microsoft Windows) \[Versión (\d+\.\d+\.\d+\.\d+)\]", windows_distro)
       if match:
            windows_name = match.group(1)
            windows_name = windows_name.split(' ', 1)[1]
            windows_version = match.group(2)
            current_system = windows_name
            current_version = windows_version
    ok_count = 0
    failed_count = 0
    total_rules = 0
    rating_counts = {}
    # Loop through directories within 'roles'
    for role_dir in os.listdir(roles_dir):
       role_path = os.path.join(roles_dir, role_dir)
       if not os.path.isdir(role_path):
           continue
    
       # Path to 'meta' directory within the role
       meta_dir = os.path.join(role_path, 'meta')
       if not os.path.exists(meta_dir) or not os.path.isdir(meta_dir):
           continue
    
       # Loop through files in 'meta' directory
       for filename in os.listdir(meta_dir):
	       if filename.endswith('_metadata.yml'):
                   metadata_path = os.path.join(meta_dir, filename)
                   metadata = load_metadata(metadata_path)
                   if metadata is None:
                      print(f"Error loading metadata from: {metadata_path}")
                      continue
                                   
                   if is_compatible(metadata, current_system, current_version):
                       description, rationale, cvss_score = obtain_metadata_info(metadata)
                       metadata_info = [description, rationale, cvss_score]
		               # Search for the corresponding playbook
                       playbook_name = filename.replace('_metadata.yml', '.yml')
                       playbook_path = os.path.join(role_path, 'tasks', playbook_name)
                       print(f"  Running {playbook_name}...")
                       results = run_playbook(playbook_path)
                       if not results:
                          failed_count += 1
                          continue
                          
                       success, state, remediations = handle_results(results, playbook_name)
                       if success:
                          ok_count += 1
                       else:
                          rating_counts = get_rating_types_counts(cvss_score)
                          failed_count += 1
                       generate_report(playbook_name, current_system, current_version, state, remediations, metadata_info)
    total_rules = ok_count + failed_count
    create_pdf_with_dashboards(ok_count, failed_count, total_rules, rating_counts )
    artifacts_dir = os.path.join(os.getcwd(), 'artifacts')
    if os.path.exists(artifacts_dir):
       shutil.rmtree(artifacts_dir)
