import math

# Simulated sensor data and diagnostic system
raw_readings = [3.2, 4.7, 1.1, 8.9, 5.5, 2.4, 7.6, 6.3]

timestamps = [1623456000, 1623456060, 1623456120, 1623456180, 1623456240, 1623456300, 1623456360, 1623456420]
calibration_offsets = [0.1, -0.2, 0.05, 0.3, -0.1, 0.15, -0.05, 0.2]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D1', 'E8', 'F3', 'G6', 'H5']
error_flags = [False, False, True, False, False, True, False, False]

# Misleading intermediate computation (dead path)
def compute_legacy_score(code_sequence):
    score = 0
    for code in code_sequence:
        if code[0] in 'ACF':
            score += ord(code[1]) - ord('0')
    return score

legacy_score = compute_legacy_score(legacy_codes)  # Dead variable

# Data correction with distraction
adjusted_readings = []
for i in range(len(raw_readings)):
    adjusted = raw_readings[i] + calibration_offsets[i]
    adjusted_readings.append(round(adjusted, 2))

# Another red herring: error-based filtering (not used in final path)
filtered_diagnostics = []
for val, err in zip(adjusted_readings, error_flags):
    if not err:
        filtered_diagnostics.append(val ** 2 > 20)

# Core transformation pipeline
scaling_factor = 1.85
delta_weights = [abs(timestamps[i+1] - timestamps[i]) for i in range(len(timestamps)-1)]
mean_weight = sum(delta_weights) / len(delta_weights)

# Apply non-linear transformation (relevant)
transformed_data = []
for x in adjusted_readings:
    temp_val = x * scaling_factor
    if temp_val > 5.0:
        transformed_data.append(math.log(temp_val) * 1.5)
    else:
        transformed_data.append(math.sqrt(temp_val) * 2.1)

# Decoy function (looks important but unused)
def analyze_trend(data_stream):
    trend_score = 0
    for i in range(1, len(data_stream)):
        if data_stream[i] > data_stream[i-1]:
            trend_score += 1
        elif data_stream[i] < data_stream[i-1]:
            trend_score -= 0.5
    return trend_score

# Unused but plausible-looking analysis
temporal_trend = analyze_trend(adjusted_readings)

# Actual logic: higher-order function filter
threshold_func = lambda x: x > 3.25

# Real processing chain
def process_metrics(data, threshold_filter):
    valid_count = 0
    total_contribution = 0.0
    
    for val in data:
        if threshold_filter(val):
            valid_count += 1
            total_contribution += val * val
        
        # Nested conditional with side-effect-like structure (but no real side effect)
        if val > 2.0:
            adjustment = 0.7
            if val < 4.0:
                adjustment = 1.1
                if val > 3.5:
                    adjustment = 0.9
            total_contribution += adjustment  # Minor additive rule
    
    # Complex aggregation
    if valid_count == 0:
        return 0.0
    
    average_contrib = total_contribution / valid_count
    
    # Final nonlinear scaling using bit manipulation hint (symbolic, not actual bit op)
    scale_hint = len([d for d in data if d > 2.5])
    bit_inspired_scale = (scale_hint ^ 5) & 7  # Bitwise decoy with real impact
    
    final_score = average_contrib * bit_inspired_scale
    
    # Additional trap: unused rounding branch
    precision_mode = True
    if precision_mode:
        final_score = round(final_score, 4)
    
    return final_score

# Execution point of interest
final_diagnostic = process_metrics(transformed_data, threshold_func)

# Print required result
print(f"Result: {final_diagnostic}")