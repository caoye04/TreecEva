import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7]
humidity_readings = [56, 58, 61, 59, 62, 64, 66, 63]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1018, 1017, 1015]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.037
CALIBRATION_OFFSET_B = -0.021
REFERENCE_VOLTAGE = 3.3
MAX_SENSOR_RANGE = 100.0

# Misleading intermediate processing (dead path)
def deprecated_normalization(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Unused transformation function (decoy)
def frequency_domain_transform(signal):
    # Simulate FFT (not actually used)
    transformed = []
    for i in range(len(signal)):
        real = sum(signal[j] * math.cos(2 * math.pi * i * j / len(signal)) for j in range(len(signal)))
        imag = sum(-signal[j] * math.sin(2 * math.pi * i * j / len(signal)) for j in range(len(signal)))
        transformed.append(complex(real, imag))
    return transformed

# Signal conditioning with red herring operations
def preprocess_signal(raw_data, factor=1.0, apply_clamp=True):
    adjusted = [x * factor for x in raw_data]
    if apply_clamp:
        adjusted = [min(max(x, 0), 100) for x in adjusted]  # Clamp to 0-100 (only relevant for humidity)
    
    # Distracting smoothing with unused window
    smoothed = []
    window_size = 3
    for i in range(len(adjusted)):
        start = max(0, i - window_size + 1)
        end = i + 1
        smoothed.append(sum(adjusted[start:end]) / (end - start))
    
    # This branch is never taken (misleading)
    consistency_check = all(abs(smoothed[i] - smoothed[i+1]) < 5 for i in range(len(smoothed)-1))
    if len(raw_data) > 100:  # Never true
        return frequency_domain_transform(smoothed)
        
    return adjusted  # Actual return

# Composite signal processor (core logic)
def process_signals(temp_data, humid_data, press_data):
    # Real processing begins here
    scaled_temps = preprocess_signal(temp_data, factor=1.8)
    scaled_humid = preprocess_signal(humid_data, factor=1.0)
    scaled_press = [p * 0.001 for p in press_data]  # Convert to kPa
    
    # Generate composite indices using list comprehension and set operations
    high_temp_flags = {i for i, t in enumerate(scaled_temps) if t > 45.0}
    high_humid_flags = {i for i, h in enumerate(scaled_humid) if h > 60}
    unstable_pressure_windows = []
    
    for i in range(2, len(scaled_press)):
        window_var = sum(abs(scaled_press[j] - scaled_press[j-1]) for j in range(i-2, i+1))
        if window_var > 0.005:
            unstable_pressure_windows.append(i)
    
    # Cross-correlation of anomalies
    temp_humid_overlap = high_temp_flags.intersection(high_humid_flags)
    critical_moments = temp_humid_overlap.union(set(unstable_pressure_windows))
    
    # Compute weighted stress index (actual answer contributor)
    base_index = 0.0
    for idx in range(len(scaled_temps)):
        temp_factor = max(0, scaled_temps[idx] - 40.0) / 10.0
        humid_factor = max(0, scaled_humid[idx] - 55) / 10.0
        press_stability = 1.0
        if idx >= 2:
            recent_drift = abs(scaled_press[idx] - scaled_press[idx-1]) + abs(scaled_press[idx-1] - scaled_press[idx-2])
            press_stability = max(0.5, 1.0 - recent_drift * 100)
        
        if idx in critical_moments:
            base_index += (temp_factor * humid_factor * 2.0) * press_stability
        else:
            base_index += (temp_factor + humid_factor) * 0.5 * press_stability
    
    return {
        'index': base_index,
        'anomalies': critical_moments,
        'size_reference': MAX_SENSOR_RANGE,  # Red herring access
        'calibration_trace': CALIBRATION_OFFSET_A + CALIBRATION_OFFSET_B  # Distractor field
    }

# Diagnostic analyzer with early termination possibility (unused)
def quick_diagnostic(data_map):
    if data_map['index'] > 5.0:
        return "CRITICAL"
    elif data_map['index'] > 3.0:
        return "ELEVATED"
    else:
        return "NORMAL"

# Final analysis with tuple unpacking and conditional logic
def analyze_readings(signal_map):
    index_val = signal_map['index']
    anomaly_set = signal_map['anomalies']
    
    # Decoy variables from unused parts
    dummy_ref = signal_map.get('size_reference', 0)
    trace_sum = signal_map.get('calibration_trace', 0)
    temp_debug_log = []
    
    # Simulated historical baseline comparison (irrelevant computation)
    historical_avg = 2.75
    fluctuation_score = abs(index_val - historical_avg) * 10
    stability_ratio = (8 - len(anomaly_set)) / 8
    
    # Real diagnostic logic
    if index_val >= 4.0 and len(anomaly_set) >= 3:
        severity = 9.2
    elif index_val >= 3.0 and len(anomaly_set) >= 2:
        severity = 6.8
    elif index_val >= 2.0:
        severity = 4.1
    else:
        severity = 1.5
    
    # Apply stability correction
    adjusted_severity = severity * stability_ratio
    
    # Final nonlinear transformation (answer determination)
    if adjusted_severity > 5.0:
        final_score = math.log(adjusted_severity * 2.0 + 1) * 3.0
    else:
        final_score = math.sqrt(adjusted_severity ** 2 + 0.25) * 2.0
    
    # Dead code branch (never executes due to data size)
    if len(temp_debug_log) > 1000:
        recovery_estimate = 1.0 / (len(temp_debug_log) * 0.001)
        return recovery_estimate
    
    # Key assignment - target of question
    final_diagnostic = int(final_score * 17) + len(anomaly_set)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution flow
processed_signals = process_signals(temperature_readings, humidity_readings, pressure_readings)
final_diagnostic = analyze_readings(processed_signals)