def analyze_frequency(text):
    freq_map = {}
    for char in text.lower():
        if char.isalpha():
            freq_map[char] = freq_map.get(char, 0) + 1
    return freq_map

# Irrelevant helper function (distractor)
def calculate_entropy(probabilities):
    from math import log2
    return -sum(p * log2(p) for p in probabilities if p > 0)

# Semi-relevant preprocessing step with red herring variables
def preprocess_data(raw):
    cleaned = ''.join(ch.lower() for ch in raw if ch.isalnum())
    length_hint = len(cleaned) % 7
    padding_factor = (length_hint * 2) if length_hint > 3 else 0  # unused
    return cleaned

# Core logic obscured by auxiliary state tracking
def compute_modular_weight(count, index):
    mod_shift = (index % 4) + 1
    return (count * 3) % mod_shift if mod_shift != 0 else count

# Main computation with conditional logic and list comprehension
def compute_final_score(input_str):
    processed = preprocess_data(input_str)
    char_freq = analyze_frequency(processed)
    
    # Distractor: unused statistical variable
    total_chars = sum(char_freq.values())
    avg_frequency = total_chars / len(char_freq) if char_freq else 0
    
    # Key logic embedded within distractions
    indices = list(range(len(char_freq)))
    weighted_values = [
        compute_modular_weight(freq, idx) 
        for idx, (char, freq) in enumerate(char_freq.items())
        if freq % 2 == 1  # Only odd frequencies contribute
    ]
    
    # Conditional expression adds cognitive load
    adjustment = len(weighted_values) if sum(weighted_values) < 10 else len(weighted_values) // 2
    
    # Final score calculation — depends only on specific path
    base_score = sum(weighted_values)
    final_score = base_score * 2 + adjustment
    
    # Dead code path (never executed, but looks relevant)
    if False:
        fallback = sum(freq ** 2 for freq in char_freq.values())
        final_score = max(final_score, fallback)
    
    return final_score

# Input data with meaningful structure
data = "DynamicAnalysisOfPythonCode2024!"

# Execution point of interest
final_score = compute_final_score(data)
print(f"Result: {final_score}")