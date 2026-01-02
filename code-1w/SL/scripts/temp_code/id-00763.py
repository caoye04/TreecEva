import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(size):
    return [i * 0.5 + (2 ** (i % 4)) for i in range(size)]

def filter_outliers(data, limit):
    # Irrelevant filtering function (not used in final computation)
    return [x for x in data if abs(x - sum(data)/len(data)) < limit]

def transform_readings(values):
    # Apply non-linear transformation
    processed = []
    for v in values:
        if v < 5:
            processed.append(v ** 2)
        elif v < 10:
            processed.append(v * 1.5)
        else:
            processed.append(math.log(v) * 3)
    return processed

def compute_entropy(arr):
    # Dead code path - not used in result
    total = sum(arr)
    probs = [a / total for a in arr if a > 0]
    return -sum(p * math.log2(p) for p in probs)

def detect_anomalies(seq, level=1.0):
    # Unused anomaly detector with red herring logic
    anomalies = 0
    for i in range(1, len(seq)):
        diff = abs(seq[i] - seq[i-1])
        if diff > level:
            anomalies += int(diff // level)
    return anomalies * 0.1  # Never contributes to answer

def evaluate_stability(readings):
    # Misleading intermediate metric
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return variance < 20

def compress_dataset(data):
    # Distractor: bit manipulation with no impact
    result = 0
    for i, val in enumerate(data):
        result ^= int(val) & (i % 16)
    return result  # Unused return

def analyze_pattern(dataset, cutoff):
    # Core logic embedded within noise
    count_valid = 0
    temp_sum = 0.0
    for item in dataset:
        if item > cutoff:
            count_valid += 1
            temp_sum += item
        else:
            # Simulate conditional side-effect (never triggers)
            temp_sum += 0.1 if item < 0 else 0
    if count_valid == 0:
        return 0
    score = temp_sum / count_valid
    
    # Secondary adjustment based on pattern length
    adjustment = len(dataset) % 7
    final_score = score * (1 + adjustment * 0.05)
    
    # Decoy branch that appears important but is logically unreachable
    if False and len(dataset) > 1000:
        backup = sum(dataset) / 100
        return backup
        
    return final_score

# Main execution flow
raw_sensor_data = collect_samples(25)

# Irrelevant transformations (distractors)
outlier_filtered = filter_outliers(raw_sensor_data, 8.0)
entropy_metric = compute_entropy(outlier_filtered)
stability_flag = evaluate_stability(raw_sensor_data)
anomaly_score = detect_anomalies(raw_sensor_data, 2.5)
compression_key = compress_dataset(raw_sensor_data)

# Relevant data path
transformed_data = transform_readings(raw_sensor_data)
threshold = 6.5

# Key statement
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Print result as required
print(f"Result: {final_diagnostic}")