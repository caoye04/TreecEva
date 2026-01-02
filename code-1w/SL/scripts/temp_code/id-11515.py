import itertools

# Irrelevant helper function (dead code path)
def unused_calculator(x):
    return (x ** 2 + 3 * x + 1) % 7

# Misleading transformation chain
def decoy_transform(seq):
    shifted = [seq[i-1] - seq[i] for i in range(1, len(seq))]
    scaled = [(v * 17) % 997 for v in shifted]
    return [s for s in scaled if s % 3 == 0]

# Unused but plausible-looking accumulator
def side_channel_analysis(seq):
    total = 0
    for idx, val in enumerate(seq):
        if idx % 4 == 0:
            total += val * 2
        elif val > 50:
            total -= val // 3
    return total  # Never used

# Core logic: recursive filtering with slicing and itertools
def recursive_compress(arr, depth=0):
    if len(arr) <= 1 or depth >= 3:
        return arr[0] if arr else 0
    
    # Meaningful slicing operation
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Use of itertools to generate combinations (relevant)
    pairs = list(itertools.combinations([len(left), len(right), depth], 2))
    factors = [abs(a - b) + 1 for a, b in pairs]
    
    # Actual compression logic
    compressed_left = [left[i] // factors[0] for i in range(0, len(left), 2) if left[i] > factors[0]]
    compressed_right = [right[i] // factors[1] for i in range(1, len(right), 2) if right[i] > factors[1]]
    
    merged = recursive_compress(compressed_left, depth + 1) + recursive_compress(compressed_right, depth + 1)
    
    return merged if isinstance(merged, int) else sum(merged)

# Main processing function
def process_sequence(stream):
    # Initial slicing to extract every third element starting from index 2
    extracted = stream[2::3]
    
    # Red herring: create a distraction with unused transformation
    noise_profile = [x ^ 255 for x in stream if x < 100]  # irrelevant
    baseline_shift = sum(noise_profile[:10]) // 2 if len(noise_profile) > 10 else 0  # unused
    
    # Real work begins: filter values above median threshold
    sorted_vals = sorted(extracted)
    median_index = len(sorted_vals) // 2
    threshold = sorted_vals[median_index]
    
    # Apply recursive compression on high-value segment
    high_band = [v for v in extracted if v >= threshold]
    if not high_band:
        return 0
    
    # Introduce misleading intermediate result
    fake_result = len([x for x in extracted if x % 7 == 0]) * 13  # looks important
    
    # Actual key computation using recursion and slicing
    candidate = recursive_compress(high_band)
    
    # Final adjustment using integer division and rounding
    adjustment_factor = (candidate // 19) + (len(extracted) % 5)
    final_value = candidate - adjustment_factor
    
    return final_value

# Simulated sensor data stream (real input)
data_stream = [127, 83, 245, 67, 191, 44, 213, 76, 178, 95, 203, 52, 241, 88, 167, 73, 182, 99]

# Dead code invocation (distraction)
unused_diagnostic = side_channel_analysis(data_stream)
intermediate_noise = decoy_transform(data_stream)

# Key execution point
filtered_result = process_sequence(data_stream)

# Output result as required
print(f"Result: {filtered_result}")