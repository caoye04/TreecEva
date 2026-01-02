import math

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.7, 25.3, 26.0, 24.8, 23.9, 25.1]
humidity_readings = [56, 61, 58, 63, 55, 60, 59, 62]
pressure_readings = [1013, 1015, 1012, 1016, 1018, 1014, 1017, 1019]

# Irrelevant calibration coefficients (distractor)
calibration_coefficients = [0.98, 1.02, 0.99, 1.01, 0.97, 1.03, 1.00, 0.96]
adjusted_temps = [t * cal for t, cal in zip(temperature_readings, calibration_coefficients)]  # unused path

# Signal processing pipeline
noise_floor = 0.5
filter_threshold = 24.0
anomaly_flags = []
processed_signals = []

for i, temp in enumerate(temperature_readings):
    # Compute derived humidity index (partially relevant)
    humidity_index = humidity_readings[i] / 100.0
    
    # Apply noise filter (relevant)
    if abs(temp - filter_threshold) < noise_floor:
        continue  # skip noisy readings
    
    # Compute signal quality score (distractor)
    signal_quality = (100 - abs(i - 3) * 2) if i % 2 == 0 else (90 - abs(i - 4) * 3)
    
    # Process valid signals
    normalized_temp = (temp - 20) / 5
    humidity_factor = math.log(humidity_index + 1) if humidity_index > 0 else 0
    composite_signal = normalized_temp + 0.3 * humidity_factor
    
    # Simulate bit-encoded status (mixed relevance)
    status_code = 0
    status_code |= (1 << 3) if temp > 24.5 else 0
    status_code |= (1 << 1) if humidity_readings[i] > 60 else 0
    status_code |= (1 << 2) if pressure_readings[i] > 1015 else 0
    
    processed_signals.append(composite_signal)
    anomaly_flags.append(status_code)

# Dead code path - unused analysis function (red herring)
def legacy_analysis(data):
    return sum(d ** 0.5 for d in data) / len(data)

# Auxiliary transformation (distractor)
shifted_pressure = [p - 1000 for p in pressure_readings]
squared_noise = [noise_floor ** 2 for _ in range(5)]

# Real-time windowing simulation (irrelevant)
window_size = 3
sliding_averages = []
for j in range(len(temperature_readings) - window_size + 1):
    window_avg = sum(temperature_readings[j:j+window_size]) / window_size
    sliding_averages.append(window_avg)

# Unused recursive helper (decoy)
def calculate_depth(value, depth=0):
    if value <= 1:
        return depth
    return calculate_depth(value / 2, depth + 1)

# Core diagnostic engine
prev_values = {}
def compute_stability_index(signal_list):
    if len(signal_list) == 0:
        return 0.0
    
    squared_diffs = []
    for k in range(1, len(signal_list)):
        diff = signal_list[k] - signal_list[k-1]
        squared_diffs.append(diff * diff)
    
    if not squared_diffs:
        return 0.0
    
    return math.sqrt(sum(squared_diffs) / len(squared_diffs))

# Secondary metric: trend consistency
consistency_score = 0
def evaluate_trend(data):
    nonlocal consistency_score
    up_count = 0
    down_count = 0
    for k in range(1, len(data)):
        if data[k] > data[k-1]:
            up_count += 1
        elif data[k] < data[k-1]:
            down_count += 1
    total_transitions = up_count + down_count
    consistency_score = (up_count - down_count) / total_transitions if total_transitions > 0 else 0
    return consistency_score

# Main analysis function
final_diagnostic = 0
def analyze_metrics(signals):
    global final_diagnostic
    
    # Step 1: Base stability
    stability = compute_stability_index(signals)
    
    # Step 2: Trend analysis
    trend_bias = evaluate_trend(signals)
    
    # Step 3: Outlier detection (simple)
    mean_signal = sum(signals) / len(signals)
    outliers = [s for s in signals if abs(s - mean_signal) > 2 * stability]
    
    # Step 4: Weighted combination
    weight_a = 0.6
    weight_b = 0.3
    weight_c = 0.1
    
    # Deliberately misleading intermediate (not used in final formula)
    fake_diagnostic = weight_a * stability + weight_b * abs(trend_bias) + weight_c * len(outliers)
    
    # Actual computation
    primary_metric = stability * 100
    secondary_metric = abs(trend_bias) * 50
    tertiary_metric = len(outliers) * 10
    
    result = primary_metric - secondary_metric + tertiary_metric
    
    # Final nonlinear adjustment
    if result > 40:
        result = result * 0.9
    elif result < 20:
        result = result * 1.1
    
    return int(result)

# Execute main logic
final_diagnostic = analyze_metrics(processed_signals)

# Print result as required
print(f"Result: {final_diagnostic}")