import math

# Simulated sensor array data from environmental monitoring system
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.1, 23.7]
humidity_readings = [45, 48, 50, 55, 60, 58, 53, 49]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1009, 1011, 1014]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_A = 0.987
CALIBRATION_FACTOR_B = 1.015
REFERENCE_VOLTAGE = 3.3
NOISE_FLOOR_DB = -95.5

# Preprocess function with red herring operations
def preprocess_sensor_data(raw_temps, raw_humid):
    normalized = []
    outlier_count = 0
    for i in range(len(raw_temps)):
        # Real transformation
        temp_scaled = raw_temps[i] * 1.02
        humid_scaled = raw_humid[i] + 2.5
        
        # Combined index (partially relevant)
        comfort_index = (temp_scaled * 0.6) + (humid_scaled * 0.4)
        
        # Dead code path - never used later (distractor)
        if comfort_index > 28.0:
            status_flag = 0x0A
        elif comfort_index < 20.0:
            status_flag = 0x0F
        else:
            status_flag = 0x05  # This is never read
        
        # Only this line matters
        normalized.append(comfort_index)
        
        # Misleading counter (looks important but unused)
        if temp_scaled > 25.5:
            outlier_count += 1
    
    return normalized

# Signal processing with multiple distractions
def process_frequency_bands(raw_pressures):
    fft_simulated = []
    for p in raw_pressures:
        # Simulate frequency domain transform (irrelevant)
        transformed = math.sin(p * 0.01) * math.cos(p * 0.007)
        fft_simulated.append(abs(transformed))
    
    # Sort for no reason (distractor)
    fft_simulated.sort(reverse=True)
    
    # Compute meaningless aggregate (red herring)
    avg_fft = sum(fft_simulated) / len(fft_simulated) if fft_simulated else 0
    
    # This is the only relevant output, disguised
    return [p % 7 for p in raw_pressures]  # Modular arithmetic result

# Main signal processor with set operations (required feature)
def process_signals(temp_data, humid_data, pressure_data):
    # Process temperature and humidity together
    processed_comfort = preprocess_sensor_data(temp_data, humid_data)
    
    # Process pressure separately
    pressure_modular = process_frequency_bands(pressure_data)
    
    # Combine using set logic (key concept)
    unique_mods = set(pressure_modular)
    base_values = {1, 2, 3, 4, 5}
    common_elements = base_values.intersection(unique_mods)
    
    # Distractor: complex-looking but unused calculation
    entropy_estimate = 0
    for x in common_elements:
        prob = pressure_modular.count(x) / len(pressure_modular)
        if prob > 0:
            entropy_estimate -= prob * math.log(prob, 2)
    
    # Critical data transformation chain
    trend_scores = []
    for i in range(1, len(processed_comfort)):
        delta = processed_comfort[i] - processed_comfort[i-1]
        score = int(delta * 10)  # Amplify small changes
        trend_scores.append(score)
    
    # Another decoy structure (unused dictionary)
    diagnostic_map = {
        'stable': {'range': [-2, 2], 'weight': 0.5},
        'warning': {'range': [-5, -3, 3, 5], 'weight': 1.2},
        'critical': {'range': [-10, -6, 6, 10], 'weight': 2.0}
    }
    
    # Actual computation path
    total_trend = sum(trend_scores)
    mod_sum = sum(common_elements)  # From set intersection
    
    # Hidden dependency: bitwise manipulation of modular result
    magic_key = 0
    for m in pressure_modular:
        magic_key ^= (m << 1)  # XOR and shift
    
    # Return tuple with one key component (others are distractions)
    return (processed_comfort, total_trend, mod_sum, magic_key, entropy_estimate)

# Final analysis with conditional logic red herrings
def analyze_readings(signal_tuple):
    comfort_levels, trend_total, mod_total, key_code, entropy = signal_tuple
    
    # Multiple logical checks (many irrelevant)
    has_anomaly = False
    critical_thresholds = []
    
    for cl in comfort_levels:
        if cl > 28.0 or cl < 18.0:
            has_anomaly = True
            critical_thresholds.append(cl)
    
    # Unused short-circuit evaluation (distractor)
    system_status = (len(critical_thresholds) == 0) and (entropy < 1.5) or has_anomaly
    
    # Decoy state machine (dead code)
    state_registry = []
    current_state = 'INIT'
    for i in range(3):
        if i == 0:
            current_state = 'ACQUIRE'
        elif i == 1:
            current_state = 'PROCESS'
        else:
            current_state = 'LOCKED'  # Never used
        state_registry.append(current_state)
    
    # The real computation - multi-step reasoning
    base_score = trend_total * 3
    adjustment = mod_total * 7
    checksum = key_code & 0xFF  # Take last 8 bits
    
    # Final formula combining multiple concepts
    intermediate = base_score + adjustment
    if intermediate < 0:
        final_value = intermediate - checksum
    else:
        final_value = intermediate + checksum
    
    # One last distraction: unused floating point conversion
    final_diagnostic_code = float(final_value)
    
    # ACTUAL ANSWER VARIABLE
    final_diagnostic = final_value + 100  # Key offset
    
    return final_diagnostic

# Execution flow with hidden logic path
processed_signals = process_signals(temperature_readings, humidity_readings, pressure_readings)
final_diagnostic = analyze_readings(processed_signals)
print(f"Target result: {final_diagnostic}")