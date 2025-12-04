def calculate_character_entropy(char):
    # Simulates entropy calculation based on ASCII value
    ascii_val = ord(char)
    potential_entropy = (ascii_val * 17) % 256
    return potential_entropy / 256.0

def analyze_string_complexity(text):
    # Returns a complexity score that we don't actually use
    vowels = sum(1 for c in text.lower() if c in 'aeiou')
    consonants = sum(1 for c in text.lower() if c in 'bcdfghjklmnpqrstvwxyz')
    digits = sum(1 for c in text if c.isdigit())
    return (vowels * 1.5) + consonants + (digits * 2.5)

def calculate_key_complexity(key_shifts):
    # Calculates a complexity score for the encryption key
    total = sum(shift % 13 for shift in key_shifts)
    multiplier = max(1, len(key_shifts) // 3)
    return total * multiplier

def calculate_security_level(message, key_shifts):
    # Main function to calculate encryption strength
    if not message or not key_shifts:
        return 0
    
    # Calculate base strength from message
    char_entropies = [calculate_character_entropy(char) for char in message]
    base_strength = sum(char_entropies) * 10
    
    # Apply key strength modifiers
    key_complexity = calculate_key_complexity(key_shifts)
    
    # These values are distractions and not used in final calculation
    message_length_factor = len(message) / 10
    key_diversity = len(set(key_shifts)) / len(key_shifts) if key_shifts else 0
    theoretical_max = 100 - (100 / (1 + len(message) * 0.1))
    
    # Extract special characters for additional security bonus
    special_chars = sum(1 for c in message if not c.isalnum() and not c.isspace())
    special_bonus = special_chars * 1.75
    
    # Calculate repeated characters (decreases security)
    char_counts = {}
    for char in message:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    repeated_chars = sum(count - 1 for count in char_counts.values() if count > 1)
    repetition_penalty = repeated_chars * 0.5
    
    # Misleading calculations that don't affect the result
    uppercase_ratio = sum(1 for c in message if c.isupper()) / len(message) if message else 0
    entropy_variance = max(char_entropies) - min(char_entropies) if char_entropies else 0
    advanced_metric = (uppercase_ratio * 10) + (entropy_variance * 15)
    
    # This is the actual calculation that matters
    encryption_strength = base_strength + key_complexity + special_bonus - repetition_penalty
    
    # Round to 2 decimal places for cleaner result
    return round(encryption_strength, 2)

# Test message and key shifts
message = "Secure@Transmission#2023"
alt_message = "TestingAlternativeMessage"

# Primary key shifts
key_shifts = [3, 7, 12, 9, 5]

# Alternative key shifts (distraction)
backup_shifts = [2, 4, 8, 16]
emergency_shifts = [1, 3, 5, 7, 9, 11]

# Calculate complexity scores (distractions)
message_complexity = analyze_string_complexity(message)
alt_complexity = analyze_string_complexity(alt_message)

# Simulate different encryption methods (distractions)
aes_strength = message_complexity * 1.5
des_strength = alt_complexity * 0.8

# This is the key calculation we're asking about
encryption_strength = calculate_security_level(message, key_shifts)

# More distractions after the main calculation
combined_strength = (aes_strength + des_strength) / 2
theoretical_max_strength = len(message) * 3.14159

# This print statement doesn't affect the calculation
print(f"Message analyzed: {message}")

# Final result
print(f"Encryption strength: {encryption_strength}")