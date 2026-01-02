import math

# Simulated sensor data processing pipeline for environmental monitoring station
def collect_readings():
    return [23.4, 25.1, 22.7, 24.3, 26.0, 23.9, 24.1, 25.5]

# Irrelevant auxiliary function - processes humidity (not used in final score)
def calculate_humidity_trend(humidity_data):
    avg = sum(humidity_data) / len(humidity_data)
    variance = sum((x - avg) ** 2 for x in humidity_data) / len(humidity_data)
    return round(avg - variance * 0.3, 2)

# Core metric computation with red herring logic
def normalize_readings(data, base=20.0):
    # Applies offset scaling but includes unused parameter
    normalized = [(x - base) * 1.8 + 2 for x in data]
    adjustment_factor = 0.95
    # Following line has no effect on output - distraction
    [x * adjustment_factor for x in normalized]  
    return normalized

# Misleading intermediate transformation
def apply_filter(signal):
    # Butterworth-like filter coefficients (simulated)
    a = [0.1, 0.25, 0.3]
    filtered = []
    for i in range(2, len(signal)):
        val = (a[0] * signal[i] + a[1] * signal[i-1] + a[2] * signal[i-2])
        filtered.append(val)
    return filtered  # Result gets discarded later

# Decoy aggregation function that looks important but isn't used
def compute_robust_mean(values, trim=0.1):
    sorted_vals = sorted(values)
    trim_count = int(len(sorted_vals) * trim)
    trimmed = sorted_vals[trim_count:-trim_count] if trim_count else sorted_vals
    return sum(trimmed) / len(trimmed)

# Weighted scoring using lambda and list comprehension
def evaluate_performance(raw_metrics, importance_weights):
    # Normalize metrics using min-max scaling
    min_val, max_val = min(raw_metrics), max(raw_metrics)
    scaled = [(x - min_val) / (max_val - min_val) if max_val != min_val else 0 for x in raw_metrics]
    
    # Apply exponential weighting via lambda
    exp_weight = lambda w: math.exp(w) - 1
    adjusted_weights = [exp_weight(w) for w in importance_weights]
    total_weight = sum(adjusted_weights)
    
    # Final weighted score
    weighted_sum = sum(scaled[i] * adjusted_weights[i] for i in range(len(scaled)))
    return int(round(weighted_sum / total_weight * 1000))  # Integer score out of 1000

# Unused anomaly detection system (dead code path)
def detect_anomalies(series, threshold=2.0):
    mean = sum(series) / len(series)
    std = math.sqrt(sum((x - mean)**2 for x in series) / len(series))
    return [i for i, x in enumerate(series) if abs(x - mean) > threshold * std]

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect temperature readings
    temperatures = collect_readings()
    
    # Step 2: Normalize readings (core step)
    processed = normalize_readings(temperatures)
    
    # Step 3: Apply filter - result stored but never used (distractor)
    filtered_signal = apply_filter(processed)
    
    # Step 4: Generate auxiliary fake metrics for confusion
    fake_enhanced_metrics = [x * 1.1 + 5 for x in processed[:5]]
    fake_enhanced_metrics.append(sum(processed) / len(processed))
    
    # Step 5: Define actual performance metrics (based on original processed data)
    metrics = [
        processed[0] * 2.1,
        processed[3] ** 1.5,
        math.log(processed[5] + 10),
        abs(processed[2] - processed[6]),
        sum(processed[:4]) / 4
    ]
    
    # Step 6: Assign weights (some look significant but all are used)
    weights = [0.8, 1.2, 0.9, 1.0, 1.1]
    
    # Step 7: Evaluate final performance score (key statement)
    final_score = evaluate_performance(metrics, weights)
    
    # Step 8: Print result
    print(f"Target result: {final_score}")
    