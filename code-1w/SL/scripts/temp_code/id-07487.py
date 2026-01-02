from collections import defaultdict, Counter
from itertools import zip_longest, cycle

# Simulated sensor data streams with noise and redundancy
def get_noisy_sensor_readings():
    raw = [12, 15, 12, 18, 14, 15, 12, 20, 13, 15]
    return [(i, val) for i, val in enumerate(raw)]

def process_diagnostics():
    # Irrelevant baseline computation (distractor)
    baseline_average = sum([x for x in range(1, 8)]) / 7
    
    # Real data ingestion
    indexed_readings = get_noisy_sensor_readings()
    
    # Misleading transformation: frequency map (partially irrelevant)
    freq_map = Counter(val for _, val in indexed_readings)
    
    # Decoy structure: unused signal buffer
    signal_buffer = defaultdict(list)
    for idx, val in indexed_readings:
        signal_buffer[val % 4].append(idx)
    
    # Red herring: simulate calibration offset (never used later)
    calibration_sequence = []
    for i, (index, reading) in enumerate(indexed_readings):
        if i % 3 == 0:
            calibration_sequence.append(reading * 0.95)
    smoothed_calibration = sum(calibration_sequence) / len(calibration_sequence) if calibration_sequence else 0
    
    # Core logic disguised among noise
    valid_readings = []
    for index, reading in indexed_readings:
        if reading > 13:
            valid_readings.append(reading)
        elif reading == 12:
            # Special case: 12 indicates stable state, count occurrences
            pass  # intention: just observe, don't include
    
    # Secondary filter based on position parity (important)
    filtered_by_index = [v for i, v in enumerate(valid_readings) if i % 2 == 0]
    
    # Tertiary manipulation: pairing with cyclic weights
    weights = cycle([0.8, 1.1])
    weighted_sum = 0.0
    for val, weight in zip_longest(filtered_by_index, weights, fillvalue=1.0):
        weighted_sum += val * weight
        if weighted_sum > 50:  # early break red herring
            break
    
    # Actual aggregation path
    aggregate_score = int(weighted_sum // 1)  # truncate to integer
    
    # Correction factor derived from mode analysis (critical)
    modes = [k for k, v in freq_map.items() if v == max(freq_map.values())]
    primary_mode = modes[0] if len(modes) > 0 else 0
    
    # Complex conditional correction (depends on multiple factors)
    size_factor = len(filtered_by_index)
    if primary_mode < 15 and size_factor >= 2:
        correction_factor = 7
    elif primary_mode >= 15 and size_factor == 1:
        correction_factor = -3
    else:
        correction_factor = 4
    
    # Dead code branch: never executed due to data
    temp_debug_log = []
    for _ in range(3):
        temp_debug_log.append('checkpoint')  # irrelevant
    
    # Key execution point
    final_diagnostic = aggregate_score + correction_factor
    
    # Unused advanced stat (distractor)
    pairwise_diffs = [abs(a - b) for a, b in zip(valid_readings, valid_readings[1:])]
    entropy_proxy = sum(d * d for d in pairwise_diffs) / len(pairwise_diffs) if pairwise_diffs else 0
    
    # Output the target result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute
def main():
    result = process_diagnostics()
    return result

main()