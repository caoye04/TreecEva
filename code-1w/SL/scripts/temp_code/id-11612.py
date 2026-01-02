from collections import defaultdict
import math

# Simulate sensor readings with noise and calibration offsets
def get_sensor_data():
    raw_readings = [105, 203, 189, 203, 97, 150, 105, 189]
    calibration_map = {105: 100, 203: 200, 189: 190, 97: 95, 150: 145}
    return [calibration_map[r] for r in raw_readings]

# Identify repeated calibrated values and count occurrences
def analyze_repeats(data):
    count = defaultdict(int)
    for val in data:
        count[val] += 1
    return {k: v for k, v in count.items() if v > 1}

# Apply nonlinear transformation to suppress high-frequency fluctuations
def stabilize(signal):
    stabilized = []
    for x in signal:
        if x < 100:
            stabilized.append(x * 0.95)
        elif x > 190:
            stabilized.append(x * 0.90 + 10)
        else:
            stabilized.append(x * 1.02)
    return stabilized

# Misleading function that calculates unused metric
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values]
    entropy = -sum(p * math.log(p) for p in probs if p > 0)
    return entropy

# Unused helper: computes pairwise differences (distractor)
def pairwise_deltas(arr):
    return [abs(arr[i] - arr[i+1]) for i in range(len(arr)-1)]

# Core computation: scale values by factor and apply weighted aggregation
def compute_aggregate(scaled, weights):
    temp_result = 0
    for i in range(len(scaled)):
        temp_result += scaled[i] * weights[i % len(weights)]
    return int(temp_result)

# Main processing pipeline
if __name__ == "__main__":
    # Step 1: Retrieve and calibrate sensor data
    calibrated = get_sensor_data()  # [100, 200, 190, 200, 95, 145, 100, 190]

    # Step 2: Analyze repeated values (used later for weighting insight)
    repeats = analyze_repeats(calibrated)
    
    # Step 3: Stabilize signal to reduce noise impact
    processed_signal = stabilize(calibrated)
    
    # Step 4: Compute entropy (distraction, not used in final result)
    signal_entropy = compute_entropy(processed_signal)
    
    # Step 5: Calculate delta variations (dead code path)
    deltas = pairwise_deltas(calibrated)
    avg_delta = sum(deltas) / len(deltas) if deltas else 0
    
    # Step 6: Scale values using lambda-based normalization
    base_factor = 1.1
    scaler = lambda x: x * base_factor if x < 150 else x * 1.05
    scaled_values = [scaler(val) for val in processed_signal]
    
    # Step 7: Construct dynamic weights based on repeat frequency
    weight_map = defaultdict(lambda: 0.8)
    for k, v in repeats.items():
        weight_map[k] = 0.8 + 0.1 * v  # boost repeated values
    
    # Normalize weights for values present in scaled_values
    weights = [weight_map[int(round(v))] for v in scaled_values]
    
    # Step 8: Compute final score using weighted aggregation
    final_score = compute_aggregate(scaled_values, weights)
    
    # Output target result
    print(f"Result: {final_score}")