def simulate_dictionary_attack(wordlist, password):
    # Direct dictionary hit
    if password in wordlist:
        return True

    # Common numeric patterns attackers always try
    if password.isdigit():
        if len(password) in [6, 8]:
            return True

    return False
