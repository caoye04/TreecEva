from collections import Counter
from functools import reduce
import base64

# Encoded payloads from network traffic
encoded_payloads = ["SGVsbG8=", "V29ybGQ=", "Q2hlY2s=", "Q29kZQ==", "SGFja3M="]

# Decoding and scoring function
def calculate_anomaly_score(decoded_string):
    char_freq = Counter(decoded_string)
    unique_chars = len(char_freq)
    total_chars = sum(char_freq.values())
    # Ternary operator to determine base score
    base_score = 10 if total_chars > 5 else 5
    # Adjust score based on character diversity
    diversity_ratio = unique_chars / total_chars if total_chars > 0 else 0
    adjusted_score = base_score * diversity_ratio
    return adjusted_score

# Process payloads
anomaly_scores = []
for payload in encoded_payloads:
    decoded_payload = base64.b64decode(payload).decode('utf-8')
    score = calculate_anomaly_score(decoded_payload)
    anomaly_scores.append(score)

# Calculate final threat score using functional programming
threat_score = reduce(lambda acc, x: acc + (x * 2 if x > 7 else x), anomaly_scores, 0)

# Apply final adjustment with ternary operator
threat_score = threat_score if threat_score < 100 else threat_score * 0.9

print(f"Target result: {threat_score}")