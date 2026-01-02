import itertools

# Simulated sensor array data from environmental monitoring system
def collect_sensor_data():
    raw_readings = [23.5, 24.1, 19.8, 22.7, 25.3, 26.0, 21.4, 20.9]
    calibration_offset = 0.7
    adjusted = [r + calibration_offset for r in raw_readings]
    return adjusted

# Legacy function for compatibility - not used in current logic
def legacy_normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Signal processing pipeline
def preprocess_signal(raw_data, filter_strength=0.9):
    smoothed = []
    for i in range(len(raw_data)):
        weight = filter_strength if i % 2 == 0 else 1.0
        smoothed.append(raw_data[i] * weight)
    return smoothed

# Redundant transformation - simulates alternate processing path
def transform_magnitude(data):
    return [abs(x) ** 0.5 for x in data]

# Frequency domain approximation (unused decoy)
def estimate_dominant_frequency(signal):
    period_guess = len(signal) // 3
    return 1.0 / period_guess if period_guess > 0 else 0.0

# Main analysis engine
def generate_signature(profile):
    base_sig = sum(x * (i + 1) for i, x in enumerate(profile[:4]))
    return base_sig * 1.07

# Threshold configuration map - critical for final decision
threshold_map = {
    'critical': 98.0,
    'elevated': 85.0,
    'normal': 60.0
}

# Secondary check with misleading intermediate result
auxiliary_score = 0.0
for val in [88, 72, 91, 67]:
    auxiliary_score += val * 0.25  # Results in 79.5 - looks important but unused

# Complex conditional activation pattern
def evaluate_stability(measurements):
    if len(measurements) < 6:
        return False
    sorted_vals = sorted(measurements)
    median_diff = sorted_vals[-1] - sorted_vals[0]
    return median_diff < 10.0

# Primary data processing workflow
def process_environmental_data(sensor_input):
    stage_one = preprocess_signal(sensor_input)
    
    # Apply corrective scaling based on time-of-day factor (simulated)
    time_factor = 1.02
    corrected = [val * time_factor for val in stage_one]
    
    # Generate diagnostic features using combinatorial approach
    feature_pool = list(itertools.combinations(corrected[:4], 2))
    derived_features = []
    for pair in feature_pool:
        derived_features.append((pair[0] + pair[1]) / 2.0)
    
    # Filter noise using moving window (simplified)
    filtered = []
    window_size = 2
    for i in range(len(derived_features) - window_size + 1):
        window_avg = sum(derived_features[i:i+window_size]) / window_size
        filtered.append(window_avg)
    
    # Final aggregation
    aggregate_metric = sum(filtered) * 0.87
    return aggregate_metric

# Core diagnostic analyzer
def analyze_signal(working_data, limits):
    signature = generate_signature(working_data)
    stability = evaluate_stability(working_data)
    
    # Determine classification level
    if signature > limits['critical'] and stability:
        level_code = 5
    elif signature > limits['elevated']:
        level_code = 4
    elif signature > limits['normal']:
        level_code = 3
    else:
        level_code = 2
    
    # Final diagnostic computation
    base_diagnostic = signature * level_code
    adjustment_factor = 0.91 if stability else 1.05
    final_diagnostic = base_diagnostic * adjustment_factor
    
    # Dead code branch - red herring
    if False:
        fallback = sum(working_data) / len(working_data)
        final_diagnostic = fallback * 10  # Never executed
    
    return final_diagnostic

# Orchestration sequence
sensor_data = collect_sensor_data()
processed_data = process_environmental_data(sensor_data)
final_diagnostic = analyze_signal(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")