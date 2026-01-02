import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.4, 19.5, 27.2, 32.1, 15.6, 24.3, 35.0, 29.8, 21.0, 18.2]
humidity_readings = [45, 60, 52, 38, 67, 50, 33, 41, 58, 63]
pressure_readings = [1013, 1009, 1015, 1020, 1005, 1012, 1025, 1018, 1010, 1007]

# Irrelevant auxiliary data (distractor)
event_log = ['start', 'calibration', 'sync', 'error_reset', 'resume']
status_flags = {'active': True, 'debug': False, 'maintenance': None}

# Mapping conditions to severity levels (used later)
severity_scale = {
    'low': 1,
    'moderate': 2,
    'high': 3,
    'critical': 4
}

# Thresholds for anomaly detection (key input)
threshold_map = {
    'temp_high': 30.0,
    'temp_low': 20.0,
    'humidity_extreme': 60,
    'pressure_stable_range': (1008, 1020)
}

# Decoy function – looks important but unused in critical path
def analyze_trend(data):
    if len(data) < 2:
        return 0
    trend = sum(1 for i in range(1, len(data)) if data[i] > data[i-1])
    return trend / (len(data) - 1)

# Another red herring: complex transformation with no downstream effect
decoded_signals = []
for val in pressure_readings:
    binary_rep = bin(val)[2:]
    ones_count = binary_rep.count('1')
    shifted = val >> 2
    decoded_signals.append(shifted + ones_count)

# Data aggregation with slicing and filtering (relevant)
combined_readings = []
for i in range(len(temperature_readings)):
    record = {
        'idx': i,
        'temp': temperature_readings[i],
        'humid': humidity_readings[i],
        'press': pressure_readings[i]
    }
    combined_readings.append(record)

# Filter based on multiple conditions (logical branching)
filtered_data = []
for entry in combined_readings:
    temp_cond = entry['temp'] > threshold_map['temp_high'] or entry['temp'] < threshold_map['temp_low']
    humid_cond = entry['humid'] > threshold_map['humidity_extreme']
    press_min, press_max = threshold_map['pressure_stable_range']
    press_cond = not (press_min <= entry['press'] <= press_max)
    
    if temp_cond or humid_cond or press_cond:
        filtered_data.append(entry)

# String-based identifier generation (distractor)
stations = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
station_codes = [s.lower() + '_sensor' for s in stations]
code_parts = [sc[1:6] for sc in station_codes]  # slicing used
lookup_table = {i: code_parts[i] for i in range(len(code_parts))}

# Unused dictionary operation (dead path)
consolidated_stats = {}
if filtered_data:
    consolidated_stats['max_temp'] = max(entry['temp'] for entry in filtered_data)
    consolidated_stats['min_humid'] = min(entry['humid'] for entry in filtered_data)

# Core processing function (used)
def process_readings(anomalies, thresholds):
    score = 0
    temp_high_ref = thresholds['temp_high']
    temp_low_ref = thresholds['temp_low']
    
    for anomaly in anomalies:
        temp = anomaly['temp']
        humid = anomaly['humid']
        press = anomaly['press']
        
        # Multi-condition scoring logic
        if temp > temp_high_ref:
            excess = temp - temp_high_ref
            score += int(excess * 2)
        elif temp < temp_low_ref:
            deficit = temp_low_ref - temp
            score += int(deficit * 1.5)
        
        if humid > thresholds['humidity_extreme']:
            over_humid = humid - thresholds['humidity_extreme']
            score += over_humid // 2
        
        press_min, press_max = thresholds['pressure_stable_range']
        if press < press_min:
            score += (press_min - press) // 5
        elif press > press_max:
            score += (press - press_max) // 5
        
        # Bit manipulation as noise (partially relevant)
        press_bits = bin(press)[-3:]
        bit_value = int(press_bits, 2)
        if bit_value > 4:
            score += 1  # minor influence
    
    # Final adjustment using string method (irrelevant but plausible)
    tag = 'diagnostic_x7'
    digit_sum = sum(int(c) for c in tag if c.isdigit())
    score -= digit_sum  # subtracts 7
    
    return score

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result for evaluation
print(f"Target result: {final_diagnostic}")