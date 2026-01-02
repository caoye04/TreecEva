import math

# Sensor calibration constants (irrelevant to final result)
CALIBRATION_FACTOR_A = 0.87
CALIBRATION_OFFSET_B = -0.34
REFERENCE_VOLTAGE = 5.0

# System thresholds and configuration (mix of relevant and irrelevant)
default_limits = [0.5, 1.2, 2.8, 4.0]
threshold_set = {1, 3, 4, 6, 7, 9}  # Used in final analysis
critical_indices = {2, 5, 8}  # Distractor: never used

# Simulated raw sensor data from environmental monitoring array
event_log = [
    (1, 15, 3.2), (2, 18, 1.9), (3, 12, 4.1),
    (4, 22, 2.3), (5, 14, 3.7), (6, 19, 2.8),
    (7, 11, 4.5), (8, 25, 1.6), (9, 17, 3.0)
]

# Irrelevant transformation: voltage simulation
def simulate_voltage(current, resistance):
    return current * resistance * REFERENCE_VOLTAGE / 100.0

# Misleading preprocessing: averages that won't be used
temp_averages = []
for _, temp, _ in event_log:
    temp_averages.append(temp * CALIBRATION_FACTOR_A + CALIBRATION_OFFSET_B)

# Core data extraction and filtering
raw_readings = [reading for _, _, reading in event_log if reading > 2.5]

# Distractor: complex bit manipulation with no impact
bit_encoded = 0
for val in raw_readings:
    bit_encoded ^= int(val * 10) << 1
bit_encoded = (bit_encoded & 0xFF) | 0x100

# Secondary derived values (some relevant, some not)
derived_metrics = []
for idx, (_, temp, reading) in enumerate(event_log):
    metric = math.sqrt(reading ** 2 + temp * 0.1)
    if idx % 2 == 0:
        metric += 0.25
    derived_metrics.append(round(metric, 2))

# Actual processing path: filter and transform raw_readings
processed_data = []
for val in raw_readings:
    transformed = abs(val - 3.0) * 2.5
    if transformed >= 1.0:
        processed_data.append(int(transformed))

# Dead code path - appears important but unused
def deprecated_analysis(data):
    if len(data) > 5:
        return sum(d ** 0.5 for d in data) / len(data)
    else:
        return max(data) - min(data)

# Key function with multiple logic branches and early returns
def analyze_readings(data, thresholds):
    if not data:
        return -999
    
    # Compute frequency of occurrence
    freq_map = {}
    for d in data:
        freq_map[d] = freq_map.get(d, 0) + 1
    
    # Identify values matching threshold set by index parity
    matched_count = 0
    for i, value in enumerate(data):
        if i in thresholds and value in thresholds:
            matched_count += 1
        elif value == 4 and i in {3, 6}:
            matched_count += 2  # Special case that doesn't trigger
    
    # Determine mode, fallback to median
    sorted_vals = sorted(freq_map.keys())
    if len(sorted_vals) == 0:
        mode = 0
    else:
        mode = max(freq_map, key=freq_map.get)
    
    median = sorted_vals[len(sorted_vals)//2]
    
    # Primary computation: weighted diagnostic score
    base_score = 0
    for v in data:
        if v in threshold_set:
            base_score += v * 1.5
        else:
            base_score -= 0.8
    
    # Apply mode/median adjustment
    if mode >= median:
        base_score += mode
    else:
        base_score -= median
    
    # Final adjustment based on matched count (mostly zero)
    adjustment = matched_count * 3
    
    # Early return red herring
    if adjustment > 10:
        return 999  # Never reached
    
    # Critical calculation
    final_score = base_score + adjustment
    
    # Round to nearest integer
    return int(round(final_score))

# Additional decoy function using set operations (unused)
def compute_anomalies(readings, limits):
    upper = {r for r in readings if r > max(limits)}
    lower = {r for r in readings if r < min(limits)}
    return upper | lower

# Execute main logic chain
baseline_check = deprecated_analysis(raw_readings)  # Unused result
anomaly_set = compute_anomalies(raw_readings, default_limits)  # Unused

# Key execution point
final_diagnostic = analyze_readings(processed_data, threshold_set)

print(f"Result: {final_diagnostic}")