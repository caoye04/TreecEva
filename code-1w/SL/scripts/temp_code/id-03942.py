def calculate_thermal_capacity(log_data):
    base_factor = 17.3
    adjustment = 0.89
    
    # Process sensor readings with string-based diagnostics
    valid_readings = [x for x in log_data if isinstance(x, (int, float)) and x > 0]
    status_messages = ['OK', 'CALIBRATE', 'ERROR', 'OK', 'OK']
    ok_count = len([s for s in status_messages if s == 'OK'])

    # Irrelevant diagnostic computation (distractor)
    avg_status_code = sum(ord(s[0]) for s in status_messages) / len(status_messages)

    # Core calculation
    raw_capacity = sum(valid_readings) * base_factor
    
    # Apply efficiency adjustments
    modifier = 1.0
    if len(valid_readings) > 3:
        modifier *= 0.95
    if ok_count >= 3:
        modifier *= 1.05

    # Secondary adjustment using string method on numeric converted data (mixed paradigm)
    str_capacity = str(raw_capacity)
    digit_sum = sum(int(c) for c in str_capacity if c.isdigit())
    checksum_adjustment = digit_sum % 7 / 100
    
    final_capacity = raw_capacity * modifier + checksum_adjustment
    
    return round(final_capacity, 4)

# Simulated system diagnostics
voltage_trace = [12.1, 13.5, 11.9, 14.2, 13.0]
efficiency_flags = [True, False, True, True, True]
sensor_temperatures = [-5, 23, 0, 18, 41]

# Generate efficiency log with mixed types (real and string markers)
efficiency_log = []
for i, v in enumerate(voltage_trace):
    if efficiency_flags[i]:
        efficiency_log.append(v * 1.05)
    else:
        efficiency_log.append('NULL')

# Dead code path - never executed but adds cognitive load
if __debug__:
    debug_snapshot = voltage_trace[:]
    temp_checksum = sum(debug_snapshot) % 1000

# Key state variable influenced by complex logic chain
thermal_capacity = calculate_thermal_capacity(efficiency_log)

# Print result as required
print(f"Result: {thermal_capacity}")