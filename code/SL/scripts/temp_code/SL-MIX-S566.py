import re
from collections import Counter

def calculate_threat_level(log_entry):
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    
    # Count vowels and consonants
    vowel_count = sum(1 for char in log_entry if char in vowels)
    consonant_count = sum(1 for char in log_entry if char in consonants)
    
    # Check for suspicious patterns
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    has_ip = bool(re.search(ip_pattern, log_entry))
    
    hex_pattern = r'0x[0-9a-fA-F]+'
    hex_matches = re.findall(hex_pattern, log_entry)
    
    # Calculate base score
    base_score = (vowel_count * 3) - (consonant_count * 2)
    
    # Adjust for IP addresses
    ip_adjustment = 10 if has_ip else 0
    
    # Adjust for hex values
    hex_values = [int(match, 16) for match in hex_matches]
    hex_adjustment = sum(hex_values) % 7 if hex_values else 0
    
    # Final calculation with ternary operator
    final_score = base_score + ip_adjustment + hex_adjustment if len(log_entry) > 20 else base_score - 5
    
    return final_score

# Log entries to analyze
log_entries = [
    "User login from 192.168.1.100 successful",
    "0x1A3F memory access violation detected",
    "System reboot initiated by admin",
    "Suspicious 0xB2C8 packet from 10.0.0.5"
]

# Process logs and calculate security metrics
threat_scores = [calculate_threat_level(entry) for entry in log_entries]
unique_scores = frozenset(threat_scores)
score_counter = Counter(threat_scores)

# Calculate weighted security score
weighted_sum = sum(score * count for score, count in score_counter.items())
average_score = weighted_sum // len(threat_scores)

# Apply final adjustment based on score distribution
score_range = max(unique_scores) - min(unique_scores)
final_security_score = average_score + (score_range if score_range > 10 else 0)

print(f"Result: {final_security_score}")