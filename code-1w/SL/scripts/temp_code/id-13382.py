import math

# Simulated sensor array diagnostics with mixed computational paradigms
def collect_readings():
    raw_values = [i * 0.5 + (i % 7) for i in range(15)]
    return raw_values

# Irrelevant preprocessing step (distractor)
def normalize_data(data):
    max_val = max(data)
    return [x / max_val for x in data] if max_val != 0 else data

# Decoy function – looks important but unused in critical path
def compute_entropy(arr):
    entropy = 0.0
    for x in arr:
        if x > 0:
            entropy -= x * math.log(x)
    return entropy

# Core transformation with red herrings
def filter_anomalies(readings):
    threshold = sum(readings) / len(readings) + 1.5
    filtered = []
    for val in readings:
        if val < threshold and (val * 10) % 2 == 0:  # Additional constraint
            filtered.append(val)
    return filtered

# Misleading aggregation function
def calculate_baseline(samples):
    temp_offset = 0.3
    adjusted = [math.sin(x) + temp_offset for x in samples]
    return sum(adjusted) / len(adjusted)

# Conditional processing chain
def reconstruct_sequence(valid_items):
    sequence = []
    for item in valid_items:
        if item > 4.0:
            sequence.append(int(item * 2))
        elif item > 2.0:
            sequence.append(int(item * 3))
        else:
            sequence.append(int(item * 5))
    return sequence

# Bit manipulation layer (actual relevance)
def encode_features(seq):
    encoded = 0
    for num in seq:
        if num > 0:
            encoded ^= (num << 1) | (num & 1)  # XOR shift pattern
    return encoded

# Higher-level analysis with conditional expression
analyze_readings = lambda log: encode_features(log) if len(log) > 5 else -1

# Unused helper (dead code path)
def compress_dataset(arr):
    result = []
    for i in range(0, len(arr), 2):
        if i+1 < len(arr):
            result.append((arr[i], arr[i+1]))
    return result

# Primary execution flow
if __name__ == "__main__":
    # Step 1: Collect raw sensor data
    sensor_output = collect_readings()  # [0.0, 1.5, 3.0, 4.5, 6.0, 7.5, 9.0, ...]
    
    # Step 2: Normalize (irrelevant to final result)
    normalized_output = normalize_data(sensor_output)
    
    # Step 3: Filter anomalies based on dynamic threshold
    processed_logs = filter_anomalies(sensor_output)
    
    # Step 4: Reconstruct diagnostic sequence
    diagnostic_chain = reconstruct_sequence(processed_logs)
    
    # Step 5: Analyze using lambda function (key logic)
    final_diagnostic = analyze_readings(diagnostic_chain)
    
    # Print final result as required
    print(f"Result: {final_diagnostic}")