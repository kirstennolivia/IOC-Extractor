# IOC-Extractor
A Python command-line tool that extracts Indicators of Compromise (IOCs) 
from clipboard text using regex and exports them to a text file.


# Requirements
- Python 3
- pyperclip (`pip install pyperclip`)

# Features
Extracts IOCs via text from clipboard and filters for:
MD5 Hashes
Domains
IP Addresses
CVEs

And exports to a text file.

# How to Run 
python IOCExtractor.py

# Example Output
Domains Found:
-malware-site.com
-phishing-page.com
-company.com

MD5 Hashes Found:
-5d41402abc4b2a76b9719d911017c592
-7215ee9c7d9dc229d2921a40e899ec5f

IP Addresses Found:
-192.168.1.105
-10.0.0.254
-172.16.0.1

CVEs Found:
-CVE-2021-44228
-CVE-2019-0708

IOCs exported to IOCs.txt

# Built With
Python3
