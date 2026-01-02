import math

# Simulated sensor data processing with diagnostic evaluation
def collect_samples(base_signal, noise_level, count):
    return [base_signal * math.sin(i) + noise_level * math.cos(i * 1.5) for i in range(count)]

def filter_outliers(raw_readings, limit):
    # Irrelevant filtering (distractor)
    return [x for x in raw_readings if abs(x) < limit]

def compute_moving_average(data, window=3):
    smoothed = []
    for i in range(len(data) - window + 1):
        smoothed.append(sum(data[i:i+window]) / window)
    return smoothed  # Not used in final computation

def transform_signal(readings):
    # Applies logarithmic compression and normalizes
    offset = min(readings)
    scale = max(readings) - offset
    if scale == 0:
        scale = 1
    return [(math.log(abs(x - offset) + 1) / math.log(10)) for x in readings]

def detect_anomalies(mapped_values):
    # Dead code path — never called
    anomalies = []
    for i, val in enumerate(mapped_values):
        if val > 0.9 or val < 0.1:
            anomalies.append((i, val))
    return anomalies

def evaluate_entropy(sequence):
    # Decoy function: computes entropy but not used
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(sequence)
    entropy = -sum((count / total) * math.log2(count / total) for count in freq_map.values())
    return round(entropy, 4)

def generate_checksum(values):
    # Irrelevant checksum calculation
    checksum = 0
    for v in values:
        checksum ^= int(v * 1000) & 0xFF
    return checksum

def analyze_pattern(processed_stream, cutoff):
    # Core logic: count how many compressed values exceed cutoff after transformation
    count_above = sum(1 for v in processed_stream if v > cutoff)
    penalty = 0
    for i in range(1, len(processed_stream)):
        if processed_stream[i] > processed_stream[i-1]:
            penalty += 1
    return count_above * 7 - penalty // 2

# Main execution flow
if __name__ == '__main__':
    sample_size = 50
    base_frequency = 2.3
    noise_magnitude = 0.4

    # Step 1: Collect simulated sensor data
    raw_sensor_data = collect_samples(base_frequency, noise_magnitude, sample_size)

    # Distractor variables
    filtered_readings = filter_outliers(raw_sensor_data, limit=3.0)
    moving_avg_trend = compute_moving_average(raw_sensor_data, window=4)
    data_checksum = generate_checksum(raw_sensor_data)

    # Step 2: Transform data using non-linear scaling
    transformed_data = transform_signal(raw_sensor_data)

    # More red herrings
    entropy_metric = evaluate_entropy([round(x, 2) for x in transformed_data])
    anomaly_list = []  # Unused initialization

    # Threshold determined from obscure rule
    threshold = 0.65 if len(transformed_data) > 40 else 0.5

    # Key statement
    final_diagnostic = analyze_pattern(transformed_data, threshold)

    # Output result as required
    print(f"Target result: {final_diagnostic}")