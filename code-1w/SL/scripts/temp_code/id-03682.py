import itertools

def preprocess_signal(raw_readings):
    filtered = [x for x in raw_readings if x > 0]
    shifted = [(x << 2) - 1 for x in filtered]
    return shifted

def generate_baseline(n):
    return [i ** 2 for i in range(n)]

def compute_entropy(data):
    # Irrelevant entropy calculation (dead-end function)
    total = sum(data)
    probs = [d / total for d in data]
    from math import log
    return -sum(p * log(p) for p in probs if p > 0)

def extract_features(signal):
    # Extract statistical features (some used, some not)
    mean_val = sum(signal) / len(signal)
    squared_devs = [(x - mean_val) ** 2 for x in signal]
    variance = sum(squared_devs) / len(squared_devs)
    peak = max(signal)
    # Decoy feature
    dummy_flag = any(x & 3 == 0 for x in signal)
    return {'mean': mean_val, 'var': variance, 'peak': peak}

def transform_sequence(seq):
    # Apply XOR mask and rotate
    masked = [x ^ 5 for x in seq]
    rotated = masked[3:] + masked[:3]
    return rotated

def validate_checksum(chunk):
    # Unused validation routine (red herring)
    checksum = 0
    for x in chunk:
        checksum ^= x
        checksum = (checksum << 1) & 0xFF
    return checksum == 0

def analyze_pattern(data):
    temp_result = 0
    for i, val in enumerate(data):
        if i % 2 == 0:
            temp_result += val * (i + 1)
        else:
            temp_result -= val // (i + 1)
    # Final transformation
    temp_result = abs(temp_result) ^ 987
    return temp_result

# Main execution block
raw_sensor_data = [12, -5, 24, 8, 0, 16, 7, 3]
threshold_mask = [x for x in raw_sensor_data if x > 10]  # Distractor list

# Step 1: Preprocess signal
processed = preprocess_signal(raw_sensor_data)

# Step 2: Generate irrelevant baseline pattern
baseline = generate_baseline(10)

# Step 3: Transform the processed data
transformed_data = transform_sequence(processed)

# Step 4: Extract features (partial usage)
features = extract_features(transformed_data)

# Step 5: Compute unused entropy
entropy_value = compute_entropy(transformed_data)  # Dead-end computation

# Step 6: Validate fake checksum (never called, but defined to distract)

# Step 7: Core analysis on transformed data
final_diagnostic = analyze_pattern(transformed_data)

# Step 8: Print result
print(f"Result: {final_diagnostic}")