import re

def calculate_threat_score(log_entry):
    score = 0
    # Check for IP addresses
    if re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', log_entry):
        score += 10
    # Check for SQL injection patterns
    if re.search(r'(UNION|SELECT|INSERT)', log_entry, re.IGNORECASE):
        score += 20
    # Check for excessive failed attempts
    if 'failed login' in log_entry.lower():
        score += 5
    # Bonus for suspicious user agents
    if 'bot' in log_entry.lower() or 'crawler' in log_entry.lower():
        score += 15
    return score

log_entries = [
    "192.168.1.100 attempted UNION SELECT attack",
    "User agent: Mozilla/5.0 bot detected with failed login attempt",
    "Normal traffic from 10.0.0.5",
    "SQL INSERT injection detected without IP"
]

threat_scores = []
with open('temp_log.txt', 'w') as f:
    for entry in log_entries:
        f.write(entry + '\n')

accumulated_score = 0
with open('temp_log.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    processed_entries = [line for line in lines if line]  # Filter out empty lines
    threat_scores = [calculate_threat_score(entry) for entry in processed_entries]
    accumulated_score = sum(threat_scores) if threat_scores else 0
    is_high_risk = accumulated_score > 30
    final_score = accumulated_score * 2 if is_high_risk else accumulated_score

print(f"Result: {final_score}")