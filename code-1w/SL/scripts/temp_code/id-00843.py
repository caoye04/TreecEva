def analyze_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    normalized = [m / max(metrics) for m in metrics]
    
    # Semi-relevant filtering
    passed = [i for i, m in enumerate(metrics) if m >= thresholds[i % len(thresholds)]]
    
    # Dead code path (misleading)
    if len(passed) > 100:
        return -1  # unreachable due to input size
    
    return passed

# Simulate sensor readings and expected baselines
sensor_data = [85, 90, 78, 92, 88, 76, 95, 89]
baseline_thresholds = [80, 85, 75, 90]

# Misleading intermediate computation (not used later)
correlation_matrix = list(zip(sensor_data[:-1], sensor_data[1:]))
drift_estimate = sum(abs(a - b) for a, b in correlation_matrix) // len(correlation_matrix)

# Extract indices of stable performance periods
stable_indices = analyze_performance(sensor_data, baseline_thresholds)

# Compute rolling efficiency (distraction with tuple unpacking)
efficiency_pairs = []
for i, val in enumerate(sensor_data[:-1]):
    efficiency_pairs.append((val, sensor_data[i+1], (val + sensor_data[i+1]) / 2))

# Use set operations to find unique high performers
high_performers = {i for i, s in enumerate(sensor_data) if s >= 90}
borderline_cases = {i for i, s in enumerate(sensor_data) if 75 <= s < 80}
ambiguous_set = high_performers & borderline_cases  # empty by design

# Core logic: score based on position and pattern
position_bonus = 0
for idx in stable_indices:
    if idx % 2 == 0:
        position_bonus += 5
    else:
        position_bonus += 2

# Secondary adjustment using distractor variables
temp_offset = len(correlation_matrix) - len(ambiguous_set)
final_score = position_bonus * 3 + temp_offset * 0  # neutralized term

# Critical output
print(f"Result: {final_score}")