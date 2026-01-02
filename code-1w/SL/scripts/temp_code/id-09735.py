def analyze_performance(metrics):
    baseline = 1.0
    adjustment_factor = 0.0
    for val in metrics:
        if val > 0.75:
            adjustment_factor += 0.1
        elif val < 0.25:
            adjustment_factor -= 0.05
    return adjustment_factor

# Irrelevant sensor array (red herring)
sensor_readings = [0.12, 0.88, 0.45, 0.67, 0.91, 0.23]
adjusted_sensors = [x * 1.05 for x in sensor_readings if x < 0.7]  # Unused list comprehension

def process_calibration(data):
    calibrated = []
    offset = 0.01
    for i in range(len(data)):
        if i % 2 == 0:
            calibrated.append(data[i] + offset)
        else:
            calibrated.append(data[i] - offset)
    return [round(x, 2) for x in calibrated]  # Another unused transformation

# Simulated efficiency timeline over 12 hours
hourly_efficiency = [0.68, 0.71, 0.73, 0.77, 0.81, 0.83, 0.80, 0.78, 0.75, 0.74, 0.70, 0.69]

# Distractor: Unrelated subsystem status check
subsystem_status = {'cooling': True, 'pressure': 'nominal', 'flow': 'stable'}
status_code = sum(1 for k in subsystem_status.keys() if 'o' in k)  # Misleading use of generator

# Real computation begins here — heavily masked by noise
filtered_efficiency = [x for x in hourly_efficiency if x >= 0.70]
efficiency_avg = sum(filtered_efficiency) / len(filtered_efficiency)

# Bit manipulation decoy (irrelevant to final result)
hash_key = 0
for val in filtered_efficiency:
    shifted = int(val * 100)
    hash_key ^= (shifted << 2) & 0xFF
    hash_key += (shifted >> 1)

# Conditional expression with red herring logic
mode_flag = 'high' if efficiency_avg > 0.75 else 'low'
scaling_factor = 1.25 if mode_flag == 'high' else 0.85

# Multiple assignment distraction
total_hours, valid_count = len(hourly_efficiency), len(filtered_efficiency)
dropout_rate = (total_hours - valid_count) / total_hours if total_hours > 0 else 0

# Core function using nested logic and list comprehension
def calculate_thermal_rating(eff_list):
    if not eff_list:
        return 0.0
    # Apply non-linear correction via list comprehension
    corrected = [e ** 1.5 for e in eff_list]
    base_score = sum(corrected) / len(corrected)
    
    # Nested conditionals with dummy branches
    if base_score > 1.0:
        adjustment = 0.1 * base_score
    elif base_score < 0.5:
        adjustment = -0.2
    else:
        adjustment = 0.05
    
    # Final rating with rounding and integer division
    raw_rating = (base_score + adjustment) * 1000
    final_rating = int(raw_rating // 1)  # Simulate fixed-point precision
    
    # Dead code path (never executed due to input constraints)
    if False:
        fallback = 0
        for bit in bin(final_rating):
            if bit == '1':
                fallback += 1
        return fallback * 100
        
    return final_rating

# Secondary log processing (looks important but partially irrelevant)
efficiency_log = [round(x * scaling_factor, 3) for x in filtered_efficiency]

# Key statement: what is the value of thermal_capacity here?
thermal_capacity = calculate_thermal_rating(efficiency_log)

# Print required output
print(f"Result: {thermal_capacity}")