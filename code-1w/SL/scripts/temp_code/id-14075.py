def transform_value(x):
    # Distractor: complex-looking but unused transformation
    return (x ** 2 + 3 * x + 1) % 97

def dummy_filter(seq):
    # Dead function: looks relevant but never called in critical path
    return [n for n in seq if n % 2 == 1]

def shift_and_clip(arr, offset=3):
    # Irrelevant data transformation with slicing red herring
    shifted = arr[-offset:] + arr[:-offset]  # Circular shift
    clipped = [min(max(val, -10), 10) for val in shifted]
    return clipped

def compute_moving_average(data, window=3):
    # Decoy computation: looks important but not used in final result
    avg = []
    for i in range(len(data) - window + 1):
        avg.append(sum(data[i:i+window]) / window)
    return avg

def accumulate_with_condition(seq):
    # Real logic starts here — accumulates only even-indexed, positive values divisible by 3
    total = 0
    for idx in range(0, len(seq), 2):  # Only even indices
        if idx < len(seq) and seq[idx] > 0:
            if seq[idx] % 3 == 0:
                total += seq[idx] * 2
            elif seq[idx] % 5 == 0:
                total -= seq[idx]  # Red herring branch: not triggered
    return total

def extract_critical_slice(arr):
    # Uses slicing but only a portion contributes to real answer
    segment = arr[2:10:2]  # Extract every second element from index 2 to 9
    extended = segment + [len(segment)]  # Add length as distraction
    return extended  # Only the sum matters later

def process_sequence(raw_data):
    # Main processing pipeline with multiple distractions
    
    # Irrelevant preprocessing block
    cleaned = [x for x in raw_data if x != 0]
    normalized = [round(x / 1.5) for x in cleaned]
    inverted = [~x for x in normalized]  # Bitwise NOT — misleading
    
    # Critical data extraction
    key_slice = extract_critical_slice(normalized)
    
    # Another decoy operation
    sorted_inv = sorted(inverted, reverse=True)
    mid_vals = sorted_inv[1::2]  # Every other from odd positions
    
    # Real accumulation begins
    base_sum = accumulate_with_condition(key_slice)
    
    # Secondary manipulation — depends on base_sum
    temp_result = base_sum * 3
    
    # Conditional adjustment based on length (actual dependency)
    if len(key_slice) >= 4:
        temp_result -= 7
    else:
        temp_result += 100  # Dead branch
    
    # Final transformation using integer division and rounding
    final_rounded = int(temp_result // 1.8)
    
    # Introduce more noise
    noise_seq = [i**2 for i in range(5)]
    checksum = sum(noise_seq) % 11
    
    # Final output — only this matters
    final_output = final_rounded + checksum
    
    return final_output

# Simulate input data with domain-specific meaning
# Sensor readings from array (simulated)
data_chunk = [15, -8, 9, 0, 12, 7, 6, -3, 18, 4, 21]

# Execute main logic
target_result = process_sequence(data_chunk)
print(f"Result: {target_result}")