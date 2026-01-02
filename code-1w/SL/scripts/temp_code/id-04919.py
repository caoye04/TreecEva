import math

# Simulated dataset representing sensor readings with noise and metadata
data_stream = [
    {'value': 12.5, 'type': 'temp', 'seq': 1, 'valid': True},
    {'value': 8.2, 'type': 'temp', 'seq': 2, 'valid': True},
    {'value': 15.3, 'type': 'temp', 'seq': 3, 'valid': False},  # Invalid reading
    {'value': 9.7, 'type': 'temp', 'seq': 4, 'valid': True},
    {'value': 11.0, 'type': 'temp', 'seq': 5, 'valid': True}
]

# Irrelevant auxiliary data — distractor (dead code path)
legacy_config = {
    'version': '1.2a',
    'debug_mode': True,
    'threshold': 999,  # Unused parameter
    'calibration': [0.1, 0.2, 0.3, 0.4]
}

# Decoy function — looks important but never called
def legacy_calibrate(x):
    return [val * 1.5 for val in x if val > 0.2]

# Another decoy — unused transformation
redundant_mapping = {i: chr(65 + i % 26) for i in range(50)}

# Extract valid temperature values using list comprehension and enumerate
valid_temps = [
    entry['value'] for idx, entry in enumerate(data_stream)
    if entry['type'] == 'temp' and entry['valid']
]

# Compute rolling differences — irrelevant intermediate result
rolling_diffs = [valid_temps[i+1] - valid_temps[i] for i in range(len(valid_temps)-1)]

# Artificially inflate some values — misleading computation
inflated_values = [x * 1.1 for x in valid_temps if x < 10]
offset_compensation = sum(inflated_values) if inflated_values else 0.0

# Hidden baseline correction using zip and offset
baseline_shifts = [0.5, -0.3, 0.7, 0.0, -0.2]
compensated = [
    a + b for a, b in zip(valid_temps, baseline_shifts[:len(valid_temps)])
]

# Apply non-linear transformation: logarithmic scaling on compensated values
log_scaled = [math.log(val) if val > 0 else 0 for val in compensated]

# Compute average log scale — red herring variable
avg_log_scale = sum(log_scaled) / len(log_scaled) if log_scaled else 0

# Now compute moving average of original valid temps (relevant path)
moving_avg = [
    sum(valid_temps[i:i+3]) / 3 for i in range(len(valid_temps) - 2)
]

# Weighted combination: emphasize stability (minimize variance)
variance_proxy = (
    sum((x - sum(valid_temps)/len(valid_temps))**2 for x in valid_temps) / len(valid_temps)
)

stability_bonus = 10.0 / (1 + variance_proxy) if variance_proxy > 0 else 10.0

# Core processing function
def calculate_final_score(data):
    base_mean = sum(data) / len(data)
    peak_factor = max(data) / base_mean
    consistency_weight = len(moving_avg)  # depends on length of moving avg
    raw_score = base_mean * peak_factor * consistency_weight
    return raw_score + stability_bonus  # final formula

# Misleading side calculation — appears significant but unused
phantom_score = 0
for i, temp in enumerate(valid_temps):
    phantom_score += temp * (i + 1) ** 0.5
phantom_score = round(phantom_score, 2)

# Critical execution point
processed_data = valid_temps
final_score = calculate_final_score(processed_data)

# Output target result
print(f"Result: {final_score}")