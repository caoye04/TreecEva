import math

# Simulated sensor data processing with performance scoring
def collect_metrics():
    raw_readings = [127, 255, 98, 153, 64, 201]
    processed = [x & 127 for x in raw_readings]  # Mask to 7 bits
    normalized = [round((x / 127.0) * 100, 2) for x in processed]
    return normalized

# Irrelevant auxiliary function - dead code path
def legacy_calibrate(data):
    return [d * 0.95 for d in data if d > 50]

# Weight adjustment using bitwise logic (real computation)
def adjust_weights(base_weights, epoch):
    shift = epoch % 3 + 1
    return [(w * 1000) ^ epoch for w in base_weights]  # XOR perturbation

# Secondary metric transformation - looks important but unused
transform_metric = lambda x: int((x ** 0.5) * 10)
temp_scaling = [transform_metric(v) for v in range(5, 10)]

# Core evaluation logic
def compute_efficiency(score_list):
    total = 0
    for s in score_list:
        if s < 70:
            continue
        elif s > 90:
            total += s * 1.2
        else:
            total += s * 0.95
    return round(total, 3)

# Distractor: fake aggregation that isn't used
fake_aggregate = sum([i * i for i in range(6)]) // 2

# Real weight configuration (used)
basic_weights = [3, 2, 4, 1, 5, 3]

def evaluate_reliability(data):
    parity_check = 0
    for val in data:
        parity_check ^= int(val)
    return parity_check % 100

# Main scoring function
def evaluate_performance(metrics, weights):
    efficiency = compute_efficiency(metrics)
    
    # Dummy transformation on weights (partially irrelevant)
    dummy_shifted = [w << 1 for w in weights]
    adjusted_weights = adjust_weights(weights, 7)
    
    # Weighted sum with modular arithmetic
    weighted_sum = 0
    for i in range(len(metrics)):
        idx = i % len(adjusted_weights)
        contribution = metrics[i] * (adjusted_weights[idx] % 7)
        weighted_sum += contribution
    
    # Apply non-linear boost
    boosted = weighted_sum * (1.0 + (efficiency / 1000))
    
    # Fake redundancy calculation - looks like error correction
    checksum = 0
    for c in str(int(boosted)):
        checksum = (checksum + int(c)) % 11
    if checksum > 5:
        boosted *= 0.97
    
    reliability = evaluate_reliability(metrics)
    final_raw = boosted + reliability
    
    # Critical red herring: similar variable name, unused
    final_score_shadow = round(final_raw * 0.85, 2)
    
    final_score = int(round(final_raw / 3.0))  # Actual answer derivation
    
    # Unused complex list slicing that appears significant
    history_log = [final_score - i*10 for i in range(5)]
    recent_trend = history_log[-3:]  # Dead end
    anomaly_detected = any(x < 0 for x in recent_trend)
    
    return final_score

# Global decoy variables
system_baseline = 420
calibration_offset = sum([i for i in range(10)]) * 2
reference_map = {i: chr(65+i) for i in range(10)}

# Execution flow
data_metrics = collect_metrics()  # [100.0, 100.0, 77.17, 120.47, 50.39, 158.27] -> clipped to valid
clipped_metrics = [min(m, 100) for m in data_metrics]

# Unused alternate processing branch
if len(clipped_metrics) > 4:
    smoothed = [sum(clipped_metrics[i:i+3])/3 for i in range(4)]

final_score = evaluate_performance(clipped_metrics, basic_weights)
print(f"Target result: {final_score}")