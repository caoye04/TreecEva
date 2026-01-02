def analyze_pattern(sequence, depth=0):
    if depth >= 3:
        return sum([x * (depth + 1) for x in sequence])

    transformed = [x ^ (depth * 2) for x in sequence]
    shifted = [(x << 1) & 255 for x in transformed]  # Bit manipulation red herring
    decoy_sum = sum(shifted) * depth  # Unused distraction

    return analyze_pattern(shifted[:len(sequence)//2 + 1], depth + 1)


# Irrelevant helper function (dead code path)
def validate_input_format(data_str):
    if not isinstance(data_str, str):
        return False
    valid_chars = set('0123456789ABCDEF')
    return all(c in valid_chars for c in data_str.upper())


# Unused data structure (distractor)
legacy_config = {
    'version': '2.1',
    'mode': 'DEPRECATED',
    'buffer_size': 1024,
    'timeout': None
}

# Real computation begins here
raw_metrics = [12, 8, 15, 3, 7, 9]
base_threshold = 6

# Distracting transformation chain
filtered_data = list(filter(lambda x: x > base_threshold - 2, raw_metrics))
indexed_pairs = list(enumerate(filtered_data))
processed_offsets = [i + val // 4 for i, val in indexed_pairs if val % 2 == 0]

# Fake correlation matrix (completely unused)
correlation_matrix = [[i * j for j in range(len(raw_metrics))] for i in range(len(raw_metrics))]
trace_sum = sum(correlation_matrix[i][i] for i in range(len(correlation_matrix)))  # Misleading calc

# Real but obscured logic
metric_data = []
for idx, val in enumerate(raw_metrics):
    adjustment = 0
    if val > base_threshold:
        adjustment += (val - base_threshold) ** 2
    else:
        adjustment -= (base_threshold - val) // 2
    
    # Additional irrelevant condition (never triggers due to data)
    if val == 42:
        adjustment = 0  # Dead branch
        
    metric_data.append(adjustment)

# Secondary distractor: string processing with no impact
status_log = "System metrics analyzed at T+00:05:12"
split_parts = status_log.split(' ')
date_flag = any(part.startswith('T+') for part in split_parts)

timestamp_value = 0
if date_flag:
    time_segment = [p for p in split_parts if 'T+' in p][0]
    timestamp_value = int(time_segment[2:].replace(':', '')) // 100  # Unused

# Core evaluation function
scaling_factor = len([x for x in metric_data if x > 0])
def evaluate_performance(data, threshold):
    total = sum(abs(x) for x in data)
    bonus = 0
    
    # Conditional expression red herring
    bonus += 10 if all(x < threshold * 2 for x in raw_metrics) else -5
    
    # Real bonus logic buried in noise
    if len(data) % 2 == 0 and scaling_factor >= 3:
        bonus += 15
    
    # Decoy bitwise operation
    masked_bonus = bonus & 0xFF  # Only relevant part is bonus itself
    
    return total + masked_bonus

# Key execution point
final_score = evaluate_performance(metric_data, base_threshold)

# Output requirement
print(f"Target result: {final_score}")