import math

# Simulated sensor array data processing with diagnostic evaluation
def preprocess_readings(raw_samples):
    filtered = [x for x in raw_samples if 0.1 <= x <= 99.9]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) * 100 for x in filtered]
    return normalized

# Irrelevant transformation: frequency analysis (dead path)
def compute_harmonics(signal):
    period = len(signal)
    harmonics = []
    for i in range(1, 6):
        harmonics.append(math.sin(2 * math.pi * i / period))
    return harmonics  # Never used

# Data windowing function (partially relevant)
def sliding_window(seq, size=3):
    windows = []
    for i in range(len(seq) - size + 1):
        windows.append(seq[i:i+size])
    return windows

# Core pattern analyzer
def detect_anomalies(series):
    anomalies = []
    for i in range(1, len(series)-1):
        if series[i] > series[i-1] and series[i] > series[i+1]:
            anomalies.append(i)
    return anomalies

# Secondary transformation chain
def apply_filters(data):
    temp_a = [x * 1.75 for x in data]
    temp_b = [math.log(x) if x > 0 else 0 for x in temp_a]
    rolled = temp_b[-5:] + temp_b[:-5]  # Circular shift
    return [round(x, 2) for x in rolled]

# Red herring: cryptographic hash simulation (no actual security use)
def generate_checksum(seq):
    acc = 0
    for val in seq:
        acc = (acc * 31 + int(val)) % 65537
    return acc  # Computed but unused

# Main pattern analysis with distractor logic
def analyze_pattern(dataset, threshold):
    # Distractor: set operations with irrelevant classification
    high_vals = {i for i, v in enumerate(dataset) if v > threshold}
    low_vals = {i for i, v in enumerate(dataset) if v <= threshold * 0.5}
    mid_range = high_vals.symmetric_difference(low_vals)
    
    # Distractor: dictionary-based mapping (unused result)
    index_map = {f'idx_{i}': val for i, val in enumerate(dataset)}
    sorted_indices = sorted(range(len(dataset)), key=lambda i: dataset[i], reverse=True)
    
    # Actual computation path
    slices = dataset[::2]  # Every other element
    slice_sum = sum(slices)
    
    # Conditional mutation based on length parity
    if len(dataset) % 2 == 0:
        adjustment = math.ceil(slice_sum / 10)
    else:
        adjustment = math.floor(slice_sum / 10)
    
    # Key intermediate value
    base_score = slice_sum + adjustment
    
    # Final branching logic
    if len(high_vals) > len(low_vals):
        multiplier = 1.5
    else:
        multiplier = 0.8
    
    final_result = base_score * multiplier
    return int(round(final_result))

# === Execution Flow ===
raw_sensor_data = [5.2, 12.8, 3.1, 88.4, 45.0, 1.9, 77.6, 92.3, 0.5, 100.1, -4.2]

# Step 1: Preprocess valid readings
cleaned_data = preprocess_readings(raw_sensor_data)

# Step 2: Apply primary transformation
transformed_data = apply_filters(cleaned_data)

# Irrelevant side computations (distractors)
freq_analysis = compute_harmonics(cleaned_data)
data_checksum = generate_checksum([int(x) for x in cleaned_data])

# Windowing applied but result not used directly
windows = sliding_window(transformed_data, 3)
anomaly_positions = detect_anomalies(transformed_data)

# Threshold derived from statistical distraction
key_threshold = sum(transformed_data) / len(transformed_data) - 5.5

# Critical statement
final_diagnostic = analyze_pattern(transformed_data, key_threshold)

# Output required format
print(f"Target result: {final_diagnostic}")