import re
from collections import namedtuple

# Define a LogEntry structure
LogEntry = namedtuple('LogEntry', ['timestamp', 'ip_address', 'user_agent'])

# Sample log entries
log_entries = [
    LogEntry('2023-05-15 10:23:01', '192.168.1.10', 'Mozilla/5.0'),
    LogEntry('2023-05-15 10:25:12', '192.168.1.12', 'Chrome/90.0'),
    LogEntry('2023-05-15 10:27:45', '10.0.0.5', 'Safari/14.0'),
    LogEntry('2023-05-15 10:30:01', '192.168.1.10', 'Mozilla/5.0'),
    LogEntry('2023-05-15 10:32:17', '192.168.2.15', 'Firefox/88.0'),
    LogEntry('2023-05-15 10:35:22', '172.16.0.1', 'Edge/91.0')
]

# Extract IP addresses matching the pattern 192.168.x.x
subnet_pattern = r'^192\.168\.\d{1,3}\.\d{1,3}$'
suspicious_ips = {entry.ip_address for entry in log_entries if re.match(subnet_pattern, entry.ip_address)}

# Count unique device IPs
unique_device_count = len(suspicious_ips)
print(f'Result: {unique_device_count}')