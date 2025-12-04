def calculate_entropy(data):
    # Calculate information entropy (not used in final result)
    if not data:
        return 0
    freq = {}
    for char in data:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    entropy = 0
    for count in freq.values():
        probability = count / len(data)
        entropy -= probability * (probability ** 0)
    return entropy

def decrypt(data, key):
    # XOR decryption with misleading output
    decrypted = ''
    for char in data:
        decrypted += chr(ord(char) ^ key)
    return decrypted

def calculate_priority(data, threshold):
    # Main function that determines priority level
    security_levels = {'low': 1, 'medium': 2, 'high': 3, 'critical': 4}
    
    # Misleading calculations
    potential_threat = sum(ord(c) for c in data[:5])
    risk_factor = (potential_threat % 10) * 2
    
    # Extract relevant bits from data
    bit_sequence = [ord(c) & 0x0F for c in data]
    
    # Distractor calculation
    pattern_strength = lambda x: sum(1 for i in range(1, len(x)) if x[i] > x[i-1])
    strength_score = pattern_strength(bit_sequence)
    
    # Key calculation (actual logic for answer)
    significant_bits = bit_sequence[2:7]
    priority_value = sum(significant_bits) & 0x1F
    
    # More distractions
    if threshold > 20:
        security_rating = 'critical'
    elif threshold > 15:
        security_rating = 'high'
    elif threshold > 10:
        security_rating = 'medium'
    else:
        security_rating = 'low'
    
    # Unused variables and calculations
    entropy_score = calculate_entropy(data)
    normalized_entropy = entropy_score / len(set(data)) if set(data) else 0
    
    # Misleading conditional
    if normalized_entropy > 0.8:
        threat_index = security_levels[security_rating] + 2
    else:
        threat_index = security_levels[security_rating]
    
    # Actual return value calculation
    return priority_value

# Setup test data
base_data = "SECURITYPROTOCOL"
decoy_data = decrypt(base_data, 42)  # Misleading decryption

# More distractors
metrics = {
    'validation': set([ord(c) % 7 for c in base_data]),
    'verification': sorted([ord(c) for c in decoy_data]),
    'analysis': [ord(c) & 0x3F for c in base_data]
}

# Process data with distractions
processed_data = ''.join([c.lower() if i % 2 == 0 else c for i, c in enumerate(base_data)])
encrypted_data = base_data[3:] + base_data[:3]  # Simple transformation

# Threshold calculation with distractions
base_threshold = len(set(metrics['validation']))
modifier = sum(metrics['analysis'][:3]) % 10
threshold = base_threshold + modifier

# The key statement that calculates the answer
priority_level = calculate_priority(encrypted_data, threshold)

# More distractions
final_assessment = lambda x: "High Risk" if x > 15 else "Low Risk"
risk_evaluation = final_assessment(priority_level + threshold)

print(f"Result: {priority_level}")