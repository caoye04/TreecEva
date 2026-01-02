def analyze_metrics(data_points):
    total = 0
    weight = 1.5
    temp_offset = 0.8
    for val in data_points:
        if val > 5:
            total += val * weight
        else:
            total -= temp_offset
    return int(total)

base_score = 42
offset_tracker = [0, 0, 0]

for i in range(3):
    offset_tracker[i] = base_score % (i + 2)

# Simulate historical corrections (irrelevant to final result)
historical_flags = {1: 'A', 2: 'B', 3: 'C'}
flag_state = set(historical_flags.values())
discard_buffer = sum([v ** 0.5 for v in range(1, 5)])  # Dead computation

feedback_map = {
    'readings': [6, 7, 4, 9],
    'weights': [1.2, 1.8],
    'threshold': 5,
    'extra_data': [0, 0, 0, 0, 0]  # Unused field
}

# Auxiliary function with partial relevance
def filter_critical(entries):
    return [e for e in entries if e >= 6]

# Secondary processing with slicing distraction
temp_sequence = feedback_map['readings'][1:3]
summed_slice = sum(temp_sequence)

scaling_factor = 1.0
if len(temp_sequence) == 2:
    scaling_factor = 1.1

adjusted_base = base_score * scaling_factor

# Core logic embedded within noise
def aggregate_performance(feedback, score):
    readings = feedback['readings']
    threshold = feedback['threshold']
    
    # Real contribution
    filtered = filter_critical(readings)
    bonus = 0
    for item in filtered:
        if item % 2 == 0:
            bonus += 2
        else:
            bonus += 1
    
    # Irrelevant dictionary manipulations
    shadow_copy = dict(feedback)
    shadow_copy['temp'] = 'intermediate'
    del shadow_copy['extra_data']
    
    # Bitwise red herring
    magic_key = 13
    decoy_value = magic_key ^ 7 & 3  # Computation not used later
    
    # Actual score update
    performance_sum = analyze_metrics(readings)
    final_component = performance_sum // 10
    
    return score + final_component + bonus

# Key execution point
final_score = aggregate_performance(feedback_map, base_score)
print(f"Result: {final_score}")