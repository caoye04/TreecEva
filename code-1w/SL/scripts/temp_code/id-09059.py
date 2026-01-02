import itertools

# Simulated sensor array data from environmental monitoring station
def acquire_sensor_data():
    raw_samples = [127, 85, 193, 44, 201, 76, 154, 221]
    offset = 3
    calibrated = [(x + offset) % 256 for x in raw_samples]
    return calibrated

# Irrelevant transformation - red herring function
def transform_coordinates(latitudes, longitudes):
    return list(zip(longitudes[::-1], [lat * 0.01 for lat in latitudes]))

# Unused helper - dead code path
def deprecated_filter(data, threshold=100):
    return [x for x in data if x > threshold]

# Signal preprocessing with multiple distraction paths
def preprocess_signal(raw_data):
    shifted = [x << 1 for x in raw_data]  # Bit shift left by 1
    masked = [x & 0xFF for x in shifted]   # Ensure 8-bit range
    
    # Distractor: complex but unused computation chain
    cumulative = 0
    history_log = []
    for idx, val in enumerate(masked):
        if idx % 3 == 0:
            cumulative += val ^ (idx + 5)
        history_log.append(cumulative * 2)
    
    # Actual relevant transformation
    filtered = [x for x in masked if x % 2 == 1]  # Keep only odd values
    normalized = [round(x / 255.0, 6) for x in filtered]
    return normalized

# Core analysis logic with modular arithmetic and counting
def analyze_readings(signals):
    count_valid = 0
    sum_phases = 0.0
    
    # Use of enumerate and zip as required
    for i, signal in enumerate(signals):
        phase = signal * (i + 1)
        if phase > 0.5:
            count_valid += 1
        sum_phases += phase
    
    # Use of itertools to create artificial complexity
    pairs = list(itertools.combinations_with_replacement([0.1, 0.25, 0.5], 2))
    adjustment_factor = 0
    for p in pairs:
        if p[0] != p[1]:
            adjustment_factor += 1
    
    # Decoy calculation - looks important but unused
    baseline_ref = sum([s * s for s in signals])
    temporal_weight = len(pairs) * 0.07
    
    # Critical logic: modular arithmetic and conditional counting
    mod_index = (count_valid * 3) % 7
    if mod_index in [1, 3, 5]:
        diagnostic_score = int((sum_phases * 1000) % 10000)
    else:
        diagnostic_score = int((sum_phases * 500) % 5000)
    
    # Final irrelevant manipulation (misleads with additional processing)
    final_adjusted = diagnostic_score
    for _ in range(3):
        final_adjusted = (final_adjusted ^ 0xAA) & 0xFFFF
    
    return final_adjusted

# Unused data structures - distractors
latitude_grid = [40.12, 41.33, 42.05, 43.78, 44.10, 45.67, 46.89, 47.21]
longitude_grid = [-74.00, -75.22, -76.45, -77.88, -78.91, -79.03, -80.15, -81.77]
coord_map = transform_coordinates(latitude_grid, longitude_grid)

# Main execution flow
sensor_input = acquire_sensor_data()
processed_signals = preprocess_signal(sensor_input)
final_diagnostic = analyze_readings(processed_signals)
print(f"Result: {final_diagnostic}")