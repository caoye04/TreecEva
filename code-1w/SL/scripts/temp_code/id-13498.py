import math

# Simulated system metrics from a distributed computing environment
def collect_metrics():
    raw_data = [127, 83, 95, 112, 64]
    processed = []
    for val in raw_data:
        if val > 100:
            processed.append(val * 0.85)
        elif val > 75:
            processed.append(val * 0.92)
        else:
            processed.append(val * 1.05)
    return processed

# Weight calibration with irrelevant transformations
def calibrate_weights(base):
    temp = [w ** 1.1 for w in base]
    adjusted = []
    for x in temp:
        if x < 3:
            adjusted.append(math.log(x + 1))
        elif x < 7:
            adjusted.append(math.sqrt(x) * 1.2)
        else:
            adjusted.append(x * 0.8)
    # Decoy normalization (never used)
    s = sum(adjusted)
    normalized = [v / s for v in adjusted]
    return adjusted  # Original adjusted returned

# Bit-flipping decoy function (looks relevant but unused)
def flip_bits(value):
    """Irrelevant bit manipulation for distraction"""
    result = 0
    for i in range(8):
        result |= ((value >> i) & 1) << (7 - i)
    return result

# Unused recursive checksum (dead path)
def checksum(arr, idx=0):
    if idx >= len(arr) - 1:
        return arr[idx] % 17
    return (arr[idx] + checksum(arr, idx + 1)) % 23

# Real evaluation logic buried among distractions
def evaluate_performance(met, wts):
    # Apply weighted harmonic mean with filtering
    filtered_pairs = [(m, w) for m, w in zip(met, wts) if m > 80]
    
    # Irrelevant set operation (distractor)
    unique_caps = set(int(m * 10) // 10 for m in met)
    threshold_set = {x for x in unique_caps if x % 16 == 0}
    dummy_enhancement = len(threshold_set) * 1.5 if threshold_set else 0
    
    # Actual computation
    weighted_inv_sum = 0.0
    weight_sum = 0.0
    for metric_val, weight in filtered_pairs:
        if metric_val > 0:
            weighted_inv_sum += weight / metric_val
            weight_sum += weight
    
    # Early exit red herring (never triggered in this case)
    if len(met) == 0:
        return -1
    
    # Correct result: harmonic mean inverse
    if weighted_inv_sum == 0:
        return 0
    harmonic_base = weight_sum / weighted_inv_sum
    
    # Secondary adjustment using unused bit function (but not actually called)
    # Misleading comment: "// adjust for bit entropy" (but no such thing)
    final = harmonic_base + (0.7 if len(filtered_pairs) >= 3 else -0.3)
    return final

# Dead code branch (never reached)
def deprecated_aggregation(data):
    total = 0
    for d in data:
        total += d << 2
    return total >> 1

# Main execution flow
if __name__ == "__main__":
    # Collect performance metrics
    metrics = collect_metrics()
    
    # These values look important but some are decoys
    base_weights = [2.1, 3.5, 1.8, 4.0, 2.7]
    weights = calibrate_weights(base_weights)
    
    # Unused variables to distract
    max_metric = max(metrics)
    avg_weight = sum(weights) / len(weights)
    
    # Checksum computed but not used (red herring)
    integrity = checksum(metrics)
    
    # Bit-noise array (irrelevant)
    noise_floor = [flip_bits(int(m)) for m in metrics]
    
    # Core calculation
    intermediate = [m * w for m, w in zip(metrics, weights)]
    aggregate = sum(intermediate) / sum(weights)
    
    # The real answer comes from evaluate_performance, not aggregate
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")