import itertools
import math

def analyze_password_patterns(pwd):
    # Analyze repeating patterns in password (not used in final calculation)
    patterns = {}
    for i in range(1, len(pwd)//2 + 1):
        for j in range(len(pwd) - i + 1):
            pattern = pwd[j:j+i]
            if pattern in patterns:
                patterns[pattern] += 1
            else:
                patterns[pattern] = 1
    
    # This section looks important but is a distraction
    pattern_score = sum(count * len(pattern) for pattern, count in patterns.items() if count > 1)
    return max(100 - pattern_score, 0) if patterns else 100

def entropy_calculator(text, base=2):
    # Calculate character frequency
    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Calculate entropy (this is used in final calculation)
    length = len(text)
    entropy = 0
    for count in char_freq.values():
        probability = count / length
        entropy -= probability * math.log(probability, base)
    
    return entropy * 10  # Scale for readability

def complexity_score(pwd):
    # Complexity factors (this appears important but is mostly a distraction)
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(not c.isalnum() for c in pwd)
    
    # This looks like it matters but the values are overwritten later
    factors = sum([has_upper, has_lower, has_digit, has_special])
    length_factor = min(len(pwd) / 8, 2)
    
    # This complexity calculation is not used
    return (factors * 25 + length_factor * 50)

def calculate_strength(password, factors):
    # Distraction calculations
    pattern_strength = analyze_password_patterns(password)
    complexity = complexity_score(password)
    
    # Extract only what we need from factors dict
    importance = factors.get('importance', 5)
    security_level = factors.get('level', 2)
    
    # The core calculation that matters
    entropy = entropy_calculator(password)
    
    # Misleading intermediate results
    base_strength = (entropy * 0.7) + (len(password) * 0.3 * security_level)
    adjusted_strength = base_strength * (importance / 5)
    
    # More distractions that look important
    if 'hash_rounds' in factors:
        hash_modifier = min(factors['hash_rounds'] / 1000, 1.5)
        misleading_value = adjusted_strength * hash_modifier
    
    # Critical section - this is what actually determines the final value
    unique_chars_ratio = len(set(password)) / len(password) if password else 0
    multiplier = 1 + (unique_chars_ratio * 0.5)
    
    # The actual calculation that matters
    result = int((entropy * security_level + importance) * multiplier)
    
    # More distraction calculations that aren't used
    for char1, char2 in itertools.pairwise(password):
        if ord(char1) == ord(char2) - 1 or ord(char1) == ord(char2) + 1:
            result = result * 0.95 if len(password) > 10 else result * 0.98
    
    return result

# Setup test scenario
password = "P@ssw0rd2023"

# Distraction dictionary with many fields
user_profile = {
    "username": "admin_user",
    "access_level": 3,
    "department": "IT Security",
    "last_login": "2023-10-15",
    "failed_attempts": 0,
    "password_age": 45
}

# Dictionary with security settings (many are distractions)
security_factors = {
    "importance": 8,      # Used in calculation
    "level": 3,          # Used in calculation
    "hash_rounds": 5000, # Distraction
    "lockout_threshold": 5,  # Distraction
    "password_history": 10,  # Distraction
    "min_length": 12,   # Distraction
    "require_special": True, # Distraction
    "expiry_days": 90   # Distraction
}

# This looks important but isn't used in the final answer
security_threshold = 75 + (user_profile["access_level"] * 10)

# More distraction variables
password_age_factor = max(1, 1.5 - (user_profile["password_age"] / 180))
compromise_risk = 25 if any(common in password.lower() for common in ["pass", "admin", "123"]) else 0

# The key statement that produces our answer
encryption_strength = calculate_strength(password, security_factors)

# Final output with some distractions mixed in
if encryption_strength > security_threshold:
    status = "Strong"
elif encryption_strength > security_threshold * 0.8:
    status = "Moderate"
else:
    status = "Weak"

print(f"Password analysis complete. Status: {status}")
print(f"Encryption strength: {encryption_strength}")