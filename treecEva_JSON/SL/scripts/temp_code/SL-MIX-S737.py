from functools import reduce

def calculate_waveform_metrics(raw_samples):
    metrics = {}
    # Apply noise reduction using XOR and bit shifting
    cleaned_samples = [sample ^ (sample >> 3) for sample in raw_samples]
    
    # Compute power levels using floating point operations
    power_levels = list(map(lambda x: round((x * 0.75) ** 0.5, 2), cleaned_samples))
    
    # Identify significant peaks using bitwise AND
    peak_flags = [1 if (int(p) & 0b1111) > 7 else 0 for p in power_levels]
    
    # Early return if no significant peaks found
    if sum(peak_flags) == 0:
        return 0
    
    # Calculate weighted average of significant peaks
    weighted_sum = 0
    count = 0
    for i in range(len(power_levels)):
        if peak_flags[i]:
            weighted_sum += power_levels[i] * (i + 1)
            count += 1
            if count >= 3:  # Limit to first 3 significant peaks
                break
    
    # Final signal strength calculation
    processed_signal_strength = int(weighted_sum / count) & 0xFF
    return processed_signal_strength

# Input data representing raw sensor readings
sensor_readings = [120, 85, 200, 95, 160, 75, 220, 110, 145, 90]

# Execute the processing pipeline
processed_signal_strength = calculate_waveform_metrics(sensor_readings)
print(f"Result: {processed_signal_strength}")