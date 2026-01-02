def analyze_text_patterns(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            char_count[lower_char] = char_count.get(lower_char, 0) + 1
    
    # Distractor: frequency distribution (not used later)
    freq_dist = {k: v / len(char_count) for k, v in char_count.items()}
    
    vowel_count = sum(char_count.get(v, 0) for v in 'aeiou')
    consonant_count = sum(char_count.values()) - vowel_count
    return vowel_count, consonant_count, char_count


def normalize_weights(raw_weights, size):
    total = sum(raw_weights)
    normalized = [w / total for w in raw_weights]
    # Dead code path - never executed due to prior return
    if False:
        extra_adjust = [n * 1.1 for n in normalized]
    return normalized

def calculate_efficiency(vowels, consonants, length):
    if length == 0:
        return 0.0
    vowel_ratio = vowels / length
    consonant_ratio = consonants / length
    efficiency = (consonant_ratio * 2 + vowel_ratio) / 3
    return round(efficiency, 4)

def evaluate_performance(metrics, weights):
    base_score = 0
    weighted_components = []
    
    # Relevant computation
    for i, (key, value) in enumerate(zip(metrics.keys(), metrics.values())):
        weight = weights[i]
        contribution = value * weight
        weighted_components.append(contribution)
    
    for val in weighted_components:
        base_score += val
    
    # Misleading intermediate calculations
    temp_offset = sum([i**2 for i in range(3)])  # Always 5, irrelevant
    noise_factor = len(weighted_components) > 5
    dummy_shift = int(noise_factor) * 10  # Unused
    
    final_score = int(base_score + 0.5)  # Round to nearest integer
    return final_score

# Main execution block
input_text = "Dynamic programming solves complex problems by breaking them down"

vowels, consonants, counts = analyze_text_patterns(input_text)
text_length = len(input_text)

# Compute auxiliary metric (used later)
efficiency = calculate_efficiency(vowels, consonants, text_length)

# Build metrics dictionary
metrics = {
    'vowel_density': vowels,
    'consonant_flow': consonants,
    'text_efficiency': efficiency,
    'char_diversity': len(counts),
    'length_stability': text_length % 7
}

# Weight vector
raw_weights = [0.2, 0.3, 0.25, 0.15, 0.1]
weights = normalize_weights(raw_weights, len(metrics))

# Key statement
final_score = evaluate_performance(metrics, weights)

# Print result
print(f"Result: {final_score}")