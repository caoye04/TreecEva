def analyze_system_metrics():
    raw_readings = [0.85, 1.23, 0.91, 2.05, 1.76, 0.64, 3.14, 2.21]
    
    # Normalize readings to percentage efficiency
    normalized_efficiency = [int(x * 100) for x in raw_readings]
    
    # Identify stable readings (between 80 and 200)
    stable_indices = []
    for i, val in enumerate(normalized_efficiency):
        if 80 <= val <= 200:
            stable_indices.append(i)
    
    # Extract corresponding raw metrics for stable performance
    filtered_metrics = [raw_readings[i] for i in stable_indices]
    
    # Compute final filtration score as sum of valid raw metrics
    filtration_score = sum(filtered_metrics)
    
    # Irrelevant tracking variable (minor distraction)
    total_entries = len(raw_readings)
    
    print(f"Result: {filtration_score}")

analyze_system_metrics()