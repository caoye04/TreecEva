def analyze_sensor_data(readings, baseline=100):
    # Process temperature and humidity readings
    sensor_vals = []
    anomalies = 0
    
    # Extract and normalize readings
    for i, reading in enumerate(readings):
        temp, humidity = reading
        normalized = (temp / 10, humidity * 2)
        
        # Track anomalies (not used in final calculation)
        if temp > 30 or humidity < 20:
            anomalies += 1
            
        sensor_vals.append(normalized)
    
    # Calculate calibration factor (distraction)
    calibration = sum(h for _, h in sensor_vals) / len(sensor_vals) if sensor_vals else 0
    
    # Generate all possible sensor pairs
    all_pairs = []
    for i, s1 in enumerate(sensor_vals):
        for j, s2 in enumerate(sensor_vals):
            if i != j:  # Don't pair a sensor with itself
                all_pairs.append((s1, s2))
    
    # Filter pairs based on compatibility criteria
    threshold = baseline / 10
    valid_pairs = []
    
    # Use zip and enumerate for processing pairs
    for idx, pair in enumerate(all_pairs):
        s1, s2 = pair
        t1, h1 = s1
        t2, h2 = s2
        
        # Calculate compatibility score
        compatibility = (t1 * h2 + t2 * h1) / 2
        
        # Store valid pairs
        if compatibility > threshold:
            valid_pairs.append((t1 + t2, h1 + h2))
    
    # Count valid combinations that exceed threshold
    valid_combinations = len([pair for pair in valid_pairs if pair[0] + pair[1] > threshold])
    
    # Calculate alternative metric (not used in final result)
    alternative_metric = sum(t for t, _ in valid_pairs) if valid_pairs else 0
    
    print(f"Result: {valid_combinations}")
    return valid_combinations

# Test with sample data
readings = [(25, 30), (28, 25), (22, 40)]
result = analyze_sensor_data(readings)