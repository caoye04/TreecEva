import math

# Simulated sensor data with noise and redundant readings
data_stream = [127, 255, 64, 191, 32, 223, 15, 175, 96, 159]

# Irrelevant constants (distractors)
CALIBRATION_OFFSET = 0.87
REFERENCE_VOLTAGE = 3.3
MAX_BUFFER_SIZE = 256
TEMPORAL_WINDOW = 10

# Misleading preprocessing function (never called)
def legacy_filter(signal):
    return [x for x in signal if x > 100]

# Auxiliary functions
def extract_significant_bits(value):
    # Extract high 4 bits and low 4 bits, combine via XOR
    high_nibble = (value >> 4) & 0xF
    low_nibble = value & 0xF
    return high_nibble ^ low_nibble

bitwise_transform = lambda val: (val ^ 0xAA) + 1  # Bit manipulation with red herring pattern

# Main processing pipeline
def process_sensor_data(raw):
    intermediate = []
    checksum = 0
    
    for i, val in enumerate(raw):
        if i % 3 == 0:
            transformed = bitwise_transform(val)
        elif i % 2 == 0:
            transformed = extract_significant_bits(val)
        else:
            transformed = val // 8
            
        # Conditional logic with misleading accumulation
        if transformed < 50:
            normalized = math.log(transformed + 1) * 2.1
        else:
            normalized = math.sqrt(transformed) * 1.5
            
        intermediate.append(normalized)
        
        # Red herring checksum calculation (unused later)
        checksum += (val ^ (i + 1)) % 255
    
    # Dead code path - unreachable due to prior logic
    if len(intermediate) > 100:
        fallback = sum(intermediate) / MAX_BUFFER_SIZE
        return [fallback]

    return intermediate

# Decoy data structure (distractor)
system_state = {
    'status': 'active',
    'mode': 'diagnostic',
    'buffer': list(range(16)),
    'metadata': {
        'version': '2.1',
        'timestamp': 1678886400,
        'sequence_id': 98765
    }
}

# Unused recursive function (misleading complexity)
def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n - 2)

# Real computation begins here
processed_data = process_sensor_data(data_stream)

# Linear search for threshold crossing (relevant step)
def find_first_peak(series, threshold=6.0):
    for idx, val in enumerate(series):
        if val > threshold:
            return idx
    return -1

first_peak_idx = find_first_peak(processed_data)

# Modular arithmetic used in final calculation
mod_index = (first_peak_idx * 7 + 4) % len(processed_data)

# Set operations as distractors
valid_indices = set(range(len(processed_data)))
dropped_indices = {0, 2, 4, 6, 8}
remaining_indices = valid_indices - dropped_indices  # Unused

# Zip usage with filtering
paired_data = list(zip(processed_data, [x**0.5 for x in range(len(processed_data))]))
filtered_pairs = [p for p in paired_data if p[0] > 5.5]

# Core scoring logic
scaling_factor = 18.3
offset_adjustment = -2.7

# This function appears complex but has deterministic flow
def calculate_final_score(data):
    base = data[mod_index]
    
    # Apply conditional multiplier based on length parity
    multiplier = 3.0 if len(data) % 2 == 1 else 2.5
    
    # Add contribution from filtered pairs count (minor effect)
    bonus = len(filtered_pairs) * 0.8
    
    # Final formula
    score = (base * multiplier) + offset_adjustment + bonus
    
    # Dead branch - always false due to known data size
    if len(data) < 5:
        score *= 0.5  # Never executed
        
    return score

# Execution point of interest
final_score = calculate_final_score(processed_data)

# Print result for evaluation
print(f"Result: {final_score}")