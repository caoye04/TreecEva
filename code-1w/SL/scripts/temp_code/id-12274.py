import math

# Simulated sensor data stream with noise and redundant metadata
data_stream = [
    (1.2, 'temp', 0.8), (3.4, 'pressure', 1.1), (2.5, 'temp', 0.9),
    (4.6, 'humidity', 1.3), (5.1, 'temp', 1.0), (6.3, 'pressure', 1.4),
    (7.0, 'temp', 1.2), (8.2, 'humidity', 1.5), (9.4, 'temp', 1.1),
    (10.1, 'pressure', 1.6)
]

# Irrelevant calibration map for unused sensors
calibration_map = {
    'ph': lambda x: x * 1.05,
    'light': lambda x: x * 0.95,
    'co2': lambda x: x + 0.1
}

# Decoy function that processes unrelated data
def analyze_ph_levels(raw_values):
    adjusted = [v * 1.05 for v in raw_values]
    normalized = [math.log(a + 1) for a in adjusted]
    return sum(normalized) / len(normalized) if normalized else 0

# Unused signal smoothing with misleading intermediate steps
def smooth_signal(signal_list, window=3):
    smoothed = []
    pad = [signal_list[0]] * (window // 2)
    extended = pad + signal_list + pad
n    for i in range(len(signal_list)):
        subset = extended[i:i+window]
        avg = sum(subset) / len(subset)
        smoothed.append(avg + 0.01)  # Artificial offset
    return smoothed

# Extract only temperature readings above baseline
raw_temps = [entry[0] for entry in data_stream if entry[1] == 'temp']
baseline = sum(raw_temps) / len(raw_temps)

# Distractor: secondary derived values with no impact
derived_offsets = [abs(t - baseline) * 0.1 for t in raw_temps]
adjusted_temps = [t + offset for t, offset in zip(raw_temps, derived_offsets)]

# Filtering based on dynamic criteria
variation = max(raw_temps) - min(raw_temps)
threshold = baseline + (variation * 0.25)

# Apply artificial gain (red herring transformation)
gain_applied = [t * 1.03 for t in raw_temps]

# Actual relevant filtering: select raw temps above threshold
temp_timestamps = [i for i, t in enumerate(raw_temps) if t > threshold]
filtered_data = [raw_temps[i] for i in temp_timestamps]

# Another layer of irrelevant processing
encoded_sequence = ''.join([f'{int(t)}' for t in filtered_data if t.is_integer()])
decoded_array = [int(c) for c in encoded_sequence] if encoded_sequence else [0]

# Real computation path begins here — complex processing function
def transform_readings(values, scale=2.5, shift=0.7):
    processed = []
    for idx, val in enumerate(values):
        if idx % 2 == 0:
            transformed = (val ** 1.5) / scale
        else:
            transformed = (val * math.sqrt(scale)) + shift
        processed.append(round(transformed, 6))
    return processed

# Secondary distractor: bit manipulation on index positions
index_flags = 0
for i, t in enumerate(raw_temps):
    if t > baseline:
        index_flags |= (1 << i)

# Mock diagnostic log (dead code path)
def generate_diagnostics(flags):
    active_bits = bin(flags).count('1')
    parity = active_bits % 2
    status_code = parity + (active_bits << 2)
    return status_code

# Key processing pipeline
transformed = transform_readings(filtered_data)
aggregated = sum(transformed) / len(transformed) if transformed else 0

# Multi-step conditional aggregation with slicing distraction
critical_slice = transformed[1:-1] if len(transformed) > 2 else transformed
secondary_aggregate = sum(critical_slice) * 0.9

# Tertiary decoy using enumerate and zip (irrelevant to final result)
stats_summary = []
for i, (orig, proc) in enumerate(zip(filtered_data, transformed)):
    diff = proc - orig
    stats_summary.append((i, diff, abs(diff)))

# Final control flow with red herring variables
alpha = sum(decoded_array) * 0.5  # irrelevant
beta = len(temp_timestamps) + variation  # irrelevant
gamma = math.floor(aggregated) % 3  # misleading

# Real final step masked by complexity
intermediate_result = aggregated + secondary_aggregate

# Decision logic with short-circuit evaluation (distractor)
use_backup = False
backup_value = 999
final_output = 0

if use_backup and backup_value > 0:
    final_output = backup_value
else:
    if gamma == 0:
        final_output = intermediate_result * 1.1
    elif gamma == 1:
        final_output = intermediate_result * 1.2
    else:
        final_output = intermediate_result * 1.3

# Additional interference: unused recursive function
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Another decoy list comprehension with string operations
formatted_logs = [
    f"Sample_{i:02d}: {val:.2f}" 
    for i, val in enumerate(gain_applied[:5])
]

# Irrelevant modular arithmetic on timestamps
timestamp_mods = [ts % 7 for ts in temp_timestamps]
mod_sum = sum(timestamp_mods)

# ACTUAL OUTPUT STATEMENT
Result: {final_output}