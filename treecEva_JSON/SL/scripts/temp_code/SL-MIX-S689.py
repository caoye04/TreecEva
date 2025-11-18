from functools import reduce

def analyze_packets(packet_signatures, attack_pattern):
    pattern_set = frozenset(attack_pattern)
    matched_sequence_length = 0
    current_match_count = 0
    
    for signature in packet_signatures:
        # String transformation and hashing for normalization
        normalized_sig = ''.join(sorted(signature.lower()))
        sig_hash = hash(normalized_sig)
        
        # Greedy matching with set operations
        if sig_hash % 23 in {hash(p) % 23 for p in attack_pattern} and \
           len(set(signature) & pattern_set) >= len(pattern_set) * 0.6:
            current_match_count += 1
            # Short-circuit evaluation for performance
            if current_match_count > matched_sequence_length and \
               any(c.isdigit() for c in signature) and \
               not (len(signature) < 3 or len(signature) > 15):
                matched_sequence_length = current_match_count
        else:
            current_match_count = 0
    
    # Final validation with comparison operations
    return matched_sequence_length if matched_sequence_length > 1 else 0

# Network packet signatures captured during monitoring
network_traffic = [
    "AB12CD", "EF34GH", "IJ56KL", "MN78OP",  # Attack pattern sequence
    "QRSTU9", "VWXYZ0",                       # Part of sequence but failing criteria
    "12AB34", "56CD78", "90EF12",            # Another potential sequence
    "A1B2C3", "D4E5F6", "G7H8I9", "J0K1L2"   # Valid continuation
]

# Known attack pattern signatures
intrusion_signatures = ["AB12CD", "EF34GH", "IJ56KL", "MN78OP", "12AB34", "56CD78"]

matched_sequence_length = analyze_packets(network_traffic, intrusion_signatures)
print(f"Result: {matched_sequence_length}")