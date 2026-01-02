from collections import defaultdict
import itertools

# Simulate sensor data from multiple sources with noise filtering
def collect_sensor_readings():
    raw_data = [105, 110, 98, None, 102, 108, 100, 103, 107, 101]
    filtered = [x for x in raw_data if x is not None and x > 95]
    normalized = [(x - 95) for x in filtered]  # Normalize base
    return normalized

# Transform and scale values based on calibration factors
def calibrate_readings(readings):
    offset = 3
    adjusted = [x + offset for x in readings]
    amplified = [x * 1.5 for x in adjusted]  # Signal amplification
    truncated = [int(x) for x in amplified]  # Convert to integers
    return truncated

# Apply weighting schema across time-series segments
def compute_weights(length):
    base_weights = [0.8, 1.0, 1.2]
    repeated = list(itertools.chain.from_iterable(itertools.repeat(w, 3) for w in base_weights))
    return (repeated[:length])

# Aggregate weighted values with decay factor
def compute_aggregate(values, weights):
    if len(values) != len(weights):
        raise ValueError("Mismatched lengths")
    
    # Irrelevant accumulator for distraction
    temp_accumulator = 0
    debug_log = []
    for i in range(len(values)):
        temp_accumulator += values[i] * (i % 2 + 1)
        debug_log.append(f"step_{i}")
    
    # Actual computation path
    weighted_sum = sum(values[i] * weights[i] for i in range(len(values)))
    decay_factor = 0.95
    smoothed = weighted_sum * decay_factor
    
    # More red herring variables
    peak_value = max(values)
    avg_weight = sum(weights) / len(weights)
    penalty = peak_value * 0.05 if peak_value > 150 else 0
    final_score = int(smoothed - penalty)  # Final integer score
    
    # Dead code branch (never executed due to fixed input)
    if False and any(v < 0 for v in values):
        fallback = sum(values) // len(values)
        final_score = fallback
        
    return final_score

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect and clean sensor data
    raw_readings = collect_sensor_readings()
    
    # Step 2: Calibrate signal (add offset, amplify)
    calibrated = calibrate_readings(raw_readings)
    
    # Step 3: Generate time-decay weights
    weights = compute_weights(len(calibrated))
    
    # Step 4: Scale values using dynamic range mapping (distraction block)
    stats = defaultdict(int)
    for val in calibrated:
        if val < 20:
            stats['low'] += 1
        elif val < 30:
            stats['medium'] += 1
        else:
            stats['high'] += 1
    
    # Apply range-based scaling (not actually used later)
    scaled_values = []
    for v in calibrated:
        if v < 25:
            scaled_values.append(v * 1.1)
        elif v < 35:
            scaled_values.append(v * 1.05)
        else:
            scaled_values.append(v * 0.95)
    scaled_values = [int(x) for x in scaled_values]  # Discretize
    
    # Critical statement: compute final score
    final_score = compute_aggregate(scaled_values, weights)
    
    # Output result
    print(f"Result: {final_score}")