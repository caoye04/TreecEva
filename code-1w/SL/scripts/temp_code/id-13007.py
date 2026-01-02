def analyze_phase_transitions(state_log):
    phase_changes = 0
    temp_history = []
    for entry in state_log:
        if entry['temp'] > 75 and entry['state'] == 'liquid':
            phase_changes += 1
        temp_history.append(entry['temp'])
    avg_temp = sum(temp_history) / len(temp_history) if temp_history else 0
    return phase_changes, avg_temp

process_sequence = [
    {'temp': 68, 'state': 'solid', 'timestamp': '00:00'},
    {'temp': 72, 'state': 'semi-solid', 'timestamp': '00:05'},
    {'temp': 80, 'state': 'liquid', 'timestamp': '00:10'},
    {'temp': 95, 'state': 'liquid', 'timestamp': '00:15'},
    {'temp': 102, 'state': 'gas', 'timestamp': '00:20'}
]

status_flags = {k: False for k in ['overheat', 'delay', 'calibration']}
baseline_threshold = 77.5

# Misleading intermediate calculation with string processing
log_strings = [f"{e['timestamp']}:{e['state'].upper()}" for e in process_sequence]
distinct_states = len(set([e['state'] for e in process_sequence]))

flagged_entries = []
for s in log_strings:
    if 'GAS' in s:
        flagged_entries.append(s)

# Distractor set operation
active_segments = set()
for i in range(len(process_sequence)):
    if process_sequence[i]['temp'] > baseline_threshold:
        active_segments.add(i)

# Auxiliary function that appears relevant but isn't directly used
def estimate_energy_usage(entries):
    total = 0
    for e in entries:
        if isinstance(e, dict) and 'temp' in e:
            total += e['temp'] * 0.37
    return round(total, 2)

energy_estimate = estimate_energy_usage(process_sequence)  # Dead-end variable

# Core logic hidden among distractions
phase_count, mean_temp = analyze_phase_transitions(process_sequence)

reference_points = [70, 85, 90]
convergence_score = 0
for p in reference_points:
    convergence_score += abs(mean_temp - p)

# Conditional mutation based on multiple factors
if phase_count >= 1 and mean_temp > 75:
    adjustment_factor = 1.25
else:
    adjustment_factor = 0.85

theoretical_yield = (mean_temp * phase_count) + 5.5

# Main assignment with dictionary-based refinement
refinement_map = {1: 0.9, 2: 1.1, 3: 1.3}
refinement_key = min(phase_count, 3)

raw_output = theoretical_yield * adjustment_factor

# Final computation buried in noise
buffer_zone = ''.join([s.split(':')[1][0] for s in log_strings if ':' in s])
checksum_value = sum(ord(c) for c in buffer_zone) % 11

final_multiplier = refinement_map.get(refinement_key, 1.0) + (checksum_value * 0.01)

thermal_capacity = 0  # Initialization

def calculate_thermal_output(seq):
    changes, avg = analyze_phase_transitions(seq)
    base = avg * changes
    if changes > 0:
        base += 12.5
    return int(base * 1.8)  # Deterministic integer result

thermal_capacity = calculate_thermal_output(process_sequence)

# Output required format
print(f"Target result: {thermal_capacity}")