def analyze_metrics(raw_values, threshold=50):
    # Irrelevant transformation (distractor)
    squared_values = [x ** 2 for x in raw_values if x < 70]
    filtered = list(filter(lambda x: x > threshold, raw_values))
    
    # Semi-relevant aggregation
    avg_val = sum(filtered) / len(filtered) if filtered else 0
    deviation_map = {i: abs(v - avg_val) for i, v in enumerate(filtered)}
    
    # Core computation hidden among distractions
    base_score = sum(1 for v in raw_values if v % 2 == 0 and v in filtered)
    return base_score

# Simulate sensor readings
readings = [45, 62, 58, 71, 49, 55, 66]

# Distractor: unused statistical calculation
mean_reading = sum(readings) / len(readings)
std_dev = (sum((x - mean_reading) ** 2 for x in readings) / len(readings)) ** 0.5

# Preprocessing with red herring operations
transformed = []
for val in readings:
    if val > 60:
        transformed.append(val - 10)
    elif val < 50:
        transformed.append(val + 5)
    else:
        transformed.append(val)  # No change

# Another distraction: set operations not directly impacting result
unique_transformed = set(transformed)
duplicates_removed = len(readings) - len(unique_transformed)

# Actual processing pipeline
processed_data = [x + 1 for x in transformed if x % 3 != 0]

# Helper function using dictionary and lambda (required features)
calculate_final_score = lambda data: {
    'score': sum(data) // len(data) if data else 0,
    'bonus': len([x for x in data if x > 60])
}['score'] + len(set(data)) % 7

# Key execution point
final_score = calculate_final_score(processed_data)

# Output required format
print(f"Result: {final_score}")