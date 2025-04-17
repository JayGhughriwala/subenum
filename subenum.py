import argparse
import os
from modules import passive,bruteforce

def main():
    # argument parser setup
    parser=argparse.ArgumentParser(description="Subdomain Enumeration Tool")
    parser.add_argument("--domain",required=True,help="Target domain (e.g. example.com)")
    parser.add_argument("--passive",action="store_true", help="Use passive enumeration")
    parser.add_argument("--brute",action="store_true",help="Use bruteforce enumeration")
    parser.add_argument("--wordlist",help="Path to wodlist for bruteforce")
    args= parser.parse_args()
    
    domain=args.domain.strip() # clean up domain input
    
    results = set() # use set for storing unique subdomains
    
    
    # now perform passive enumeration if selected
    if args.passive:
        print(f"[*] Starting Passive enumeration for {domain} ...")
        passive_results=passive.enumerate(domain)
        results.update(passive_results)
        
    # perform bruteforce enumeration if selected
    if args.brute:
        if not args.wordlist or not os.path.exists(args.wordlist):
            print(f"[!] Please provide a valid wordlist with --wordlist")
            return
        print(f"[*] Starting brute-force enumeration for {domain} ...")
        brute_results=bruteforce.enumerate(domain,args.wordlist)
        results.update(brute_results)
        
    # ensure output directory exists or not
    if not os.path.exists("output"):
        os.makedirs("output")

    # now save results
    output_path = os.path.join("output",f"{domain}_subs.txt")
    with open(output_path,"w") as f:
        for sub in sorted(results):
            f.write(sub+"\n")
    print(f"[+] Found {len(results)} subdomains. Results Saved to {output_path}")



if __name__ == "__main__":
    main()