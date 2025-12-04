def calculate_sequence_value(n):
    # Helper function that calculates a sequence value
    if n <= 1:
        return n
    return calculate_sequence_value(n-1) + calculate_sequence_value(n-2)

# Dataset of temperature readings from different sensors
temperature_readings = [
    ("sensor_A", [32.5, 31.8, 33.2, 32.9, 33.0]),
    ("sensor_B", [31.7, 32.3, 32.6, 31.9, 32.1]),
    ("sensor_C", [33.1, 32.8, 33.3, 32.7, 32.5])
]

# Process temperature readings
processed_data = {}
for i, (sensor_name, readings) in enumerate(temperature_readings):
    # Calculate average temperature for this sensor
    avg_temp = sum(readings) / len(readings)
    processed_data[sensor_name] = {
        "readings": readings,
        "average": avg_temp,
        "index": i
    }

# Extract sensor readings that exceed threshold
threshold = 32.5
exceeded_count = 0
filtered_values = []

# Analyze data from sensors
for sensor_name, data in processed_data.items():
    # Track position in the original dataset
    position = data["index"]
    
    # Calculate a threshold modifier based on sensor position
    modifier = calculate_sequence_value(position + 1) * 0.1
    adjusted_threshold = threshold + modifier
    
    # Extract readings exceeding the adjusted threshold
    for i, temp in enumerate(data["readings"]):
        if temp > adjusted_threshold:
            exceeded_count += 1
            # Apply a transformation to the reading
            transformed_value = round(temp - adjusted_threshold, 1) * 10
            filtered_values.append(transformed_value)

# Calculate statistics on filtered values
filtered_stats = {
    "count": len(filtered_values),
    "max": max(filtered_values) if filtered_values else 0,
    "min": min(filtered_values) if filtered_values else 0
}

# Process slices of the filtered values for additional analysis
slice_1 = filtered_values[::2]  # Every other value
slice_2 = filtered_values[1::2] if len(filtered_values) > 1 else []

# Compute the final filtered sum
filtered_sum = sum(value for value in filtered_values)

# Display results
print(f"Exceeded count: {exceeded_count}")
print(f"Filtered statistics: {filtered_stats}")
print(f"Result: {filtered_sum}")