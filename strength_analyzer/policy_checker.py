import string

def check_policy(password):
    issues = []

    if len(password) < 8:
        issues.append("Password too short")

    if password.isdigit():
        issues.append("Password is numeric only")

    if not any(c.isupper() for c in password):
        issues.append("No uppercase letters")

    if not any(c.islower() for c in password):
        issues.append("No lowercase letters")

    if not any(c.isdigit() for c in password):
        issues.append("No digits")

    if not any(c in string.punctuation for c in password):
        issues.append("No special characters")

    return issues
