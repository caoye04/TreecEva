import re
from collections import defaultdict

def analyze_security_logs(log_entries):
    # Group failures by IP
    failure_times = defaultdict(list)
    
    for timestamp, ip, status in log_entries:
        if status == 'failure':
            # Validate IP format using pattern matching
            if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip):
                failure_times[ip].append(timestamp)
    
    suspicious_ips = set()
    
    for ip, times in failure_times.items():
        times.sort()
        # Check for any 10-minute window with >3 failures
        for i in range(len(times)):
            count = 1  # Count the current failure
            for j in range(i+1, len(times)):
                # Early break if outside 10-minute window
                if times[j] - times[i] > 10:
                    break
                count += 1
                # Early return equivalent - stop checking this window if threshold met
                if count > 3:
                    suspicious_ips.add(ip)
                    break
            # Another early break - if IP already flagged, no need to check other windows
            if ip in suspicious_ips:
                break
    
    return len(suspicious_ips)

# Log data: (timestamp_in_minutes, ip_address, status)
security_logs = [
    (0, '192.168.1.10', 'failure'),
    (2, '192.168.1.10', 'failure'),
    (3, '192.168.1.10', 'failure'),
    (5, '192.168.1.10', 'failure'),
    (6, '192.168.1.10', 'failure'),
    (1, '10.0.0.5', 'failure'),
    (15, '10.0.0.5', 'failure'),
    (30, '10.0.0.5', 'failure'),
    (45, '10.0.0.5', 'failure'),
    (2, '172.16.0.1', 'success'),
    (4, '172.16.0.1', 'failure'),
    (6, '172.16.0.1', 'failure'),
    (8, '172.16.0.1', 'failure'),
    (9, '172.16.0.1', 'failure'),
    (10, '172.16.0.1', 'failure'),
    (50, '172.16.0.1', 'failure')
]

alert_count = analyze_security_logs(security_logs)
print(f"Result: {alert_count}")