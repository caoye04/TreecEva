import itertools

def analyze_sensor_readings(readings, threshold):
    # Process readings from multiple environmental sensors
    processed = []
    
    # Apply baseline correction (doesn't affect final result)
    baseline = sum(readings[:3]) / 3
    adjusted = [r - baseline for r in readings]
    
    # First filter: remove outliers using lambda
    outlier_filter = lambda x: abs(x) < threshold * 2
    preliminary = list(filter(outlier_filter, adjusted))
    
    # Calculate some statistics (not used in final answer)
    stats = {
        'mean': sum(preliminary) / len(preliminary) if preliminary else 0,
        'range': max(preliminary) - min(preliminary) if preliminary else 0
    }
    
    # Group readings into pairs and calculate differences
    # This is the key operation that affects our answer
    pairs = list(itertools.pairwise(preliminary))
    differences = [abs(b - a) for a, b in pairs]
    
    # Another filter: keep only significant differences
    filtered_data = [d for d in differences if d > threshold]
    
    # Count unique difference values (our target result)
    unique_items = len(set(filtered_data))
    
    # Extra calculations that don't affect the answer
    total_variance = sum([abs(d - stats['mean']) for d in filtered_data])
    normalized = [d / stats['range'] if stats['range'] else d for d in filtered_data]
    
    print(f"Result: {unique_items}")
    return unique_items

# Test with sample data
sensor_readings = [12, 15, 14, 17, 19, 22, 25, 22, 19, 17]
threshold = 2
result = analyze_sensor_readings(sensor_readings, threshold)
