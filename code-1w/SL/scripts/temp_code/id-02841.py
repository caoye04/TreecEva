from collections import defaultdict, Counter
import math

# Simulated sensor data processing for environmental monitoring station
def analyze_readings(raw_samples):
    processed = []
    noise_floor = 0.041
    calibration_offset = 0.003
    for sample in raw_samples:
        corrected = sample - calibration_offset
        if abs(corrected) > noise_floor:
            processed.append(round(corrected * 1.02, 6))
    return processed

def compute_entropy(values):
    if not values:
        return 0.0
    counter = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counter.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def detect_anomalies(data_stream):
    anomalies = []
    moving_avg = 0
    count = 0
    for val in data_stream:
        moving_avg = (moving_avg * count + val) / (count + 1) if count > 0 else val
        count += 1
        if abs(val - moving_avg) > 0.05 and val > 0.1:
            anomalies.append((count-1, val))
    # Dead code path - never used in final logic
    if len(anomalies) > 10:
        return anomalies[:10]
    return anomalies

def transform_metrics(raw_data):
    # Irrelevant transformation chain
    temp_store = defaultdict(list)
    keys_used = ['A', 'B', 'C']
    for i, v in enumerate(raw_data):
        bucket = keys_used[i % 3]
        temp_store[bucket].append(v * (i + 1))
    
    flat_vals = []
    for k in ['A','B','C']:
        flat_vals.extend(temp_store[k])n    
    # Distractor computation: complex but unused result
    squared_sums = sum(x ** 2 for x in flat_vals) / len(flat_vals) if flat_vals else 0
    normalized = [x / max(flat_vals) if max(flat_vals) != 0 else 0 for x in flat_vals]
    
    # Actual relevant output
    return [round(x, 6) for x in raw_data[::3]]  # Every third element only

def evaluate_performance(metrics, threshold):
    score = 100
    penalty = 0
    
    # Meaningful logic step 1
    if len(metrics) == 0:
        return 0
    
    # Meaningful logic step 2
    avg_metric = sum(metrics) / len(metrics)
    
    # Meaningful logic step 3
    if avg_metric < threshold:
        penalty += 15
    
    # Meaningful logic step 4
    high_count = sum(1 for m in metrics if m > 0.5)
    
    # Meaningful logic step 5
    if high_count > len(metrics) // 2:
        penalty -= 10
    
    # Meaningful logic step 6
    stability = metrics[-1] - metrics[0]
    
    # Meaningful logic step 7
    if abs(stability) > 0.2:
        penalty += 12
    
    # Meaningful logic step 8
    adjustment = int(abs(avg_metric * 50))
    
    # Final calculation
    score = score - penalty + adjustment
    
    # Irrelevant block - dead code
    if score > 200:
        score = 200
    elif score < 0:
        score = 0
        
    return score

# --- Main Execution ---
raw_input_data = [
    0.12, 0.095, 0.11, 0.13, 0.088, 0.092,
    0.31, 0.33, 0.30, 0.42, 0.44, 0.41,
    0.52, 0.51, 0.53, 0.62, 0.63, 0.61
]

# Step 1: Analyze readings (relevant)
cleaned = analyze_readings(raw_input_data)

# Step 2: Compute entropy (distractor)
entropy_value = compute_entropy([int(x*100) for x in cleaned])

# Step 3: Detect anomalies (partially relevant index info, but not used directly)
anomaly_list = detect_anomalies(cleaned)

# Step 4: Transform metrics - extracts every third element
metric_data = transform_metrics(cleaned)

# Step 5: Base threshold derived from entropy (but entropy not actually needed)
dynamic_factor = len(anomaly_list) / 100 if anomaly_list else 0
base_threshold = 0.15 + dynamic_factor

# Step 6: Critical evaluation point
final_score = evaluate_performance(metric_data, base_threshold)

# Output result
print(f"Result: {final_score}")