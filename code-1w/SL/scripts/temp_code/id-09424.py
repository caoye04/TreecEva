from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulated sensor array data with noise and calibration offsets
def collect_sensor_readings():
    raw_signals = [127, 255, 86, 194, 63, 215, 94]
    calibration_map = {i: val * 0.95 for i, val in enumerate(raw_signals)}
    noise_profile = [0.1, -0.2, 0.15, -0.05, 0.3, -0.1, 0.08]
    readings = []
    for i in range(7):
        calibrated = calibration_map[i] + noise_profile[i] * 10
        if i % 3 == 0:
            adjusted = abs(calibrated - 5)  # Red herring adjustment
        else:
            adjusted = calibrated + 2  # Irrelevant offset
        readings.append(round(adjusted, 2))
    return readings

# Legacy function - unused but looks important
def legacy_normalization(data):
    max_val = max(data)
    return [x / max_val * 100 for x in data]

# Signal trend analyzer with decoy logic
def extract_trends(readings):
    trends = []
    for i in range(1, len(readings)):
        delta = readings[i] - readings[i-1]
        if delta > 10:
            trend_code = 1
        elif delta < -10:
            trend_code = -1
        else:
            trend_code = 0
        trends.append(trend_code)
    
    # Decoy accumulation (never used)
    cumulative_drift = sum(abs(readings[i+1] - readings[i]) for i in range(len(readings)-1))
    stability_score = 100 - cumulative_drift  # Looks important, not used
    
    # Inject artificial oscillation pattern
    extended_trends = []
    for t in trends:
        extended_trends.extend([t] * 2)
    
    # Use itertools to create cyclic padding
    padded = [0] * 3 + list(islice(cycle(extended_trends), 20))
    return padded[:len(trends)]

# Main processing pipeline
def compute_weights(trends):
    weight_map = defaultdict(float)
    counter = Counter(trends)
    total = sum(counter.values())
    
    # Assign weights based on frequency (relevant)
    for key in counter:
        weight_map[key] = counter[key] / total
    
    # Add irrelevant categories with zero impact
    weight_map[-2] = 0.05  # Fake rare event
    weight_map[2] = 0.02   # Another decoy
    
    # Dead code path - never executed due to logic above
    if len(trends) > 100:
        fallback = {k: v * 0.1 for k, v in weight_map.items()}
        return fallback
    
    return dict(weight_map)

# Core aggregation function with critical computation
def aggregate_metrics(trends, weights):
    base_score = 0
    for i, trend in enumerate(trends):
        # Only trends with even index contribute meaningfully
        if i % 2 == 0:
            base_score += trend * weights.get(trend, 0.1)
    
    # Complex-looking but irrelevant transformation
    transformed = base_score ** 2 + base_score * 0.5
    normalized = abs(transformed) % 100
    
    # Final answer is actually just base_score rounded
    final_value = round(base_score, 4)
    
    # Distractor: elaborate logging that doesn't affect result
    debug_info = []
    for w in weights:
        debug_info.append(f"W{w}:{weights[w]:.3f}")
    log_entry = '|'.join(debug_info)  # Unused string construction
    
    return final_value

# Orchestration
if __name__ == "__main__":
    # Step 1: Collect sensor data
    sensor_output = collect_sensor_readings()
    
    # Step 2: Extract temporal trends
    trend_data = extract_trends(sensor_output)
    
    # Step 3: Compute weighting schema
    weights = compute_weights(trend_data)
    
    # Step 4: Aggregate into diagnostic metric (KEY STATEMENT)
    final_diagnostic = aggregate_metrics(trend_data, weights)
    
    # Output target result
    print(f"Result: {final_diagnostic}")