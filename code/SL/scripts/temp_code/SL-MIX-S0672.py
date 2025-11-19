import re
import statistics

def is_suspicious_packet(size):
    size_str = str(size)
    return bool(re.match(r'^(\d).*\1$', size_str))

packet_log = [202, 1024, 515, 1001, 999, 404, 777, 8008, 121, 303]
suspicious_sizes = [s for s in packet_log if is_suspicious_packet(s)]

anomaly_count = 0
if suspicious_sizes and statistics.mean(suspicious_sizes) > 500:
    anomaly_count = len([s for s in suspicious_sizes if s > statistics.mean(suspicious_sizes)])
else:
    anomaly_count = -1

print(f"Result: {anomaly_count}")