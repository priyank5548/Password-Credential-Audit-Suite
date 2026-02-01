import time
import itertools
import string

def run_real_brute_force(target_password, max_length=4):
    """
    Performs an actual incremental brute-force simulation for short passwords.
    """
    chars = string.ascii_letters + string.digits
    attempts = 0
    start_time = time.time()

    print(f"[*] Starting incremental simulation (Max Length: {max_length})...")
    
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess_str = ''.join(guess)
            if guess_str == target_password:
                duration = time.time() - start_time
                return True, attempts, round(duration, 4)
    
    return False, attempts, round(time.time() - start_time, 4)
