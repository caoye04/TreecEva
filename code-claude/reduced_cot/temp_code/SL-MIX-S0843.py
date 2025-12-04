def analyze_password_patterns(password):
    # Analyze patterns in password (this is a distractor function)
    pattern_score = 0
    consecutive_count = 0
    for i in range(1, len(password)):
        if ord(password[i]) == ord(password[i-1]) + 1:
            consecutive_count += 1
        else:
            consecutive_count = 0
    
    pattern_score = max(0, 100 - consecutive_count * 5)
    return pattern_score

def calculate_entropy(text):
    # Calculate character distribution entropy (distractor)
    char_freq = {}
    for char in text:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    entropy = len(char_freq) * sum([freq for freq in char_freq.values()])
    return entropy / 10

def calculate_security_strength(metrics):
    # Extract only relevant metrics for security calculation
    length_factor = metrics['length'] * 0.4
    
    # This complexity calculation is what matters
    complexity = 0
    for char_type, count in metrics['char_counts'].items():
        if char_type == 'lowercase' and count > 0:
            complexity += 10
        elif char_type == 'uppercase' and count > 0:
            complexity += 15
        elif char_type == 'digits' and count > 0:
            complexity += 12
        elif char_type == 'special' and count > 0:
            complexity += 20
    
    # Misleading calculations that don't affect the result
    potential_strength = metrics['length'] ** 1.3
    resistance_factor = (metrics['entropy'] / 10) - metrics['patterns']
    theoretical_max = 100 + (metrics['length'] - 8) * 5
    
    # The actual calculation that determines the result
    base_security = length_factor + complexity
    
    # More distractions that don't contribute to final result
    if metrics['has_common_words']:
        potential_adjustment = -25
    else:
        potential_adjustment = 10
    
    # Final result is just base_security capped between 0 and 100
    return max(0, min(100, base_security))

# Password analysis
password = "P@ssw0rd123!"

# Calculate various password metrics
char_types = {'lowercase': 0, 'uppercase': 0, 'digits': 0, 'special': 0}

# Count character types
for char in password:
    if char.islower():
        char_types['lowercase'] += 1
    elif char.isupper():
        char_types['uppercase'] += 1
    elif char.isdigit():
        char_types['digits'] += 1
    else:
        char_types['special'] += 1

# Misleading processing of password
reversed_pwd = password[::-1]
rotated_pwd = password[3:] + password[:3]

# More distracting calculations
pattern_score = analyze_password_patterns(password)
entropy_value = calculate_entropy(password)
common_words = ['password', 'admin', '123456']

# Check if password contains common words (distractor)
contains_common = False
lower_pwd = password.lower()
for word in common_words:
    if word in lower_pwd:
        contains_common = True
        break

# Misleading strength metrics
strength_indicators = {
    'length_score': len(password) * 4,
    'variety_score': sum([1 for t, c in char_types.items() if c > 0]) * 10,
    'entropy_score': entropy_value / 2
}

# This is the actual data that matters for the calculation
password_metrics = {
    'length': len(password),
    'char_counts': char_types,
    'entropy': entropy_value,  # This won't actually be used
    'patterns': pattern_score,  # This won't actually be used
    'has_common_words': contains_common  # This won't actually be used
}

# Calculate final security level
security_level = calculate_security_strength(password_metrics)

# More distracting calculations that happen after the answer is determined
adjusted_level = security_level * (1 - 0.1 * contains_common)
final_rating = "Strong" if adjusted_level > 70 else "Medium" if adjusted_level > 40 else "Weak"

print(f"Password: {password}")
print(f"Security Level: {security_level}")