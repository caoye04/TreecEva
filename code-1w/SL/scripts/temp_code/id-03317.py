from collections import defaultdict, Counter
from itertools import combinations, cycle

# Simulated sensor network diagnostic tool
sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5']
timestamps = [100, 105, 110, 115, 120, 125]
raw_readings = [23.1, 24.5, 19.8, 25.6, 22.3, 20.1, 26.7, 23.4, 18.9, 24.0]

# Irrelevant mapping - red herring
id_to_location = {sid: f'Zone-{i % 3}' for i, sid in enumerate(sensor_ids)}

# Distractor function - never called
def legacy_calibrate(x):
    return [val * 0.98 + 0.5 for val in x]

# Another decoy - looks important but unused
baseline_shift = sum([abs(raw_readings[i] - raw_readings[i-1]) for i in range(1, len(raw_readings))]) / len(raw_readings)

# Real processing begins
readings_by_sensor = defaultdict(list)
sensor_cycle = cycle(sensor_ids)
for val in raw_readings:
    readings_by_sensor[next(sensor_cycle)].append(val)

# Misleading intermediate aggregation
peak_analysis = {sid: max(readings) - min(readings) for sid, readings in readings_by_sensor.items()}

# Fake fault detection (dead path)
fault_candidates = []
for sid, peaks in peak_analysis.items():
    if peaks > 5.0:
        fault_candidates.append(sid)  # This never triggers

# Actual relevant transformation
rolling_averages = []
for i in range(len(raw_readings) - 2):
    rolling_averages.append(sum(raw_readings[i:i+3]) / 3)

# Distractor: complex but unused combinatorial analysis
triplet_patterns = list(combinations(['low', 'med', 'high'], 3))
state_counter = Counter(triplet_patterns[0])  # Only used once, meaningless

# Data normalization (partially relevant)
normalized_offsets = []
base_ref = sum(rolling_averages) / len(rolling_averages)
for val in rolling_averages:
    normalized_offsets.append((val - base_ref) * 1.1)

# Decoy statistical measure
skew_proxy = sum([x**3 for x in normalized_offsets[:4]])  # Not used later

# Key processing function
processed_logs = []
for i, offset in enumerate(normalized_offsets):
    entry = {
        'seq': i,
        'value': offset,
        'flag': 'A' if offset > 0.5 else 'B' if offset < -0.5 else 'C',
        'meta': f'T-{timestamps[i] // 5}'
    }
    processed_logs.append(entry)

# Unused debugging artifact
log_summary = {item['flag']: sum(1 for e in processed_logs if e['flag'] == item['flag']) 
               for item in processed_logs}

# Critical function: actual answer computation path
def analyze_readings(log_entries):
    total_impact = 0.0
    decay_factor = 1.0
    
    # Real logic with accumulation
    for entry in log_entries:
        magnitude = abs(entry['value'])
        if entry['flag'] == 'A':
            total_impact += magnitude * decay_factor * 1.2
        elif entry['flag'] == 'B':
            total_impact -= magnitude * decay_factor * 0.8
        else:
            total_impact += magnitude * decay_factor * 0.5
        decay_factor *= 0.9  # Exponential decay
    
    # Secondary adjustment based on pattern density
    flag_sequence = [e['flag'] for e in log_entries]
    window_matches = 0
    for i in range(len(flag_sequence) - 2):
        if flag_sequence[i] == flag_sequence[i+1] == flag_sequence[i+2]:
            window_matches += 1
    
    # Final adjustment
    if window_matches >= 2:
        total_impact *= 1.15
    else:
        total_impact *= 0.95
    
    return round(total_impact, 6)

# Dead code path - looks like fallback
if not processed_logs:
    final_diagnostic = -999.0
else:
    final_diagnostic = analyze_readings(processed_logs)

print(f"Result: {final_diagnostic}")