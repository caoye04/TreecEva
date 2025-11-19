from collections import defaultdict, Counter
from functools import reduce
import base64

def calculate_base_score(header_data):
    return sum(ord(c) for c in header_data) % 17

def is_suspicious_pattern(pattern):
    return pattern.startswith('X-') and len(pattern) > 5

def decode_packet_header(encoded_header):
    try:
        decoded = base64.b64decode(encoded_header).decode('utf-8')
        return decoded if decoded.isprintable() else ''
    except:
        return ''

# Packet data stream
packet_headers = [
    'WFgtU3VzcGljaW91czoxMjM=',  # X-Suspicious:123
    'Tm9ybWFsLVBhY2tldA==',       # Normal-Packet
    'WFgtQXR0YWNrOkRBTkdFUg==',   # X-Attack:DANGER
    'U2VjcmV0LUluZm8=',           # Secret-Info
    'WFgtVHJhY2tlcltTVUNDRVNTXQ==' # X-Tracer[SUCCESS]
]

# Initialize tracking structures
threat_scores = defaultdict(int)
pattern_counter = Counter()

# Process each packet
for idx, encoded_header in enumerate(packet_headers):
    decoded_header = decode_packet_header(encoded_header)
    
    # Skip invalid headers
    if not decoded_header:
        continue
    
    # Update pattern counter
    pattern_parts = decoded_header.split(':')
    main_pattern = pattern_parts[0] if pattern_parts else decoded_header
    pattern_counter[main_pattern] += 1
    
    # Calculate base threat score
    base_score = calculate_base_score(decoded_header)
    
    # Apply suspicious pattern modifier
    is_suspicious = is_suspicious_pattern(main_pattern)
    modifier = 3 if is_suspicious else 1
    
    # Apply dynamic programming approach to accumulate scores
    threat_scores[idx] = threat_scores.get(idx-1, 0) + (base_score * modifier)
    
    # String transformation for special cases
    transformed_header = decoded_header[::-1].upper() if ':' in decoded_header else decoded_header.lower()
    
    # Additional encoding check
    contains_encoded_data = any(c.isdigit() for c in transformed_header)
    
    # Logical combination affecting final calculation
    if is_suspicious and contains_encoded_data:
        threat_scores[idx] += 10
    elif not is_suspicious or not contains_encoded_data:
        threat_scores[idx] -= 2

# Final aggregation using functional approach
score_values = list(threat_scores.values())
adjusted_scores = list(map(lambda x: x * 2 if x > 15 else x // 2, score_values))

# Calculate final threat score with ternary logic
final_threat_score = reduce(lambda acc, val: acc + val, adjusted_scores, 0) if adjusted_scores else 0
final_threat_score = final_threat_score if final_threat_score > 0 else -final_threat_score

print(f"Result: {final_threat_score}")