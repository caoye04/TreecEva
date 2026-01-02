import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 27.3, 26.0, 22.7, 20.9, 28.1, 25.4]
humidity_readings = [45, 48, 52, 58, 61, 54, 49, 50, 63, 57]
pressure_readings = [1013, 1015, 1012, 1008, 1005, 1007, 1010, 1011, 1004, 1006]

# Irrelevant auxiliary arrays (distractors)
elevation_zones = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
station_ids = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
dummy_flags = [False, True, False, True, False, False, True, False, True, False]

# Misleading preprocessing - looks important but unused in final calculation
calibration_offsets = [x * 0.05 for x in range(10)]
adjusted_temps = [round(t + calibration_offsets[i], 2) for i, t in enumerate(temperature_readings)]

# Real processing begins: filter readings above humidity threshold
humidity_threshold = 50
high_humidity_indices = [i for i, h in enumerate(humidity_readings) if h > humidity_threshold]

# Extract corresponding temperature and pressure using indexing
selected_temps = [temperature_readings[i] for i in high_humidity_indices]
selected_pressures = [pressure_readings[i] for i in high_humidity_indices]

# Create composite data tuples
raw_samples = [(t, p) for t, p in zip(selected_temps, selected_pressures)]

# Apply nonlinear transformation to detect instability patterns
instability_scores = []
for temp, press in raw_samples:
    score = (temp ** 2) / (press + 1)  # Prevent division by zero
    instability_scores.append(round(score, 3))

# Decoy function - never called (dead code path)
def analyze_elevation_risk(elevations):
    risk_map = {}
    for zone in elevations:
        risk_map[zone] = sum([ord(c) for c in zone]) % 7
    return risk_map

# Another decoy: complex bit manipulation with no effect
aggregate_flag = 0
for flag in dummy_flags:
    aggregate_flag ^= int(flag)
    aggregate_flag <<= 1
    if aggregate_flag > 255:
        aggregate_flag = aggregate_flag % 256

# Real logic: group instability scores by temperature bands using conditional expression
band_mapping = []
for s, (temp, _) in zip(instability_scores, raw_samples):
    band = 'critical' if temp > 26 else 'elevated' if temp > 24 else 'normal'
    band_mapping.append((s, band))

# Filter only 'critical' and 'elevated' bands
filtered_data = [s for s, b in band_mapping if b in ['critical', 'elevated']]

# Threshold configuration map (used later)
threshold_map = {
    'critical': 1.85,
    'elevated': 1.65,
    'normal': 1.45
}

# Secondary decoy: unused combinatorics on irrelevant data
pair_combinations = list(itertools.combinations(station_ids, 2))
mean_id_pairs = [sum(pair) / 2 for pair in pair_combinations]
high_mean_groups = [m for m in mean_id_pairs if m > 1005]

# Tertiary decoy: slicing operation that does nothing meaningful
temp_slice = adjusted_temps[3:7:2]
scratch_value = sum(temp_slice) / len(temp_slice)

# Core diagnostic processor function
def process_readings(scores, thresholds):
    # Apply dynamic thresholding based on category
    critical_limit = thresholds['critical']
    elevated_limit = thresholds['elevated']
    
    # Count violations
    critical_violations = len([s for s in scores if s >= critical_limit])
    elevated_violations = len([s for s in scores if s >= elevated_limit and s < critical_limit])
    
    # Compute weighted risk index
    base_risk = critical_violations * 3.0 + elevated_violations * 1.5
    
    # Normalize by number of samples
    sample_count = len(scores) if scores else 1
    normalized_risk = base_risk / sample_count
    
    # Final nonlinearity
    diagnostic_score = (normalized_risk ** 2) * 10
    
    return int(round(diagnostic_score))

# Execute main computation
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")