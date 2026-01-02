import itertools

# Simulate sensor data with noise and valid readings
def generate_sensor_stream():
    raw_readings = [18, 22, 95, 14, 73, 67, 38, 41, 88, 29]
    noise_mask = [0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
    return [raw_readings[i] if noise_mask[i] == 0 else None for i in range(len(raw_readings))]

# Filter out corrupted values and apply calibration offset
def clean_data(stream):
    cleaned = [x + 3 for x in stream if x is not None]  # Calibration: +3 adjustment
    padded = [0] * 2 + cleaned + [0] * 2  # Edge padding (irrelevant for final result)
    return padded[2:-2]  # Return only valid portion

# Transform data using modular arithmetic and slicing
def transform_data(data):
    shifted = [d % 17 for d in data]  # Normalize via mod
    reversed_chunk = shifted[::-1][:6]   # Reverse and slice first 6 (decoy usage)
    slice_a = shifted[1::2]             # Odd indices — actually used
    slice_b = shifted[::2]              # Even indices — red herring
    combined = []
    for i in range(len(slice_a)):
        combined.append(slice_a[i] * 2 + (i % 3))  # Key transformation
    return combined

# Recursive reduction with misleading base case
def recursive_reduce(seq, index=0):
    if index >= len(seq):
        return 0
    if seq[index] < 10:  # Rare condition — almost never true
        return seq[index] + recursive_reduce(seq, index + 1)
    return seq[index] // 2 + recursive_reduce(seq, index + 1)  # Dominant path

# Secondary function that looks important but is unused
def deprecated_aggregator(x):
    return sum(v ** 0.5 for v in x if v % 2 == 0)

# Main processing chain
def process_sequence(seq):
    temp_result = 0
    for idx, val in enumerate(itertools.cycle([2, 3])):
        if idx >= len(seq):
            break
        temp_result += seq[idx] * val  # Alternating multiplier pattern
    adjusted = temp_result - 17  # Final adjustment
    
    # Dead code branch — looks like error correction
    if adjusted > 1000:
        adjusted = sum([adjusted // (i+1) for i in range(5)]) // 2
    
    return adjusted

# Irrelevant utility: computes statistical decoy
def compute_moving_average(data, window=3):
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages  # Never called in main flow

# --- Execution Flow ---
sensor_data = generate_sensor_stream()
cleaned_data = clean_data(sensor_data)
transformed_data = transform_data(cleaned_data)

# Critical statement
final_output = process_sequence(transformed_data)

print(f"Result: {final_output}")