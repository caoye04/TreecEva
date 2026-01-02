import math

# Simulate sensor data processing with noise filtering and performance scoring
def preprocess_entry(entry):
    raw_value = int(entry.strip('s').split('_')[1])
    quality_flag = entry.count('x') > 0
    return raw_value if not quality_flag else -1

def filter_noisy_data(log_entries):
    filtered = []
    for entry in log_entries:
        if 'corrupt' in entry:
            continue
        processed = preprocess_entry(entry)
        if processed != -1:
            filtered.append(processed)
    return filtered

def calculate_entropy(values):
    if len(values) == 0:
        return 0.0
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    entropy = 0.0
    total = len(values)
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def bitwise_diagnostic(arr):
    diagnostic = 0
    for val in arr:
        diagnostic ^= val  # XOR all values
    return diagnostic & 0xFF  # Keep within byte range

def evaluate_performance(log, weight_map):
    clean_data = filter_noisy_data(log)
    
    # Irrelevant distraction: string analysis with lambda
    char_count = sum(map(lambda s: len(s), log))
    avg_length = char_count / len(log) if log else 0
    size_metric = avg_length * 10  # Unused downstream
    
    base_sum = sum(clean_data)
    squared_total = sum(x * x for x in clean_data)
    
    # Distractor variables
    temp_offset = len([x for x in clean_data if x > 50])
    debug_state = {"high_val_count": temp_offset, "array_len": len(clean_data)}
    
    entropy = calculate_entropy(clean_data)
    health_key = bitwise_diagnostic(clean_data)
    
    # Real computation chain
    weight_factor = weight_map.get('base', 1.0)
    entropy_penalty = weight_map.get('entropy_penalty', 0.8) * entropy
    adjusted_score = (base_sum * weight_factor) - (entropy_penalty * 10)
    
    # More distractions
    dummy_shift = health_key << 2
    unused_combination = dummy_shift | int(avg_length)
    
    final_score = int(adjusted_score + health_key)
    
    # This print is required to expose the answer
    print(f"Result: {final_score}")
    return final_score

# Input data with mixed valid, corrupt, and flagged entries
data_log = [
    "s_34", "s_67x", "s_23", "corrupt_s_89", "s_34", "s_67", "s_23xx", "s_91"
]

weights = {
    'base': 1.2,
    'entropy_penalty': 1.15
}

# Execute main function
target_var_init = 0
intermediate_result = None
final_score = evaluate_performance(data_log, weights)