import itertools

def preprocess_data(raw_data):
    # Normalize and filter out outliers
    processed = []
    for value in raw_data:
        adjusted = value * 0.8 + 10
        if 15 <= adjusted <= 85:
            processed.append(adjusted)
    return processed

def apply_transformations(data):
    # Apply various transformations to the data
    transformed = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            transformed.append(val + 5)
        else:
            transformed.append(val - 3)
    
    # Additional calculation that doesn't affect result
    complexity_factor = sum(data) / len(data) if data else 0
    return transformed

def calculate_final_score(data, weights):
    # Apply weights and compute final score
    if not data or not weights:
        return 0
    
    # Use slicing to get subset of data
    relevant_data = data[1:6]
    
    # Create pairs using itertools and lambda
    paired_values = list(itertools.zip_longest(relevant_data, weights, fillvalue=1))
    weighted_sum = sum(map(lambda pair: pair[0] * pair[1], paired_values))
    
    # Compute average (this is what we want)
    result = weighted_sum / len(relevant_data)
    
    # Unnecessary calculation for intervention
    max_possible = max(relevant_data) * max(weights)
    min_possible = min(relevant_data) * min(weights)
    range_values = max_possible - min_possible
    
    return round(result, 2)

# Main execution
raw_sensor_data = [12, 45, 67, 23, 89, 34, 56, 78, 15, 38]
weights = [0.5, 1.2, 0.8, 1.0, 0.7]

# Process raw data
processed_data = preprocess_data(raw_sensor_data)

# Generate some statistics that aren't used
data_stats = {
    'min': min(processed_data),
    'max': max(processed_data),
    'mean': sum(processed_data) / len(processed_data)
}

# Apply transformations
transformed_data = apply_transformations(processed_data)

# Filter data based on threshold
threshold = 50
filtered_data = [x for x in transformed_data if x <= threshold]

# Calculate the final score
final_score = calculate_final_score(filtered_data, weights)
print(f"Target result: {final_score}")