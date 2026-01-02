def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return [round(x, 3) for x in normalized]


def generate_checksum(sequence):
    # Irrelevant helper with misleading complexity
    checksum = 0
    for i, val in enumerate(sequence):
        checksum += val * (i + 1) ** 2
    return checksum % 1000


def shift_window(data, size=3):
    # Unused function — red herring
    windows = []
    for i in range(len(data) - size + 1):
        windows.append(data[i:i+size])
    return windows


def encode_features(values):
    # Distractor transformation
    encoded = []
    for v in values:
        if v > 0.5:
            encoded.append(int(v * 10) | 7)
        else:
            encoded.append(int(v * 5) & 3)
    return encoded


def analyze_pattern(dataset, limit):
    count = 0
    trend = []
    for val in dataset:
        if val > 0.3 and val < 0.8:
            count += 1
            trend.append(val * 2)
    
    # Real logic branch
    if count >= limit:
        aggregate = sum(trend)
        adjustment = len([x for x in dataset if x < 0.1])  # List comprehension used
        result = int(aggregate * 100) - adjustment * 5
    else:
        result = -1 * count
    
    # Decoy manipulation — looks important but unused
    decoy_result = 0
    for i in range(len(dataset)):
        decoy_result += dataset[i] * (count % 5)
    decoy_result = round(decoy_result, 4)
    
    return result

# Main execution flow
raw_sensor_data = [0.05, 0.12, 0.34, 0.67, 0.23, 0.71, 0.01, 0.52, 0.88, 0.03]

# Irrelevant intermediate variables
checksum_diagnostic = generate_checksum(raw_sensor_data)
dummy_metadata = {'source': 'sensor_v2', 'calibrated': False}

# Preprocess step — relevant
processed_signal = preprocess_signal(raw_sensor_data)

# Encoding branch — dead end, not used later
feature_codes = encode_features(processed_signal)

# Transform data through filtering logic
transformed_data = [x for x in processed_signal if x > 0.05]

# Threshold computed from character counting in a fixed string (non-obvious)
config_tag = 'DLX_TRIG_2048'
thresh_str = ''.join([c for c in config_tag if c.isdigit()])
threshold = len(thresh_str)  # evaluates to 4

# Key statement
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Print result as required
print(f"Target result: {final_diagnostic}")