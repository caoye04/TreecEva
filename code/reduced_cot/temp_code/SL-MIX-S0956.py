import base64
import math
from collections import Counter

def xor_cipher(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

def calculate_shannon_entropy(s):
    counts = Counter(s)
    total_chars = len(s)
    entropy = 0.0
    for count in counts.values():
        probability = count / total_chars
        entropy -= probability * math.log2(probability)
    return entropy

# Initial log entries
log_entries = [
    "USER_LOGIN_SUCCESS",
    "FILE_ACCESS_GRANTED",
    "DATA_EXPORT_INITIATED",
    "SECURITY_SCAN_COMPLETED"
]

# Encoding parameters
xor_key = "Cyb3rS3cur1ty"
encoded_logs = []

for entry in log_entries:
    # Step 1: Base64 encode the entry
    b64_encoded = base64.b64encode(entry.encode()).decode()
    # Step 2: Apply XOR cipher with rotating key
    encrypted = xor_cipher(b64_encoded, xor_key)
    encoded_logs.append(encrypted)

# Combine all encoded logs into one string
combined_logs = ''.join(encoded_logs)

# Convert to set to get unique characters
unique_chars = frozenset(combined_logs)

# Calculate entropy of unique character set
char_string = ''.join(unique_chars)
entropy_per_char = [calculate_shannon_entropy(c*10) for c in char_string]  # Amplify for measurement

# Compute final entropy score
final_entropy_score = round(sum(
    (i + 1) * entropy_val 
    for i, entropy_val in enumerate(entropy_per_char)
), 2)

print(f"Result: {final_entropy_score}")