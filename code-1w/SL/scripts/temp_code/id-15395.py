def preprocess_telemetry(raw_data):
    # Irrelevant transformation: normalizes signal strength (not used in final result)
    normalized = [max(0, min(100, x + 5)) for x in raw_data]
    return [x * 0.9 for x in normalized]


def detect_anomalies(data_stream):
    # Red herring function: detects spikes but result is unused
    anomalies = []
    for i in range(1, len(data_stream) - 1):
        if data_stream[i] > data_stream[i-1] and data_stream[i] > data_stream[i+1]:
            anomalies.append(i)
    return anomalies


def compute_health_score(metrics):
    # Distractor computation: looks important but not part of final logic
    base = sum(metrics) / len(metrics)
    penalty = 0
    for val in metrics:
        if val < 30:
            penalty += 10
    return max(0, base - penalty)


def decode_fault_signature(code_list):
    # Meaningless decoding of fault codes (unused path)
    decoded = {}
    for code in code_list:
        decoded[code] = f"ERR_{hex(code)[2:].upper()}"
    return decoded


def analyze_system_state(log, faults):
    # Core relevant logic buried among distractions
    
    # Real processing begins here
    filtered_log = log[::2]  # Slicing: take every second reading
    
    # Track state transitions using dictionary
    state_counter = {'stable': 0, 'warning': 0, 'critical': 0}
    
    for reading in filtered_log:
        if reading < 40:
            state_counter['critical'] += 1
        elif reading < 70:
            state_counter['warning'] += 1
        else:
            state_counter['stable'] += 1
    
    # Complex conditional chain with interdependent logic
    primary_factor = 0
    if state_counter['critical'] > 0:
        primary_factor = -500
        temp_adjust = state_counter['warning'] * 15
        if temp_adjust > 100:
            primary_factor -= 80  # Additional penalty
    else:
        if state_counter['stable'] >= 3:
            primary_factor = 200 + state_counter['stable'] * 25
        else:
            primary_factor = 100
    
    secondary_factor = 0
    if len(faults) % 2 == 1:
        secondary_factor = len(faults) * 12
    else:
        secondary_factor = -len(faults) * 7
    
    # Final calculation combines multiple concepts
    intermediate = primary_factor + secondary_factor
    
    # Bit manipulation red herring (looks complex but irrelevant)
    bit_fiddle = 0
    for i in range(5):
        bit_fiddle ^= (intermediate >> i) & 1
    
    # Actual answer determined here
    final_diagnostic = abs(intermediate) + state_counter['warning']
    
    # Dead code path: never executed due to fixed condition
    if False:
        fallback = sum(filtered_log) // len(filtered_log)
        final_diagnostic = fallback * 2
    
    return final_diagnostic

# Simulated input data
telemetry_readings = [85, 32, 77, 29, 61, 45, 88, 30, 73, 28]
active_fault_codes = [101, 102, 103, 104]

# Unused preprocessing steps (distractors)
processed_signal = preprocess_telemetry(telemetry_readings)
anomaly_positions = detect_anomalies(telemetry_readings)
system_health = compute_health_score(telemetry_readings)
decoded_errors = decode_fault_signature(active_fault_codes)

# Key execution point
final_diagnostic = analyze_system_state(telemetry_readings, active_fault_codes)

# Output result as required
print(f"Result: {final_diagnostic}")