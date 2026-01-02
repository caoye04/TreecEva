def analyze_temperature_readings():
    raw_readings = [23.5, 19.0, 27.3, 31.2, 18.8, 24.1, 29.5, 22.7, 30.0, 25.4]
    threshold = 25.0
    
    # Normalize readings by adjusting offset
    adjusted_readings = [x + 0.5 for x in raw_readings]
    
    # Use enumerate to identify high readings with their positions
    high_reading_indices = []
    for i, temp in enumerate(adjusted_readings):
        if temp > threshold:
            high_reading_indices.append(i)
    
    # Extract qualifying temperatures using slicing after sorting
    sorted_readings = sorted(adjusted_readings)
    start_idx = len(sorted_readings) - len(high_reading_indices)
    top_third_readings = sorted_readings[start_idx:]
    
    # Filter data using zip to pair original and adjusted values
    paired_readings = list(zip(raw_readings, adjusted_readings))
    filtered_data = [adj for orig, adj in paired_readings if adj >= 24.5]
    
    # Final computation
    filtered_sum = sum(filtered_data)
    print(f"Result: {filtered_sum}")

analyze_temperature_readings()