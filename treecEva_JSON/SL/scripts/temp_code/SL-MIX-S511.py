from functools import reduce

# Packet header values from network capture
packet_headers = [0x1A3F, 0x7B2C, 0x4E81, 0xF056, 0x29DA]

# Initialize security tracking variables
packet_risk_scores = []
cumulative_security_score = 0

# Process each packet header to compute risk scores
for idx, header in enumerate(packet_headers):
    # Extract relevant bit fields using masking
    priority_bits = (header & 0xF000) >> 12  # Upper 4 bits
    protocol_bits = (header & 0x0FF0) >> 4   # Middle 8 bits
    flag_bits = header & 0x000F              # Lower 4 bits
    
    # Calculate base risk using XOR of priority and flags
    base_risk = priority_bits ^ flag_bits
    
    # Apply protocol modifier using AND operation
    protocol_modifier = protocol_bits & 0x07  # Only consider 3 LSBs
    
    # Compute enhanced risk with short-circuit evaluation
    enhanced_risk = base_risk if protocol_modifier == 0 else (base_risk | protocol_modifier)
    
    # Add to collection
    packet_risk_scores.append(enhanced_risk)

# Calculate cumulative score using reduction and bit shifting
if packet_risk_scores:  # Short-circuit check
    cumulative_security_score = reduce(lambda acc, score: (acc << 1) ^ score, packet_risk_scores, 0)

print(f"Result: {cumulative_security_score}")