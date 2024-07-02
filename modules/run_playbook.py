from alive_progress import alive_bar
import time
import ansible_runner
import os

def run_playbook(playbook_path):
    """
    Runs an Ansible playbook and returns the results.

    Args:
        playbook_path (str): The path to the playbook file to run.

    Returns:
        obj: The results object of the playbook execution.
    """
    with alive_bar() as bar:
        start_time = time.time()
        results = ansible_runner.run(private_data_dir=os.getcwd(), playbook=playbook_path, quiet=True)
        elapsed_time = time.time() - start_time
    print(f"  Rule {os.path.basename(playbook_path)} checked in {elapsed_time:.2f} seconds", end="\n")
    return results
