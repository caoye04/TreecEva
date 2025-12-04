def analyze_password(pwd):
    # Security analysis function - returns complexity score
    length_score = len(pwd) * 4
    uppercase_count = sum(1 for c in pwd if c.isupper())
    lowercase_count = sum(1 for c in pwd if c.islower())
    digit_count = sum(1 for c in pwd if c.isdigit())
    
    # Potential breach detection (not relevant for final score)
    breach_risk = 0
    common_patterns = ['123', 'admin', 'pass', 'pwd']
    for pattern in common_patterns:
        if pattern in pwd.lower():
            breach_risk += 10
    
    # Calculate character diversity bonus
    diversity_score = (uppercase_count > 0) + (lowercase_count > 0) + (digit_count > 0)
    diversity_score *= 10
    
    # Final score calculation
    return length_score + diversity_score - breach_risk

# Network security assessment (distractor code)
def network_scan(ports):
    open_ports = [p for p in ports if (p % 3 == 0) or (p % 7 == 0)]
    vulnerability_index = len(open_ports) * 5
    return vulnerability_index

# Main security evaluation
passwords = ['Admin123', 'Secure_P@ss', 'qwerty']
network_status = 'secure' if network_scan([22, 80, 443, 8080]) < 50 else 'vulnerable'

# Calculate password strengths
password_strengths = {}
for i, pwd in enumerate(passwords):
    # Basic strength assessment
    raw_score = analyze_password(pwd)
    
    # Apply contextual modifiers (distractors)
    context_multiplier = 1.5 if i == len(passwords) - 1 else 1.0
    entropy_factor = sum(ord(c) for c in pwd) % 10
    
    # Store calculated strength
    password_strengths[pwd] = raw_score

# Distractor calculations
entropy_values = [ord(p[0]) - ord('a') if p[0].lower() >= 'a' and p[0].lower() <= 'z' else 0 for p in passwords]
network_factor = 2 if network_status == 'secure' else 0.5

# Extract just the scores for final calculation
password_scores = [password_strengths[pwd] for pwd in passwords]

# Calculate encryption baseline (distractor)
base_encryption = sum(len(pwd) for pwd in passwords) * network_factor

# This is the key statement
encryption_strength = sum(password_scores)

# Additional security metrics (distractors)
firewall_strength = base_encryption * 0.8
anti_malware_score = sum(entropy_values) * 3

# Output the results
print(f"Password analysis complete")
print(f"Network status: {network_status}")
print(f"Firewall strength: {firewall_strength}")
print(f"Anti-malware rating: {anti_malware_score}")
print(f"Result: {encryption_strength}")