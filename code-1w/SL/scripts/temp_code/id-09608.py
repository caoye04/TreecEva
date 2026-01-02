import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 18.2, 20.9, 24.4, 23.8]
humidity_readings = [45, 52, 61, 48, 55, 67, 70, 50, 53, 58]
pressure_readings = [1013, 1015, 1010, 1008, 1017, 1020, 1005, 1012, 1014, 1018]

# Irrelevant auxiliary data (distractor)
sound_levels = [32, 45, 50, 38, 41, 65, 72, 36, 40, 55]
lux_values = [12000, 25000, 8000, 15000, 30000, 35000, 6000, 18000, 22000, 28000]

# Misleading preprocessing path (dead code)
def normalize_signal(data):
    max_val = max(data)
    return [x / max_val for x in data]

scaled_sound = normalize_signal(sound_levels)  # Unused
scaled_light = normalize_signal(lux_values)   # Unused

# Core processing begins
status_flags = []
for i in range(len(temperature_readings)):
    temp = temperature_readings[i]
    humid = humidity_readings[i]
    press = pressure_readings[i]
    
    # Conditional logic with nesting (3 levels deep)
    if temp > 24.0:
        if humid > 55:
            if press < 1015:
                status_flags.append(3)
            else:
                status_flags.append(2)
        else:
            if temp > 25.0:
                status_flags.append(4)
            else:
                status_flags.append(1)
    else:
        if humid < 50:
            if press > 1015:
                status_flags.append(-1)
            else:
                status_flags.append(0)
        else:
            status_flags.append(0)

# Bit manipulation decoy (irrelevant)
flag_summary = 0
for flag in status_flags:
    flag_summary ^= flag  # XOR accumulation - looks important but unused later
    flag_summary = (flag_summary << 1) & 0xFF  # Shift and mask - red herring

# Real data transformation starts here
zipped_data = list(zip(temperature_readings, humidity_readings, pressure_readings, status_flags))
filtered_data = [row for row in zipped_data if row[0] >= 20.0 and row[1] >= 45]

# Decoy aggregation functions (unused)
def calculate_averages(data_list):
    n = len(data_list)
    return [sum(col)/n for col in zip(*data_list)]

def detect_outliers(values, threshold=1.5):
    q1, q3 = sorted(values)[n//4], sorted(values)[3*n//4]
    iqr = q3 - q1
    return [v for v in values if not (q1 - threshold*iqr <= v <= q3 + threshold*iqr)]

# Threshold map based on empirical models (actually used)
threshold_map = {
    'temp_high': 24.5,
    'humid_high': 58,
    'press_stable': (1010, 1018)
}

# Conditional generator using itertools (relevant)
state_combinations = list(itertools.product(['alert', 'normal'], ['stable', 'fluctuating']))
mode_transitions = dict(zip(range(len(state_combinations)), state_combinations))

# Main processing function with multiple concepts
def process_readings(data, thresholds):
    alert_count = 0
    stable_pressure_events = 0
    diagnostic_score = 0
    
    for reading in data:
        temp, humid, press, flag = reading
        
        # Boolean logic chain with short-circuiting
        is_critical = (temp > thresholds['temp_high']) and (humid > thresholds['humid_high'])
        pressure_in_range = (press >= thresholds['press_stable'][0]) and (press <= thresholds['press_stable'][1])
        
        # Modular arithmetic decoy
        cycle_index = (int(temp) + int(humid)) % 7  # Computed but mostly unused
        
        # Real logic
        if is_critical:
            alert_count += 1
            # Only add score if pressure also unstable
            if not pressure_in_range:
                diagnostic_score += 17
        
        if pressure_in_range:
            stable_pressure_events += 1
            # Bonus points only in specific mode (from itertools-generated transitions)
            mode_key = (temp + humid) // 10
            if mode_key in mode_transitions and 'fluctuating' in mode_transitions[mode_key]:
                diagnostic_score += 3
        
        # Dead branch (never reached due to prior filtering)
        if temp < 10.0:
            diagnostic_score -= 100  # This never executes
    
    # Final computation: mix of counts and logic
    final_value = (alert_count * 23) + (stable_pressure_events * 2) + diagnostic_score
    
    # Additional misdirection
    checksum = sum(len(str(val)) for val in [alert_count, stable_pressure_events, diagnostic_score])
    # But checksum is not used in result
    
    return final_value

# Execute critical statement
target_threshold = {'temp_high': 24.5, 'humid_high': 58, 'press_stable': (1010, 1018)}
final_diagnostic = process_readings(filtered_data, threshold_map)

print(f"Target result: {final_diagnostic}")