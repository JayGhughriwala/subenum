import requests
import json

def enumerate(domain):
    """
    Perform passive subdomain enumeration using crt.sh

    Args:
        domain (str): The domain to enumerate

    Returns:
        set: A set of discovered subdomains
    """
    subdomains = set()

    try:
        print("[*] Querying crt.sh ...")
        # Use crt.sh API to search for SSL certificates containing subdomains
        url = f"https://crt.sh/?q=%25.{domain}&output=json"
        response = requests.get(url, timeout=10)

        # If the request is successful, parse the JSON response
        if response.ok:
            data = json.loads(response.text)
            for entry in data:
                name = entry.get("name_value", "")
                for sub in name.split("\\n"):
                    # Add subdomains related to the domain
                    if domain in sub:
                        subdomains.add(sub.strip())
    except Exception as e:
        print(f"[!] Error querying crt.sh: {e}")

    return subdomains
