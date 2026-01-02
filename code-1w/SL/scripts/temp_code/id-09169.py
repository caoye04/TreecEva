def analyze_frequency(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count


def normalize_values(count_dict):
    total = sum(count_dict.values())
    normalized = {k: v / total for k, v in count_dict.items()}
    return normalized


def filter_relevant_chars(freq_dict, min_threshold=0.05):
    filtered = {k: v for k, v in freq_dict.items() if v >= min_threshold}
    return filtered


def compute_entropy(values):
    import math
    entropy = 0
    for v in values:
        if v > 0:
            entropy -= v * math.log2(v)
    return round(entropy, 4)


def process_metrics(data, thresholds):
    # Step 1: Analyze character frequencies
    raw_counts = analyze_frequency(data)
    
    # Step 2: Normalize to get probabilities
    norm_freqs = normalize_values(raw_counts)
    
    # Step 3: Filter characters above threshold
    relevant = filter_relevant_chars(norm_freqs, thresholds['freq'])
    
    # Distractor: Unused transformation
    case_mapped = {k.upper(): v for k, v in norm_freqs.items()}
    temp_sum = sum(case_mapped[c] for c in case_mapped if c in 'AEIOU')
    adjustment = temp_sum * 0.1  # Not actually used
    
    # Step 4: Compute entropy of relevant distribution
    entropy_value = compute_entropy(relevant.values())
    
    # Step 5: Apply weighting based on length and entropy
    length_factor = len(data) % 25
    weighted_score = (entropy_value * 100) + length_factor
    
    # Step 6: Additional logic with enumerate and zip (required features)
    indices = [i for i, c in enumerate(data) if c.isupper()]
    shifts = [ord(c) % 3 for c in data]
    paired = list(zip(indices, shifts))
    pair_offset = sum(i * s for i, s in paired if i < 10) % 7
    
    # Final computation
    final_score = int(weighted_score + pair_offset)
    
    # Irrelevant debugging print (dead code effect)
    debug_info = [f'{k}:{v:.3f}' for k, v in relevant.items()]
    debug_str = '|'.join(debug_info)
    
    return final_score

# Main execution
if __name__ == '__main__':
    sample_text = "QuantumComputingAndMachineLearningRevolution"
    config = {'freq': 0.06, 'weight': 1.5}
    final_score = process_metrics(sample_text, config)
    print(f"Result: {final_score}")