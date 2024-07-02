def process_metadata_file(meta_dir, filename, role_path, current_system, current_version):
    """
    Processes a metadata file and checks its compatibility with the current system.

    Args:
        meta_dir (str): The directory where the metadata file is located.
        filename (str): The name of the metadata file.
        role_path (str): The directory path of the role that contains the playbook.
        current_system (str): The name of the current system.
        current_version (str): The current system version.

    Returns:
        tuple: A tuple containing:
            - metadata_info (list): List with the description, rationale and CVSS score extracted from the metadata.
            - playbook_name (str): The name of the associated playbook.
            - playbook_path (str): The path of the playbook file.
            - metadata (dict): The loaded metadata dictionary.
            - bool: Processing success or failure indicator.
            If the file is not supported or there is an error in the upload, None and False values ​​are returned
    """
    if not filename.endswith('_metadata.yml'):
        return None, None, None, None, False

    metadata_path = os.path.join(meta_dir, filename)
    metadata = load_metadata(metadata_path)
    if metadata is None:
        print(f"Error loading metadata from: {metadata_path}")
        return None, None, None, None, False

    if not is_compatible(metadata, current_system, current_version):
        return None, None, None, None, False

    description, rationale, cvss_score = obtain_metadata_info(metadata)
    metadata_info = [description, rationale, cvss_score]
    playbook_name = filename.replace('_metadata.yml', '.yml')
    playbook_path = os.path.join(role_path, 'tasks', playbook_name)
    return metadata_info, playbook_name, playbook_path, metadata, True
