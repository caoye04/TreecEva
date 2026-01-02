import math

# Simulated sensor fusion system for environmental diagnostics
def preprocess_readings(readings):
    # Irrelevant transformation: normalize to z-scores (not used in final path)
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    z_scores = [(x - mean_val) / (variance ** 0.5) for x in readings]
    return [x * 1.1 for x in readings]  # Only scaled original values matter

def filter_anomalies(data):
    # Apply moving average filter (distraction)
    smoothed = [sum(data[i:i+3]) / 3 for i in range(len(data) - 2)]
    
    # Key logic hidden among distractors
    threshold = 50
    filtered_set = {x for x in data if x > threshold}  # Set operation (required)
    outlier_buffer = [x for x in data if x < 30]
    
    # Decoy correction using slicing
    adjusted = data[5:] + data[:5]  # Unused rotation
    return list(filtered_set)  # Return cleaned list above threshold

def rolling_window_average(values, window_size=3):
    # Dead function - looks important but unused
    if len(values) < window_size:
        return []
    return [sum(values[i:i+window_size]) / window_size for i in range(len(values) - window_size + 1)]

def recursive_energy_estimate(n):
    # Distractor recursion with no impact on result
    if n <= 1:
        return 1
    return n * 0.9 + recursive_energy_estimate(n - 2)

energy_baseline = recursive_energy_estimate(15)  # Red herring variable

# Sensor cluster simulation with decoy elements
temp_readings = [23, 45, 52, 61, 70, 44, 88, 31, 95, 67, 29, 55]
pressure_readings = [101, 98, 110, 120, 95, 105, 115, 125, 90, 130]
anomaly_flags = [False, True, False, True, False] * 2

# Primary diagnostic chain
primary_stream = preprocess_readings(temp_readings)

# Critical filtering operation
active_readings = filter_anomalies(primary_stream)

# Multi-step accumulation with distractions
accumulated_stress = 0
for i, val in enumerate(active_readings):
    if i % 2 == 0:
        accumulated_stress += val * 1.5
    else:
        accumulated_stress += val * 0.8

# Decoy data structure transformations
reading_pairs = [(active_readings[i], active_readings[i+1]) for i in range(0, len(active_readings)-1, 2)]
corrected_pairs = [pair[::-1] for pair in reading_pairs]  # Slicing operation (required)

# Final analysis function with logical branching
def analyze_readings(cleaned):
    base_score = sum(cleaned)
    penalty = 0
    
    # Logical operations and comparisons
    if len(cleaned) > 4 and sum(cleaned) > 300:
        penalty = 15
    elif len(cleaned) > 2:
        penalty = 5
    else:
        penalty = 0
    
    # Complex conditional with bit manipulation red herring
    debug_flag = 0b1010 ^ 0b1100  # XOR distraction
    mask_applied = debug_flag & 0b0101  # Unused bitwise result
    
    # Final computation
    diagnostic_value = base_score - penalty
    
    # Additional irrelevant transformation
    normalized_diag = diagnostic_value / max(cleaned)
    capped_result = min(normalized_diag, 100)
    
    return int(diagnostic_value)  # Answer derived here

# Execution point of interest
final_diagnostic = analyze_readings(filter_anomalies(sensor_cluster))

# Data that flows into critical path
sensor_cluster = [50, 51, 49, 75, 85, 60, 90, 48, 80]  # Original source

# Print final result as required
print(f"Result: {final_diagnostic}")