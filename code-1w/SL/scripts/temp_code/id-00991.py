import math

# Irrelevant helper function (dead code path)
def unused_diagnostic_check(x):
    return sum(i * 2 for i in x if i % 3 == 0)

# Misleading transformation chain
def transform_readings(readings):
    temp_a = [x + 10 for x in readings]
    temp_b = [x * 0.95 for x in temp_a]
    temp_c = [math.log(x) if x > 0 else 0 for x in temp_b]  # Distractor: not used later
    return [x for x in temp_a if x > 50]

# Decoy accumulator with red herring logic
def accumulate_metrics(values):
    total = 0
    bonus = 0
    for v in values:
        if v > 75:
            total += v * 0.1
            bonus += 5  # Unused bonus
        elif v < 60:
            total -= 2
    return int(total)  # Not actually used in final result

# Core evaluation logic hidden among distractions
def evaluate_performance(dataset):
    filtered = [x for x in dataset if 40 <= x <= 100]
    
    # Real computation begins here
    adjusted = list(map(lambda x: x * 1.1 if x < 70 else x * 0.9, filtered))
    
    # Bit manipulation decoy (irrelevant but looks important)
    bit_mask = 0b110101
    masked_values = [v ^ bit_mask & 0b111 for v in adjusted]  # Useless transformation
    
    # Actual signal extraction via set operations
    base_set = set(range(65, 85))
    reading_set = set([int(x) for x in adjusted])
    overlap = base_set & reading_set  # Meaningful intersection
    enhancement_factor = len(overlap) * 0.5
    
    # Secondary validation using min/max
    peak = max(adjusted)
    floor = min(adjusted)
    spread_bonus = (peak - floor) / 10 if (peak - floor) > 20 else 0
    
    # Accumulation through filtering and summation
    valid_points = [v for v in adjusted if v > 60]
    base_score = sum(valid_points) / len(valid_points) if valid_points else 0
    
    # Final composition
    raw_final = base_score + enhancement_factor + spread_bonus
    
    # Rounding to obscure traceability
    return round(raw_final * 1.07, 2)

# Extraneous global variables (distractors)
baseline_threshold = 65
normalization_shift = 0.98
diagnostic_trace = {'status': 'active', 'level': 7}

# Simulated input data - looks like sensor readings
raw_data_stream = [58, 72, 61, 45, 83, 77, 69, 55, 91, 66, 74, 52, 88]

# Apply transformations in a way that obscures relevance
temp_results = []
for item in raw_data_stream:
    if item >= 50:
        temp_results.append(item + 3)

# Main processing pipeline
processed_diagnostics = transform_readings(raw_data_stream)
cached_metrics = accumulate_metrics(processed_diagnostics)  # Call with no effect

data_set = [x - 2 for x in raw_data_stream]  # Final input preparation

# Key execution point
final_score = evaluate_performance(data_set)

print(f"Result: {final_score}")