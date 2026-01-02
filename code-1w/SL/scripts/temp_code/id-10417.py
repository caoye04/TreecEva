from collections import defaultdict, Counter

# Simulated sensor array data with noise and redundant readings
data_stream = [
    ('sensor_1', 15), ('sensor_2', 19), ('sensor_3', 14), ('sensor_1', 17),
    ('sensor_4', 22), ('sensor_2', 20), ('sensor_5', 13), ('sensor_3', 15),
    ('sensor_1', 16), ('sensor_4', 21), ('sensor_5', 14), ('sensor_2', 18)
]

# Irrelevant baseline metadata (distractor)
system_info = {
    'model': 'SA-2X',
    'firmware': '3.1.7',
    'calibration_interval': '90d',
    'location': 'Grid Sector 7'
}

# Misleading preprocessing: appears important but unused in final logic
raw_stats = defaultdict(list)
for sensor, val in data_stream:
    raw_stats[sensor].append(val)

summary_report = {}
for k, v in raw_stats.items():
    summary_report[k] = {
        'count': len(v),
        'peak': max(v),
        'truncated_avg': int(sum(v) / len(v))  # Integer division distractor
    }

# Decoy function that looks relevant but is never called
def analyze_trend(data):
    trend_score = 0
    for readings in data.values():
        for i in range(1, len(readings)):
            if readings[i] > readings[i-1]:
                trend_score += 1
    return trend_score // 2 if trend_score else 0

# Actual signal filtering logic buried in noise
valid_sensors = [s for s, _ in data_stream if s in ['sensor_1', 'sensor_3', 'sensor_5']]
unique_valid = list(set(valid_sensors))
unique_valid.sort(key=lambda x: int(x[-1]))

# Real processing begins here — obscured by prior distractions
aggregated = defaultdict(int)
for sensor, value in data_stream:
    if sensor in unique_valid:
        aggregated[sensor] += value

# Simulated threshold policy (some are red herrings)
threshold_levels = {
    'sensor_1': 45,
    'sensor_2': 50,  # Unused
    'sensor_3': 25,
    'sensor_4': 60,  # Unused
    'sensor_5': 20
}

# Filtering only sensors present in threshold_levels and aggregated
filtered_data = {s: v for s, v in aggregated.items() if s in threshold_levels}

# Secondary decoy: complex string-based validation that does nothing
validation_chain = "".join([k + str(v) for k, v in filtered_data.items()])
checksum_flag = validation_chain.upper().replace("SENSOR", "").isdigit()  # Always False, irrelevant

# Core logic hidden among distractions
def process_readings(readings, thresholds):
    score = 0
    penalty = 0
    
    # Real computation interlaced with noise
    for sid, total in readings.items():
        base_threshold = thresholds[sid]
        diff = total - base_threshold
        
        # Meaningful branching
        if diff >= 0:
            score += abs(diff) * 2
        else:
            penalty += abs(diff)
    
    # Another layer of obfuscation: dead code block
    if checksum_flag:  # Never true
        adjustment = len(validation_chain) % 7
        score += adjustment
    
    # Critical result calculation
    final_score = score - penalty
    
    # Distracting transformation
    temp_result = f"DIAG-{final_score}-STATUS_OK"
    diagnostic_code = sum([ord(c) for c in temp_result if c.isdigit()])  # Sum of digit character codes
    
    # Final answer derived from meaningful logic path
    return final_score + (diagnostic_code % 10)  # Adds small offset based on checksum digits

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold_levels)

# Output result as required
print(f"Result: {final_diagnostic}")