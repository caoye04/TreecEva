import re
from functools import reduce

def preprocess_headers(packet_headers):
    return [header.strip().lower() for header in packet_headers]

def calculate_base_scores(processed_headers):
    scores = []
    for header in processed_headers:
        if re.search(r'authorization:\s*bearer\s+[a-z0-9]{32}', header):
            scores.append(10)
        elif re.search(r'cookie:\s*sessionid=[a-f0-9]{32}', header):
            scores.append(7)
        elif 'x-forwarded-for' in header:
            scores.append(3)
        else:
            scores.append(0)
    return scores

def apply_modifiers(scores, modifiers):
    return [score + mod for score, mod in zip(scores, modifiers)]

def compute_weighted_sum(scores):
    weights = [i for i in range(len(scores), 0, -1)]
    return sum(score * weight for score, weight in zip(scores, weights))

# Simulated packet headers
packet_sequence = [
    "Authorization: Bearer abcdef1234567890abcdef1234567890",
    "User-Agent: Mozilla/5.0",
    "Cookie: sessionid=1234567890abcdef1234567890abcdef; path=/",
    "X-Forwarded-For: 192.168.1.100",
    "Content-Type: application/json"
]

processed_headers = preprocess_headers(packet_sequence)
base_scores = calculate_base_scores(processed_headers)
modifiers = [1 if 'bearer' in h or 'sessionid' in h else 0 for h in processed_headers]
modified_scores = apply_modifiers(base_scores, modifiers)
final_anomaly_score = compute_weighted_sum(modified_scores)

print(f"Result: {final_anomaly_score}")