import itertools

# Simulated sensor diagnostics for a distributed system
sensor_ids = ['S1', 'S2', 'S3', 'S4']
base_readings = [54, 27, 81, 36]
status_codes = [1, 0, 1, 1]
timestamps = [1623456780, 1623456785, 1623456790, 1623456795]

def normalize_reading(value, max_val=100):
    # Irrelevant normalization function (not used in final path)
    return round(value / max_val, 3)

def compute_hash(sensors, codes):
    # Distractor: computes a hash but not used in main logic
    combined = ''.join([sid + str(c) for sid, c in zip(sensors, codes)])
    return sum(ord(c) for c in combined) % 1000

# Dead code path — never called
def legacy_diagnose(data):
    if len(data) > 3:
        return sum(data) // len(data)
    return -1

# Unused transformation
shifted_readings = [r + 10 for r in base_readings if r < 50]
filtered_sensors = {sid: val for sid, val in zip(sensor_ids, base_readings) if val > 30}

# Real processing begins here
readings_set = set(base_readings)
enabled_sensors = [sid for sid, code in zip(sensor_ids, status_codes) if code == 1]

# Generate all valid pairs of enabled sensors
sensor_pairs = list(itertools.combinations(enabled_sensors, 2))
pair_scores = {}
for pair in sensor_pairs:
    idx1 = sensor_ids.index(pair[0])
    idx2 = sensor_ids.index(pair[1])
    score = abs(base_readings[idx1] - base_readings[idx2]) * (idx1 + idx2 + 1)
    pair_scores[pair] = score

# Threshold computation with red herring intermediate
threshold_basis = [v for v in pair_scores.values() if v > 20]
noise_floor = sum(threshold_basis) / len(threshold_basis) if threshold_basis else 0
primary_threshold = int(noise_floor * 0.45)  # Key threshold
secondary_threshold = sum(base_readings) // 4  # Distractor

# Diagnostic levels based on multiple conditions
level_map = {}
for i, reading in enumerate(base_readings):
    if status_codes[i] == 0:
        level_map[sensor_ids[i]] = 0
    elif reading > primary_threshold and (i+1)*(reading//9) % 2 == 0:
        level_map[sensor_ids[i]] = 2
    else:
        level_map[sensor_ids[i]] = 1

# Another unused diagnostic path
historical_trends = []
for t in timestamps:
    if t % 5 == 0:
        historical_trends.append(t % 17)

# Core analysis function
thresholds = {
    'critical': primary_threshold,
    'warning': primary_threshold * 0.6,
    'info': 5
}
diagnostics = []
for sid, reading in zip(sensor_ids, base_readings):
    lvl = level_map[sid]
    trend_factor = (timestamps[sensor_ids.index(sid)] // 1000) % 4
    adjusted = reading + trend_factor * lvl
n    diagnostics.append(adjusted)

# Misleading aggregation
aggregate_diagnostics = sum(diagnostics) + len(sensor_pairs)
buffer_overflow_sim = aggregate_diagnostics % 97

# Final pattern analysis (key statement)
def analyze_pattern(data, limits):
    count_above_critical = 0
    total_contribution = 0
    critical_limit = limits['critical']
    
    for val in data:
        # Complex filtering condition
        if val > critical_limit:
            # Additional check involving index-like behavior
            pos = data.index(val)
            if (pos + 1) * val > 100:
                count_above_critical += 1
                total_contribution += val // (pos + 1)
    
    # Redundant checks
    if count_above_critical == 0:
        return -100
    elif count_above_critical == 1:
        return total_contribution * 2
    else:
        return total_contribution + count_above_critical * 10

final_diagnostic = analyze_pattern(diagnostics, thresholds)
print(f"Result: {final_diagnostic}")