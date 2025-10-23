import re
from functools import reduce

def calculate_base_score(payload):
    return sum(ord(c) for c in payload if c.isalnum())

def is_suspicious_pattern(payload):
    return bool(re.search(r'[0-9]{4,}', payload))

def contains_hex_sequences(payload):
    return bool(re.search(r'[a-fA-F0-9]{6,}', payload))

# Encoded payload data
encoded_payload = "X5k9#abcd1234#ZmFsc2U="  # Base64 for 'false'

# Decoding step
import base64
decoded_payload = base64.b64decode(encoded_payload.split('#')[2]).decode('utf-8')

# Pattern analysis
suspicious_flags = {
    'has_long_digits': is_suspicious_pattern(decoded_payload),
    'has_hex_sequences': contains_hex_sequences(decoded_payload),
    'is_non_printable': any(not c.isprintable() for c in decoded_payload)
}

# Scoring logic
base_score = calculate_base_score(decoded_payload)
suspicion_indicators = frozenset(flag for flag, value in suspicious_flags.items() if value)
indicator_weights = {'has_long_digits': 10, 'has_hex_sequences': 15, 'is_non_printable': 20}

# Calculate weighted suspicion score using dictionary comprehension and set operations
weighted_scores = {indicator: indicator_weights[indicator] for indicator in suspicion_indicators}
suspicion_score = sum(weighted_scores.values()) if weighted_scores else 0

# Final threat calculation with short-circuit logic
threat_score = base_score + suspicion_score if not (suspicious_flags['is_non_printable'] and len(decoded_payload) > 10) else 0

print(f"Result: {threat_score}")