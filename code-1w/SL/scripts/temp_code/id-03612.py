def analyze_text_segment(segment):
    char_freq = {}
    for char in segment:
        if char.isalpha():
            char_freq[char.lower()] = char_freq.get(char.lower(), 0) + 1
    
    # Distractor: vowel counting (not used later)
    vowels = 'aeiou'
    total_vowels = sum(char_freq.get(v, 0) for v in vowels)
    average_consonant_usage = (sum(char_freq.values()) - total_vowels) / 21 if total_vowels > 0 else 0
    
    return sum(char_freq.values())


def preprocess_entries(raw_entries):
    cleaned = [entry.strip().replace('.', '').replace(',', '') for entry in raw_entries]
    filtered = [entry for entry in cleaned if len(entry) > 3]
    return [entry[:10] for entry in filtered]


def calculate_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * log2(p)
    return round(entropy, 4)

# Main data
raw_input_data = [
    "The quick brown fox jumps over", 
    "the lazy dog near the riverbank",
    "Programming requires logical thinking", 
    "and careful attention to detail.",
    "AI models must reason step by step"
]

# Irrelevant auxiliary computation (distractor)
word_length_sum = sum(len(word) for entry in raw_input_data for word in entry.split())
modification_factor = word_length_sum % 7 or 1

# Preprocess
processed_segments = preprocess_entries(raw_input_data)

# Extract lengths and analyze each
lengths = [len(seg) for seg in processed_segments]
analysis_results = [analyze_text_segment(seg) for seg in processed_segments]

# Another distractor: matrix-like structure with no impact
shift_matrix = [[i + j for j in range(3)] for i in range(len(lengths))]
matrix_trace = sum(shift_matrix[i][i] for i in range(min(len(shift_matrix), 3)))

# Core logic chain
weighted_sum = 0
for i, val in enumerate(analysis_results):
    if lengths[i] % 2 == 1:
        weighted_sum += val * (i + 1)
    else:
        weighted_sum -= val // 2

# Secondary transformation
transformed_values = [x * 2 + 3 for x in lengths if x > 5]
entropy_value = calculate_entropy(transformed_values)

# Final score depends only on weighted_sum and entropy_value
scaling_factor = 1 + (entropy_value // 1)
final_score = int(weighted_sum * scaling_factor)

# Debugging red herring (never used)
counterfactual_score = sum(transformed_values) * matrix_trace // max(modification_factor, 1)

# Output result as required
Result: {final_score}