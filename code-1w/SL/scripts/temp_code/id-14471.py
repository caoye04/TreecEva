from collections import defaultdict
from itertools import combinations

# Simulated system telemetry data with noise
raw_signals = [1.2, 0.8, 3.1, 2.9, 0.5, 4.0, 3.8, 2.2, 1.9, 0.7]
noise_floor = 0.3
system_threshold = 2.5
diagnostic_history = []

# Irrelevant auxiliary function (decoy)
def analyze_bandwidth(signal_list):
    total = 0
    for x in signal_list:
        if x > 1.5:
            total += x * 0.7
    return total // 2  # Misleading truncation

# Unused but plausible helper
unused_checksum = lambda seq: sum(x ** 2 for x in seq if x < 3.0)

# Distractor: fake aggregation path
shadow_buffer = defaultdict(int)
for i, val in enumerate(raw_signals):
    shadow_buffer[f'entry_{i % 4}'] += val * 0.1

# Real processing begins here — heavily masked by noise
filtered_readings = [x for x in raw_signals if x > noise_floor]

# Simulate corrupted packet detection (irrelevant to final result)
corruption_flags = []
for x in filtered_readings:
    if abs(x - round(x)) < 0.15:
        corruption_flags.append(True)
    else:
        corruption_flags.append(False)

# Another red herring: complex but unused transformation
temp_profile = list(combinations([int(x) for x in filtered_readings if x > 1.0], 2))
weight_matrix = [[a + b for a in range(3)] for b in range(3)]

def integrate_stability_index(data, base):
    accumulator = 0.0
    decay = 1.0
    for val in data:
        if val > base:
            accumulator += val * decay
            decay *= 0.9  # Exponential fade
    return accumulator  # Never actually used below

# Actual critical data preparation
log_data = {
    'entries': [],
    'meta': {'version': '3.1', 'mode': 'diagnostic'}
}
for idx, val in enumerate(filtered_readings):
    log_data['entries'].append({
        'id': f'data_{idx}',
        'value': val,
        'flagged': corruption_flags[idx] if idx < len(corruption_flags) else False,
        'derived': int(val * 10) % 4 == 0
    })

# Fake recursive trap (never invoked in execution path)
def recursive_summer(arr, limit):
    if limit <= 0 or not arr:
        return 0
    return arr[0] + recursive_summer(arr[1:], limit - 1)

# Core logic disguised among distractions
def evaluate_integrity(entry_list):
    count_valid = 0
    temp_sum = 0.0
    for entry in entry_list:
        # Only entries with derived property contribute
        if entry['derived'] and not entry['flagged']:
            temp_sum += entry['value']
            count_valid += 1
    return temp_sum / count_valid if count_valid > 0 else 0.0

# Secondary metric (looks important but unused)
def compute_density_score(entries):
    ids = [e['id'] for e in entries]
    return len([i for i in ids if '3' in i]) * 1.5

# Main processing function — only one that matters
def process_metrics(log, threshold):
    entries = log['entries']
    high_priority = [e for e in entries if e['value'] > threshold]
    
    # Distraction: irrelevant accumulation
    phantom_total = 0
    for hp in high_priority:
        phantom_total += len(hp['id'])
    
    # Real computation buried here
    raw_values = [e['value'] for e in entries]
    above_threshold_count = sum(1 for v in raw_values if v > threshold)
    total_energy = sum(v ** 2 for v in raw_values)  # Emphasis on magnitude
    
    # Final diagnostic is ratio of energy to count (only if count > 0)
    if above_threshold_count > 0:
        result = total_energy / above_threshold_count
    else:
        result = 0.0
    
    return result

# Dead code path — looks like state update
if __name__ == "__main__":
    diagnostic_history.append("INIT")
    current_mode = "ACTIVE"
    final_diagnostic = 0
    
    # This assignment is the key statement
    final_diagnostic = process_metrics(log_data, system_threshold)
    
    # Noise: additional meaningless print
    debug_snapshot = {"size": len(shadow_buffer), "status": "nominal"}
    
    # Output required for evaluation
    print(f"Result: {final_diagnostic}")