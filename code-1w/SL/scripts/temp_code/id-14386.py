from collections import defaultdict, Counter
import itertools

# Simulated sensor readings over time (timestamp, temperature, pressure)
sensor_log = [
    (100, 22.5, 101.3), (105, 23.1, 101.2), (110, 24.0, 101.5),
    (115, 25.3, 102.1), (120, 26.0, 102.5), (125, 26.8, 102.7),
    (130, 27.5, 103.0), (135, 28.1, 103.2), (140, 28.8, 103.5),
    (145, 29.0, 103.7), (150, 29.2, 103.8)
]

# Irrelevant mapping - decoy for atmospheric models
atmosphere_zones = {'troposphere': 1, 'stratosphere': 2, 'mesosphere': 3}
zone_weights = defaultdict(float)
for zone, weight in atmosphere_zones.items():
    zone_weights[zone] += weight * 0.1

# Misleading preprocessing: unused transformation chain
def transform_pressure(p):
    return (p - 100) * 10 + 5  # Scaled but never used

scaled_pressures = [transform_pressure(p) for _, _, p in sensor_log]

# Distractor: fake entropy calculation with no impact
def compute_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        prob = count / total
        if prob > 0:
            entropy -= prob * __import__('math').log2(prob)
    return entropy

pressure_entropy = compute_entropy(scaled_pressures)

temperature_series = [t for _, t, _ in sensor_log]

def extract_trend(data):
    diffs = [data[i+1] - data[i] for i in range(len(data)-1)]
    return sum(diffs) / len(diffs)

temp_trend = extract_trend(temperature_series)

# Real processing begins here — subtle separation from noise
valid_readings = [(ts, t, p) for ts, t, p in sensor_log if 22 <= t <= 29]

# Filter using itertools and conditional logic
grouped_by_phase = []
current_group = []
for reading in valid_readings:
    if not current_group or reading[0] - current_group[-1][0] < 10:
        current_group.append(reading)
    else:
        if len(current_group) >= 3:
            grouped_by_phase.append(current_group)
        current_group = [reading]
if len(current_group) >= 3:
    grouped_by_phase.append(current_group)

# Only first phase group is relevant
primary_phase = grouped_by_phase[0] if grouped_by_phase else []

# Extract timestamps and temps for integration
phase_timestamps = [r[0] for r in primary_phase]
phase_temps = [r[1] for r in primary_phase]

# Simulate thermal hysteresis effect with shift
shifted_temps = [phase_temps[-1]] + phase_temps[:-1]

# Compute delta-time weighted temp accumulation
thermal_integral = 0
for i in range(1, len(phase_timestamps)):
    dt = phase_timestamps[i] - phase_timestamps[i-1]
    avg_temp = (shifted_temps[i] + phase_temps[i]) / 2
    thermal_integral += dt * avg_temp

# Decoy function — looks important but unused
def estimate_heat_flux(ts_list, temp_list):
    if len(ts_list) < 2:
        return 0.0
    delta_t = ts_list[-1] - ts_list[0]
    delta_temp = temp_list[-1] - temp_list[0]
    rate = delta_temp / delta_t if delta_t != 0 else 0
    conductivity = 0.87
    return rate * conductivity

# Another red herring: combinatorial explosion of invalid pairs
invalid_pairs = list(itertools.combinations(sensor_log, 2))
dummy_sum = sum(hash(str(p)) % 100 for p in invalid_pairs[:50])

# Critical processing path
processed_readings = [
    (ts, t, p, (t - 22.5) ** 2) for ts, t, p in primary_phase
    if t > 23.0 or ts < 115
]

# Main calculation function — only called once
def calculate_thermal_integral(readings):
    if not readings:
        return 0.0
    base = readings[0][1] * 10
    acc = 0
    for i, (ts, t, p, adj) in enumerate(readings):
        if i == 0:
            continue
        weight = 1 + (i * 0.1)
        acc += (t * weight) - adj
    # Final adjustment using modular arithmetic
    mod_factor = len(readings) % 7 or 1
    final_value = (base + acc) / mod_factor
    return round(final_value, 6)

# Key assignment statement
thermal_capacity = calculate_thermal_integral(processed_readings)

# Output result as required
print(f"Target result: {thermal_capacity}")