# Domain Fuzzing Tool

## Overview

This is a simple Python script for domain fuzzing, allowing you to test a list of domains with a specified wordlist to discover potential endpoints. It supports fuzzing a single target or a list of domains.

## Usage
python fuzzy.py -l domain1.com domain2.com -w wordlist.txt -o output.txt -mc 200

python fuzzy.py -f domains.txt -w wordlist.txt -o output.txt


### Prerequisites

- Python 3.x
- `requests` library: Install it using `pip install requests`
- `termcolor` library: Install it using `pip install termcolor`

### Running the Script

1. Clone or download the repository: git clone https://github.com/yourusername/domain-fuzzing-tool.git
