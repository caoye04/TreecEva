from collections import Counter
import math

def analyze_text_complexity(text):
    # Calculate text complexity score (distractor function)
    vowels = set('aeiou')
    consonants = set('bcdfghjklmnpqrstvwxyz')
    
    v_count = sum(1 for char in text.lower() if char in vowels)
    c_count = sum(1 for char in text.lower() if char in consonants)
    
    if c_count == 0:
        return 0
    
    complexity = (v_count / c_count) * math.log(len(text) + 1)
    return round(complexity, 2)

def calculate_common_chars(samples):
    # Find common characters and their frequencies
    sample_counters = [Counter(sample.lower()) for sample in samples]
    
    # Process the first three samples only (key insight)
    relevant_counters = sample_counters[:3]
    
    # Extract common characters appearing in all relevant samples
    common_chars = set.intersection(*[set(counter.keys()) for counter in relevant_counters])
    
    # Filter out spaces and punctuation
    filtered_chars = {c for c in common_chars if c.isalpha()}
    
    # Calculate frequency of most common character
    if not filtered_chars:
        return 0
    
    # Calculate average frequency for each common character
    char_avg_freqs = {}
    for char in filtered_chars:
        frequencies = [counter[char] for counter in relevant_counters]
        char_avg_freqs[char] = sum(frequencies) // len(frequencies)
    
    # Find the maximum frequency
    return max(char_avg_freqs.values()) if char_avg_freqs else 0

# Main processing
text_samples = [
    "The quick brown fox jumps over the lazy dog",
    "The five boxing wizards jump quickly",
    "Pack my box with five dozen liquor jugs",
    "How vexingly quick daft zebras jump"
]

# Calculate complexity scores (distractor)
complexity_scores = [analyze_text_complexity(text) for text in text_samples]

# Find average complexity (distractor)
avg_complexity = sum(complexity_scores) / len(complexity_scores)

# Calculate letter frequencies (distractor)
all_letters = ''.join(text_samples).lower()
all_letter_counts = Counter(all_letters)

# Remove non-alphabetic characters (distractor)
filtered_counts = {k: v for k, v in all_letter_counts.items() if k.isalpha()}

# Calculate maximum frequency (distractor)
max_letter = max(filtered_counts, key=filtered_counts.get)
max_frequency = filtered_counts[max_letter]

# Sort letters by frequency (distractor)
sorted_letters = sorted(filtered_counts.items(), key=lambda x: (-x[1], x[0]))

# Find unique letters in each sample (distractor)
unique_letters = [set(sample.lower()) for sample in text_samples]
common_unique = set.intersection(*unique_letters)

# Calculate primary result
target_frequency = calculate_common_chars(text_samples)

# Alternative calculation path (distractor)
reverse_samples = [sample[::-1] for sample in text_samples]
reverse_frequency = calculate_common_chars(reverse_samples)

# Misleading combined result (distractor)
combined_result = (max_frequency + reverse_frequency) // 2

# Generate misleading result (distractor)
final_misleading = target_frequency * 2 - reverse_frequency

print(f"Result: {target_frequency}")