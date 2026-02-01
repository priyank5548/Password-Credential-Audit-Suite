def generate_report(password, entropy, dict_hit, policy_issues, rating):
    with open("audit_report.txt", "w") as f:
        f.write("Password Security Audit Report\n")
        f.write("=" * 35 + "\n\n")

        f.write(f"Password Length: {len(password)}\n")
        f.write(f"Entropy Score: {entropy}\n")
        f.write(f"Dictionary Match: {'YES' if dict_hit else 'NO'}\n")
        f.write(f"Final Rating: {rating}\n\n")

        f.write("Vulnerability Analysis:\n")
        if policy_issues or dict_hit:
            if dict_hit:
                f.write("- CRITICAL: Password found in common pattern dictionary.\n")
            for issue in policy_issues:
                f.write(f"- {issue}\n")
        else:
            f.write("- No immediate policy vulnerabilities detected.\n")

        # NEW: Mitigation Section required by documentation
        f.write("\nRecommended Mitigations & Policies:\n")
        f.write("1. Enforce a minimum length of 12-14 characters.\n")
        f.write("2. Implement account lockout after 5 failed brute-force attempts.\n")
        f.write("3. Use Salting (e.g., Argon2 or bcrypt) for secure storage.\n")
        f.write("4. Discourage use of personal data (DOB, username) in passwords.\n")
