def is_compatible(metadata, system_name, system_version):
    """
    Checks if a given system is compatible with the provided metadata.

    Args:
        metadata (dict): A dictionary containing information about supported systems, with the key 'systems'.
        system_name (str): The name of the system to check.
        system_version (str): The system version to check.

    Returns:
        bool: Returns True if the system is compatible or if no systems are specified in the metadata. 
              Returns False if the system is not supported
        
    """
    systems = metadata.get('systems', [])
    if not systems:
        return True  
    for system in systems:
        if system['name'] == system_name and system_version in system['versions']:
            return True
    return False
