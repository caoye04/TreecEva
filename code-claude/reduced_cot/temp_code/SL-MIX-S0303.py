def calculate_strength(pwd):
    base_score = 0
    length_factor = min(len(pwd), 12) / 4
    
    # Count character types
    has_lower = any(c.islower() for c in pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(not c.isalnum() for c in pwd)
    
    # Calculate diversity score
    diversity = sum([has_lower, has_upper, has_digit, has_special])
    
    # Track character frequency (not directly used in final calculation)
    char_freq = {}
    for c in pwd:
        if c in char_freq:
            char_freq[c] += 1
        else:
            char_freq[c] = 1
    
    # Calculate repeated character penalty (not used in final score)
    repeat_penalty = sum(freq - 1 for freq in char_freq.values() if freq > 1)
    
    # Calculate sequential characters (misleading calculation)
    sequential = 0
    for i in range(len(pwd) - 2):
        if ord(pwd[i]) + 1 == ord(pwd[i+1]) and ord(pwd[i+1]) + 1 == ord(pwd[i+2]):
            sequential += 1
    
    # Calculate unique patterns (distraction)
    pattern_score = 0
    for i, (char, count) in enumerate(zip(['a', 'e', 'i', 'o', 'u'], [3, 1, 4, 1, 5])):
        if char in pwd.lower():
            pattern_score += count
    
    # Calculate final strength score
    strength_multiplier = 1.5 if diversity >= 3 else 1.0
    base_score = 10 * length_factor * strength_multiplier
    
    # Apply security classification
    if base_score > 30:
        security_class = "high"
    elif base_score > 20:
        security_class = "medium"
    else:
        security_class = "low"
    
    # This is the key calculation for password strength
    password_strength = int(base_score + diversity * 5)
    
    # Log some information (distraction)
    print(f"Password analysis complete. Result: {password_strength}")
    return password_strength

# Test with a sample password
password = "Py@3xCode"
password_entropy = len(set(password)) * 2  # Distraction calculation
password_strength = calculate_strength(password)