from collections import defaultdict

# Simulate sensor data with noise and metadata
data_stream = [
    {'type': 'temp', 'value': 23.5, 'status': 'ok'},
    {'type': 'pressure', 'value': 1013, 'status': 'ok'},
    {'type': 'temp', 'value': 24.1, 'status': 'ok'},
    {'type': 'humidity', 'value': 45, 'status': 'warning'},
    {'type': 'temp', 'value': -999, 'status': 'error'},  # invalid reading
    {'type': 'pressure', 'value': 1010, 'status': 'ok'},
    {'type': 'temp', 'value': 22.8, 'status': 'ok'}
]

# Data aggregation structures
temp_readings = []
pressure_readings = []
humidity_readings = []
status_counter = defaultdict(int)

# Noise filter threshold
valid_temp_range = (15, 35)
baseline_pressure = 1013.25

# Process raw data stream
for entry in data_stream:
    status_counter[entry['status']] += 1
    reading_type = entry['type']
    value = entry['value']
    
    # Filter out invalid temperature readings
    if reading_type == 'temp' and value != -999 and valid_temp_range[0] <= value <= valid_temp_range[1]:
        temp_readings.append(value)
    elif reading_type == 'pressure':
        pressure_readings.append(value)
    elif reading_type == 'humidity':
        humidity_readings.append(value)

# Compute rolling average for temperature (relevant)
smoothed_temps = []
for i in range(len(temp_readings)):
    window = temp_readings[max(0, i-1):i+1]
    smoothed_temps.append(sum(window) / len(window))

# Misleading intermediate calculations (distractors)
avg_pressure = sum(pressure_readings) / len(pressure_readings) if pressure_readings else 0
drift_compensation = abs(avg_pressure - baseline_pressure) * 0.5
adjusted_humidity = [h * 1.1 for h in humidity_readings if h > 0]
effective_humidity = sum(adjusted_humidity) / len(adjusted_humidity) if adjusted_humidity else 0

# String-based status analysis (semi-relevant)
status_summary = "".join(sorted(status_counter.keys()))
status_flag = status_summary.upper().replace("OK", "") or "NONE"
flag_value = len(status_flag) * 100

# Redundant data transformation
readings_dict = {
    'temperatures': temp_readings[:],
    'pressures': pressure_readings[:],
    'humidity_levels': humidity_readings[:]
}

# Core logic: quality score based on temperature consistency
variance_numerator = sum((t - (sum(temp_readings)/len(temp_readings)))**2 for t in temp_readings)
temp_variance = variance_numerator / len(temp_readings) if temp_readings else 0
temp_stability_score = 100 - (temp_variance * 10)

# Secondary factor: system reliability based on status logs
error_count = status_counter['error']
warning_count = status_counter['warning']
system_reliability = 100
if error_count > 0:
    system_reliability -= 50
elif warning_count > 0:
    system_reliability -= 20

# Final computation chain
intermediate_score = temp_stability_score * 0.7 + system_reliability * 0.3

# Apply minor correction based on data completeness
completion_ratio = len(temp_readings) / 5.0  # expected at least 5 valid temps
completeness_bonus = min(completion_ratio * 10, 5)

# Irrelevant string processing (distraction)
summary_tag = f"Q{int(intermediate_score)}".zfill(3)
tag_check = summary_tag.endswith('5')
bonus_adjustment = 3 if tag_check else 0

# Key statement
final_score = int(intermediate_score + completeness_bonus + bonus_adjustment)

Result: final_score