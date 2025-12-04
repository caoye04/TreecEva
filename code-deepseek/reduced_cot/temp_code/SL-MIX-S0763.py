def analyze_sensor_readings(sensor_data):
    # Distractor: irrelevant temperature conversions
    temp_celsius = [25.7, 23.1, 28.9, 22.4, 26.8]
    temp_fahrenheit = [(t * 9/5) + 32 for t in temp_celsius]
    
    # Actual processing
    quality_threshold = 85
    calibration_offset = 7
    
    # Multiple operations with misleading intermediate values
    adjusted_readings = []
    for idx, reading in enumerate(sensor_data):
        # Distractor: unused calculation
        noise_reduction = reading % 3
        
        # Relevant processing
        if reading > quality_threshold:
            adjusted = reading - calibration_offset
        else:
            adjusted = reading + (calibration_offset // 2)
        
        # Distractor: dead code path
        if idx % 2 == 0:
            spectral_analysis = adjusted * 0.8  # Never used
        
        adjusted_readings.append(adjusted)
    
    # More distractors
    sensor_stats = {
        'max_temp': max(temp_fahrenheit),  # Irrelevant
        'avg_reading': sum(sensor_data) / len(sensor_data)
    }
    
    # Core logic with bitwise operations
    processed_scores = []
    for val in adjusted_readings:
        # Bitwise operations as distractors
        bit_mask = 0b10101010
        masked_val = val & bit_mask  # Irrelevant result
        
        # Actual scoring logic
        if val > 90:
            score = (val * 1.2) - 15
        elif val > 80:
            score = val + (val % 10)
        else:
            score = val * 0.9
        
        processed_scores.append(int(score))
    
    # Final computation with tuple unpacking
    high_scores = [s for s in processed_scores if s > 85]
    low_scores = [s for s in processed_scores if s <= 85]
    
    # Multiple assignments as distraction
    score_ranges = (min(high_scores), max(high_scores)) if high_scores else (0, 0)
    unused_range_diff = score_ranges[1] - score_ranges[0]
    
    # The key variable
    final_quality_metric = processed_scores[-1]
    
    print(f"Result: {final_quality_metric}")
    return final_quality_metric

# Main execution
sensor_samples = [92, 87, 94, 79, 96, 88, 91]
analyze_sensor_readings(sensor_samples)