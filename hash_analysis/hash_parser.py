import os

def extract_linux_hashes(shadow_path="/etc/shadow"):
    """
    Simulates or performs extraction of Linux shadow entries.
    In a real lab, this requires root/sudo.
    """
    extracted_data = []
    if not os.path.exists(shadow_path):
        return "[!] Shadow file not found. Ensure you are in a Linux lab environment."

    try:
        with open(shadow_path, 'r') as f:
            for line in f:
                parts = line.strip().split(':')
                if len(parts) > 1 and parts[1] not in ['*', '!']:
                    username = parts[0]
                    full_hash = parts[1]
                    # Format: $id$salt$hash
                    extracted_data.append({"user": username, "hash": full_hash})
        return extracted_data
    except PermissionError:
        return "[!] Permission Denied: Extraction requires root privileges."
