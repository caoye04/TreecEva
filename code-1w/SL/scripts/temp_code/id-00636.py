import math

# Simulated sensor data processing with diagnostic analysis
raw_samples = [0.8, 1.2, -0.5, 3.1, 2.7, -1.3, 0.9, 1.1]
decoy_counter = 0
baseline_shift = 0.35
temp_buffer = []
scaling_factor = 1.7
irrelevant_sum = 0

# Irrelevant statistical placeholder (dead computation)
for x in raw_samples:
    if x > 1.0:
        irrelevant_sum += math.log(x) * 2.1

# Primary signal preprocessing chain
filtered_data = []
for val in raw_samples:
    adjusted = abs(val - baseline_shift) * scaling_factor
    if adjusted > 1.5:
        filtered_data.append(adjusted)

# Decoy transformation (unused path)
decoy_transform = []
for i in range(len(filtered_data)):
    phase = (i + 1) * math.pi / 4
    decoy_transform.append(filtered_data[i] * math.sin(phase))
    if decoy_transform[-1] < 0:
        decoy_counter += 1

# Real processing: frequency binning and energy calculation
energy_levels = set()
cumulative_energy = 0.0
bin_mapping = {0: [], 1: [], 2: [], 3: []}

for idx, sample in enumerate(filtered_data):
    freq_bin = int((sample * 1.3) % 4)
    dampened_sample = sample * (0.8 ** idx)
    cumulative_energy += dampened_sample
    energy_levels.add(round(dampened_sample, 3))
    bin_mapping[freq_bin].append(dampened_sample)

    # Early termination red herring (never triggered due to data)
    if len(energy_levels) > 100:
        break

# String-based status encoding (uses string method)
status_flags = ['norm', 'alert', 'caution']
encoded_status = ''.join([flag[1:].upper() for flag in status_flags])
status_checksum = sum(ord(c) for c in encoded_status) / len(encoded_status)

# Secondary transformation of data
transformed_magnitudes = []
for e in energy_levels:
    transformed_magnitudes.append(e ** 1.5)

# Tertiary aggregation with conditional logic
aggregated_score = 0
for mag in transformed_magnitudes:
    if mag > 2.0:
        aggregated_score += mag * 0.7
    elif mag > 1.0:
        aggregated_score += mag * 0.4
    else:
        aggregated_score += mag * 0.2

processed_data = {
    'total_energy': cumulative_energy,
    'score': aggregated_score,
    'bins': bin_mapping,
    'count': len(energy_levels)
}

# Misleading auxiliary function (looks important but unused)
def compute_resonance(seq):
    return sum(s * (i+1) for i, s in enumerate(seq)) % 7

# Core analysis function with key logic
def analyze_signal(data):
    base = data['total_energy']
    adjustment = 0

    # Complex conditional adjustment
    if data['score'] > 5.0:
        adjustment += 1.2
    if data['count'] in {3, 4, 5}:
        adjustment *= 1.8
    else:
        adjustment += 0.3

    # Bit manipulation red herring
    binary_hint = len(data['bins'][0]) << 2 | len(data['bins'][1])
    decoy_value = (binary_hint ^ 5) & 10

    # Final computation using only total_energy and count
    result = base * (data['count'] + adjustment)

    # String-based override check (distractor - condition never met)
    trigger_code = 'ALERT_OVERRIDE'
    if 'Z' in trigger_code.lower().replace('a', '').replace('e', ''):
        result = -999.0

    return result

# Execute critical statement
final_diagnostic = analyze_signal(processed_data)
print(f"Target result: {final_diagnostic}")