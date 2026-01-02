def transform_data(data, limit):
    filter_func = lambda x: x > limit
    filtered = [x for x in data if filter_func(x)]
    
    adjustment = 3
    adjusted_values = [val - adjustment for val in filtered]
    
    sum_val = sum(adjusted_values)
    count = len(adjusted_values)
    
    # Irrelevant variable (minor distraction)
    temp_message = "Processing complete"
    
    if count > 0:
        result = sum_val / count
    else:
        result = 0
    
    return result

values = [10, 15, 4, 8, 12, 7]
threshold = 6
result = transform_data(values, threshold)
print(f"Result: {result}")