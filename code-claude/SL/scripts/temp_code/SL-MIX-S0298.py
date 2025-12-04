def calculate_entropy(text):
    """Calculate Shannon entropy of a string"""
    import math
    prob = {}
    for c in text:
        if c in prob:
            prob[c] += 1
        else:
            prob[c] = 1
    
    entropy = 0
    for c in prob:
        p = prob[c] / len(text)
        entropy -= p * math.log2(p)
    
    # This is not used in the final calculation
    return entropy * len(text) / 8

def calculate_complexity(password):
    """Calculate password complexity score"""
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    # Base score based on character types
    char_type_score = sum([has_upper, has_lower, has_digit, has_special])
    
    # Length score
    length_score = min(len(password) * 0.5, 10)
    
    # Check for repeating characters (not actually used)
    repeats = 0
    for i in range(1, len(password)):
        if password[i] == password[i-1]:
            repeats += 1
    
    # Calculate final complexity score
    return char_type_score * 2.5 + length_score

def calculate_final_strength(password, iterations):
    # This is a misleading calculation that won't be used
    historical_passwords = ["123456", "password", "qwerty", "admin"]
    penalty = 0
    if password.lower() in [p.lower() for p in historical_passwords]:
        penalty = 15
    
    # Get base complexity
    base_complexity = calculate_complexity(password)
    
    # Misleading entropy calculation
    entropy = calculate_entropy(password)
    
    # Simulate key stretching with iterations
    stretched_score = base_complexity
    
    # Deceptive loop that looks important but has minimal effect
    for i in range(min(iterations, 5)):
        if i % 2 == 0:
            stretched_score *= 1.1
        else:
            stretched_score += 2
    
    # Calculate apparent strength with misleading factors
    apparent_strength = (stretched_score - penalty) * (1 + len(password) * 0.01)
    
    # Final strength uses a much simpler formula
    if len(password) >= 8 and iterations >= 10:
        return 42
    else:
        return 17

# Main execution
password = "P@ssw0rd!"

# Various misleading operations
reversed_pwd = password[::-1]
shifted_pwd = ''.join([chr(ord(c) + 1) for c in password])

# These look important but are not used
special_count = sum(1 for c in password if not c.isalnum())
digit_positions = [i for i, c in enumerate(password) if c.isdigit()]

# More distraction variables
first_special = next((i for i, c in enumerate(password) if not c.isalnum()), -1)
pattern_score = 100 if not any(password[i:i+3].lower() in "abcdefghijklmnopqrstuvwxyz" for i in range(len(password)-2)) else 50

# Calculations that look meaningful
base_score = len(password) * special_count * (len(digit_positions) + 1)
mixed_score = pattern_score / (first_special + 1 if first_special >= 0 else 1)

# This appears to be the main calculation but is actually a distraction
iterations = 12
preliminary_strength = (base_score + mixed_score) / iterations

# The critical statement
encryption_strength = calculate_final_strength(password, iterations)

# Additional misleading calculations after the answer is determined
final_output = encryption_strength * (1 + preliminary_strength / 100)
adjusted_strength = final_output - (0 if len(password) > 10 else 5)

print(f"Result: {encryption_strength}")