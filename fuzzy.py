import os
import requests
import argparse
from termcolor import colored

header = colored(r'''
█▀▀ █░░█ ▀▀█ ▀▀█ █░░█ 
█▀▀ █░░█ ▄▀░ ▄▀░ █▄▄█ 
▀░░ ░▀▀▀ ▀▀▀ ▀▀▀ ▄▄▄█

Kaiz3nn | Dhane Ashley Diabajo''', 'green')

print(header)

def colorize_status_code(status_code):
    if status_code == 200:
        return colored(str(status_code), 'green')
    elif status_code == 403:
        return colored(str(status_code), 'blue')
    elif status_code == 404:
        return colored(str(status_code), 'red')
    elif status_code >= 500 and status_code < 600:
        return colored(str(status_code), 'orange')
    else:
        return str(status_code)

def fuzz_domains(domains, wordlist, output_file, match_code):
    with open(wordlist, 'r') as fuzz_file:
        fuzz_words = [line.strip() for line in fuzz_file.readlines()]

    with open(output_file, 'w') as output:
        for domain in domains:
            for fuzz_word in fuzz_words:
                try:
                    url = f"{domain}/{fuzz_word}"
                    response = requests.get(url, timeout=5)
                    status_colored = colorize_status_code(response.status_code)

                    if not match_code or response.status_code == match_code:
                        output.write(f"[{status_colored}] {url}\n")

                    print(f"[{status_colored}] {url}")

                except requests.RequestException as e:
                    print(colored(f"[-] Error with {url}: {e}", 'red'))

def main():
    parser = argparse.ArgumentParser(description="Simple domain fuzzing tool.")
    parser.add_argument("-l", "--domains", nargs="+", help="List of domains separated by space")
    parser.add_argument("-f", "--file", help="File containing domains")
    parser.add_argument("-w", "--wordlist", required=True, help="Fuzzing wordlist filename")
    parser.add_argument("-o", "--output", default="output.txt", help="Output filename (default: output.txt)")
    parser.add_argument("-mc", "--match-code", type=int, help="Filter codes to match (e.g., 200)")

    args = parser.parse_args()

    if not args.domains and not args.file:
        print("Error: Please provide either a list of domains or a file containing domains.")
        return

    if args.domains:
        domains = args.domains
    else:
        with open(args.file, 'r') as file:
            domains = [line.strip() for line in file.readlines()]

    fuzz_domains(domains, args.wordlist, args.output, args.match_code)

if __name__ == "__main__":
    main()
