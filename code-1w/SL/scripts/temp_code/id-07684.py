def analyze_pattern(seq, mask):
    """Irrelevant helper that looks important but isn't used in final calculation."""
    return [a ^ b for a, b in zip(seq, mask)]

# Simulated sensor data from environmental monitoring array
temperature_readings = [23.5, 24.1, 25.0, 26.3, 25.8, 24.9, 23.7]
humidity_levels = [45, 47, 50, 55, 58, 53, 49]
pressure_data = [1013, 1015, 1017, 1016, 1014, 1012, 1011]

# Irrelevant transformation chain
smoothed_temp = [round(t * 1.02, 2) for t in temperature_readings]
normalized_humidity = [h / 100 for h in humidity_levels]
adjusted_pressure = [p - 1000 for p in pressure_data]

# Core diagnostic signature (bit-encoded health status)
health_signature = [0b1101, 0b1011, 0b1110, 0b0111, 0b1001]

# Red herring: unused but plausible-looking weight matrix
weight_matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
scaling_factor = sum(sum(row) for row in weight_matrix)  # Distractor computation

# Decoy function that appears relevant
def compute_stress_index(data):
    return sum(d ** 0.5 for d in data if d > 24) * 0.1

# Unused intermediate result
temp_stress = compute_stress_index(temperature_readings)

# Threshold configuration map (key part disguised among noise)
threshold_map = {
    't1': 7, 't2': 11, 't3': 13, 't4': 14, 't5': 10  # Prime and near-prime thresholds
}

# Auxiliary bit utilities (some relevant, some not)
def bit_population(n):
    return bin(n).count('1')

def left_rotate(n, d, bits=4):
    return ((n << d) | (n >> (bits - d))) & ((1 << bits) - 1)

# Dead code path - never called
def legacy_decode(patterns):
    return [p ^ 0b1010 for p in patterns]

# Main processing function with embedded logic chain
def process_metrics(signature, thresholds):
    accumulated = 0
    
    # Step 1: Rotate each signature element and extract character
    rotated_set = [left_rotate(val, 1) for val in signature]
    
    # Step 2: Compute population count (bits set)
    pop_counts = [bit_population(x) for x in rotated_set]
    
    # Step 3: Map to indexed threshold values
    keys = sorted(thresholds.keys())
    selected_thresholds = [thresholds[k] for k in keys[:len(pop_counts)]]
    
    # Step 4: Compare and generate binary decision vector
    decisions = [int(pc >= thresh - 8) for pc, thresh in zip(pop_counts, selected_thresholds)]
    
    # Step 5: Combine using weighted XOR pattern
    for i, (rot_val, decision) in enumerate(zip(rotated_set, decisions)):
        if decision:
            # Only certain indices contribute
            accumulated ^= (rot_val * (i + 1))
    
    # Step 6: Add checksum of original signature lengths (distractor addition)
    accumulated += len(signature) * 2
    
    # Step 7: Apply false dependency on humidity (but it's constant offset)
    fake_dependency = len([h for h in humidity_levels if h > 50])  # evaluates to 3
    accumulated -= fake_dependency
    
    # Step 8: Final adjustment based on string metadata (red herring use of string method)
    metadata_tag = 'DIAGNOSTIC_V4'
    if metadata_tag.lower().startswith('diagnostic'):
        accumulated += metadata_tag.count('O')  # adds 2
    
    return accumulated

# Execution point of interest
final_diagnostic = process_metrics(health_signature, threshold_map)

# Print required output
print(f"Result: {final_diagnostic}")