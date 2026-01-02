import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 25.8, 24.7, 23.9]
humidity_readings = [55, 58, 60, 53, 49, 51, 57, 61]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1009, 1011, 1014]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_X = 0.987
CALIBRATION_FACTOR_Y = 1.015
REFERENCE_OFFSET = 273.15

# Noise filter threshold (misleading parameter)
NOISE_THRESHOLD = 0.5

# Decoy function: appears useful but unused in main logic
def apply_calibration(data, factor):
    return [x * factor for x in data]

# Auxiliary transformation function used in processing
def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    return [(x - mean_val) / mean_val for x in signal]

# Complex signal conditioner with red herring operations
def condition_signal(raw_data):
    conditioned = []
    temp_offset = REFERENCE_OFFSET  # Unused in logic, distractor
    scaling_factor = 1.0
    
    for i, val in enumerate(raw_data):
        if i % 2 == 0:
            # Apply non-linear transformation on even indices
            transformed = math.log(val + 1) * scaling_factor
        else:
            # Apply bitwise-like adjustment (simulated via int casting)
            shifted = int(val) >> 1
            transformed = math.sin(shifted) if shifted > 0 else 0.0
        conditioned.append(abs(transformed))
    
    # Dead code path - never executed due to fixed condition (distractor)
    debug_mode = False
    if debug_mode:
        print(f'Debug: {conditioned}')
    
    return conditioned

# Signal processor that combines multiple data streams
def process_signals(temp, hum, pres):
    # Normalize all signals
    norm_temp = normalize_signal(temp)
    norm_hum = normalize_signal(hum)
    norm_pres = normalize_signal(pres)
    
    # Condition each signal path
    proc_temp = condition_signal(norm_temp)
    proc_hum = condition_signal(norm_hum)
    proc_pres = condition_signal(norm_pres)
    
    # Combine signals using weighted fusion (weights are misleading)
    weights = [0.3, 0.4, 0.3]  # Suggests importance, but not used directly
    fused_signal = []
    for a, b, c in zip(proc_temp, proc_hum, proc_pres):
        fused = (a * 0.3) + (b * 0.4) + (c * 0.3)  # Actual usage
        fused_signal.append(fused)
    
    # Additional transformation using lambda (required python feature)
    enhance = lambda x: round(x ** 2, 4) if x > 0 else 0.0
    enhanced = [enhance(x) for x in fused_signal]
    
    # Misleading entropy calculation (unused)
    entropy = -sum(x * math.log(x) for x in enhanced if x > 0)
    
    return enhanced

# Diagnostic analyzer with conditional logic chain
def analyze_readings(signal_sequence):
    cumulative_score = 0
    threshold = 0.25
    
    for idx, reading in enumerate(signal_sequence):
        # Multiple layered conditions (complex branching)
        if reading > threshold:
            if idx % 3 == 0:
                cumulative_score += int(reading * 100)
            elif idx % 3 == 1 and reading < 0.5:
                cumulative_score -= 10
            else:
                cumulative_score += 5
        
        # Nested modular arithmetic and bit check (red herring)
        if idx > 0:
            prev = signal_sequence[idx - 1]
            checksum = (int(prev * 100) ^ int(reading * 100)) & 0xFF
            if checksum % 7 == 0:
                cumulative_score += 1  # Minor influence, but distracting
    
    # Final adjustment based on set property (actual key step)
    unique_values = set(round(x, 3) for x in signal_sequence)
    size_penalty = len(unique_values) - 5
    final_adjustment = cumulative_score - (size_penalty * 3)
    
    # Dead computation: complex but irrelevant trigonometric sum
    dummy_sum = sum(math.cos(i * math.pi / 4) for i in range(len(signal_sequence)))
    
    return final_adjustment

# Main execution flow
if __name__ == '__main__':
    # Process raw sensor data into unified signal
    processed_signals = process_signals(temperature_readings, humidity_readings, pressure_readings)
    
    # Trigger key statement: analyze the processed signals
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")