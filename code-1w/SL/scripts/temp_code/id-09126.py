def transform_sequence(seq, factor):
    """Irrelevant transformation function (dead code path)"""
    return [x * factor + 2 for x in seq if x % 3 != 0]

# Simulated sensor readings from multiple environmental sources
temperature_readings = [23.4, 25.1, 22.8, 26.5, 30.2, 28.7, 24.3, 27.0]
humidity_readings = [45, 48, 55, 60, 62, 58, 53, 49]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1009, 1011, 1014]

# Decoy data structures with misleading significance
aggregated_metrics = {
    'avg_temp': sum(temperature_readings) / len(temperature_readings),
    'max_humidity': max(humidity_readings),
    'trend_pressure': pressure_readings[-1] - pressure_readings[0],
    'volume_factor': 3.14159,
    'scaling_constant': 2.71828
}

# Real processing begins here — subtle due to surrounding noise
status_flags = []
for temp in temperature_readings:
    if temp < 24.0:
        status_flags.append('LOW')
    elif temp > 27.0:
        status_flags.append('HIGH')
    else:
        status_flags.append('NORMAL')

# Character analysis on flag labels (irrelevant but plausible)
char_count = {}
for flag in status_flags:
    for char in flag:
        char_count[char] = char_count.get(char, 0) + 1

# Unused recursive red herring
def calculate_entropy(data, depth=0):
    if depth >= 3 or len(data) == 1:
        return 0.0
    mid = len(data) // 2
    return calculate_entropy(data[:mid], depth+1) + calculate_entropy(data[mid:], depth+1)

# Actual relevant data preparation
processed_data = []
for i in range(len(temperature_readings)):
    entry = {
        'idx': i,
        'temp': temperature_readings[i],
        'humid': humidity_readings[i],
        'press': pressure_readings[i],
        'status': status_flags[i]
    }
    processed_data.append(entry)

# Threshold logic map — key to final computation
threshold_map = {
    'TEMP_HIGH': 27.5,
    'TEMP_LOW': 24.0,
    'HUMID_MAX': 57,
    'PRESS_DELTA': -3
}

# Diagnostic analyzer that combines arithmetic, boolean, and dictionary logic
def analyze_readings(data, thresholds):
    count_abnormal = 0
    cumulative_score = 0.0
    recent_pressures = [entry['press'] for entry in data]
    pressure_trend = recent_pressures[-1] - recent_pressures[0]

    # Irrelevant nested loop (looks important)
    for entry in data:
        for k in ['idx', 'temp']:
            _ = entry[k]  # dummy access

    # Core logic hidden among distractions
    for record in data:
        temp = record['temp']
        humid = record['humid']
        status = record['status']

        # Logical conditions with short-circuit evaluation
        if temp > thresholds['TEMP_HIGH'] and humid > thresholds['HUMID_MAX']:
            count_abnormal += 1
            cumulative_score += temp * 1.5
        elif temp < thresholds['TEMP_LOW'] or humid < 40:
            cumulative_score += temp * 0.8
        else:
            cumulative_score += temp

        # Bitwise red herring — looks like state encoding
        flag_code = 0
        if status == 'LOW':
            flag_code |= 1
        if temp > 30:
            flag_code |= 4
        if humid > 60:
            flag_code |= 2

    # Final computation uses only cumulative_score, others are decoys
    adjustment = 0
    if pressure_trend <= thresholds['PRESS_DELTA']:
        adjustment = -50
    else:
        adjustment = 25

    result = int(cumulative_score) + adjustment  # Final deterministic integer

    # Dead return paths
    if result < 0:
        return 0
    if result > 1000:
        return 999

    return result

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output must be printed exactly once
print(f"Target result: {final_diagnostic}")