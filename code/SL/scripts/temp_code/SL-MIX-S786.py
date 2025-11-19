import re

def is_valid_ipv4(ip):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return bool(re.match(pattern, ip))

candidate_ips = ['192.168.1.1', '256.1.1.1', '10.0.0.0', '172.16.254.3', '999.999.999.999']
verified_malicious_count = 0

for ip in candidate_ips:
    if is_valid_ipv4(ip):
        octets = list(map(int, ip.split('.')))
        if (octets[0] & 0b11110000) == 0b00000000:  # Check if first octet has specific bit pattern
            verified_malicious_count += 1

print(f'Result: {verified_malicious_count}')