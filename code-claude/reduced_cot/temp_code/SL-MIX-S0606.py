def analyze_sensor_readings(readings):
    # Process sensor data to extract meaningful patterns
    processed = {}
    noise_factor = 3.7
    for i, reading in enumerate(readings):
        processed[f'sensor_{i}'] = reading * noise_factor - (i % 3)
    
    # Calculate irrelevant metrics for diagnostic purposes
    avg_reading = sum(readings) / len(readings)
    max_diff = max(readings) - min(readings)
    variance = sum((r - avg_reading) ** 2 for r in readings) / len(readings)
    
    return processed, avg_reading, max_diff, variance

def calculate_priority(data, threshold):
    # Priority calculation based on filtered sensor data
    if not data:
        return 0
    
    # Extract relevant measurement components
    components = []
    for key, value in data.items():
        if 'critical' in key:
            components.append(value * 2.5)
        elif 'warning' in key:
            components.append(value * 1.5)
        else:
            # Regular components have standard weight
            components.append(value)
    
    # Calculate baseline priority score
    baseline = sum(components) / len(components)
    
    # Apply threshold adjustment
    if baseline > threshold:
        return int(baseline + (baseline - threshold) * 0.8)
    else:
        return int(baseline * 0.9)

# Sensor readings from multiple locations
readings = [12, 15, 9, 18, 14]

# Process readings with noise and interference
processed_data, average, delta, var = analyze_sensor_readings(readings)

# Additional environmental factors (not used in final calculation)
environmental_factors = {
    'temperature': 22.5,
    'humidity': 45,
    'pressure': 1013
}

# Apply various filters to identify patterns
filtered_data = {}
threshold = 20

# Enrich data with metadata and apply filters
for sensor_id, value in processed_data.items():
    # Create enriched data structure with unnecessary fields
    enriched = {
        'value': value,
        'normalized': (value - average) / max(1, delta),
        'timestamp': '2023-10-15T14:30:00Z',
        'status': 'active' if value > average else 'standby'
    }
    
    # Determine sensor category based on value
    if value > average + delta/2:
        category = 'critical'
    elif value < average - delta/2:
        category = 'warning'
    else:
        category = 'normal'
    
    # Store only filtered data that meets criteria
    if category in ['critical', 'warning'] or value > threshold - 5:
        filtered_data[f'{category}_{sensor_id}'] = round(value, 1)

# Calculate priority based on filtered data
priority_value = calculate_priority(filtered_data, threshold)

# Prepare supplementary analysis (not used in result)
supplementary = {}
for key in filtered_data:
    parts = key.split('_')
    if len(parts) > 1:
        category = parts[0]
        if category not in supplementary:
            supplementary[category] = 0
        supplementary[category] += 1

# Calculate alternative priority metrics (distractors)
weighted_sum = sum(value * (i+1) for i, value in enumerate(sorted(filtered_data.values())))
alternative_priority = int(weighted_sum / len(filtered_data) if filtered_data else 0)

# Final result
print(f"Result: {priority_value}")