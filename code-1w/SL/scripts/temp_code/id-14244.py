def analyze_readings(readings):
    base_level = 23.5
    adjustment_factor = 1.2
    offset = 7
    
    # Normalize readings and apply adjustment
    normalized = [r * adjustment_factor for r in readings]
    
    # Filter readings above dynamic threshold
    dynamic_threshold = base_level + offset
    filtered_readings = [val for val in normalized if val > dynamic_threshold]
    
    # Irrelevant auxiliary calculation (minor distraction)
    average_reading = sum(readings) / len(readings) if readings else 0
    
    energy_threshold = sum(filtered_readings)
    return energy_threshold

# Input data
data_stream = [18.0, 20.5, 25.0, 30.0, 19.0]
result = analyze_readings(data_stream)
print(f"Result: {result}")