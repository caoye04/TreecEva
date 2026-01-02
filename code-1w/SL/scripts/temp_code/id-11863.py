import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw_samples = [127, 255, 192, 64, 224, 32, 168, 96]
    scaled_data = [x / 2.0 for x in raw_samples]
    filtered_data = [x for x in scaled_data if x > 50]
    return filtered_data

# Irrelevant auxiliary function (decoy)
def calculate_checksum(data):
    checksum = 0
    for val in data:
        checksum ^= int(val)
    return checksum + 1000  # Red herring

# Bit manipulation for noise filtering (relevant only in part)
def mask_noise(value):
    shifted = int(value) & 0b111111
    return shifted | (shifted << 8)

# Data transformation using lambda and list comprehension
def transform(readings):
    base_shift = 42.5
    adjusted = [(lambda x: (x - base_shift) * 1.2)(val) for val in readings]
    exponent_mapped = [math.log(abs(x) + 1) for x in adjusted]
    return [round(x, 3) for x in exponent_mapped]

# Misleading statistical analysis (distractor)
def compute_anomalies(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    outliers = [x for x in data if abs(x - mean_val) > 1.5 * math.sqrt(variance)]
    return len(outliers) * 100  # Not used in final result

# Core pattern analyzer (critical path)
def detect_sequence(values):
    sequence_score = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            sequence_score += 1
        else:
            sequence_score -= 0.5
    return sequence_score

# Higher-level aggregation with tuple unpacking
def extract_features(data):
    count = len(data)
    total = sum(data)
    peak = max(data)
    trough = min(data)
    avg = total / count
    return (count, total, peak, trough, avg)

# Decoy diagnostic chain
def legacy_diagnostic(features):
    c, t, p, tr, a = features
    score = (p - tr) * c // (a + 1)
    return score * 5  # Dead end

# Actual core logic buried among distractions
def analyze_pattern(metrics):
    feature_set = extract_features(metrics)
    count, _, _, _, avg = feature_set
    
    # Irrelevant conditional branch (misleads control flow understanding)
    if count > 100:
        adjustment = 0.1 * avg
    elif count < 5:
        adjustment = -0.2 * avg
    else:
        adjustment = 0.05 * avg  # Only this branch matters
    
    trend = detect_sequence(metrics)
    base_index = avg * trend
    
    # Apply adjustment even though it's minor
    refined_index = base_index + adjustment
    
    # Final computation disguised among red herrings
    final_value = int(refined_index * 10) + 333
    return final_value

# Unused recursive function (distractor)
def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n - 2)

# Main execution flow
if __name__ == "__main__":
    # Collect initial sensor data
    sensor_metrics = collect_readings()
    
    # Compute irrelevant checksum
    verification_key = calculate_checksum(sensor_metrics)
    
    # Transform data through nonlinear mapping
    transformed_metrics = transform(sensor_metrics)
    
    # Generate decoy anomaly count
    anomaly_flag = compute_anomalies(transformed_metrics)
    
    # Extract structural features
    features = extract_features(transformed_metrics)
    
    # Run legacy diagnostic (unused)
    deprecated_result = legacy_diagnostic(features)
    
    # Critical statement: analyze the transformed pattern
    final_diagnostic = analyze_pattern(transformed_metrics)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")