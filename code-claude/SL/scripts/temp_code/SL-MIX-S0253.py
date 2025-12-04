from collections import Counter

def analyze_data(readings):
    # Process sensor readings
    processed = [max(0, min(r, 100)) for r in readings]
    
    # Calculate standard statistics (some not used in final calculation)
    mean_value = sum(processed) / len(processed)
    median_value = sorted(processed)[len(processed) // 2]
    
    # Count frequency of readings
    reading_counts = Counter(processed)
    most_common = reading_counts.most_common(1)[0][0]
    
    # Calculate a weighted average based on occurrence patterns
    weights = {}
    for reading, count in reading_counts.items():
        # More frequent readings get higher weights
        weights[reading] = count / len(processed) * 1.5
    
    weighted_sum = 0
    weight_total = 0
    
    # Apply weights to readings
    for reading in processed:
        # Skip outliers for weighted calculation
        if abs(reading - mean_value) > 30:
            continue
        weighted_sum += reading * weights.get(reading, 1.0)
        weight_total += weights.get(reading, 1.0)
    
    # Weighted average calculation
    weighted_avg = weighted_sum / weight_total if weight_total > 0 else mean_value
    
    # Penalty calculation based on variance from most common reading
    variance_sum = sum((r - most_common)**2 for r in processed)
    variance_factor = variance_sum / (len(processed) * 100)
    penalty = variance_factor * 2.5
    
    # Apply bitwise operations for final adjustment
    base_adjustment = int(median_value) | 0x10  # Bitwise OR with 16
    noise_filter = base_adjustment & 0x1E      # Bitwise AND with 30
    bitwise_factor = 1 + (noise_filter / 16)   # Normalize to reasonable range
    
    # Calculate final score
    final_score = bitwise_factor * (weighted_avg - penalty)
    
    return final_score

# Sensor readings from monitoring system
sensor_data = [65, 68, 65, 70, 65, 72, 65, 68]

# Process readings and get result
result = analyze_data(sensor_data)
print(f"Result: {result}")