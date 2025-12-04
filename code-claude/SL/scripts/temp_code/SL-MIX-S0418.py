from collections import Counter

def process_text(text):
    # Count character frequencies
    char_freq = Counter(text.lower())
    
    # Extract some values for encryption
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    # Calculate values based on character frequencies
    vowel_sum = sum(char_freq[v] for v in vowels)
    consonant_sum = sum(char_freq[c] for c in consonants)
    
    # Some distracting calculations
    special_chars = sum(1 for c in text if not c.isalnum())
    digit_count = sum(1 for c in text if c.isdigit())
    
    # More distraction with unused string methods
    capitalized = text.capitalize()
    reversed_text = text[::-1]
    
    return vowel_sum, consonant_sum, special_chars, digit_count

# Sample cryptographic message
message = "Hello, World! This is a test message with 123 numbers."

# Process the text
vowel_count, consonant_count, special_count, digit_count = process_text(message)

# Calculate a base value using the counts
base_value = vowel_count * 16 + consonant_count

# This calculation is a distraction
distractor_value = special_count * digit_count
if distractor_value > 20:
    temp_val = distractor_value * 2
else:
    temp_val = distractor_value * 3

# Define encryption parameters
key = 0xA5  # Hexadecimal value (equals 165 in decimal)
mask = 0xFF  # Hexadecimal value (equals 255 in decimal)

# Another distraction calculation
shift_amount = (special_count % 4) + 1
temp_shifted = base_value << shift_amount
if temp_shifted > 1000:
    temp_shifted = temp_shifted % 1000

# The key encryption operation
encrypted_value = (base_value ^ key) & mask

# Final distraction
final_check = consonant_count - vowel_count
if final_check > 0:
    result_code = "positive"
else:
    result_code = "non-positive"

print(f"Result: {encrypted_value}")