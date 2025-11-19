import re
from functools import reduce

def compute_log_hash(log_entry):
    return sum(ord(char) << (i % 8) for i, char in enumerate(log_entry))

def extract_patterns(log_batch):
    pattern_scores = {}
    for log in log_batch:
        matches = re.findall(r'\b(attack|breach|malware|phishing)\b', log, re.IGNORECASE)
        for match in matches:
            pattern_scores[match.lower()] = pattern_scores.get(match.lower(), 0) + 1
    return pattern_scores

def calculate_threat_score(pattern_dict, log_hashes):
    base_score = sum(hash_val % 100 for hash_val in log_hashes)
    pattern_bonus = sum(count**2 for count in pattern_dict.values())
    return base_score + pattern_bonus

# Log batch processing
log_entries = [
    "User attempted unauthorized access - possible attack vector",
    "Detected malware signature in network traffic",
    "Phishing email bypassed initial filters",
    "System breach reported from external IP",
    "Normal system operation with no anomalies"
]

# Hash computation for each log entry
entry_hashes = list(map(compute_log_hash, log_entries))

# Pattern extraction and frequency mapping
threat_patterns = extract_patterns(log_entries)

# Greedy selection of top threat indicators
top_indicators = dict(sorted(threat_patterns.items(), key=lambda x: x[1], reverse=True)[:3])

# Dynamic programming optimization for threat response
response_costs = [10, 20, 30, 40, 50]
n = len(response_costs)
dp_table = [float('inf')] * (n+1)
dp_table[0] = 0
for i in range(1, n+1):
    for j in range(i):
        dp_table[i] = min(dp_table[i], dp_table[j] + response_costs[i-1])

# Final threat calculation incorporating DP optimization
threat_base = calculate_threat_score(top_indicators, entry_hashes)
optimization_factor = dp_table[-1] // 10
final_threat_score = threat_base - optimization_factor

print(f"Result: {final_threat_score}")