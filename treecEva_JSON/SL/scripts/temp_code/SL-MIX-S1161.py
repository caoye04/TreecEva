import re
from collections import defaultdict

def calculate_anomaly_points(entry):
    points = 0
    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', entry) and 'failed' in entry.lower():
        points += 5
    if 'admin' in entry.lower() or 'root' in entry.lower():
        points += 3
    return points

log_entries = [
    "Authentication failed for user admin from 192.168.1.105",
    "User john_doe logged in successfully",
    "Failed login attempt for root from 10.0.0.23",
    "File access granted to guest_user",
    "Unauthorized access attempt from 172.16.254.1"
]

anomaly_counter = defaultdict(int)
intrusion_score = 0
threshold = 4

for idx, entry in enumerate(log_entries):
    points = calculate_anomaly_points(entry)
    anomaly_counter[points] += 1
    if points > 0:
        intrusion_score += points
    if intrusion_score >= threshold and (lambda x: x % 2 == 0)(idx):
        intrusion_score <<= 1
    elif intrusion_score > threshold or (lambda y: y > 10)(len(entry)):
        intrusion_score += 1

final_adjustment = sum(k*v for k, v in anomaly_counter.items() if k > 3)
intrusion_score ^= final_adjustment

print(f"Result: {intrusion_score}")