![Python](https://img.shields.io/badge/Python-3.x-blue)
![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red)
![Project](https://img.shields.io/badge/Project-Password%20Audit-green)

# Password Cracking & Credential Attack Suite

This project is a practical cybersecurity toolkit that demonstrates how weak passwords are exploited and how authentication systems can be strengthened through password auditing and analysis.

This project simulates password attack techniques in a **controlled, ethical lab environment** and generates a detailed password security audit report.

---

## Project Objective

Weak passwords are one of the most exploited vulnerabilities in cybersecurity. This project helps you understand:

- Dictionary and brute-force attack techniques
- How password hashes are stored in Linux and Windows
- Entropy and policy-based strength evaluation
- Practical password security auditing

> All techniques are implemented strictly for educational and defensive security purposes.

---

## Features

### Red Team Simulation
- Dictionary generator using username and DOB patterns
- Dictionary attack simulation
- Real-time brute-force demo for short passwords
- Linux shadow hash extraction (demo)
- Windows SAM hash parsing (demo)

### Blue Team Analysis
- Entropy-based strength calculation
- Password policy validation
- Weak password detection
- Security recommendations

### Reporting
- Automatic `audit_report.txt` generation
- Weak / Moderate / Strong rating
- Actionable mitigation suggestions

---

## Project Structure

```
main.py

dictionary/
  generator.py
  mutations.py

attack_simulator/
  dictionary_sim.py
  brute_force_sim.py

hash_analysis/
  hash_parser.py
  hash_identifier.py
  sam_parser.py

strength_analyzer/
  entropy_calc.py
  policy_checker.py

reporting/
  audit_report.py

screenshots/
```

---

## Workflow

1. User enters username, DOB, password
2. Dictionary wordlist is generated
3. Dictionary attack simulation is performed
4. Entropy & policy checks are applied
5. Password strength is evaluated
6. Audit report is created

---

## Sample Results

| Password Type | Result |
|---------------|--------|
| Strong complex password | STRONG |
| Username + DOB pattern | WEAK |
| Numeric only password | WEAK |

Screenshots in the `screenshots` folder.

---

## How to Run

```bash
python main.py
```

---

## Output

Produces:

`audit_report.txt`

Containing:
- Entropy score
- Dictionary match result
- Policy issues
- Final rating
- Mitigation suggestions

---

## Security Notice

This project is strictly for educational purposes.  
No real password cracking is performed on live systems.

---

## Learning Outcomes

- Understanding password attack methods
- Understanding secure password storage
- Perform password security audits
