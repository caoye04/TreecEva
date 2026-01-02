import itertools

# Simulated sensor data from wind turbine array
turbine_ids = [101, 102, 103, 104]
sensor_readings = [
    [120, 125, 130, 118, 127],  # Turbine 101
    [145, 143, 150, 140, 142],  # Turbine 102 (slightly hotter)
    [119, 121, 123, 120, 122],  # Turbine 103
    [160, 165, 158, 162, 161]   # Turbine 104 (overheating?)
]

# Environmental compensation factors (irrelevant for final logic but looks important)
wind_speeds = [12.1, 13.4, 11.8, 14.0, 12.5]
temperature_humidity = [(25, 40), (26, 38), (24, 42), (27, 35), (25, 41)]

# Threshold configurations (only 'temp_threshold' is actually used)
thresholds = {
    'vibration_limit': 180,
    'pressure_floor': 85,
    'temp_threshold': 155,
    'rpm_ceiling': 1800,
    'current_cap': 220
}

# Historical baselines (distractor: not used in computation)
historical_averages = {
    101: 123.4,
    102: 144.6,
    103: 121.2,
    104: 130.1  # Incorrect entry — doesn't match current readings
}

# Auxiliary function that appears critical but is never called
def calculate_turbine_efficiency(rpm, load, temp):
    if temp > 150:
        return (load * 0.85) / rpm
    return load / rpm

# Another red herring: complex transformation with no downstream use
elevations = [80, 85, 78, 90]
adjusted_readings = []
for idx, readings in enumerate(sensor_readings):
    adjusted_row = []
    for r in readings:
        adj = r * (1 + (elevations[idx] * 0.001))  # Altitude adjustment
        adjusted_row.append(round(adj, 2))
    adjusted_readings.append(adjusted_row)

# Bit manipulation routine to simulate 'checksum' (unused)
def compute_sensor_checksum(data):
    checksum = 0
    for val in data:
        checksum ^= int(val * 10)
        checksum = (checksum << 1) & 0xFFFF
    return checksum

# Unused list comprehension with zip and enumerate (looks sophisticated)
reindexed_data = [
    (i, tid, max(readings))
    for i, (tid, readings) in enumerate(zip(turbine_ids, sensor_readings))
    if max(readings) > 140
]

# Core diagnostic logic — only this affects the final result
def analyze_temperature_spikes(readings, limit):
    spike_count = 0
    for seq in readings:
        for val in seq:
            if val > limit:
                spike_count += 1
    return spike_count

# Data transformer that seems essential but output isn't fully utilized
def preprocess_turbine_data(raw_data):
    flattened = list(itertools.chain.from_iterable(raw_data))
    normalized = [x - min(flattened) for x in flattened]  # Normalization step
    stats = {
        'mean': sum(normalized) / len(normalized),
        'max': max(normalized),
        'min': min(normalized)
    }
    return flattened, stats  # Only 'flattened' is used later

# Main aggregation function that computes the answer
def aggregate_metrics(turbine_data, config):
    flat_data, _ = preprocess_turbine_data(turbine_data)
    
    # Determine outlier count using threshold
    temp_limit = config['temp_threshold']
    outliers = [val for val in flat_data if val > temp_limit]
    
    # Compute secondary metric (appears important)
    avg_gap = sum([val - temp_limit for val in outliers]) / len(outliers) if outliers else 0
    
    # Diagnostic score based on bitwise interaction of counts
    base_count = len(outliers)
    spike_index = analyze_temperature_spikes(turbine_data, temp_limit)
    
    # Critical calculation: XOR then scale by modular factor
    raw_diagnostic = base_count ^ spike_index  # Should be 0 since both are 4
    scaled_diagnostic = raw_diagnostic * 100
    
    # Final adjustment using modular arithmetic (only relevant if scaled_diagnostic > 0)
    if scaled_diagnostic > 0:
        final_score = (scaled_diagnostic + 7) % 113
    else:
        final_score = 442  # Default when no variance detected
    
    # Dead code branch — never reached due to logic above
    if base_count == 0 and avg_gap < 5:
        final_score = 999
    
    return final_score

# Execution point of interest
turbine_data = sensor_readings
final_diagnostic = aggregate_metrics(turbine_data, thresholds)
print(f"Result: {final_diagnostic}")