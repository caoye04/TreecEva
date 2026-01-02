import math

# Simulate a diagnostic signal processing pipeline for sensor array
def preprocess_segment(segment):
    smoothed = []
    for i in range(1, len(segment) - 1):
        filtered_val = (segment[i-1] + 2*segment[i] + segment[i+1]) / 4.0
        smoothed.append(filtered_val)
    return smoothed

# Misleading helper: not used in final path
def legacy_calibrate(data):
    peak = max(data)
    norm_factor = 1.0 / (peak if peak != 0 else 1)
    return [x * norm_factor for x in data]

# Core analysis function
def analyze_signal(buffer, thresholds):
    diagnostics = []
    temp_accum = 0
    
    for key in sorted(thresholds.keys()):
        slice_start = key * 2
        slice_end = slice_start + 6
        data_slice = buffer[slice_start:slice_end]
        
        # Preprocess the slice (smoothing)
        if len(data_slice) >= 3:
            processed = preprocess_segment(data_slice)
        else:
            processed = data_slice
        
        # Evaluate against threshold
        avg_val = sum(processed) / len(processed) if processed else 0
        if avg_val > thresholds[key]:
            temp_accum += int(avg_val)
            diagnostics.append(1)
        else:
            temp_accum -= 1
            diagnostics.append(0)
    
    # Secondary computation (distraction)
    entropy = 0.0
    counts = {0: diagnostics.count(0), 1: diagnostics.count(1)}
    total = len(diagnostics)
    for count in counts.values():
        if count > 0:
            prob = count / total
            entropy -= prob * math.log(prob)
    
    # Final result computation
    stability_score = diagnostics.count(1) * temp_accum
    final_diagnostic = stability_score + len([x for x in diagnostics if x == 1])
    
    # Dead code path (never reached in normal flow)
    if False:
        fallback = sum(buffer) // len(buffer)
        final_diagnostic = fallback
        
    return final_diagnostic

# Initialize sensor data and parameters
pattern_buffer = [3, 7, 2, 8, 5, 9, 1, 6, 4, 10, 0, 5, 3, 8, 2]
evaluation_phases = {'baseline': 4.5, 'critical': 6.0}
threshold_map = {0: 4.0, 1: 5.5, 2: 3.0}

# Unused variables (distractors)
signal_power = sum(x**2 for x in pattern_buffer)
normalized_rms = (signal_power / len(pattern_buffer)) ** 0.5
alignment_shift = pattern_buffer[-3:] + pattern_buffer[:-3]

# Key execution point
final_diagnostic = analyze_signal(pattern_buffer, threshold_map)

# Print result
print(f"Result: {final_diagnostic}")