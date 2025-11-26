def calculate_metrics(values):
    total = sum(values)
    avg = total / len(values)
    squared_diffs = [pow((x - avg), 2) for x in values]
    variance = sum(squared_diffs) / len(values)
    return variance, total

def filter_data(records, threshold):
    filtered = [r for r in records if r > threshold]
    return len(filtered), sum(filtered)

def process_data(dataset, flags):
    # Irrelevant computation path 1
    temp_calc = (flags[0] * 3.14) + (flags[1] * 2.71)
    unused_var = temp_calc % 7
    
    # Main logic path
    base_values = [x for x in dataset if x % 2 == flags[2]]
    variance, total_base = calculate_metrics(base_values)
    
    # Irrelevant computation path 2
    bit_ops = (flags[0] & flags[1]) | (flags[1] ^ flags[2])
    redundant_calc = bit_ops * 3 - 7
    
    # Secondary processing
    threshold = total_base / len(base_values) if base_values else 0
    count_above, sum_above = filter_data(dataset, threshold)
    
    # Dead code path
    if count_above > 1000:
        bonus = count_above * 2
    else:
        bonus = count_above // 2
    
    # Final computation
    result = (total_base + sum_above) // (count_above + 1)
    return result

# Initialize data
initial_set = [15, 28, 42, 56, 71, 89, 103, 117, 132, 148]
configuration = [3, 5, 1]

# Misleading intermediate variable
temp_result = process_data(initial_set, [1, 2, 0])
distraction = temp_result * 2 + 10

# Actual computation
final_result = process_data(initial_set, configuration)

# Verify execution
print(f"Result: {final_result}")