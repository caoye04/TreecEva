from collections import Counter

def process_text(text):
    # Process text and extract numerical values
    chars = Counter(text.lower())
    
    # Calculate some statistics about the text
    vowels = sum(chars.get(v, 0) for v in 'aeiou')
    consonants = sum(chars.get(c, 0) for c in 'bcdfghjklmnpqrstvwxyz')
    
    # Extract digits and convert to values
    digits = [int(c) for c in text if c.isdigit()]
    digit_sum = sum(digits)
    
    return vowels, consonants, digits, digit_sum

# Sample data from a sensor reading
sensor_data = "Temperature23C at Location19A showed 45% humidity"

# Process the text data
vowel_count, consonant_count, extracted_digits, digit_total = process_text(sensor_data)

# Apply a transformation based on vowel-consonant ratio
transformation_factor = 3 if vowel_count > consonant_count else 2

# Generate sequence based on extracted digits
base_values = extracted_digits[:]

# Apply modular arithmetic to the values
modified_values = [(x * transformation_factor) % 10 for x in base_values]

# Some additional calculations that won't affect our result
max_possible = max(base_values) * transformation_factor
min_possible = min(base_values)

# Create tuples of original and modified values
paired_values = list(zip(base_values, modified_values))

# Filter values based on a condition
valid_values = [v[1] for v in paired_values if v[0] % 2 == 0]

# Calculate the sum of valid values
filtered_sum = sum(valid_values)

# Calculate an alternative sum (distraction)
alternative_sum = sum(v[1] for v in paired_values if v[0] > 3)

print(f"Result: {filtered_sum}")