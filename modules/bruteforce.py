import socket
import requests
import json

def enumerate(domain,wordlist_path):
    """
    
    Perform Passive Subdomain enumerating using crt,.sh
    
    Args:
        domain (str): The domain to enumerate
        
    Returns:
        set: A set of all discovered subdomains
        
    """
    subdomains=set()
    
    # read wordlist line by line
    with open(wordlist_path,'r') as f:
        for line in f:
            sub = line.strip()
            if not sub:
                continue
            
            
            full_domain = f"{sub}.{domain}"
            try:
                # attempt DNS resolution
                
                socket.gethostbyname(full_domain)
                print(f"[+] Found: {full_domain}")
                subdomains.add(full_domain)
            except socket.gaierror:
                # skip domain that not resolve
                pass
            
    return subdomains