import requests
import json

def enumerate(domain):
    """
    
    Perform Passive Subdomain enumerating using crt,.sh
    
    Args:
        domain (str): The domain to enumerate
        
    Returns:
        set: A set of all discovered subdomains
        
    """
    
    subdomains = set()
    try:
        print("[*] Querying crt.sh ... ")
        # use crt.sh API to search for SSL certificates containing subdomains 
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response=requests.get(url,timeout=10)

        # if the request is successful , parse the JSON reponse
        
        if response.ok:
            data = json.loads(response.text)
            for entry in data:
                name = entry.get("name_value","")
                for sub in name.split("\\n")
                    # add subdomains related to the domain
                    if domain in sub:
                        subdomains.add(sub.strip())
    except Exception as e:
        print(f"[!] Error Querying crt.sh {e}")

    return subdomains