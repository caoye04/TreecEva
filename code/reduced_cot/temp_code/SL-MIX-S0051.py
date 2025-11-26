def process_data(values, threshold):
    filter_func = lambda x: x if x % 2 == 0 else x // 2
    processed = [filter_func(val) for val in values]
    total = sum(processed)
    
    # Apply threshold rounding
    if total > threshold:
        return total // 10 * 10
    else:
        return total

data_points = [7, 14, 21, 28, 35]
rounding_threshold = 60
final_computation = process_data(data_points, rounding_threshold)

print(f"Result: {final_computation}")