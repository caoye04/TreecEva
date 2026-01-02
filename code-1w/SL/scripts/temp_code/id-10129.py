import itertools

# Simulated sensor data processing with red herrings and complex flow
def collect_signals(base_sequence, multiplier=1.37):
    processed = []
    temp_sum = 0
    
    for i in range(len(base_sequence)):
        if i % 3 == 0:
            temp_sum += base_sequence[i] * multiplier
        elif i % 5 == 0:
            temp_sum += base_sequence[i] // 2
        else:
            temp_sum -= base_sequence[i] % 7
    
    # Distractor: irrelevant aggregation
    decoy_avg = sum(base_sequence) / len(base_sequence)
    spike_count = len([x for x in base_sequence if x > 50])
    
    # Actual relevant transformation
    for val in base_sequence:
        processed.append(int(val * multiplier) % 101)
    
    return processed

# Irrelevant helper (dead path)
def deprecated_filter(data):
    """Old method, no longer used."""
    return [x for x in data if x > 10]

# Core transformation with combinatorics distraction
def generate_combinations(arr):
    # Real use: generates pair count for downstream logic
    pairs = list(itertools.combinations(arr[:4], 2))  # Only first 4 elements matter
    
    # Distractor: complex-looking but unused high-order combinations
    triplets = list(itertools.combinations(arr, 3))
    quads = list(itertools.permutations(arr[:3]))
    
    # Only this value is actually used later
    combination_count = len(pairs)
    return combination_count

# Data reshaping with misleading intermediate outputs
def reshape_data(seq, factor):
    buffer = []
    offset = factor % 8
    
    for idx, val in enumerate(seq):
        shifted = (val ^ idx) + offset
        if shifted < 0:
            shifted = abs(shifted)
        buffer.append(shifted % 97)
    
    # Distractor variables
    max_val = max(buffer)
    min_val = min(buffer)
    range_val = max_val - min_val
    entropy_proxy = sum(b % 5 for b in buffer)  # Unused
    
    # This is the only output that matters
    transformed = [b * 2 for b in buffer]
    return transformed

# Recursive pattern analyzer (key logic hidden in recursion)
def analyze_pattern(data, depth=0):
    if depth >= 3 or len(data) == 0:
        return 1
    
    if len(data) == 1:
        return data[0] + depth
    
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    
    # Key recursive computation
    left_result = analyze_pattern(left, depth + 1)
    right_result = analyze_pattern(right, depth + 1)
    
    # Mixing function - critical to final result
    return (left_result * right_result + depth) % 9973

# Misleading diagnostic (decoy function)
def legacy_diagnostic(x):
    return sum(x) % 10000

# Main execution flow
if __name__ == '__main__':
    raw_input_sequence = [12, 15, 23, 34, 45, 56, 67, 78, 89]
    scaling_factor = 1.37
    
    # Step 1: Collect signals (only returned processed array matters)
    signal_output = collect_signals(raw_input_sequence, scaling_factor)
    
    # Distractor: call but don't use
    combo_size = generate_combinations(signal_output)
    
    # Step 2: Reshape the collected signal
    transformed_data = reshape_data(signal_output, scaling_factor)
    
    # Distractor: unused legacy check
    if len(transformed_data) > 10:
        validation_score = sum(transformed_data) // 100
    else:
        validation_score = -1  # Dead branch
    
    # Critical statement: recursive analysis of pattern
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Print required for deterministic output
    print(f"Target result: {final_diagnostic}")