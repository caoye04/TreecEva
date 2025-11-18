import re

def process_packet_headers(headers):
    processed = []
    for header in headers:
        # Convert hex to integer
        value = int(header, 16)
        # Apply mask and shift operations
        masked = (value & 0xFF00) >> 8
        if masked > 0x7F:
            masked = masked ^ 0xFF  # XOR with all bits set
        processed.append(masked)
    return processed

def calculate_intrusion_score(transformed_data, pattern_db):
    score = 0
    pattern_matches = {}
    
    # Dictionary comprehension to create match counts
    for pattern_id, pattern in pattern_db.items():
        pattern_matches[pattern_id] = sum(1 for data in transformed_data if data in pattern)
    
    # Early termination if high-risk pattern detected
    if pattern_matches.get('P999', 0) >= 2:
        return -1  # Immediate alert
    
    # Calculate weighted score
    for pid, count in pattern_matches.items():
        weight = int(pid[1:])  # Extract numeric part as weight
        score += count * weight
    
    return score

def analyze_network_traffic(packet_stream):
    # Known malicious patterns (frozensets for immutability)
    malicious_patterns = {
        'P100': frozenset([0x1A, 0x2B, 0x3C]),
        'P200': frozenset([0x4D, 0x5E, 0x6F]),
        'P999': frozenset([0xAA, 0xBB, 0xCC])
    }
    
    # Process packets through multiple stages
    stage1_processed = process_packet_headers(packet_stream)
    
    # Sort processed data for pattern analysis
    stage1_processed.sort(reverse=True)
    
    # Check for specific byte sequence using regex on hex representations
    hex_string = ''.join(f'{b:02X}' for b in stage1_processed)
    suspicious_sequence = re.search(r'(AA..BB|CC..DD)', hex_string)
    
    if suspicious_sequence:
        # Boost score if suspicious sequence found
        return calculate_intrusion_score(stage1_processed, malicious_patterns) + 50
    else:
        return calculate_intrusion_score(stage1_processed, malicious_patterns)

# Main analysis pipeline
network_packets = ['1A2B', '3C4D', 'AAFF', 'BBCC', '5E6F']
intrusion_score = analyze_network_traffic(network_packets)
print(f"Result: {intrusion_score}")