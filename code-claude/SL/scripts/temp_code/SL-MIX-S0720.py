def count_special_chars(text):
    # Count special characters in text
    special_chars = "!@#$%^&*()_-+={}[]|:;<>,.?/~`"
    count = 0
    for char in text:
        if char in special_chars:
            count += 1
    return count

def calculate_entropy(text):
    # Calculate entropy score based on character diversity
    char_freq = {}
    for char in text:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    # This entropy calculation is not used in final result
    entropy = 0
    for char, freq in char_freq.items():
        probability = freq / len(text)
        entropy -= probability * (freq / len(text))
    return entropy * 10

def analyze_password_patterns(password):
    # Analyze patterns in password (red herring function)
    sequential_count = 0
    repeated_count = 0
    
    for i in range(len(password) - 1):
        # Check for sequential characters
        if ord(password[i+1]) - ord(password[i]) == 1:
            sequential_count += 1
        # Check for repeated characters
        if password[i+1] == password[i]:
            repeated_count += 1
            
    pattern_penalty = sequential_count * 2 + repeated_count * 3
    return pattern_penalty

def calculate_complexity(password):
    # Calculate password complexity score
    has_lowercase = any(char.islower() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = count_special_chars(password) > 0
    
    complexity = 0
    if has_lowercase:
        complexity += 10
    if has_uppercase:
        complexity += 15
    if has_digit:
        complexity += 12
    if has_special:
        complexity += 18
    
    # Length bonus (this is what matters)
    length_bonus = len(password) * 4
    
    # Misleading calculation that isn't used
    advanced_score = (complexity + length_bonus) * 1.5
    return complexity + length_bonus

def calculate_final_strength(password):
    # Security baseline score - seems important but isn't
    security_baseline = 42
    
    # Distractor variables
    potential_strength = len(password) * 8
    character_diversity = len(set(password)) / len(password) if password else 0
    misleading_factor = potential_strength * character_diversity
    
    # Calculate actual components
    complexity = calculate_complexity(password)
    special_char_count = count_special_chars(password)
    
    # Misleading calculations
    pattern_penalty = analyze_password_patterns(password)
    entropy = calculate_entropy(password)
    advanced_metric = (complexity - pattern_penalty + entropy) / 2
    
    # The actual calculation that matters
    actual_strength = complexity + special_char_count * 6
    
    # More distractions
    if len(password) > 12:
        potential_strength += 25
    if special_char_count > 3:
        misleading_factor += 15
    
    # Misleading conditional that looks important
    if character_diversity > 0.7 and special_char_count > 2:
        advanced_metric += 30
    
    # What actually gets returned
    return actual_strength

# Test with a sample password
password = "P@ssw0rd123!"

# Distractor variables
weak_threshold = 50
medium_threshold = 80
strong_threshold = 120

# More distractions
potential_rating = "Unknown"
if len(password) < 8:
    potential_rating = "Very Weak"
elif len(password) < 10:
    potential_rating = "Weak"
elif len(password) < 12:
    potential_rating = "Medium"
else:
    potential_rating = "Potentially Strong"

# Calculate the strength
raw_strength = calculate_complexity(password) - analyze_password_patterns(password)
entropy_factor = calculate_entropy(password)

# The key statement
encryption_strength = calculate_final_strength(password)

# Final output
print(f"Result: {encryption_strength}")