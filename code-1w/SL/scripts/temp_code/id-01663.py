import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(i > 0 for i in x) if isinstance(x, list) else False

# Decoy transformation chain
def decoy_transform(sequence):
    shifted = [i << 1 for i in sequence]  # Bit shifting distraction
    mapped = list(map(lambda x: x ^ 7, shifted))
    return [m for m in mapped if m % 3 != 0]

# Unused intermediate processing (misleading computation)
temp_buffer = [3, 6, 9, 12]
processed_buffer = []
for val in temp_buffer:
    if val % 4 == 0:
        processed_buffer.append(val * 1.5)
    else:
        processed_buffer.append(val // 2)

# Core data refinement pipeline
def normalize_signal(raw):
    return [round(math.log(abs(x) + 1), 3) for x in raw]

def apply_mask(signal, threshold=2.0):
    return [s if s >= threshold else 0.0 for s in signal]

def aggregate_peaks(data):
    total = 0.0
    count = 0
    for d in data:
        if d > 0:
            total += d ** 1.5
            count += 1
    return int(total) if count > 0 else -1

# Multi-step preprocessing with distractor branches
def preprocess_segment(segment):
    # Real processing branch
    amplified = [x * 2.5 for x in segment]
    filtered = [f for f in amplified if f.is_integer()]
    
    # Red herring: conditional that never triggers due to data constraints
    if any(z < 0 for z in filtered):
        filtered = [abs(z) for z in filtered]
    
    return sorted(filtered, reverse=True)

# Higher-order composition using lambda and set logic
def generate_signature(elements):
    unique_roots = list(set(int(math.sqrt(e)) for e in elements if e > 1))
    checksum = sum(u * (u % 4) for u in unique_roots)
    return checksum + len(unique_roots)

# Final filter combines multiple concepts
def final_filter(dataset):
    # Real critical operation
    base_norm = normalize_signal(dataset)
    masked = apply_mask(base_norm)
    peak_value = aggregate_peaks(masked)
    
    # Distractor: complex-looking but unused bitwise manipulation
    decoy_val = 0
    for i in range(len(dataset)):
        decoy_val ^= (dataset[i] & 15) << (i % 4)
    decoy_val = decoy_val & 0xFFFF
    
    # Another irrelevant string-based side computation
    status_flag = ''.join([chr(97 + (len(dataset) % 26))]) * 3
    
    # Key assignment - this is what matters
    filtration_score = peak_value * 2 - generate_signature(dataset)
    
    return filtration _score

# Simulated sensor input (real data source)
raw_sensor_data = [15, 25, 30, 45, 50, 60]

# Execution chain with multiple diversions
intermediate_data = preprocess_segment(raw_sensor_data)
processed_data = normalize_signal(intermediate_data)

# Dead function call (no effect)
decoy_transform(intermediate_data)

# Critical execution point
filtration_score = final_filter(processed_data)

print(f"Result: {filtration_score}")