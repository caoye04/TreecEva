def analyze_distribution(data, limit):
    count = 0
    frequency = {}
    for item in data:
        if item < limit:
            count += item * 2
            frequency[item] = frequency.get(item, 0) + 1
        else:
            temp_offset = item // 4
            count -= temp_offset
    return count


def validate_sequence(seq):
    reversed_seq = seq[::-1]
    midpoint = len(seq) // 2
    left_half = seq[:midpoint]
    right_half = reversed_seq[:midpoint]
    match_count = 0
    for i in range(midpoint):
        if left_half[i] == right_half[i]:
            match_count += 1
    return match_count > 0


def optimize_resources(mapping, cutoff):
    total_load = 0
    surplus = []
    deficit = 0
    
    # Real computation path
    keys = list(mapping.keys())
    sorted_keys = sorted(keys)
    
    for k in sorted_keys:
        value = mapping[k]
        if k.startswith('res'):
            if value > cutoff:
                total_load += value * 0.8
                surplus.append(value - cutoff)
            else:
                adjustment = (cutoff - value) * 0.1
                deficit += adjustment
                total_load -= adjustment
    
    # Irrelevant tracking variables (distractors)
    avg_surplus = sum(surplus) / len(surplus) if surplus else 0
    peak_surplus = max(surplus) if surplus else 0
    
    # Secondary logic that influences final result
    stability_factor = 1.0
    if deficit > 50:
        stability_factor = 0.9
    elif deficit < 20:
        stability_factor = 1.05
    
    final_calc = total_load * stability_factor
    
    # Dead code path (misleading)
    if False:
        fallback = 0
        for v in mapping.values():
            fallback += v % 7
        final_calc = max(final_calc, fallback)
    
    return int(final_calc)

# Main execution
workload_data = [3, 7, 2, 8, 5, 9, 1]
limit_val = 6
analyzed_score = analyze_distribution(workload_data, limit_val)

sequence_check = [4, 2, 7, 2, 4]
valid_pattern = validate_sequence(sequence_check)

allocation_map = {
    'resA': 120,
    'resB': 85,
    'aux_mem': 200,  # irrelevant key
    'resC': 95,
    'temp_buf': 40,  # irrelevant key
    'resD': 60
}

cutoff_threshold = 90
final_capacity = 0

if valid_pattern:
    final_capacity = optimize_resources(allocation_map, cutoff_threshold)
else:
    final_capacity = analyzed_score * 10

print(f"Result: {final_capacity}")