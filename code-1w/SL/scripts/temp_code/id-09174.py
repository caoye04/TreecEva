def analyze_frequency(text):
    freq = {}
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq


def normalize_values(freq_dict):
    total = sum(freq_dict.values())
    normalized = {}
    for k, v in freq_dict.items():
        normalized[k] = round(v / total, 4)
    return normalized


def filter_relevant_letters(norm_dict, threshold=0.05):
    filtered = {}
    for letter, prob in norm_dict.items():
        if prob >= threshold:
            filtered[letter] = prob
    return filtered


def compute_entropy(values):
    import math
    entropy = 0.0
    for v in values:
        if v > 0:
            entropy -= v * math.log2(v)
    return round(entropy, 4)


def build_lookup(keys):
    # Distractor: builds a mapping that isn't used in final result
    lookup = {}
    for i, key in enumerate(sorted(keys)):
        lookup[key] = (i * 2 + 1) % 97
    return lookup

def validate_sequence(seq):
    # Distractor function with dead-end logic
    if len(seq) < 3:
        return False
    for i in range(len(seq) - 2):
        if seq[i] + seq[i+1] != seq[i+2]:
            return True  # early exit, misleading
    return False

def process_metrics(raw_data, limits):
    # Main data processing chain
    frequencies = analyze_frequency(raw_data)
    normal_freqs = normalize_values(frequencies)
    important_letters = filter_relevant_letters(normal_freqs, limits['prob'])
    
    # Intermediate distractor computations
    dummy_seq = [1, 2, 3, 5, 8]
    _ = validate_sequence(dummy_seq)
    _ = build_lookup(important_letters.keys())
    
    entropy_value = compute_entropy(list(important_letters.values()))
    letter_count = len(important_letters)
    
    # Simulated scoring formula
    score_component_1 = entropy_value * 100
    score_component_2 = letter_count * 10
    adjustment = 5  # hardcoded offset
    
    # More red herring variables
    temp_debug_log = f'Processing {letter_count} letters with entropy {entropy_value}'
    debug_metadata = {'run_id': 98765, 'version': 'beta', 'active': True}
    
    final_score = int(score_component_1 + score_component_2 + adjustment)
    
    # Irrelevant string manipulation
    report_str = f"Final score: {final_score}"
    report_str = report_str.replace('Final', 'Computed').upper()
    
    return final_score

# Input data and parameters
raw_text = "The quick brown fox jumps over the lazy dog repeatedly every morning"
thresholds = {'prob': 0.06}
data = raw_text

# Execution point
final_score = process_metrics(data, thresholds)
print(f"Result: {final_score}")