from Wappalyzer import Wappalyzer, WebPage
import csv
import requests
import subprocess
import warnings
import sys 
 
# Ignore specific UserWarnings from Wappalyzer
warnings.filterwarnings("ignore", message="Caught 'unbalanced parenthesis at position 119' compiling regex")
 
def find_subdomains(domain):
    # Run the subfinder command and capture the output
    result = subprocess.run(['subfinder', '-d', domain, '-silent'], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.splitlines()
    else:
        print(f"Error finding subdomains for {domain}: {result.stderr}")
        return []
 
def check_https(url):
    try:
        # Try connecting with HTTPS
        response = requests.get(f"https://{url}", timeout=5)
        if response.status_code == 200:
            return f"https://{url}"
    except requests.ConnectionError:
        pass
    # Fallback to HTTP if HTTPS fails
    return f"http://{url}"
 
def analyze_urls():
    wappalyzer = Wappalyzer.latest()
 
    # Open the CSV file for writing
    with open('results.csv', 'w', newline='') as csvfile:
        fieldnames = ['domain', 'technology', 'version', 'categories']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
 
        # Read domains from a file
        with open('domains.txt', 'r') as file:
            domains = file.read().splitlines()
 
        for domain in domains:
            if domain:
                subdomains = find_subdomains(domain)
                for subdomain in subdomains:
                    url = check_https(subdomain)  # Check and prepend the correct scheme
                    attempts = 0
                    success = False
                    while attempts < 3 and not success:  # Retry logic for robustness
                        try:
                            # Increase timeout to handle slow responses
                            webpage = WebPage.new_from_url(url, timeout=40)
                            analysis_results = wappalyzer.analyze_with_versions_and_categories(webpage)
                            success = True  # Mark success if no exception was raised
 
                            for tech, details in analysis_results.items():
                                versions = details.get('versions', [])
                                version = versions[0] if versions else ''  
                                categories = ', '.join(details.get('categories', []))  
 
                                row = {
                                    'domain': url,
                                    'technology': tech,
                                    'version': version,
                                    'categories': categories
                                }
                                writer.writerow(row)
                        except requests.exceptions.ReadTimeout:
                            attempts += 1
                            print(f"Timeout on {url}, attempt {attempts}")
                        except Exception as e:
                            writer.writerow({'domain': url, 'technology': 'Error', 'version': str(e), 'categories': ''})
                            break  # Exit the retry loop on non-timeout exceptions

def print_banner():
    banner = """
 ██╗    ██╗███████╗██████╗     ██╗███╗   ██╗███████╗██████╗ ███████╗ ██████╗████████╗
██║    ██║██╔════╝██╔══██╗    ██║████╗  ██║██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝
██║ █╗ ██║█████╗  ██████╔╝    ██║██╔██╗ ██║███████╗██████╔╝█████╗  ██║        ██║   
██║███╗██║██╔══╝  ██╔══██╗    ██║██║╚██╗██║╚════██║██╔═══╝ ██╔══╝  ██║        ██║    
╚███╔███╔╝███████╗██████╔╝    ██║██║ ╚████║███████║██║     ███████╗╚██████╗   ██║   
 ╚══╝╚══╝ ╚══════╝╚═════╝     ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   
                                                                                    
    """
    print(banner)
    print("Starting Web Inspect...")

 
if __name__ == "__main__":
    print_banner()
   # analyze_urls()
    try:
        analyze_urls()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting...")
        sys.exit(0)
