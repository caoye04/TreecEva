def analyze_telemetry(data_stream):
    checksum = 0
    for i, val in enumerate(data_stream):
        if i % 2 == 0:
            checksum += val * (i + 1)
        else:
            checksum -= val // 2
    return checksum

def extract_features(records):
    features = []
    for idx, record in enumerate(records):
        magnitude = sum([x ** 2 for x in record]) ** 0.5
        parity_flag = magnitude > 50 and idx % 3 == 0
        if parity_flag:
            features.append(magnitude * 1.1)
        else:
            features.append(magnitude)
    return features

def filter_outliers(seq, threshold=75.0):
    # Irrelevant filtering pass: does not impact final result
    cleaned = [x for x in seq if x <= threshold]
    return cleaned if len(cleaned) > 0 else [0]

def evaluate_performance(metrics, weights):
    base_score = 0
    temp_adjustment = 0
    
    for j, (m, w) in enumerate(zip(metrics, weights)):
        if j == 0:
            base_score += m * w
        elif j == 1:
            temp_adjustment = int(m) // 4
            base_score += (m + temp_adjustment) * w
        elif j == 2:
            # Simulate bitwise sensitivity
            influence = int(m) ^ int(w * 10)
            base_score += influence * 0.5
        else:
            base_score += m * w * 0.9
    
    # Additional distraction: unused intermediate calculation
    peak_metric = max(metrics) if metrics else 0
    decay_factor = peak_metric * 0.01
    dummy_state = [decay_factor * i for i in range(5)]
    
    return int(base_score)

# Main execution
raw_data = [12, 18, 25, 30, 14]
data_checksum = analyze_telemetry(raw_data)

sensor_records = [
    [3, 4, 5],
    [10, 11, 12],
    [7, 24, 25],
    [8, 15, 17]
]
feature_vector = extract_features(sensor_records)

filtered_metrics = filter_outliers(feature_vector, threshold=80.0)

# Add irrelevant transformation
scaled_metrics = [(x * 1.05) for x in feature_vector]

# Key variables for evaluation
metrics = [data_checksum, feature_vector[2], 45.0, 60.0]
weights = [0.2, 0.3, 0.4, 0.1]

# Dead code path - misleading state tracking
status_log = []
for step in range(3):
    status_log.append(f"Processing phase {step}")

# Critical statement
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")