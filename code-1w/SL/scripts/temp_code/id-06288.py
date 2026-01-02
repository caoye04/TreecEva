from collections import defaultdict, Counter

# Simulated sensor data processing for a thermal regulation system
raw_readings = [3.2, 3.5, 3.1, 3.4, 3.3, 3.6, 3.0, 3.7, 3.2, 3.5]

temperature_history = defaultdict(float)
for i, val in enumerate(raw_readings):
    temperature_history[f'sensor_{i % 3}'] += val

# Irrelevant: Count digit occurrences in string representations (red herring)
digit_counter = Counter()
for reading in raw_readings:
    for char in str(reading):
        if char.isdigit():
            digit_counter[char] += 1

# Decoy function: Unused but plausible
def calculate_stability_index(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return 1 / (1 + variance)

# Simulate multiple diagnostic phases
phase_weights = {
    'startup': 0.1,
    'calibration': 0.3,
    'operation': 0.6
}

# Misleading intermediate computation (dead path)
stability_metrics = []
for key, value in temperature_history.items():
    if 'sensor_1' in key:
        stability_metrics.append(value * 0.9)
    else:
        stability_metrics.append(value * 1.1)

# Actual relevant logic begins here — deeply nested and obscured
baseline_ref = sum(raw_readings[:4]) / 4
fluctuation_score = sum(abs(raw_readings[i] - raw_readings[i-1]) for i in range(1, len(raw_readings)))

if fluctuation_score > 1.5:
    aggregate_score = 45
else:
    aggregate_score = 30

# Simulated environmental compensation
external_factors = [-0.2, 0.3, -0.1, 0.4, 0.0]
compensation_factor = 0
for factor in external_factors:
    if factor > 0.25:
        compensation_factor += factor * 1.5
    elif factor < -0.15:
        compensation_factor -= 0.1  # Minor penalty

# Temperature normalization using conditional expression
current_temperature = raw_readings[-1]
temperature_factor = 2.0 if current_temperature > 3.5 else (1.0 if current_temperature > 3.3 else 0.5)

# Phase simulation with red herrings
active_phase = 'operation'
phase_multiplier = phase_weights.get(active_phase, 0.0)

# Dead code: complex bit manipulation (distractor)
bit_analysis = 0
for i in range(len(raw_readings)):
    shifted = i << 2
    masked = shifted & 0b1101
    bit_analysis ^= masked

# Another decoy: string-based status check
status_flags = ['OK', 'STABLE', 'ACTIVE', 'CALIBRATING']
overall_status = 'CRITICAL' if 'CAL' in ''.join(status_flags) else 'NORMAL'

# Key statement embedded in irrelevant context
intermediate_diagnostic = aggregate_score * phase_multiplier
temp_adjustment_log = f"Adjusting for {current_temperature:.1f}C"
final_diagnostic = aggregate_score + temperature_factor * phase_weights['operation']

# Print required output
print(f"Result: {final_diagnostic}")