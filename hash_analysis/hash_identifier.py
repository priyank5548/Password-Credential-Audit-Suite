
def identify_hash(hash_value):
    if len(hash_value)==32:
        return "MD5"
    if len(hash_value)==40:
        return "SHA1"
    if len(hash_value)==64:
        return "SHA256"
    return "Unknown"
