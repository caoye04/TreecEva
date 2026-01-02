from itertools import compress

def process_data(data, limit):
    # Calculate squared deviations from mean
    mean_val = sum(data) / len(data)
    squared_devs = [(x - mean_val) ** 2 for x in data]
    
    # Use conditional expression to filter significant deviations
    is_significant = lambda x: x >= limit
    filtered_devs = list(filter(is_significant, squared_devs))
    
    # Compute weighted contribution using conditional logic
    weights = [dev / sum(filtered_devs) if filtered_devs else 0 for dev in squared_devs]
    
    # Aggregate final result using element-wise condition
    adjusted_values = [data[i] * (1 + weights[i]) if weights[i] > 0 else data[i] for i in range(len(data))]
    
    # Final result: sum of adjusted values above original mean
    result = sum(compress(adjusted_values, [v > mean_val for v in adjusted_values]))
    return result

# Input data and threshold
values = [12, 15, 23, 18, 14, 20]
thresh = 16.0

# Execute function
temp_var = sum(values)  # Irrelevant operation (minimal distraction)
result = process_data(values, thresh)
print(f"Target result: {result}")