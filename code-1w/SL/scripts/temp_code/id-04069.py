def analyze_sensor_network():
    # Simulated environmental sensor readings (temperature in Celsius)
    raw_readings = [23.5, 19.0, 25.3, 18.7, 30.1, 27.4, 22.0, 19.5, 26.8, 24.2]
    thresholds = {'min_safe': 20.0, 'max_safe': 28.0}
    
    # Irrelevant transformation: normalize to percentage (not used in final logic)
    max_val = max(raw_readings)
    normalized = [round(100 * x / max_val, 2) for x in raw_readings]  # Distractor
    
    # Track state: count how many times we reset (misleading counters)
    reset_count = 0
    buffer_overflow_sim = 0
    temp_history = []
    
    # Filter readings within safe operating range (core logic step 1)
    valid_range = []
    for i, temp in enumerate(raw_readings):
        if thresholds['min_safe'] <= temp <= thresholds['max_safe']:
            valid_range.append((i, temp))
        else:
            if temp > thresholds['max_safe']:
                buffer_overflow_sim += 1
            reset_count += 1  # Counts out-of-range, but not used later

    # Extract indices and values using enumerate and zip (required Python feature)
    indices, temps = zip(*valid_range) if valid_range else ([], [])
    
    # Compute rolling adjustment factor (semi-relevant computation)
    adjustment_factor = 0.0
    for j in range(1, len(temps)):
        adjustment_factor += abs(temps[j] - temps[j-1])
    adjustment_factor = round(adjustment_factor / len(temps), 2) if temps else 0.0
    
    # Simulate diagnostic flags with bitwise operations (XOR pattern for anomaly detection)
    flags = 0
    for idx, t in enumerate(temps):
        flag_bit = int(t * 10) & 7  # Use lower 3 bits
        flags ^= flag_bit << (idx % 5)  # Spread across bit positions
    
    # Apply smoothing filter (distractor list accumulation)
    smoothed = []
    window_size = 3
    for k in range(len(temps)):
        start = max(0, k - window_size + 1)
        segment = temps[start:k+1]
        smoothed.append(sum(segment) / len(segment))
    
    # Core data for processing: use only 'temps' and derived stats
    baseline = sum(temps) / len(temps) if temps else 0.0
    variance = sum((t - baseline) ** 2 for t in temps) / len(temps) if temps else 0.0
    filtered_data = {"baseline": baseline, "variance": variance, "count": len(temps), "flags": flags}
    
    # Misleading secondary analysis (dead code path - never called)
    def simulate_failure_modes():
        return [x * 1.5 for x in normalized if x > 75]  # Not invoked
    
    # Critical function call
    final_diagnostic = process_readings(filtered_data)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")
    return final_diagnostic


def process_readings(data):
    # Unpack data
    base = data["baseline"]
    var = data["variance"]
    n = data["count"]
    f = data["flags"]
    
    # Diagnostic score calculation (core logic)
    stability_score = 100 - (var * 5)
    size_penalty = 10 if n < 5 else 0
    
    # Bitwise influence: number of set bits modulates sensitivity
    bit_count = bin(f).count('1')
    sensitivity_modifier = 1.0 + (bit_count % 4) * 0.05
    
    # Final diagnostic (only this matters)
    result = round((stability_score - size_penalty) * sensitivity_modifier, 2)
    
    # Additional distraction: unused correction based on prime check
    def is_prime(x):
        if x < 2: return False
        for i in range(2, int(x**0.5)+1):
            if x % i == 0: return False
        return True
    
    # This variable is computed but irrelevant
    phantom_correction = 2.5 if is_prime(n + 10) else 0.0  # Dead computation
    
    return result

# Execute and capture result
analyze_sensor_network()