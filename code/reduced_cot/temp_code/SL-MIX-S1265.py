import re
from functools import reduce

# Security log entries with timestamps and messages
log_entries = [
    "2023-10-01 14:30:00 SELECT * FROM users WHERE id = 1 OR 1=1",
    "2023-10-01 14:31:15 Normal user login attempt",
    "2023-10-01 14:32:30 DROP TABLE users; -- malicious command",
    "2023-10-01 14:33:45 User updated profile information",
    "2023-10-01 14:34:50 UNION SELECT username, password FROM admin_credentials",
    "2023-10-01 14:35:05 Regular API call for data retrieval"
]

# Define suspicious patterns and their base weights
suspicious_patterns = {
    r'(UNION|SELECT).*FROM': 20,
    r'DROP TABLE': 25,
    r'OR 1=1': 15
}

severity_keywords = ['malicious', 'DROP', 'UNION']

# Step 1: Filter logs with suspicious SQL patterns
suspicious_logs = list(filter(lambda log: any(re.search(pattern, log) for pattern in suspicious_patterns.keys()), log_entries))

# Step 2: Calculate weighted scores for suspicious logs
weighted_scores = []
for log in suspicious_logs:
    base_score = sum(weight for pattern, weight in suspicious_patterns.items() if re.search(pattern, log))
    severity_multiplier = 2 if any(keyword in log for keyword in severity_keywords) else 1
    weighted_scores.append(base_score * severity_multiplier)

# Step 3: Apply normalization using bitwise operations
normalized_scores = [score & 0xFF for score in weighted_scores]  # Mask to 8-bit values

# Step 4: Combine scores using XOR reduction
final_security_score = reduce(lambda x, y: x ^ y, normalized_scores, 0)

# Step 5: Final adjustment based on number of suspicious logs
if len(suspicious_logs) > 3:
    final_security_score |= 0x100  # Set 9th bit if many threats detected
else:
    final_security_score &= ~0x100  # Clear 9th bit otherwise

print(f"Result: {final_security_score}")