from collections import Counter
import itertools

# Text analysis for a scientific abstract
text = "DNA sequencing reveals genetic variations across populations. Repeated elements may indicate evolutionary adaptations."

# Process the text: remove punctuation and convert to lowercase
processed_text = ""

for char in text:
    if char.isalnum() or char.isspace():
        processed_text += char.lower()

# Count character frequencies
char_freq = Counter(processed_text)

# Find most common characters (distractor)
common_chars = char_freq.most_common(3)
most_common = common_chars[0][0]

# Calculate character type statistics (partial distractor)
total_chars = len(processed_text)
alpha_count = sum(1 for c in processed_text if c.isalpha())
digit_count = sum(1 for c in processed_text if c.isdigit())
space_count = sum(1 for c in processed_text if c.isspace())

# Generate pairs for analysis (distractor)
char_pairs = list(itertools.combinations(set(processed_text), 2))[:5]
pair_product = 1
for a, b in char_pairs:
    # Convert characters to their ASCII values for computation
    pair_product *= (ord(a) + ord(b)) % 10

# Calculate unique character ratio
unique_ratio = len(set(processed_text)) / total_chars
scaled_ratio = unique_ratio * 100

# Count vowels (distractor)
vowels = set('aeiou')
vowel_count = sum(1 for c in processed_text if c in vowels)

# Our target calculation
unique_chars = len(set(processed_text))

# Theoretical diversity score (distractor)
diversity_score = unique_chars * (vowel_count / total_chars) * 1.5

print(f"Result: {unique_chars}")