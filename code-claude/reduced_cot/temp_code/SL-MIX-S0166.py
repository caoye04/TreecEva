def calculate_entropy(values):
    # Calculate information entropy (unused function)
    from math import log2
    total = sum(values)
    return -sum((x/total) * log2(x/total) if x > 0 else 0 for x in values)

def filter_outliers(data, threshold=2.5):
    # Remove statistical outliers (this function is a distraction)
    if not data:
        return []
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean) <= threshold * std_dev]

def calculate_priority(data_points):
    # Main function that determines priority level based on data points
    if not data_points or len(data_points) < 3:
        return 0
    
    # Distraction: creating a complex data structure we won't fully use
    metrics = {
        'max': max(data_points),
        'min': min(data_points),
        'range': max(data_points) - min(data_points),
        'count': len(data_points),
        'sum': sum(data_points),
        'product': 1
    }
    
    # Misleading calculation that won't be used in final result
    for point in data_points:
        if point % 2 == 0:
            metrics['product'] *= point
    
    # More distractions - create unnecessary transformations
    transformed = []
    for i, val in enumerate(data_points):
        if i % 3 == 0:
            transformed.append(val * 2)
        elif i % 3 == 1:
            transformed.append(val // 2 if val > 0 else val)
        else:
            transformed.append(val + 3)
    
    # Distraction: create a binary representation we won't use
    binary_flags = [bin(abs(int(x)) % 256)[2:].zfill(8) for x in data_points]
    bit_counts = [s.count('1') for s in binary_flags]
    
    # Distraction: lambda functions that aren't relevant to final calculation
    weight_func = lambda x: x**2 if x > 0 else -x**2
    normalize = lambda values: [(x - min(values)) / (max(values) - min(values)) 
                              if max(values) != min(values) else 0.5 for x in values]
    
    # Dead code path - this condition is always False with our input
    if sum(data_points) < 0 and all(x < -10 for x in data_points):
        return metrics['max'] - metrics['min']
    
    # This is where the actual calculation happens
    # The key logic for priority calculation
    even_count = len([x for x in data_points if x % 2 == 0])
    odd_count = len(data_points) - even_count
    
    # Actual priority calculation - uses bit manipulation as distraction
    base_priority = (even_count * 3) ^ (odd_count * 2)
    multiplier = 1 + (metrics['count'] & 0x7) / 10
    
    # More distraction with list comprehension
    adjusted_values = [x + (i % 3) for i, x in enumerate(data_points)]
    unused_adjustment = sum(adjusted_values) / len(adjusted_values) if adjusted_values else 0
    
    # The actual calculation that matters
    priority_level = int(base_priority * multiplier)
    
    # Final distraction with conditional expression
    return priority_level + (1 if metrics['max'] > 100 else 0)

# Main execution
data_points = [15, 23, 42, 8, 16, 31]

# Distractions - create derived data that won't be used
data_squared = [x**2 for x in data_points]
data_filtered = filter_outliers(data_points)
entropy = calculate_entropy(data_points)

# More distractions - various transformations
processed_data = []
for i, val in enumerate(data_points):
    if i % 2 == 0:
        processed_data.append(val * 3)
    else:
        processed_data.append(val - 5)

# Set of distracting values
max_val = max(processed_data)
min_val = min(processed_data)
diff_val = max_val - min_val

# The key statement we're evaluating
priority_level = calculate_priority(data_points)

# Misleading operations after the key statement
adjusted_priority = priority_level * 2 - 10
weighted_priority = adjusted_priority + (max_val % 10)

print(f"Result: {priority_level}")