import argparse
import requests
import concurrent.futures
from coloredoutput import coloredoutput as co
import logging
import os
import pyfiglet
import sys

logging.basicConfig(filename='vhost_enumerator.log', level=logging.ERROR, format='%(asctime)s %(levelname)s: %(message)s')

def check_vhost(url):
    try:
        response = requests.get(url, timeout=5, allow_redirects=False)
        if response.status_code != 404:
            print(f"{co.brightblue(f'[+] Valid vhost found: {url}' ):<100} {co.brightgreen(f'Status code: {response.status_code}'):>10}")
            return url
        else:
            print(co.brightred(f"[-] Invalid vhost: {url}"))
    except requests.exceptions.RequestException as e:
        logging.error(f"Error checking vhost: {url} - {e}")
    return None

def check_vhosts(target_url, wordlist_path):
    valid_vhosts = []
    with open(wordlist_path, 'r') as wordlist_file:
        vhosts = [word.strip() for word in wordlist_file]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(lambda vhost: check_vhost(target_url.replace("SCAN", vhost)), vhosts)

    valid_vhosts = [vhost for vhost in results if vhost is not None]

    with open('valid_vhosts.txt', 'w') as output_file:
        output_file.write('\n'.join(valid_vhosts))

if __name__ == "__main__":
    if sys.platform == 'win32':
        banner = pyfiglet.Figlet(font='slant')
        print(banner.renderText('VHost Enumerator'))
    else:    
        os.system('figlet -f slant VHost Enumerator | lolcat')
    print()
    print(co.darkblue("Author: Shabari"),"\t\t",co.darkblue("Instagram: @_.sourcecode._"),"\n\n")
    print(co.yellow("Note: This tool is for educational purposes only."))
    print(co.yellow("I am not responsible for any misuse of this tool."))
    print()


    parser = argparse.ArgumentParser(description="VHostEnumerator - Discover valid virtual hosts")
    parser.add_argument("-u", "--url", type=str, required=True, help="Target URL")
    parser.add_argument("-w", "--wordlist", type=str, required=True, help="Path to wordlist file")
    args = parser.parse_args()


    print(co.brightgreen("The Url is: "), co.brightblue(f"{args.url}"))
    print()

    check_vhosts(args.url, args.wordlist)
