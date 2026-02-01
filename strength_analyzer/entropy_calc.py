import math

def calculate_entropy(password):
    unique_chars = len(set(password))
    if unique_chars == 0:
        return 0
    return round(len(password) * math.log2(unique_chars), 2)
