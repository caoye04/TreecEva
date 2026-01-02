import math

# Simulated sensor data processing system
def collect_sensor_data():
    return [0.85, 0.92, 0.78, 0.96, 0.88]

def normalize_readings(readings):
    max_val = max(readings)
    return [r / max_val for r in readings]

def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def apply_calibration(signal, factor=1.05):
    # Irrelevant calibration function (dead path)
    return [s * factor for s in signal]

def filter_outliers(data, threshold=2.0):
    # Misleading: not actually used in main logic
    mean = sum(data) / len(data)
    std = math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))
    return [x for x in data if abs(x - mean) <= threshold * std]

def compute_entropy(data):
    # Distractor: computes entropy but unused
    total = sum(data)
    probs = [d / total for d in data]
    return -sum(p * math.log(p) for p in probs if p > 0)

def transform_metrics(raw):
    # Applies nonlinear transformation to metrics
    transformed = []
    for val in raw:
        if val > 0.9:
            transformed.append(val ** 1.5)
        elif val > 0.8:
            transformed.append(val ** 1.2)
        else:
            transformed.append(val ** 0.9)
    return transformed

def bitwise_diagnostic(arr):
    # Complex-looking but irrelevant bit manipulation
    checksum = 0
    for i, val in enumerate(arr):
        checksum ^= int(val * 100) & 0xFF
        checksum = (checksum << 1) | (checksum >> 7)
        checksum &= 0xFF
    return checksum

def temporal_smoothing(data, alpha=0.3):
    # Unused smoothing function (red herring)
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(alpha * data[i] + (1 - alpha) * smoothed[-1])
    return smoothed

def evaluate_performance(metrics, weights):
    # Core logic hidden among distractions
    weighted_sum = 0
    for i in range(len(metrics)):
        weighted_sum += metrics[i] * weights[i]
    
    # Additional transformation
    if weighted_sum > 0.85:
        weighted_sum *= 1.1
    else:
        weighted_sum *= 0.95
    
    # Final adjustment based on arbitrary rule
    penalty = 0
    for m in metrics:
        if m < 0.8:
            penalty += 0.02
    
    result = weighted_sum - penalty
    return round(result, 6)

# Main execution flow
raw_metrics = collect_sensor_data()
normalized = normalize_readings(raw_metrics)

# Dead code paths and decoy variables
variance = calculate_variance(normalized)
entropy = compute_entropy(normalized)
diag_code = bitwise_diagnostic(normalized)
smoothed_data = temporal_smoothing(normalized)
calibrated = apply_calibration(normalized)

# Real processing begins here
transformed_metrics = transform_metrics(normalized)

# Weight vector - some distraction with unused alternatives
weights_full = [0.2, 0.25, 0.15, 0.3, 0.1]
weights_alt = [0.1, 0.3, 0.2, 0.25, 0.15]  # Not used
weights = weights_full  # Critical selection

# Secondary distractor: set operations with no impact
unique_set = set(transformed_metrics)
threshold_set = {x for x in unique_set if x > 0.8}
excluded_set = unique_set - threshold_set
size_diff = len(threshold_set) - len(excluded_set)  # Unused

# This looks like a fallback but never triggers
if len(excluded_set) > 3:
    weights = weights_alt

# Key statement
final_score = evaluate_performance(transformed_metrics, weights)

# Print final result
print(f"Result: {final_score}")