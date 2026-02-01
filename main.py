from dictionary.generator import generate_dictionary
from attack_simulator.dictionary_sim import simulate_dictionary_attack
from strength_analyzer.entropy_calc import calculate_entropy
from strength_analyzer.policy_checker import check_policy
from reporting.audit_report import generate_report

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def main():
    print("\n=== Password Security Assessment Toolkit ===\n")

    username = input("[?] Enter username (for dictionary simulation): ")
    year = input("[?] Enter year/DOB (optional, press Enter to skip): ")
    password = input("[?] Enter password to analyze: ")

    print("\n[+] Generating dictionary...")
    wordlist = generate_dictionary(username, year)

    print("[+] Simulating dictionary attack...")
    dict_hit = simulate_dictionary_attack(wordlist, password)

    print("[+] Analyzing password strength...")
    entropy = calculate_entropy(password)
    policy_issues = check_policy(password)
    
    # Real-time brute-force simulation for short passwords
    if len(password) <= 4:
        from attack_simulator.brute_force_sim import run_real_brute_force
        print(f"\n[!] Short password ({len(password)} chars) detected. Running active demo...")
        found, tries, sec = run_real_brute_force(password)
        if found:
            print(f"    {RED}[!] CRACKED in {tries} attempts ({sec} seconds)!{RESET}")

    print("\n=== Analysis Result ===")
    print(f"• Password length: {len(password)}")
    print(f"• Entropy score: {entropy}")

    if dict_hit:
        print(f"• Dictionary analysis: {RED}[MATCH FOUND]{RESET}")
    else:
        print(f"• Dictionary analysis: {GREEN}[NOT FOUND]{RESET}")

    if policy_issues:
        print("• Policy issues detected:")
        for issue in policy_issues:
            print(f"  - {issue}")
    else:
        print(f"• Password policy: {GREEN}[COMPLIANT]{RESET}")

    # FINAL RATING LOGIC (NO CONTRADICTION)
    if entropy < 40 or dict_hit or policy_issues:
        rating = "WEAK"
    elif entropy < 70:
        rating = "MODERATE"
    else:
        rating = "STRONG"

    print(f"\n[!] Overall Rating: {rating}")

    generate_report(password, entropy, dict_hit, policy_issues, rating)
    print("\n[+] Audit report generated: audit_report.txt")

if __name__ == "__main__":
    main()
