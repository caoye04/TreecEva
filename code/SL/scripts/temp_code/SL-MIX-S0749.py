import re
from functools import reduce

def threat_calculator(entries):
    scores = []
    for entry in entries:
        base_score = len(entry) if 'ALERT' in entry else 0
        ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', entry)
        ip_segments = ip_match.group().split('.') if ip_match else []
        segment_sum = sum(int(seg) for seg in ip_segments) if ip_segments else 0
        adjusted_score = base_score + (segment_sum // 10)
        scores.append(adjusted_score)
    return scores

def aggregate_threat(scores):
    return reduce(lambda x, y: x ^ y, scores, 0)

log_entries = [
    "INFO 192.168.1.10 Normal system operation",
    "ALERT 10.0.0.23 Suspicious login attempt",
    "DEBUG 172.16.254.1 Process started",
    "ALERT 10.0.0.45 Multiple failed authentications"
]

processed_scores = threat_calculator(log_entries)
final_threat_level = aggregate_threat(processed_scores)
print(f'Result: {final_threat_level}')