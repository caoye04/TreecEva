import itertools

def analyze_temperatures(temp_readings):
    # Irrelevant helper function – never called
    moving_averages = []
    for i in range(len(temp_readings) - 2):
        avg = sum(temp_readings[i:i+3]) / 3
        moving_averages.append(round(avg, 2))
    return moving_averages

def filter_outliers(data, threshold=50):
    # This function is used but contains red herrings
    filtered = []
    high_count = 0
    temp_warning_log = []
    for val in data:
        if val > threshold:
            high_count += 1
            temp_warning_log.append(f'High reading: {val}')
        else:
            filtered.append(val)
    # Distraction: unused computation
    adjustment_factor = high_count * 0.5 if high_count > 0 else 1.0
    scaling_matrix = [[adjustment_factor * i for i in range(3)] for _ in range(3)]
    return filtered

def transform_sequence(seq):
    # Applies bit manipulation and filtering – some steps are relevant, others not
    processed = []
    bit_flags = []
    total_shifts = 0
    for index, num in enumerate(seq):
        shifted = num << 1
        total_shifts += shifted
        xor_mask = (index ^ 7) & 15
        masked = shifted ^ xor_mask
        if masked % 3 == 0:
            processed.append(masked)
        bit_flags.append(bin(masked))  # Collected but unused
    # Dead code path – misleading structure
    if len(processed) > 100:
        backup = [p >> 2 for p in processed]
        return backup
    return processed

def calculate_entropy(values):
    # Unused complex function – distractor
    from math import log
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        prob = count / total
        entropy -= prob * log(prob, 2)
    return round(entropy, 4)

def calculate_final_score(data_chunk):
    # Core logic hidden among distractions
    base_sum = sum(data_chunk)
    count_above_20 = len([x for x in data_chunk if x > 20])
    multiplier = count_above_20 if count_above_20 > 0 else 1
    
    # Real transformation: apply XOR fold
    folded_value = 0
    for i, x in enumerate(data_chunk):
        folded_value ^= (x + i)  # Key operation
    
    # Decoy aggregation
    decoy_stats = {
        'max': max(data_chunk),
        'min': min(data_chunk),
        'range': max(data_chunk) - min(data_chunk),
        'median_guess': sorted(data_chunk)[len(data_chunk)//2]
    }
    perturbation = 0
    for k, v in decoy_stats.items():
        perturbation += hash(k + str(v)) % 10  # Meaningless accumulation
    
    # Actual score formula (non-obvious)
    raw_score = base_sum * multiplier
    final_score = (raw_score >> 2) ^ folded_value  # Critical step
    return final_score

# Main execution block
if __name__ == '__main__':
    # Simulated sensor data – realistic context
    raw_sensor_data = [23, 15, 42, 8, 37, 29, 11, 55, 4, 19, 33, 26]
    
    # Irrelevant pre-processing step (only partially used)
    status_flags = [1 if x > 25 else 0 for x in raw_sensor_data]
    indexed_pairs = list(enumerate(raw_sensor_data))
    paired_with_flag = list(zip(raw_sensor_data, status_flags))
    
    # Apply real filtering (uses one irrelevant function with side paths)
    cleaned_data = filter_outliers(raw_sensor_data, threshold=60)
    
    # Transform using bit logic – relevant
    processed_data = transform_sequence(cleaned_data)
    
    # Introduce red herring: dummy grouping
    grouped_by_parity = {k: list(g) for k, g in itertools.groupby(sorted(processed_data), key=lambda x: x % 2)}
    even_group_size = len(grouped_by_parity.get(0, []))
    odd_group_size = len(grouped_by_parity.get(1, []))
    balance_score = abs(even_group_size - odd_group_size) * 100  # Computed but unused
    
    # Core calculation – answer derived here
    final_score = calculate_final_score(processed_data)
    
    # Output required result
    print(f"Result: {final_score}")