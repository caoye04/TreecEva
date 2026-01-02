import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0, 21.4, 27.3, 25.0, 22.8, 24.5, 19.9]
humidity_readings = [45, 48, 52, 58, 44, 50, 60, 54, 49, 53, 62, 56, 47, 51, 59]
pressure_readings = [1013, 1015, 1012, 1018, 1014, 1011, 1020, 1016, 1013, 1017, 1022, 1019, 1010, 1015, 1014]

# Irrelevant backup readings (distractor)
backup_temp_readings = [22.1, 23.0, 20.5, 24.8, 21.9]
backup_humidity_readings = [46, 49, 55, 57, 52]

# System thresholds and calibration data
critical_threshold = 26.0
warning_threshold = 24.0
humidity_baseline = 50
pressure_variation_limit = 10

# Decoy threshold sets (red herring)
decoy_thresholds_a = {20.0, 22.5, 25.0, 27.5}
decoy_thresholds_b = {18.5, 21.0, 23.5, 26.0, 28.5}

def preprocess_sensor_data(raw_temps, raw_humid, raw_pressure):
    # Normalize temperature using moving average (relevant)
    smoothed_temps = []
    for i in range(len(raw_temps)):
        window = raw_temps[max(0, i-2):min(len(raw_temps), i+3)]
        smoothed_temps.append(sum(window) / len(window))
    
    # Humidity correction based on temperature (irrelevant but plausible)
    corrected_humidity = [h + 0.1 * t for t, h in zip(smoothed_temps, raw_humid)]
    
    # Pressure trend analysis (distractor)
    pressure_trend = []
    for i in range(1, len(raw_pressure)):
        pressure_trend.append(raw_pressure[i] - raw_pressure[i-1])
    avg_trend = sum(pressure_trend) / len(pressure_trend) if pressure_trend else 0
    
    # Return only temperature data (misleading: other calculations are unused)
    return smoothed_temps

# Apply preprocessing
calibrated_temps = preprocess_sensor_data(temperature_readings, humidity_readings, pressure_readings)

# Generate composite index (unused distractor)
composite_health_index = 0
for t, h, p in zip(calibrated_temps, humidity_readings, pressure_readings):
    if t > warning_threshold:
        composite_health_index += 1
    if h > humidity_baseline:
        composite_health_index += 0.5
    if abs(p - 1015) > 5:
        composite_health_index -= 0.2

# Filtering logic with set operations
exceedance_set = {i for i, t in enumerate(calibrated_temps) if t >= critical_threshold}
warm_zones = {i for i, t in enumerate(calibrated_temps) if warning_threshold <= t < critical_threshold}
stable_zones = {i for i in range(len(calibrated_temps))} - exceedance_set - warm_zones

# Create threshold set using list comprehension and set logic (critical path)
thresh_values = [warning_threshold + 0.5 * i for i in range(5)]
threshold_set = {round(t, 1) for t in thresh_values if t >= 24.5}  # Results in {24.5, 25.0, 25.5, 26.0, 26.5}

# Simulate diagnostic classification matrix (complex but partially irrelevant)
diag_matrix = [[0 for _ in range(5)] for _ in range(3)]
for i, temp in enumerate(calibrated_temps):
    row = min(i // 5, 2)
    col = min(int((temp - 20) // 2), 4)
    diag_matrix[row][col] += 1

# Secondary validation map (dead code path)
validation_map = {}
for idx in exceedance_set:
    key = f"zone_{idx}"
    validation_map[key] = {
        'status': 'critical',
        'confirmations': 2,
        'retry_count': 0
    }

# Data filtering based on spatial proximity (relevant)
def filter_by_proximity(indices, max_gap=2):
    if not indices:
        return set()
    sorted_indices = sorted(indices)
    groups = []
    current_group = [sorted_indices[0]]
    
    for i in range(1, len(sorted_indices)):
        if sorted_indices[i] - sorted_indices[i-1] <= max_gap:
            current_group.append(sorted_indices[i])
        else:
            groups.append(current_group)
            current_group = [sorted_indices[i]]
    groups.append(current_group)
    
    # Return largest cluster
    largest = max(groups, key=len) if groups else []
    return set(largest)

filtered_exceedances = filter_by_proximity(exceedance_set)

# Mock temporal correlation analysis (distractor)
temporal_correlation = 0
if len(exceedance_set) > 1:
    gaps = [list(exceedance_set)[i+1] - list(exceedance_set)[i] for i in range(len(exceedance_set)-1)]
    temporal_correlation = sum(1 for g in gaps if g <= 3)

# Main diagnostic analyzer (critical function)
def analyze_readings(temp_data, thresh):
    # Count how many readings cross any threshold
    cross_count = 0
    for t in temp_data:
        if any(abs(t - ref) < 0.1 for ref in thresh):  # Exact match within float tolerance
            cross_count += 1

    # Compute entropy-like complexity measure (irrelevant)
    unique_vals = list(set(round(t, 1) for t in temp_data))
    value_freq = {v: temp_data.count(v) for v in unique_vals}
    total = len(temp_data)
    complexity_score = 0
    for freq in value_freq.values():
        p = freq / total
        complexity_score -= p * math.log(p) if p > 0 else 0
    
    # Spatial coherence metric (unused)
    sorted_vals = sorted(temp_data)
    coherence = 0
    for i in range(1, len(sorted_vals)):
        if sorted_vals[i] - sorted_vals[i-1] < 0.5:
            coherence += 1
    
    # Final diagnostic is cross_count multiplied by a scaling factor
    # Only cross_count matters; rest are distractions
    scaling_factor = 17
    final_diagnostic = cross_count * scaling_factor
    
    # Dead return path (misleading)
    detailed_report = {
        'coherence_index': coherence,
        'complexity_metric': complexity_score,
        'anomaly_count': len([t for t in temp_data if t >= 24.0]),
        'cross_threshold_events': cross_count
    }
    
    return final_diagnostic

# Execute main analysis
final_diagnostic = analyze_readings(calibrated_temps, threshold_set)
print(f"Target result: {final_diagnostic}")