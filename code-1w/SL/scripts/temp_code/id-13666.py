import math

def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return normalized

def compute_entropy(values):
    total = 0
    for v in values:
        if v > 0:
            total -= v * math.log(v)
    return round(total, 6)

def analyze_peaks(signal):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(i)
    return peaks if peaks else [0]

def simulate_buffer_overflow(data, size_limit=15):
    # Irrelevant simulation function - dead code path
    buffer = []
    for item in data:
        buffer.append(item * 2)
        if len(buffer) > size_limit:
            break
    return len(buffer) > size_limit

def evaluate_integrity(nodes):
    # Decoy function with misleading intermediate logic
    checksum = 0
    for node in nodes:
        for bit in range(8):
            checksum ^= (node >> bit) & 1
    return checksum % 7 == 0

def transform_coordinates(x_vals, y_vals):
    # Unused transformation - red herring
    transformed = []
    for x, y in zip(x_vals, y_vals):
        r = math.sqrt(x**2 + y**2)
        theta = math.atan2(y, x)
        transformed.append((r, theta))
    return transformed

def calculate_dispersion(arr):
    mean_val = sum(arr) / len(arr)
    variance = sum((x - mean_val) ** 2 for x in arr) / len(arr)
    return math.sqrt(variance)

def filter_anomalies(dataset, tolerance=2):
    dispersion = calculate_dispersion(dataset)
    mean_val = sum(dataset) / len(dataset)
    return [x for x in dataset if abs(x - mean_val) <= tolerance * dispersion]

def aggregate_metrics(readings_set, threshold):
    flattened = []
    for sublist in readings_set:
        for val in sublist:
            flattened.append(val)

    clean_data = filter_anomalies(flattened)
    entropy = compute_entropy([abs(x)/max(clean_data) for x in clean_data if x != 0])

    peak_indices = analyze_peaks(clean_data)
    avg_peak_pos = sum(peak_indices) / len(peak_indices)

    # Key computational branch
    if entropy > threshold:
        temp_score = (entropy * 100) + avg_peak_pos
        secondary_metric = len(clean_data) // 3
        temp_score -= secondary_metric
    else:
        temp_score = (entropy * 50) + 10

    # Critical distraction: irrelevant set operations
    unique_segments = set()
    for val in clean_data:
        segment = int(val * 10) % 5
        unique_segments.add(segment)

    decoy_value = len(unique_segments) * 17
    temp_score += decoy_value  # Misleading contribution

    # Another red herring: complex but unused calculation
    phantom_magnitude = 0
    for i, v in enumerate(clean_data):
        if i % 4 == 0:
            phantom_magnitude += math.sin(v) ** 2
    phantom_magnitude = int(phantom_magnitude * 100)

    # Final determination
    adjustment_factor = 1 if len(unique_segments) > 3 else 0.8
    final_diagnostic = int(temp_score * adjustment_factor)

    return final_diagnostic

# Simulated sensor input - realistic domain context (medical device diagnostics)
nested_readings = [
    [0.12, 0.88, 0.45, 0.91, 0.23, 0.67, 0.55],
    [0.33, 0.76, 0.41, 0.82, 0.59],
    [0.68, 0.71, 0.39, 0.93, 0.44, 0.62]
]

activation_threshold = 0.65

# Dead code assignments - irrelevant variables
baseline_reference = preprocess_signal([0.11, 0.22, 0.89, 0.43, 0.77])
diagnostic_map = transform_coordinates([1, 2, 3], [4, 5, 6])
overflow_flag = simulate_buffer_overflow(baseline_reference)
validity_check = evaluate_integrity([255, 128, 64, 32])

# Core execution point
final_diagnostic = aggregate_metrics(nested_readings, activation_threshold)

print(f"Result: {final_diagnostic}")