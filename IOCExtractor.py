import pyperclip
import re

text = pyperclip.paste()

#Finds domains
def domains(text):
    domain_1 = re.compile(r'[\w\-]+\.com')
    domain_match = domain_1.findall(text)

    print('Domains Found:')
    for domain in domain_match:
        print('-' + domain)
    return domain_match

#Finds hashes
def hash(text):
    md5_hash = re.compile(r'[0-9a-f]{32}')
    hash_match = md5_hash.findall(text)

    print('MD5 Hashes Found:')
    for hash in hash_match:
        print ('-'+ hash)
    return hash_match

#Finds IP Addresses
def ip_address(text):
    ip_addr = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    ip_match = ip_addr.findall(text)

    print('IP Addresses Found:')

    for ip in ip_match:

        print('-' + ip )
    return ip_match

#Finds CVEs
def cve(text):
    cves = re.compile(r'CVE-\d{4}-\d{1,5}')
    cve_match = cves.findall(text)

    print('CVEs Found:')
    for cve in cve_match:
        print('-' + cve )
    return cve_match

#Writes file with all matches
def export(domain_match, hash_match, ip_match, cve_match):
    with open('IOCs.txt', 'w') as file:
        file.write('Domains:\n')
        for domain in domain_match:
            file.write('- ' + domain + '\n')
        for hash in hash_match:
            file.write('- ' + hash + '\n')
        for ip in ip_match:
            file.write('- ' + ip + '\n')
        for cve in cve_match:
            file.write('- ' + cve + '\n')
    print('IOCs exported to IOCs.txt')

#Calls function and stores return value to pass to export function
domain_results = domains(text)
hash_results = hash(text)
ip_results = ip_address(text)
cve_results = cve(text)
export(domain_results, hash_results, ip_results, cve_results)




