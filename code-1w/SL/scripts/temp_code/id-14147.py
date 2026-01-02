import itertools

# Simulated sensor data with noise and redundant readings
def generate_sensor_data():
    base_signal = [i * 0.5 + (i % 7) for i in range(20)]
    noise_floor = [(i ** 2) % 5 for i in range(20)]
    corrupted_mask = [1 if (i + 3) % 6 == 0 else 0 for i in range(20)]  # Unused red herring
    return [base_signal[i] + noise_floor[i] for i in range(20)]

# Irrelevant auxiliary function – decoy for signal smoothing
def smooth_signal(signal):
    smoothed = []
    for i in range(len(signal)):
        neighbors = []
        for j in [-2, -1, 0, 1, 2]:
            idx = max(0, min(len(signal) - 1, i + j))
            neighbors.append(signal[idx])
        smoothed.append(sum(neighbors) / len(neighbors))
    return smoothed  # Never actually used

# Core processing with multiple concepts
noise_threshold = 3.5
dynamic_weights = {i: (i % 4) * 0.25 for i in range(10)}  # Unused dictionary red herring

config = {
    'active': True,
    'mode': 'process',
    'version': '2.1a'
}

# Data transformation pipeline
def filter_and_transform(data):
    filtered = []
    temp_log = []  # Distractor list
    cumulative_shift = 0

    for i, val in enumerate(data):
        if val < noise_threshold:  # Real filtering condition
            adjusted = val * (1 + (i % 3) * 0.1)
            filtered.append(round(adjusted, 3))
        else:
            shifted = val - (i % 4)  # Partially relevant
            temp_log.append(shifted)  # Logged but unused later

    # Real logic hidden among distractions
    if len(filtered) > 5:
        sliced_part = filtered[2:8:2]  # Slicing: elements at indices 2,4,6
        sum_slice = sum(sliced_part)
        
        # Bit manipulation red herring
        magic_flag = 0b1010
        trigger_mask = 0b1100
        if magic_flag & trigger_mask:
            sum_slice += 0.5  # Misleading adjustment

        # Actual critical transformation
        exponent_offset = len(filtered) % 4
        final_sum = sum_slice * (2 ** exponent_offset)

        # Use of itertools: grouping by value range
        grouped = {k: len(list(g)) for k, g in itertools.groupby(
            sorted(filtered), key=lambda x: int(x))}
        
        # This count influences result but indirectly
        count_distribution = sum(1 for v in grouped.values() if v >= 2)

        # Final computation chain
        intermediate = final_sum + count_distribution * 1.5
        return round(intermediate, 6)
    
    return 0.0

# Another decoy function dealing with irrelevant state tracking
def track_processing_states(data):
    states = {}
    for idx, x in enumerate(data):
        key = f"state_{idx % 5}"
        if key not in states:
            states[key] = []
        states[key].append(x * (idx % 3))
    return states  # Unused return

# Main orchestrator
def process_sequence(raw):
    # Apply real transformation
    result = filter_and_transform(raw)
    
    # Dead code path: early exit never taken
    if not config['active']:
        return -999.0
        
    # Multiple assignments – some irrelevant
    temp_a, temp_b, temp_c = result, result * 0.9, result * 1.1
    backup_check = temp_b + temp_c
    
    # Key operation
    final_output = int(temp_a) if temp_a > 20 else int(temp_a + 4)  # Final integer conversion
    
    # Unused tuple unpacking distraction
    metadata_tags = ['src_A', 'mode_X', 'v2']
    src_label, _, version_tag = metadata_tags
    
    # Decoy conditional that looks important
    if version_tag == 'v2' and backup_check > 100:
        final_output -= 1  # Not triggered

    return final_output

# Execution flow
if __name__ == '__main__':
    data = generate_sensor_data()
    # Redundant call to decoy function
    _ = track_processing_states(data)
    # Smoothed version computed but ignored
    _ = smooth_signal(data)
    
    final_output = process_sequence(data)
    print(f"Target result: {final_output}")