def extract_remediation(remediation_tip):
    """
    Extracts and returns the part of the 'remediation_tip' string that follows the '[Remediation]' marker.
    
    Args:
        remediation_tip (str): The string from which you want to extract the content after '[Remediation]'.

    Returns:
        str: The content after '[Remediation]' if found, otherwise None.
    """
    try:
        try:
            remediation_tip = remediation_tip.replace('{"', '').replace('"}', '')
            # Find the position of the '[Remediation]' marker in the string
            remediation_start = remediation_tip.index('[Remediation]')
            # If found, extract and return the content following the marker.
            remediation_start += len('[Remediation]')
            remediation_str = remediation_tip[remediation_start:]
            return remediation_str
        except ValueError:
            print("[Remediation] not found")
    
    except Exception as e:
        print(f"Error al procesar la cadena: {e}")
