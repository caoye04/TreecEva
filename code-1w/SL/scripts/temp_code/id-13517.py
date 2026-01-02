def analyze_signal_quality(buffer, thresholds):
    # Initialize diagnostic variables
    signal_strength = sum(abs(x) for x in buffer)
    peak_magnitude = max(abs(x) for x in buffer)
    baseline_shift = (buffer[0] + buffer[-1]) / 2
    
    # Irrelevant intermediate computation: noise entropy (not used in final result)
    noise_levels = [abs(val - baseline_shift) for val in buffer]
    noise_entropy = 0
    for n in noise_levels:
        if n > 0:
            noise_entropy += n * math.log(n, 2)
    
    # Distractor: frequency distribution analysis (semi-relevant but unused)
    freq_count = {}
    for val in buffer:
        rounded = round(val, 1)
        freq_count[rounded] = freq_count.get(rounded, 0) + 1
    dominant_frequency = max(freq_count, key=freq_count.get) if freq_count else 0
    
    # Actual logic path: compute weighted quality score
    quality_score = 0
    weight_sum = 0
    
    for i, sample in enumerate(buffer):
        zone = 'high' if abs(sample) > thresholds['critical'] else 'normal'
        zone = 'moderate' if thresholds['warning'] < abs(sample) <= thresholds['critical'] else zone
        
        # Weight assignment based on position and zone
        positional_weight = 1.0 + (i / len(buffer))  # Slight emphasis on later samples
        if zone == 'high':
            contribution = abs(sample) * 1.8 * positional_weight
        elif zone == 'moderate':
            contribution = abs(sample) * 1.2 * positional_weight
        else:
            contribution = abs(sample) * 0.8 * positional_weight
        
        quality_score += contribution
        weight_sum += positional_weight
    
    normalized_quality = quality_score / weight_sum if weight_sum > 0 else 0
    
    # Secondary adjustment based on trend analysis (using slicing)
    early_segment = buffer[:len(buffer)//2]
    late_segment = buffer[len(buffer)//2:]
    
    early_avg = sum(early_segment) / len(early_segment) if early_segment else 0
    late_avg = sum(late_segment) / len(late_segment) if late_segment else 0
    trend_factor = 1.1 if late_avg > early_avg + 0.5 else 0.95
    
    adjusted_diagnostic = normalized_quality * trend_factor
    
    # Final mapping through conditional expression
    final_diagnostic = adjusted_diagnostic if adjusted_diagnostic > 5 else adjusted_diagnostic * 1.5
    
    # Dead code branch - never executed due to fixed condition (distractor)
    if False and peak_magnitude > 100:
        emergency_override = True
        final_diagnostic *= 2
    
    return final_diagnostic

# Main execution
import math

data_stream = [2.1, -3.5, 4.8, 6.2, -5.1, 3.3, 7.0, 8.4, -6.6, 5.9]
threshold_map = {
    'warning': 4.0,
    'critical': 6.0
}
diagnostic_buffer = [x * 0.85 for x in data_stream]  # Apply gain correction

# Red herring: unused statistical moment calculation
moment_2 = sum(x**2 for x in diagnostic_buffer) / len(diagnostic_buffer)
skew_proxy = sum(x**3 for x in diagnostic_buffer) / (len(diagnostic_buffer) * moment_2**1.5)

# Key statement
final_diagnostic = analyze_signal_quality(diagnostic_buffer, threshold_map)

print(f"Result: {final_diagnostic}")