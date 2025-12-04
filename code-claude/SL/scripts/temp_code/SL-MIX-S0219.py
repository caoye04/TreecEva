def analyze_pattern(sequence, pattern_type="standard"):
    if pattern_type == "reverse":
        return sequence[::-1]
    elif pattern_type == "alternate":
        return sequence[::2] + sequence[1::2]
    else:
        return sequence

def calculate_entropy(data):
    # Calculate mock entropy - not real entropy calculation
    total = sum(ord(c) for c in data if c.isalnum())
    return total % 100 + len(data) / 10

def apply_transformation(value, transform_type):
    if transform_type == "square":
        return value ** 2
    elif transform_type == "root":
        return value ** 0.5
    elif transform_type == "invert":
        return 1000 / value if value else 0
    return value

def process_security_metrics(data, thresholds):
    # Extract meaningful parts from data
    important_segment = data[5:15]  # First key slice
    
    # These calculations are distractors
    checksum = sum(ord(c) for c in data) % 256
    hash_factor = (len(data) * 7) % 13
    entropy_level = calculate_entropy(data + str(checksum))
    
    # More distractors with misleading variable names
    security_index = len([c for c in data if c.isupper()]) * 5
    vulnerability_score = sum(1 for c in data if c.isdigit()) * 10
    false_positive_rate = (checksum + hash_factor) / 10
    
    # Process thresholds (distractor calculations)
    adjusted_thresholds = []
    for t in thresholds:
        if t > 100:
            adjusted_thresholds.append(t / 2)  # This branch is never taken
        else:
            adjusted_thresholds.append(t * 1.5)
    
    # Second key slice - this is important
    critical_segment = data[-8:]
    
    # More distractions
    if "high" in data.lower():
        risk_factor = 2.5
        intrusion_probability = security_index / 100
    else:
        risk_factor = 1.8
        intrusion_probability = vulnerability_score / 50
    
    # This is where the actual calculation happens
    upper_count = sum(1 for c in critical_segment if c.isupper())
    digit_count = sum(1 for c in critical_segment if c.isdigit())
    special_count = sum(1 for c in critical_segment if not c.isalnum())
    
    # Key calculation for the answer
    base_strength = upper_count * 10 + digit_count * 5 + special_count * 15
    
    # More distractors
    if entropy_level > 50:
        threat_level = "high"
        mitigation_factor = 0.8
    else:
        threat_level = "medium"
        mitigation_factor = 1.2
    
    # The key threshold application
    threshold_modifier = adjusted_thresholds[0] / 100
    
    # Final calculation - this is what determines the answer
    encryption_strength = int(base_strength * threshold_modifier)
    
    # Distractor operations that don't affect the result
    attack_surface = security_index + vulnerability_score
    defense_rating = (false_positive_rate * mitigation_factor) / risk_factor
    compliance_score = apply_transformation(entropy_level, "root")
    
    # This never executes because the condition is always false
    if "CRITICAL_BREACH" in data and attack_surface > 1000:
        encryption_strength = 0  # Security compromised
    
    return encryption_strength

# Test data
raw_data = "Test@Security123PATTERN"
threshold_values = [40, 75, 90]

# Process the data
encryption_strength = process_security_metrics(raw_data, threshold_values)

# More distractor calculations after the result is determined
potential_threats = ["malware", "phishing", "ddos"]
risk_matrix = [[i*j for j in range(1, 4)] for i in range(2, 5)]
auditing_flag = any(threat in raw_data.lower() for threat in potential_threats)

print(f"Result: {encryption_strength}")