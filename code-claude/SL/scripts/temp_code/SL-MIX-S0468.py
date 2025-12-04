import itertools
from functools import reduce

def calculate_hash(password_list):
    # Irrelevant security metrics
    security_metrics = {
        'entropy': lambda x: sum(ord(c) for c in x) % 256,
        'complexity': lambda x: len(set(x)) * 2,
        'length_factor': lambda x: len(x) ** 1.5
    }
    
    # Misleading hash calculation that isn't used
    def sha_simulator(text):
        base = 31
        result = 0
        for char in text:
            result = (result * base + ord(char)) & 0xFFFFFFFF
        return result
    
    # Process each password with bit operations
    processed = []
    for pwd in password_list:
        # Misleading metrics calculation
        metrics = {k: v(pwd) for k, v in security_metrics.items()}
        
        # The actual processing we care about - extracts ASCII values
        ascii_vals = [ord(c) for c in pwd]
        
        # Distractor operation
        xor_result = reduce(lambda x, y: x ^ y, ascii_vals, 0)
        
        # Only add to processed if it meets certain criteria
        if len(pwd) > 3:
            # The important calculation
            strength = sum(ascii_vals) % 1000
            processed.append(strength)
        else:
            # Distractor for short passwords
            processed.append(0)
    
    # More distractor operations that don't affect the result
    potential_combinations = list(itertools.combinations(processed, 2))
    max_combo = max(potential_combinations, key=lambda x: x[0] + x[1], default=(0, 0))
    
    # Final hash calculation
    if processed:
        # The actual formula that matters
        result = (sum(processed) * 17) % 10000
        return result
    else:
        return 0

# Password database (some strong, some weak)
pwd_database = [
    "p@ssw0rd",  # Common password
    "qwerty123",  # Simple password
    "zX9#2aLm",   # Strong password
    "abc",        # Too short
    "S3cure!Pass",  # Another strong one
    "letmein"     # Another common one
]

# Distractor function that isn't used in the final calculation
def analyze_password_patterns(passwords):
    patterns = {}
    for pwd in passwords:
        # Look for repeating characters
        repeats = len(pwd) - len(set(pwd))
        # Look for sequential characters
        sequential = sum(1 for i in range(len(pwd)-1) if ord(pwd[i+1]) - ord(pwd[i]) == 1)
        patterns[pwd] = {'repeats': repeats, 'sequential': sequential}
    return patterns

# Filter passwords based on arbitrary criteria
def filter_passwords(passwords, min_length=4):
    # Calculate some misleading metrics
    pattern_analysis = analyze_password_patterns(passwords)
    
    # String manipulation with meaningful distractors
    passwords_with_numbers = [p for p in passwords if any(c.isdigit() for c in p)]
    passwords_with_symbols = [p for p in passwords if any(not c.isalnum() for c in p)]
    
    # Lambda for length check
    length_check = lambda p: len(p) >= min_length
    
    # This is the actual filter we care about
    filtered = list(filter(length_check, passwords))
    return filtered

# Some distracting operations that don't contribute to the answer
common_passwords = {"password", "123456", "qwerty", "admin"}
pwd_set = set(pwd_database)
common_pwd_intersection = pwd_set.intersection(common_passwords)

# Main execution flow
filtered_passwords = filter_passwords(pwd_database)

# Create a misleading hash that isn't the final result
misleading_hash = sum(len(p) for p in filtered_passwords) * 42

# This is the statement we're interested in
crypto_hash = calculate_hash(filtered_passwords)

# Additional distractor calculations
security_score = len(filtered_passwords) * 25 - len(common_pwd_intersection) * 50
normalized_score = min(100, max(0, security_score))

print(f"Result: {crypto_hash}")
