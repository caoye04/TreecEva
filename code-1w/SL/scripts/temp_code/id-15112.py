def analyze_patterns(sequence):
    unique_chars = set(sequence)
    char_count = {c: sequence.count(c) for c in unique_chars}
    
    # Irrelevant computation: counts vowels (not used later)
    vowels = 'aeiou'
    vowel_count = sum(1 for c in sequence if c.lower() in vowels)

    # Semi-relevant transformation: normalize case and remove duplicates
    cleaned = ''.join(sorted(set(sequence.lower())))
    
    # Dummy statistical distraction
    avg_ascii = sum(ord(c) for c in sequence) / len(sequence) if sequence else 0
    
    return cleaned, char_count, avg_ascii


def filter_noise(data_map, threshold=2):
    # Filtering entries with frequency above threshold
    filtered = {k: v for k, v in data_map.items() if v > threshold}
    
    # Dead code path: never accessed
    if False:
        redundant_calc = max(data_map.values()) - min(data_map.values())
        print(f"Redundant range: {redundant_calc}")
    
    return filtered


def compute_entropy(values):
    from math import log2
    total = sum(values)
    probabilities = [v / total for v in values]
    entropy = -sum(p * log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)


def calculate_final_score(data):
    # Extract relevant frequencies
    freq_list = list(data.values())
    
    # Distractor: unused string operation
    label = "result_code"
    suffix = label.upper().replace('_', '')
    
    # Real logic: use min, max, and average to derive score
    max_freq = max(freq_list)
    min_freq = min(freq_list)
    avg_freq = sum(freq_list) / len(freq_list)
    
    # Core formula
    spread = max_freq - min_freq
    balance_factor = (avg_freq - min_freq) / (max_freq - min_freq) if spread > 0 else 1
    
    # Final deterministic calculation
    raw_score = (spread * balance_factor) + compute_entropy(freq_list)
    return int(round(raw_score * 100))

# Main execution
raw_input = "aabbbccccddddd"
processed_data, counts, _ = analyze_patterns(raw_input)
filtered_counts = filter_noise(counts, threshold=1)

# Key statement
final_score = calculate_final_score(filtered_counts)

print(f"Result: {final_score}")