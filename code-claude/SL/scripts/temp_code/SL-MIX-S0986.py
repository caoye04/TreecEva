import itertools

def compute_hash(text):
    # Misleading hash function that isn't actually used for the answer
    hash_val = 0
    for char in text:
        hash_val = (hash_val * 31 + ord(char)) % 10000
    return hash_val

def analyze_pattern(text):
    # Distractor function that performs complex but irrelevant analysis
    frequencies = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    
    entropy_value = sum(count * len(char) for char, count in frequencies.items())
    pattern_score = (entropy_value % 256) ^ 42
    return pattern_score

def compute_final_strength(message, keys):
    # Main function that computes the encryption strength
    
    # Distractor operations
    message_hash = compute_hash(message)
    pattern_value = analyze_pattern(message)
    potential_keys = [k for k in keys if len(k) > 2]
    
    # Complex but irrelevant calculations
    key_combinations = list(itertools.combinations(keys, 2))
    combination_strengths = {}
    for k1, k2 in key_combinations:
        combination_strengths[(k1, k2)] = len(k1) * len(k2)
    
    # Actual relevant calculation starts here
    base_strength = 0
    for key in keys:
        # Extract digits from each key and add to strength
        digits = ''.join(c for c in key if c.isdigit())
        if digits:
            base_strength += int(digits)
    
    # More distractors
    message_words = message.split()
    word_count = len(message_words)
    character_count = len(message)
    
    # Split message into segments and process (distractor)
    segments = [message[i:i+5] for i in range(0, len(message), 5)]
    segment_values = [sum(ord(c) for c in segment) for segment in segments]
    
    # Key calculation - this is what matters
    key_chars = ''.join(keys)
    key_sum = sum(ord(c) % 10 for c in key_chars)
    
    # Final strength computation (the actual answer logic)
    strength_multiplier = 7
    encryption_strength = base_strength * strength_multiplier + key_sum
    
    # More distractor calculations that don't affect the result
    alternative_strength = (message_hash ^ pattern_value) % 1000
    security_level = sum(len(k) for k in potential_keys) // 2
    
    # Dead code path with misleading calculations
    if False:
        encryption_strength = alternative_strength + security_level
    
    return encryption_strength

# Set up test data
message = "The quick brown fox jumps over the lazy dog"
keys = ["key123", "secure456", "pass789", "alpha"]

# Compute some irrelevant metrics
security_score = sum(len(key) for key in keys)
character_density = len(message) / len(keys)

# Distractor variables
alternative_keys = [k.upper() for k in keys]
reversed_message = message[::-1]
processed_segments = []

# This is the key statement that computes the answer
encryption_strength = compute_final_strength(message, keys)

# More distractor calculations
backup_strength = (security_score * 5) % 100
combined_keys = ''.join(keys)
key_hash = compute_hash(combined_keys)

print(f"Result: {encryption_strength}")