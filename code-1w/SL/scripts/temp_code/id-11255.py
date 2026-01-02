import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.6]
humidity_readings = [45, 48, 50, 55, 60, 62, 58, 53]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1018, 1017, 1015]

# Irrelevant backup logs (distractor data)
backup_logs = ['OK', 'OK', 'ERROR_01', 'OK', 'OK', 'OK', 'WARNING_05', 'OK']
log_status_codes = {"OK": 0, "WARNING_05": 5, "ERROR_01": -1}

# Misleading intermediate transformation (dead path)
def legacy_transform(data):
    return [round(x * 1.02) for x in data if x > 0]

legacy_result = legacy_transform(temperature_readings)  # Unused

# Threshold configuration map (critical for final result)
threshold_map = {
    'temp_high': 25.5,
    'temp_low': 24.0,
    'humidity_alert': 55,
    'pressure_drift': 3
}

# Auxiliary function: not actually used but looks relevant
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

variance_check = calculate_variance(humidity_readings)  # Distractor

# Data normalization function with red herring logic
def normalize_readings(raw_data, base=100):
    min_val, max_val = min(raw_data), max(raw_data)
    range_val = max_val - min_val
    if range_val == 0:
        return [base] * len(raw_data)
    return [base + (x - min_val) / range_val * 50 for x in raw_data]

# Normalize temperature (used)
norm_temp = normalize_readings(temperature_readings, base=100)

# Normalize humidity (used)
norm_humid = normalize_readings(humidity_readings, base=200)

# Spurious sorting operation on pressure (misleading)
sorted_pressure_desc = sorted(pressure_readings, reverse=True)
pressure_changes = [abs(sorted_pressure_desc[i] - sorted_pressure_desc[i+1]) 
                     for i in range(len(sorted_pressure_desc)-1)]

# Real processing begins here
processed_data = []
for i in range(len(temperature_readings)):
    entry = {
        'idx': i,
        't': temperature_readings[i],
        'h': humidity_readings[i],
        'p': pressure_readings[i],
        'norm_t': norm_temp[i],
        'norm_h': norm_humid[i]
    }
    processed_data.append(entry)

# Decoy analysis function
def superficial_diagnostic(data_list):
    high_temp_count = len([d for d in data_list if d['t'] > 25.0])
    return high_temp_count * 100  # Fake metric

superficial_score = superficial_diagnostic(processed_data)  # Red herring

# Real analysis logic with conditional branches and list comprehension
condition_flags = [
    (entry['t'] > threshold_map['temp_high'], 
     entry['h'] > threshold_map['humidity_alert'],
     abs(entry['p'] - 1015) > threshold_map['pressure_drift'])
    for entry in processed_data
]

flag_summary = []
for flags in condition_flags:
    severity = 0
    if flags[0]:  # High temp
        severity += 3
    if flags[1]:  # High humidity
        severity += 2
    if flags[2]:  # Pressure drift
        severity += 1
    flag_summary.append(severity)

# Conditional expression chain (key logic step)
adjusted_severity = []
for i, sev in enumerate(flag_summary):
    if sev >= 4:
        adjusted_severity.append(sev * 2)
    elif sev == 3:
        adjusted_severity.append(sev + 1)
    else:
        adjusted_severity.append(max(sev, 1))

# Final diagnostic computation
baseline = sum(adjusted_severity)
dynamic_weight = math.log(len(processed_data) + 1)  # Always log(9) ~ 2.197

# Secondary adjustment based on pattern recognition
longest_streak = 0
current_streak = 0
for flag_set in condition_flags:
    if flag_set[0] or flag_set[1]:  # Heat/humidity combo
        current_streak += 1
    else:
        longest_streak = max(longest_streak, current_streak)
        current_streak = 0
longest_streak = max(longest_streak, current_streak)

streak_bonus = longest_streak * 5 if longest_streak >= 3 else 0

# Critical assignment
final_diagnostic = int(baseline * dynamic_weight + streak_bonus)

# Print result as required
print(f"Result: {final_diagnostic}")