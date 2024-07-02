from rich.console import Console
from modules.extract_remediation import extract_remediation

console = Console()
def handle_results(results, playbook_name):
    """
    Processes the results of a playbook execution and determines its final state.
    
    Args:
        results (obj): Object that contains the events generated during the execution of the playbook.
        playbook_name (str): Name of the executed playbook.

    Returns:
        tuple: A tuple containing a boolean indicating the success or failure of the execution, 
               the final status as a string ("OK" or "FAILED"), and a list of remedies.
    """

    state = "OK"
    remediations = []
    for event in results.events:
        if event['event'] == 'runner_on_failed':
            state = "FAILED"
            console.print(f"  {state}:x:", style="bold red")
            output = event['stdout']
            remediations = extract_remediation(output)
            console.print("  REMEDIATION:warning:", remediations, style="bold #FFA500", end="\n\n\n")
            return False, state, remediations
    console.print(f"  {state}:heavy_check_mark:", style="bold green", end="\n\n\n")
    return True, state, remediations

