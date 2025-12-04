def process_inventory(items):
    # Distractor: irrelevant inventory processing
    total_items = len(items)
    max_price = max(items) if items else 0
    min_price = min(items) if items else 0
    irrelevant_sum = sum(items) * 2  # Misleading calculation
    return total_items, max_price, min_price, irrelevant_sum

def calculate_stats(data_points):
    # More distractors: unused statistics
    mean_val = sum(data_points) / len(data_points)
    median_idx = len(data_points) // 2
    dead_var = data_points[median_idx] ** 2  # Dead code path
    range_val = max(data_points) - min(data_points)
    return mean_val, range_val

def final_calc(input_list):
    # Core logic with interventions
    filtered_vals = [x for i, x in enumerate(input_list) if i % 3 == 0]
    
    # Distractor: misleading intermediate
    temp_sum = sum(input_list) + len(input_list)
    
    # Relevant operations with enumerate
    indexed_data = [(idx, val) for idx, val in enumerate(filtered_vals)]
    
    # Distractor: unused zip operation
    pairs = list(zip(filtered_vals, input_list[:len(filtered_vals)]))
    
    # Core calculation
    result = 0
    for idx, val in indexed_data:
        if idx % 2 == 0:
            result += val * (idx + 1)
        else:
            result -= val // (idx + 1)
    
    # Final adjustment
    result = result % 1000 if result > 0 else abs(result) % 1000
    return result

# Main execution
inventory_data = [45, 23, 67, 89, 12, 34, 56, 78, 90, 11]
stats_data = [10, 25, 40, 15, 30, 20, 35]

# Irrelevant function calls
inv_results = process_inventory(inventory_data)
stats_results = calculate_stats(stats_data)

# Dead variable assignments
unused_var1 = inv_results[3] * 3
unused_var2 = stats_results[0] - stats_results[1]

# Processing target data
processed_data = [x + 5 for x in inventory_data[2:8]]

# Key statement
target_value = final_calc(processed_data)

print(f"Target result: {target_value}")