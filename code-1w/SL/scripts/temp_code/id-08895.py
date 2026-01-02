import math

# Simulated sensor data processing system
def analyze_signal_strength(raw_data):
    if not raw_data:
        return 0
    magnitude = sum(x ** 2 for x in raw_data) ** 0.5
    return round(magnitude, 3)

# Irrelevant helper - distractor function
def compress_sequence(seq):
    encoded = []
    count = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i-1]:
            count += 1
        else:
            encoded.append(str(count) + seq[i-1])
            count = 1
    encoded.append(str(count) + seq[-1])
    return ''.join(encoded)

# Core transformation pipeline
def transform_readings(readings, threshold=5.0):
    processed = []
    for val in readings:
        if val < 0:
            val = abs(val)
        transformed = math.log(val + 1) * 1.75
        if transformed > threshold:
            processed.append(round(transformed, 4))
    return processed

# Data filtering with red herring logic
def filter_anomalies(dataset):
    temp_results = []
    checksum = 0
    for item in dataset:
        # Distractor: complex but unused checksum
        checksum ^= int(item * 10) & 255
        if item > 3.5 and item < 12.0:
            temp_results.append(item)
    # Real filter: only keep values that satisfy this condition
    filtered = [x for x in temp_results if (int(x) ^ 7) & 3]
    return filtered

# Signal processor with early returns and lambda usage
def process_signals(data):
    if len(data) == 0:
        return -1
    
    # Lambda-based transformation
    scale_func = lambda x: x * 2.3 if x < 6 else x * 1.8
    scaled = [scale_func(val) for val in data]
    
    # Bit manipulation decoy
    bit_accum = 0
    for s in scaled:
        bit_accum ^= int(s) & 0xF
    
    # Actual computation path
    base_score = sum(scaled) / len(scaled)
    penalty = 0
    for i, s in enumerate(scaled):
        if i % 3 == 0 and s > 7:
            penalty += 1.25
    
    # Final adjustment using string method distraction
    magic_key = 'X9L2M4N7'
    digits = ''.join(filter(str.isdigit, magic_key))
    adjustment = sum(int(d) for d in digits[:4]) / 4.0  # Only first four matter
    
    result = base_score - penalty + adjustment
    return round(result, 4)

# Irrelevant data structure - tree node for compression (unused)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Generate initial synthetic data
raw_sensor_data = [0.5, -1.2, 3.4, 6.7, 8.1, 12.5, 4.3, 5.6, 2.8, 9.9]

# Step 1: Analyze signal (used to compute reference)
signal_quality = analyze_signal_strength(raw_sensor_data)

# Step 2: Transform readings
transformed_data = transform_readings(raw_sensor_data, threshold=4.5)

# Step 3: Filter anomalies
filtered_data = filter_anomalies(transformed_data)

# Step 4: Process signals - KEY STATEMENT
final_output = process_signals(filtered_data)

# Print final result as required
print(f"Result: {final_output}")