import math

# Simulated sensor array diagnostics with interference
sensor_ids = [f'SNSR-{i:03d}' for i in range(1, 21)]
active_zones = {'Zone-A', 'Zone-B', 'Zone-C', 'Zone-D'}
calibration_offsets = {i: round(math.sin(i * 0.3) * 0.7, 4) for i in range(20)}

# Irrelevant lookup table for deprecated hardware
legacy_mapping = {
    'L01': 'Alpha', 'L02': 'Beta', 'M03': 'Gamma', 'X04': 'Delta',
    'Y05': 'Epsilon', 'Z06': 'Zeta'
}

# Fake signal noise generator (dead code path)
def generate_noise(samples, freq=0.1):
    return [math.cos(freq * i) + 0.1 * math.sin(i * 0.5) for i in range(samples)]

# Unused recursive filter (decoy function)
def recursive_dampen(signal, depth=3):
    if depth == 0 or len(signal) < 2:
        return signal
    smoothed = [(signal[i] + signal[i+1]) / 2 for i in range(len(signal)-1)]
    return recursive_dampen(smoothed, depth-1)

# Core diagnostic engine
operational_thresholds = {
    'voltage': (2.0, 3.6),
    'current': (0.1, 1.2),
    'temperature': (-40.0, 85.0),
    'frequency_lock': True
}

# Simulated raw telemetry logs
raw_logs = [
    {'id': 'SNSR-003', 'v': 2.8, 'i': 0.45, 't': 23.1, 'locked': True},
    {'id': 'SNSR-007', 'v': 1.9, 'i': 0.67, 't': 31.8, 'locked': False},
    {'id': 'SNSR-012', 'v': 3.1, 'i': 0.33, 't': -12.5, 'locked': True},
    {'id': 'SNSR-015', 'v': 2.5, 'i': 1.35, 't': 72.4, 'locked': True},
    {'id': 'SNSR-019', 'v': 3.4, 'i': 0.89, 't': 86.1, 'locked': True}
]

# Extraneous data transformation (irrelevant)
shadow_copy = [
    {k: (v * 1.01 if isinstance(v, float) else v) for k, v in log.items()}
    for log in raw_logs
]

# Distractor: unused statistical summary
data_skew = sum(log['t'] ** 2 for log in raw_logs) / len(raw_logs)
baseline_anchor = math.sqrt(abs(data_skew - 2000))

# Real processing begins here
voltage_warnings = 0
temp_violations = 0
unstable_sensors = 0

processed_logs = []

for entry in raw_logs:
    # Extract readings
    v, i, t = entry['v'], entry['i'], entry['t']
    is_locked = entry['locked']

    # Validate against thresholds
    v_min, v_max = operational_thresholds['voltage']
    t_min, t_max = operational_thresholds['temperature']

    # Check anomalies (real logic)
    if v < v_min or v > v_max:
        voltage_warnings += 1

    if t < t_min or t > t_max:
        temp_violations += 1

    if not is_locked or i > 1.2:
        unstable_sensors += 1

    # Transform into processed format
    processed_entry = {
        'sensor': entry['id'],
        'power_index': round(v * i, 3),
        'thermal_zone': 'HIGH' if t > 50 else 'NORMAL',
        'status_flag': 0 if (v_min <= v <= v_max and t_min <= t <= t_max and is_locked) else 1
    }
    processed_logs.append(processed_entry)

# Secondary analysis pass (real logic)
flagged_count = sum(log['status_flag'] for log in processed_logs)
efficiency_metric = sum(log['power_index'] for log in processed_logs) / len(processed_logs)

# Set-based zone analysis (core concept)
affected_zones = set()
for log in processed_logs:
    sensor_num = int(log['sensor'][5:])
    if sensor_num < 5:
        affected_zones.add('Zone-A')
    elif sensor_num < 10:
        affected_zones.add('Zone-B')
    elif sensor_num < 15:
        affected_zones.add('Zone-C')
    else:
        affected_zones.add('Zone-D')

# Critical cross-check: only zones with flagged sensors contribute
valid_zones = affected_zones.intersection({'Zone-A', 'Zone-B', 'Zone-C'})
zone_penalty = len(valid_zones) * 100

# Irrelevant geometric calculation (distraction)
phantom_area = 0
for i in range(1, 6):
    phantom_area += math.pi * (i ** 2) * 0.001

# Final diagnostic computation chain
base_score = 500
base_score -= voltage_warnings * 15
base_score -= temp_violations * 25
base_score -= unstable_sensors * 20
base_score -= flagged_count * 30
base_score -= int(efficiency_metric * 5)
base_score -= zone_penalty

# Final adjustment using set difference (key operation)
dormant_zones = active_zones.difference(affected_zones)
if len(dormant_zones) >= 2:
    base_score += 42  # recovery bonus

# Key assignment statement
final_diagnostic = analyze_readings(processed_logs)

# Function definition moved here to obscure relevance
def analyze_readings(logs):
    # This function actually just returns the precomputed base_score
    # All above processing mutates global state; this is a facade
    return base_score

# Print result as required
print(f"Result: {final_diagnostic}")