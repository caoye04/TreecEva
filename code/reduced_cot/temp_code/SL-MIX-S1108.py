import re
from functools import lru_cache

class LogFileHandler:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'w')
        self.file.write('192.168.1.1 - - [01/Jan/2023:00:00:01 +0000] "GET /index.html HTTP/1.1" 200 1234\n')
        self.file.write('10.0.0.5 - - [01/Jan/2023:00:00:02 +0000] "POST /login HTTP/1.1" 200 5678\n')
        self.file.write('192.168.1.1 - - [01/Jan/2023:00:00:03 +0000] "GET /profile HTTP/1.1" 200 9012\n')
        self.file.write('172.16.0.10 - - [01/Jan/2023:00:00:04 +0000] "GET /index.html HTTP/1.1" 200 1234\n')
        self.file.write('10.0.0.5 - - [01/Jan/2023:00:00:05 +0000] "GET /logout HTTP/1.1" 200 5678\n')
        self.file.close()
        self.file = open(self.filename, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

@lru_cache(maxsize=128)
def is_valid_ip(ip):
    pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return bool(re.match(pattern, ip))

log_filename = 'server_access.log'
visitor_ips = set()

with LogFileHandler(log_filename) as log_file:
    for line in log_file:
        match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
        if match:
            ip = match.group(1)
            if is_valid_ip(ip):
                visitor_ips.add(ip)

unique_visitors_count = len(visitor_ips)
print(f'Result: {unique_visitors_count}')