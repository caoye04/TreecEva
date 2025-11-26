text_samples = ['Python', 'PROGRAMMING', 'lambda', 'comprehension']

# Process characters from each word
char_processor = lambda s: [c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(s)]

all_chars = []
for sample in text_samples:
    processed = char_processor(sample)
    all_chars.extend(processed)

# Intermediate calculations (somewhat relevant but not critical)
vowel_check = [c for c in all_chars if c in 'aeiouAEIOU']
consonant_count = len([c for c in all_chars if c not in 'aeiouAEIOU'])

# Key processing step
processed_chars = [ord(c) - 96 if c.islower() else ord(c) - 64 for c in all_chars]

# Distractor operations
unused_sum = sum(processed_chars[:5])
temp_product = len(text_samples) * consonant_count

# Final conversion
final_conversion = processed_chars[-1]

print(f"Result: {final_conversion}")