from itertools import groupby, cycle
import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    raw_signals = [math.sin(i * 0.1) + 0.5 * math.cos(i * 0.3) for i in range(100)]
    timestamps = list(range(100))
    statuses = ['OK', 'WARN', 'ERROR']
    return [{'time': t, 'value': round(v, 4), 'status': statuses[i % 3]} 
            for i, (t, v) in enumerate(zip(timestamps, raw_signals))]

# Irrelevant auxiliary function – dead code path (red herring)
def analyze_frequency(signal_list):
    fft_magnitude = []
    for i in range(len(signal_list)):
        component = 0
        for j in range(len(signal_list)):
            angle = 2 * math.pi * i * j / len(signal_list)
            component += signal_list[j] * (math.cos(angle) - math.sin(angle))
        fft_magnitude.append(abs(component))
    return fft_magnitude[:10]

# Decoy transformation – never used but looks important
temporal_weights = [round(math.exp(-i * 0.05), 3) for i in range(100)]
weighted_values = [0] * 100
for idx in range(100):
    weighted_values[idx] = idx * temporal_weights[idx]

# Real processing chain begins here
log_entries = generate_telemetry()
system_threshold = 0.75

# Extract magnitude peaks above noise floor (real logic step 1)
filtered_peaks = [entry['value'] for entry in log_entries if abs(entry['value']) > 0.65]

# Compute rolling window energy (real logic step 2)
window_size = 4
energy_levels = []
for i in range(len(filtered_peaks) - window_size + 1):
    window = filtered_peaks[i:i+window_size]
    energy = sum(x**2 for x in window)
    energy_levels.append(round(energy, 4))

# Apply adaptive threshold filtering (real logic step 3)
adaptive_mask = [e for e in energy_levels if e > system_threshold * 1.2]

# Count transitions in original log (distractor computation)
transition_count = 0
prev_status = log_entries[0]['status']
for entry in log_entries[1:]:
    if entry['status'] != prev_status:
        transition_count += 1
    prev_status = entry['status']

# Fake diagnostic from decoy function (misleading intermediate)
fake_spectrum = [round(1.0 / (1 + i), 3) for i in range(1, 11)]
decoy_metric = sum(fake_spectrum) * 0.23

# Real signal: compute entropy of peak distribution (real logic step 4)
if adaptive_mask:
    mean_energy = sum(adaptive_mask) / len(adaptive_mask)
    variance = sum((x - mean_energy)**2 for x in adaptive_mask) / len(adaptive_mask)
    if variance > 0:
        entropy = round(math.log(variance * 2 * math.pi * math.e) / 2, 4)
    else:
        entropy = 0.0
else:
    entropy = 0.0

# Secondary validation via bit analysis of timestamps (real logic step 5)
timestamp_bits = ''.join([bin(e['time'])[-2:] for e in log_entries[::10]])
binary_pattern_score = timestamp_bits.count('1') * 0.17

# Conditional expression combining real and fake signals (logic step 6)
preliminary_flag = 'CRITICAL' if len(filtered_peaks) > 30 and entropy > 0.8 else 'NORMAL'

# Dictionary-based state mapping with unused entries (distractors)
state_weights = {
    'CRITICAL': 3.0,
    'ELEVATED': 1.8,
    'NORMAL': 0.5,
    'STANDBY': 0.1,  # unused
    'MAINTENANCE': 0.05  # unused
}

# Real weighting application (logic step 7)
basic_weight = state_weights[preliminary_flag]

# Accumulation through cyclic modulation (logic step 8)
cycle_phases = cycle([0.5, 0.7, 1.0, 0.8])
modulated_sum = 0.0
for i, e in enumerate(adaptive_mask):
    phase = next(cycle_phases)
    modulated_sum += e * phase * basic_weight

# Final adjustment using character count from status logs (logic step 9)
status_string = ''.join([e['status'][0] for e in log_entries])
char_count_bonus = status_string.count('W') * 0.25 + status_string.count('E') * 0.45

# Key statement: final diagnostic score computation (logic step 10)
final_diagnostic = round(modulated_sum + char_count_bonus - decoy_metric, 4)

# Output result as required
print(f"Result: {final_diagnostic}")