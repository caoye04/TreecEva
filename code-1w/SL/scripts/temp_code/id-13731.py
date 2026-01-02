def analyze_pattern(sequence):
    count_vowels = lambda s: sum(1 for c in s if c.lower() in 'aeiou')
    temp_stats = {}
    temp_stats['length'] = len(sequence)
    temp_stats['vowels'] = count_vowels(sequence)
    temp_stats['consonants'] = temp_stats['length'] - temp_stats['vowels']
    
    # Distractor: irrelevant transformation
    reversed_seq = sequence[::-1]
    vowel_ratio = temp_stats['vowels'] / max(temp_stats['length'], 1)
    
    # Semi-relevant processing
    normalized_score = (temp_stats['consonants'] * 0.7) + (temp_stats['vowels'] * 0.3)
    return int(normalized_score)


def filter_outliers(data_list):
    mean_val = sum(data_list) / len(data_list)
    std_dev = (sum((x - mean_val) ** 2 for x in data_list) / len(data_list)) ** 0.5
    threshold = mean_val - 1.5 * std_dev
    
    # Dead code path - never used
    if False:
        debug_info = { 'outliers': [x for x in data_list if x < threshold] }
    
    # Actual filtering
    cleaned = [x for x in data_list if x >= threshold]
    return cleaned


def harvest_results(dataset):
    base_values = []
    for item in dataset:
        if isinstance(item, str):
            base_values.append(analyze_pattern(item))
        elif isinstance(item, int):
            base_values.append(item % 19)  # Arbitrary modulus
    
    # Irrelevant intermediate
    weighted_sum = sum(x * (i+1) for i, x in enumerate(base_values))
    scaling_factor = len(base_values) / max(sum(base_values), 1)
    
    # Final computation
    final_yield = sum(base_values) + len(dataset) // 2
    
    # Red herring: unused transformation
    encrypted_tag = ''.join([chr((ord(c) + 3) % 97 + 32) for c in 'yield_secure'])
    
    return final_yield

# Main execution
raw_input = ['algorithm', 'function', 'variable', 42, 'iteration', 'loop', 105]
processed_data = filter_outliers([len(x) if isinstance(x, str) else x for x in raw_input])
intermediate_flag = any(len(str(x)) > 2 for x in processed_data)  # Not used later
final_yield = harvest_results(processed_data)
print(f"Target result: {final_yield}")