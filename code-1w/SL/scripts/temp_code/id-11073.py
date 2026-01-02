import itertools

# Simulated sensor fusion system for autonomous drone navigation
sensory_data = [0.88, 0.92, 0.76, 0.81, 0.94]
weights = [0.2, 0.3, 0.15, 0.1, 0.25]

def normalize_readings(data):
    total = sum(data)
    return [x / total for x in data]

def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def apply_calibration(readings):
    # Irrelevant calibration function (dead path)
    scale_factor = 1.05
    return [r * scale_factor for r in readings]

def filter_outliers(data, threshold=0.1):
    median_val = sorted(data)[len(data)//2]
    return [x for x in data if abs(x - median_val) < threshold]

def compute_entropy(data):
    # Distractor: entropy calculation not used in final logic
    from math import log2
    return -sum(p * log2(p) for p in data if p > 0)

def rolling_average(data, window=2):
    # Unused signal processing function
    result = []
    for i in range(len(data) - window + 1):
        result.append(sum(data[i:i+window]) / window)
    return result

def detect_spike_pattern(sequence):
    # Red herring: detects rising-falling pattern but unused
    for i in range(1, len(sequence)-1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            return True
    return False

def generate_combinations(values):
    # Distractor using itertools - creates combinations but not used
    return list(itertools.combinations(values, 2))

def temporal_weight_adjustment(w):
    # Irrelevant transformation on weights
    shifted = [w[-1]] + w[:-1]
    return [(i+1)*val for i, val in enumerate(shifted)]

def dynamic_thresholding(score):
    # Dead branch: modifies score based on arbitrary rules
    if score > 0.9:
        return score * 0.95
    elif score < 0.7:
        return score * 1.1
    else:
        return score

def xor_fold(data):
    # Bit manipulation distractor
    int_vals = [int(x * 100) for x in data]
    result = 0
    for val in int_vals:
        result ^= val
    return result  # Never used

event_log = [{'type': 'sensor_update', 'value': s} for s in sensory_data]

# Real-time preprocessing stage (only normalization matters)
normalized_metrics = normalize_readings(sensory_data)

# Irrelevant combinatorial analysis
pairwise_interactions = generate_combinations(normalized_metrics)

# Security checksum (distractor)
security_hash = sum(int(x * 1000) & 255 for x in normalized_metrics)

# Main evaluation pipeline
config_flags = {"enable_fusion": True, "debug_mode": False}

# Weight validation (actually modifies weights)
if sum(weights) != 1.0:
    scaling = 1.0 / sum(weights)
    weights = [w * scaling for w in weights]

# Core performance evaluator
def evaluate_performance(metrics, w):
    # Actual critical computation
    base_score = sum(m * weight for m, weight in zip(metrics, w))
    
    # Distraction: complex conditional that doesn't affect outcome
    adjustment_factor = 1.0
    if base_score > 0.85:
        adjustment_factor = 0.98
    elif base_score < 0.75:
        adjustment_factor = 1.02
    
    # This lambda performs a redundant transformation
    enhance = lambda x: round(x, 4)
    adjusted_score = enhance(base_score * adjustment_factor)
    
    # Additional irrelevant bit operation
    fingerprint = adjusted_score * 10000
    bit_noise = int(fingerprint) ^ 0xFFFF
    
    # Final score assignment - only this matters
    final = int(round(adjusted_score * 10000)) / 10000.0
    
    # Early exit red herring (never triggered)
    if final < 0:
        return 0.0
        
    return final

# Execute main logic
final_score = evaluate_performance(normalized_metrics, weights)

# Print result as required
print(f"Result: {final_score}")