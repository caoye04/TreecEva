import itertools

def analyze_data_patterns(data_stream):
    # Distractor: Complex data processing that's mostly irrelevant
    temp_sum = sum(x * 2 for x in data_stream if x % 3 == 0)
    redundant_metric = temp_sum // len(data_stream) if data_stream else 0
    
    # More distractor calculations
    permutations_count = len(list(itertools.combinations(data_stream[:4], 2)))
    misleading_total = temp_sum + permutations_count * 10
    
    # Actual relevant path (well hidden)
    relevant_values = [x for x in data_stream if x > 15 and x < 45]
    if len(relevant_values) >= 2:
        sorted_relevant = sorted(relevant_values)
        # Key computation
        core_metric = (sorted_relevant[-1] - sorted_relevant[0]) * 3
        return core_metric
    return misleading_total  # Dead code path for this input

def calculate_scaling(offset_values):
    # More distractors
    avg_offset = sum(offset_values) / len(offset_values) if offset_values else 1
    normalized_range = max(offset_values) - min(offset_values) if len(offset_values) > 1 else 2
    
    # Irrelevant bitwise operations
    bit_mask = 0b10101010
    masked_result = int(avg_offset) & bit_mask
    
    # Actual scaling factor
    if len(offset_values) > 3:
        scaling = (offset_values[1] + offset_values[3]) // 2
        return scaling
    return normalized_range  # Another dead path

# Main execution with heavy interference
input_data = [25, 18, 42, 7, 33, 29, 56, 11]
offset_sequence = [8, 15, 22, 9, 14]

# Multiple irrelevant variables
preliminary_analysis = sum(x ** 2 for x in input_data[:3])
secondary_metric = preliminary_analysis % 17
misleading_buffer = [x + 5 for x in input_data if x < 20]

# Core computations (well hidden among distractors)
processed_data = analyze_data_patterns(input_data)
scaling_factor = calculate_scaling(offset_sequence)

# Final answer computation
final_composite = processed_data * scaling_factor

# Print irrelevant results first
print(f"Preliminary: {preliminary_analysis}")
print(f"Secondary: {secondary_metric}")
print(f"Target result: {final_composite}")