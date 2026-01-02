import math

# Simulated sensor data processing with diagnostic output
def preprocess_sensor_readings(raw_readings):
    filtered = [x for x in raw_readings if x > -50 and x < 150]
    baseline = sum(filtered) / len(filtered)
    normalized = [round(x - baseline, 3) for x in filtered]
    return normalized

# Irrelevant helper - looks important but unused in critical path
def deprecated_calibrate(arr):
    return [a * 0.98 for a in arr if a > 0]

# Signal transformation using frequency masking
mask_profile = lambda vals, shift: [math.sin(v / (shift + 1e-5)) for v in vals]

# Decoy mapping - never actually used
status_codes = {
    'OK': 200,
    'CALIBRATE': 206,
    'ANALYZE': 208,
    'FAULT': 500
}

# Real mapping used in analysis
threshold_map = {
    'low': 0.35,
    'mid': 0.75,
    'high': 1.15
}

raw_sensor_data = [
    12.5, 13.8, 11.2, 14.1, 9.6, 10.3, 15.0, 13.2, 11.8, 12.9,
    45.2, 13.5, 14.0, 12.7, 11.9, 13.1, 12.4, 13.7, 12.6, 13.3
]

# Dead code path - simulates calibration sequence
if len(raw_sensor_data) % 2 == 0:
    calibration_factor = 1.05
else:
    calibration_factor = 0.95

calibration_factor = 1.0  # Override - nullifies prior logic

# Preprocessing stage
cleaned_data = preprocess_sensor_readings(raw_sensor_data)

# Transform via harmonic masking
transformed_data = mask_profile(cleaned_data, 3.5)

# Decoy statistical summary
summary_stats = {
    'mean': sum(transformed_data) / len(transformed_data),
    'variance': sum((x - sum(transformed_data)/len(transformed_data))**2 for x in transformed_data) / len(transformed_data),
    'peak': max(transformed_data),
    'truncated': transformed_data[::2]  # Slicing red herring
}

# Unused recursive filter
def recursive_denoise(signal, depth=0):
    if depth >= 3 or len(signal) < 2:
        return signal
    smoothed = [(signal[i-1] + signal[i] + signal[i+1])/3 for i in range(1, len(signal)-1)]
    return recursive_denoise(smoothed, depth + 1)

# Core analysis function with embedded logic chain
def analyze_signal(data, thresholds):
    count_low = count_mid = count_high = 0
    
    for val in data:
        abs_val = abs(val)
        if abs_val < thresholds['low']:
            count_low += 1
        elif abs_val < thresholds['mid']:
            count_mid += 1
        else:
            count_high += 1
    
    # Complex scoring with distractor weights
    weights = {'low': 0.1, 'mid': 0.3, 'high': 0.6}
    total_weighted = (count_low * weights['low'] + 
                     count_mid * weights['mid'] + 
                     count_high * weights['high'])
    
    # Secondary adjustment based on distribution pattern
    ratio_high = count_high / len(data)
    ratio_low = count_low / len(data)
    
    adjustment = 0
    if ratio_high > 0.25:
        adjustment += 15
    elif ratio_low > 0.5:
        adjustment -= 10
    
    # Hidden key computation: sum of squared indices where |val| > 0.75
    special_sum = 0
    for idx, val in enumerate(data):
        if abs(val) > 0.75:
            special_sum += idx ** 2  # Critical result embedded here
    
    # Final diagnostic combines irrelevant components
    dummy_flag = len(data) > 15 and math.isclose(summary_stats['mean'], 0, abs_tol=0.1)
    offset = 128 if dummy_flag else 64
    
    # The real answer is special_sum, masked within complex expression
    final_value = int(special_sum + adjustment + offset - total_weighted * 10)
    
    return final_value

# Misleading intermediate call (no side effects)
analyze_signal(transformed_data, {'low': 0.1, 'mid': 0.5, 'high': 0.9})

# Critical execution point
final_diagnostic = analyze_signal(transformed_data, threshold_map)

print(f"Result: {final_diagnostic}")