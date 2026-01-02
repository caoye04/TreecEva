def process_data(values, limit):
    # Irrelevant pre-processing: reverse and shift (not affecting final logic)
    shifted = [v >> 1 for v in values]
    reversed_vals = values[::-1]

    # Semi-relevant transformation using lambda and enumerate
    indexed_sum = 0
    modifier = lambda x: x ** 2 if x % 2 == 0 else x + 1
    
    temp_accum = []
    for i, val in enumerate(values):
        if i % 3 == 0:
            temp_accum.append(modifier(val))

    # Dead code path: never executed due to condition
    debug_mode = False
    if debug_mode:
        print(f'Debug: {temp_accum}')

    # Core logic: sum elements exceeding threshold, then apply zip-based pairing
    filtered = [v for v in values if v > limit]
    
    # Use zip to pair with offset version of itself (for distraction)
    paired = list(zip(filtered, filtered[1:] + [0]))
    pair_product_sum = sum(a * b for a, b in paired)

    # Actual result depends only on sum of squares of filtered elements
    squared_filtered = [x ** 2 for x in filtered]
    base_result = sum(squared_filtered)

    # Conditional expression based on length parity
    adjustment = 5 if len(squared_filtered) % 2 == 0 else -3

    # Final result
    result = base_result + adjustment

    return result

# Main execution
config_flag = True
aux_data = [1, 4, 9, 16]  # unused beyond assignment

threshold = 7
data = [3, 8, 5, 12, 6, 14, 10]

# Key computation
result = process_data(data, threshold)

print(f'Result: {result}')