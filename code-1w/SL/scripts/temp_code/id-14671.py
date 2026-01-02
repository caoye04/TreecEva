def analyze_component(x, threshold=5.0):
    if x < threshold:
        return x * 1.2
    else:
        return (x + 3) * 0.8

# Simulate sensor readings with noise and calibration
data_stream = [3.4, 6.1, 2.8, 7.5, 4.9, 8.2]
calibrated = []
noise_offset = 0.3

for val in data_stream:
    adjusted = val + noise_offset
    calibrated.append(adjusted)

# Apply component analysis with filtering
processed = []
for c in calibrated:
    result = analyze_component(c)
    processed.append(round(result, 2))

# Initialize tracking variables (some are distractions)
temp_accum = 0
state_log = {}
valid_entries = 0
checksum = 0

benchmark_data = []
for i, (raw, proc) in enumerate(zip(data_stream, processed)):
    temp_accum += raw
    checksum ^= i  # Red herring: not used in final score
    entry = {
        'index': i,
        'raw_input': raw,
        'processed_output': proc,
        'status': 'valid' if proc > 4.0 else 'low'
    }
    state_log[i] = 'checked'
    benchmark_data.append(entry)
    if proc > 4.0:
        valid_entries += 1

# Secondary validation pass (partially redundant)
redundant_sum = sum([e['raw_input'] for e in benchmark_data if e['status'] == 'valid'])
filter_ratio = valid_entries / len(benchmark_data) if benchmark_data else 0

# Core performance calculation function
def calculate_performance(logs):
    base = 0
    penalty = 0
    bonus = 0
    stage_intermediate = []

    for idx, record in enumerate(logs):
        out_val = record['processed_output']
        base += out_val

        # Bonus logic
        if record['status'] == 'valid' and idx % 2 == 0:
            bonus += 1.5

        # Penalty for high raw inputs
        if record['raw_input'] > 7.0:
            penalty += 0.8

        # Intermediate tracking (distraction)
        stage_intermediate.append(out_val * 0.1)

    aggregate = base + bonus - penalty

    # Normalize by number of entries (only if non-empty)
    if logs:
        aggregate /= len(logs)
    
    # Additional smoothing step (semi-relevant but minor)
    smoothed = aggregate * 0.95 + 2.1
    
    return round(smoothed, 4)

# Final computation
current_mode = 'performance'
activation_key = None
final_score = calculate_performance(benchmark_data)

print(f"Result: {final_score}")