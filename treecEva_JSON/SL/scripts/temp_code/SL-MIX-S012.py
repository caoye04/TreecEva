import re

def check_suspicious_ips():
    log_ips = [
        '192.168.1.205',
        '10.0.0.50',
        '192.168.5.199',
        '192.168.10.255',
        '172.16.0.1',
        '192.168.20.201',
        '192.168.30.150'
    ]
    
    pattern = r'^192\.\d+\.\d+\.(\d+)$'
    suspicious_count = 0
    
    for ip in log_ips:
        match = re.match(pattern, ip)
        # Short-circuit evaluation: only check the octet condition if regex matches
        if match and int(match.group(1)) > 200:
            suspicious_count += 1
    
    return suspicious_count

result = check_suspicious_ips()
print(f"Result: {result}")