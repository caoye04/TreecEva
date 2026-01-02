import math

# Sensor calibration constants (some are red herrings)
CALIBRATION_A = 0.872
CALIBRATION_B = 1.045
CALIBRATION_C = 2.11  # Unused in actual logic
CALIBRATION_D = 0.0034  # Used only in decoy function

# Simulated raw sensor readings from environmental array
temp_readings = [22.1, 23.5, 24.0, 25.8, 26.3, 25.9, 24.7, 23.2]
humidity_readings = [45, 47, 50, 55, 58, 54, 50, 48]
pressure_readings = [1013, 1012, 1015, 1017, 1016, 1014, 1013, 1012]  # Not used directly

# Decoy transformation - looks important but unused
def apply_pressure_compensation(data, factor=0.0012):
    return [x * (1 + factor) for x in data]

# Function to filter anomalies using sliding window (actually used)
def detect_anomalies(series, threshold=1.5):
    mean_val = sum(series) / len(series)
    std_dev = (sum((x - mean_val) ** 2 for x in series) / len(series)) ** 0.5
    return [abs(x - mean_val) <= threshold * std_dev for x in series]

# Data normalization with misleading scaling factors
def normalize_range(value, old_min, old_max, new_min, new_max):
    return ((value - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min

# Core processing: integrates multiple concepts
def process_sensor_data(temp, humidity):
    # Step 1: Normalize temperature to weighted index
    temp_norm = [normalize_range(t, 20, 30, 0, 1) * 0.6 for t in temp]
    
    # Step 2: Normalize humidity with different scale
    humidity_norm = [normalize_range(h, 0, 100, 0, 1) * 0.4 for h in humidity]
    
    # Step 3: Combine indices
    combined_index = [t + h for t, h in zip(temp_norm, humidity_norm)]
    
    # Step 4: Apply logarithmic stabilization (avoids negative values)
    stabilized = [math.log(1 + x) for x in combined_index]
    
    # Step 5: Detect valid readings based on anomaly detection
    validity_mask = detect_anomalies(stabilized, threshold=1.2)
    
    # Step 6: Only keep stabilized values where reading is valid
    filtered_stabilized = [s for s, valid in zip(stabilized, validity_mask) if valid]
    
    # Step 7: Compute moving average over 2-point window
    if len(filtered_stabilized) < 2:
        return filtered_stabilized
    
    moving_avg = [
        (filtered_stabilized[i] + filtered_stabilized[i+1]) / 2
        for i in range(len(filtered_stabilized)-1)
    ]
    
    # Step 8: Amplify signal using exponential (relevant to final result)
    amplified = [math.exp(m * 0.5) for m in moving_avg]
    
    return amplified

# Secondary analysis function that appears complex but mostly distracts
def compute_harmonic_weights(n):
    """Decoy function - looks useful but not part of main flow"""
    if n == 0:
        return []
    weights = []
    for i in range(1, n+1):
        weights.append(1/i)
    total = sum(weights)
    return [w/total for w in weights]

# Critical recursive function for diagnostic scoring
def recursive_diagnostic_score(seq, depth=0):
    if depth >= 3 or len(seq) == 0:
        return 0.0
    if len(seq) == 1:
        return seq[0] * (3 - depth)
    mid = len(seq) // 2
    left_part = seq[:mid]
    right_part = seq[mid:]
    return (
        recursive_diagnostic_score(left_part, depth + 1) +
        recursive_diagnostic_score(right_part, depth + 1)
    )

# Main analysis function - entry point for correct logic chain
def analyze_readings(signal_data):
    if not signal_data:
        return -1
    
    # Apply bit manipulation mask to simulate digital filtering (key step)
    int_equivalents = [int(x * 1000) for x in signal_data]
    masked_values = [val & 0xFF for val in int_equivalents]  # Extract lower 8 bits
    
    # Convert back to fractional form
    reduced_signal = [mv / 1000.0 for mv in masked_values]
    
    # Perform final integration via recursive scoring
    score = recursive_diagnostic_score(reduced_signal)
    
    # Final adjustment based on list comprehension with conditional logic
    adjusted_values = [
        v * 1.1 if i % 2 == 0 else v * 0.9
        for i, v in enumerate(reduced_signal)
    ]
    
    # The real answer depends on sum of adjusted values multiplied by depth factor
    final_component = sum(adjusted_values) * (3 - len(str(int(sum(reduced_signal)))) + 1)
    
    return int(round(final_component * 100))  # Scale up and round to integer

# Irrelevant preprocessing block (distractor)
baseline_correction = [
    (p - 1012) * CALIBRATION_D for p in pressure_readings
]

# Another decoy: harmonic interpolation that isn't used
harmonics = compute_harmonic_weights(len(temp_readings))
interpolated = [temp_readings[i] * harmonics[i] for i in range(len(temp_readings))] if harmonics else temp_readings

# Actual execution path starts here
processed_data = process_sensor_data(temp_readings, humidity_readings)

# Additional distraction: fake fusion routine
fusion_matrix = [
    [a * b for b in humidity_readings] for a in temp_readings
]

# Key statement
final_diagnostic = analyze_readings(processed_data)

print(f"Result: {final_diagnostic}")