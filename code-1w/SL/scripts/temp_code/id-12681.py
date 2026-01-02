import math

# Simulated sensor data processing with diagnostic analysis
def fetch_raw_readings():
    return [14.2, 18.7, 25.3, 9.1, 30.5, 11.8, 22.4]

def calibrate(value, factor=0.93):
    return value * factor + 1.2

def is_anomaly(x):
    return x < 10.0 or x > 28.0

def smooth_sequence(data):
    smoothed = []
    for i in range(len(data)):
        left = data[i-1] if i > 0 else data[i]
        right = data[i+1] if i < len(data)-1 else data[i]
        avg = (left + data[i] + right) / 3
        smoothed.append(avg)
    return smoothed

def encode_status(code):
    # Irrelevant encoding function (dead path)
    mapping = {1: 'OK', 2: 'WARN', 3: 'ALERT'}
    return mapping.get(code, 'UNKNOWN')

def recursive_transform(seq, depth):
    if depth == 0 or not seq:
        return seq
    updated = [round(math.sqrt(x) * 1.5, 2) for x in seq]
    return recursive_transform(updated, depth - 1)

def filter_critical(data_list):
    # Misleading filter: looks important but unused later
    return [x for x in data_list if x > 20.0]

def compute_entropy(values):
    # Distractor: computes something plausible but irrelevant
    total = sum(values)
    probs = [v/total for v in values]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def case_convert(text):
    # Unused decoy function
    return ''.join(c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(text))

def analyze_pattern(dataset, limit):
    count = 0
    for val in dataset:
        if val > limit:
            count += 1
    return count * 17

def main():
    raw_readings = fetch_raw_readings()
    
    # Step 1: Calibrate each reading
    calibrated = [calibrate(x) for x in raw_readings]
    
    # Step 2: Detect anomalies (some are present)
    anomalies = list(filter(is_anomaly, calibrated))
    
    # Step 3: Smooth the sequence to reduce noise
    smoothed_data = smooth_sequence(calibrated)
    
    # Step 4: Apply recursive transformation (depth=2)
    transformed_data = recursive_transform(smoothed_data, 2)
    
    # Irrelevant intermediate computations (distractors)
    average_reading = sum(calibrated) / len(calibrated)
    outlier_count = len([x for x in calibrated if x > 25.0])
    entropy_metric = compute_entropy(calibrated)
    status_msg = encode_status(2)
    
    # Key control flow with conditional expression
    threshold = 4.5 if len(anomalies) > 2 else 3.8
    
    # Dead code path - never executed
    if False:
        fallback_data = filter_critical(transformed_data)
        case_convert('diagnostics')
    
    # Core computation: analyze pattern based on threshold
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()