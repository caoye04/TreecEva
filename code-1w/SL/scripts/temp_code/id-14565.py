import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(base_val, count):
    return [base_val * (i + 1) % 97 for i in range(count)]

# Irrelevant helper: computes statistical moment (not used in final result)
def compute_moment(data, order):
    mean_val = sum(data) / len(data)
    return sum((x - mean_val) ** order for x in data) / len(data)

# Distraction function: looks important but unused in critical path
def deprecated_filter(seq, limit):
    return [x for x in seq if x > limit]

# Core transformation: applies modular inversion and offset
def transform_sequence(raw_seq):
    inverted = []
    for val in raw_seq:
        if val == 0:
            inverted.append(0)
        else:
            inverted.append(pow(val, -1, 97))  # Modular inverse mod 97
    offset = sum(inverted) % 53
    return [(x + offset) % 97 for x in inverted]

# Recursive reduction function (used in critical path)
def recursive_reduce(seq, depth):
    if depth <= 0 or len(seq) == 1:
        return seq[0] if seq else 0
    new_seq = [(seq[i] ^ seq[(i+1) % len(seq)]) for i in range(len(seq))]
    return recursive_reduce(new_seq, depth - 1)

# Character frequency scoring (distractor - appears useful)
def score_characters(text):
    freq_map = {}
    for c in text:
        freq_map[c] = freq_map.get(c, 0) + 1
    return sum(ord(k) * v for k, v in freq_map.items())

# Unused sorting routine (dead code path)
def sort_by_bit_count(arr):
    return sorted(arr, key=lambda x: bin(x).count('1'))

# Critical pattern analyzer
def analyze_pattern(data_list, threshold_fn):
    size = len(data_list)
    if size == 0:
        return 0
    
    # Apply threshold filter
    filtered = [x for x in data_list if threshold_fn(x)]
    
    # Decoy accumulation (looks important)
    cumulative = 0
    temp_vals = []
    for i, v in enumerate(filtered):
        cumulative = (cumulative + v * (i + 1)) % 10000
n    temp_vals.append(cumulative)
    
    # Real computation: XOR reduction with depth based on length
    reduction_depth = len(filtered) % 7
    reduced_value = recursive_reduce(filtered, reduction_depth)
    
    # Secondary transformation
    adjusted = (reduced_value * 17) % 89
    
    # Final adjustment using lambda-embedded logic
    modifier = (lambda x: (x ** 2 + x + 1) % 61)(len(filtered))
    return (adjusted + modifier) % 10000

# Misleading string-to-data converter (unused)
def encode_string_to_data(s):
    return [ord(c) % 97 for c in s]

# Main execution block
if __name__ == "__main__":
    # Generate initial dataset
    raw_sensor_data = collect_samples(13, 25)
    
    # Compute irrelevant statistics
    moment_2 = compute_moment(raw_sensor_data, 2)
    moment_4 = compute_moment(raw_sensor_data, 4)
    
    # Transform data (critical path)
    transformed_data = transform_sequence(raw_sensor_data)
    
    # Create unused filtered version
    filtered_irrelevant = deprecated_filter(transformed_data, 50)
    
    # Build threshold function using lambda (actually used)
    threshold_func = lambda x: x % 2 == 1  # Only odd values pass
    
    # Analyze character pattern from fake input (distraction)
    dummy_text = "sensor_diag_v9"
    char_score = score_characters(dummy_text)
    
    # Sort transformed data by bit count (not used later)
    sorted_by_bits = sort_by_bit_count(transformed_data)
    
    # UNUSED: string encoded data
    encoded_data = encode_string_to_data("config_xf2")
    
    # CRITICAL STATEMENT: compute final diagnostic
    final_diagnostic = analyze_pattern(transformed_data, threshold_func)
    
    # Print result
    print(f"Target result: {final_diagnostic}")