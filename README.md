# 🔍 Subenum — Subdomain Enumeration Tool

Subenum is a Python-based subdomain enumeration tool designed for bug bounty hunters, penetration testers, and cybersecurity researchers.

---

## ✅ Features

- Passive Enumeration using [crt.sh](https://crt.sh)
- Bruteforce Enumeration using DNS resolution
- Saves results to output file
- Clean CLI interface
- Easy to customize and expand

---

## 🚀 Usage

```bash
# Passive Enumeration
python3 subenum.py --domain example.com --passive

# Bruteforce Enumeration
python3 subenum.py --domain example.com --brute --wordlist wordlists/top100.txt

# Both
python3 subenum.py --domain example.com --passive --brute --wordlist wordlists/top100.txt
