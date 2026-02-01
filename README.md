!\[Python](https://img.shields.io/badge/Python-3.x-blue)

!\[Security](https://img.shields.io/badge/Domain-Cybersecurity-red)

!\[Type](https://img.shields.io/badge/Project-Password%20Audit-green)



\# Password Cracking \& Credential Attack Suite



A practical cybersecurity toolkit that demonstrates how weak passwords are exploited and how authentication systems can be strengthened through password auditing and analysis.



This project simulates common password attack techniques in a \*\*controlled, ethical lab environment\*\* and generates a detailed password security audit report.



---



\## Project Objective



Weak passwords remain one of the most exploited vulnerabilities in cybersecurity. This project helps in understanding:



\- Dictionary and brute-force attack methodologies

\- How password hashes are stored in Linux and Windows systems

\- Entropy and password policy based strength evaluation

\- Practical password security auditing techniques



> ⚠️ All techniques are implemented for educational and defensive security purposes only.



---



\## Features



\### 🔴 Red Team Simulation

\- Dictionary generator using username and DOB patterns

\- Dictionary attack simulation

\- Real-time brute-force demo for passwords ≤ 4 characters

\- Linux shadow hash extraction (demo)

\- Windows SAM hash parsing using offline hives (demo)



\### 🔵 Blue Team Analysis

\- Entropy-based password strength calculation

\- Password policy validation (upper/lower/digits/symbols)

\- Weak password detection

\- Security recommendations for improvement



\### 📝 Reporting Engine

\- Automatic generation of `audit\_report.txt`

\- Rating: \*\*Weak / Moderate / Strong\*\*

\- Actionable mitigation policies



---



\## Project Structure



```

main.py



dictionary/

&nbsp; generator.py

&nbsp; mutations.py



attack\_simulator/

&nbsp; dictionary\_sim.py

&nbsp; brute\_force\_sim.py



hash\_analysis/

&nbsp; hash\_parser.py

&nbsp; hash\_identifier.py

&nbsp; sam\_parser.py



strength\_analyzer/

&nbsp; entropy\_calc.py

&nbsp; policy\_checker.py



reporting/

&nbsp; audit\_report.py



screenshots/

```



---



\## Workflow



1\. User inputs username, DOB, and password

2\. Dictionary wordlist is generated

3\. Dictionary attack simulation is performed

4\. Entropy and policy checks are applied

5\. Password strength is evaluated

6\. Audit report is generated



---



\## Sample Results



| Password Type | Result |

|--------------|--------|

| Strong complex password | STRONG |

| Username + DOB pattern | WEAK |

| Numeric only password | WEAK |



Screenshots available in the `screenshots` folder.



---



\## How to Run



```bash

python main.py

```



