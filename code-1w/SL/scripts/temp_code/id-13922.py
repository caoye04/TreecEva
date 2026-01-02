from collections import defaultdict
import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 20.4, 21.9]
humidity_readings = [45, 52, 58, 61, 47, 55, 60, 50]
pressure_readings = [1013, 1015, 1012, 1018, 1010, 1014, 1016, 1011]

# Irrelevant backup data (distractor)
backup_temperatures = [23.4, 24.0, 19.7, 21.8]  # Unused in final calculation
legacy_humidity = {"site_A": 46, "site_B": 54}  # Dead code path

# Preprocessing: Normalize temperature using z-score
mean_temp = sum(temperature_readings) / len(temperature_readings)
std_temp = (sum((x - mean_temp) ** 2 for x in temperature_readings) / len(temperature_readings)) ** 0.5
normalized_temps = [(t - mean_temp) / std_temp for t in temperature_readings]

# Humidity mapping to categorical risk (distraction logic)
humidity_risk = {}
for h in humidity_readings:
    if h < 50:
        humidity_risk[h] = 'low'
    elif h < 57:
        humidity_risk[h] = 'moderate'
    else:
        humidity_risk[h] = 'high'

# Pressure trend analysis (misleading intermediate)
pressure_deltas = [pressure_readings[i+1] - pressure_readings[i] for i in range(len(pressure_readings)-1)]
pressure_trend = 'stable'
if any(d > 3 for d in pressure_deltas):
    pressure_trend = 'rising'
elif any(d < -3 for d in pressure_deltas):
    pressure_trend = 'falling'

# Create composite data structure (core relevant step)
sensor_data = defaultdict(dict)
for i in range(len(temperature_readings)):
    sensor_data[i]['temp'] = temperature_readings[i]
    sensor_data[i]['humidity'] = humidity_readings[i]
    sensor_data[i]['pressure'] = pressure_readings[i]

# Normalization function with bit manipulation red herring
def normalize_value(val, base=10):
    """Dummy normalization with irrelevant bitwise ops"""
    shifted = val * (1 << 2)  # Multiply by 4, never used
    masked = shifted & 0xFF   # Bitwise mask distraction
    return round(val / base, 3)

# Apply normalization (only temp matters)
normalized_data = []
for i in sensor_data:
    norm_temp = normalize_value(sensor_data[i]['temp'], base=25)
    norm_humid = (sensor_data[i]['humidity'] - 40) / 20  # Computed but unused
    normalized_data.append(norm_temp)

# Threshold logic with string processing distraction
defect_codes = ['ERR01', 'WARN03', 'INFO05']
cleaned_codes = [code.lower().replace('0', 'O') for code in defect_codes]  # Distractor list

threshold_map = {}
for idx, nt in enumerate(normalized_data):
    if nt < 0.8:
        threshold_map[idx] = 'green'
    elif nt < 1.0:
        threshold_map[idx] = 'yellow'
    else:
        threshold_map[idx] = 'red'

# Core diagnostic processor
state_counter = defaultdict(int)
for state in threshold_map.values():
    state_counter[state] += 1

# Auxiliary confusion matrix (dead computation)
confusion_matrix = [
    [state_counter['green'], state_counter['yellow']],
    [state_counter['red'], 0]
]
determinant = confusion_matrix[0][0] * confusion_matrix[1][1] - confusion_matrix[0][1] * confusion_matrix[1][0]  # Unused

# Final processing with conditional expression and dictionary lookup
def process_readings(norm_vals, thresh_map):
    raw_sum = sum(norm_vals)
    penalty = 0
    for k, v in thresh_map.items():
        if v == 'red':
            penalty += 0.25
        elif v == 'yellow':
            penalty += 0.1
    # Actual answer derived here
    adjustment = math.log(penalty + 1) if penalty > 0 else 0
    base_score = raw_sum * 100
    # Final diagnostic combines arithmetic, logic, and math
    result = int(base_score - (adjustment * 1000))
    
    # Decoy assignments (never used)
    _ = [result * (2 ** i) for i in range(3)]  # List comprehension distraction
    temp_cache = {'final': result, 'timestamp': '2023-09-15'}  # Unused dict
    
    return result

# Key execution point
final_diagnostic = process_readings(normalized_data, threshold_map)
print(f"Target result: {final_diagnostic}")