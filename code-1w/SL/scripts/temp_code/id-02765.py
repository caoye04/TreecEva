from collections import defaultdict, Counter

# Simulate sensor data from a manufacturing line
temperature_readings = [23.5, 24.1, 24.8, 25.0, 24.9, 25.3, 26.0, 25.7, 25.2, 24.6]
pressure_readings = [98, 99, 101, 102, 103, 104, 103, 102, 100, 99]
vibration_levels = [3, 4, 5, 7, 10, 12, 9, 6, 5, 4]

def preprocess_sensor_data(temp, pressure, vibration):
    # Normalize temperature to base 25C
    normalized_temp = [round(t - 25.0, 2) for t in temp]
    
    # Misleading: calculate pressure differences but don't use them
    pressure_diffs = []
    for i in range(1, len(pressure)):
        pressure_diffs.append(pressure[i] - pressure[i-1])
    avg_pressure_change = sum(pressure_diffs) / len(pressure_diffs) if pressure_diffs else 0
    
    # Track high-vibration events
    high_vibration_threshold = 8
    high_vib_events = []
    for i, v in enumerate(vibration):
        if v >= high_vibration_threshold:
            high_vib_events.append(i)
    
    # Build time-series profile using defaultdict
    profile = defaultdict(dict)
    for i in range(len(temp)):
        profile[i]['temp'] = temp[i]
        profile[i]['norm_temp'] = normalized_temp[i]
        profile[i]['pressure'] = pressure[i]
        profile[i]['vibration'] = vibration[i]
        profile[i]['alert'] = vibration[i] >= high_vibration_threshold
    
    return profile, high_vib_events, avg_pressure_change

processed_data, alerts, unused_trend = preprocess_sensor_data(temperature_readings, pressure_readings, vibration_levels)

# Extract sequences for analysis
valid_periods = []
current_period = []
for i in range(len(processed_data)):
    if processed_data[i]['alert'] == False:
        current_period.append(i)
    else:
        if len(current_period) > 0:
            valid_periods.append(current_period)
            current_period = []
if len(current_period) > 0:
    valid_periods.append(current_period)

# Determine dominant period length
period_lengths = [len(p) for p in valid_periods]
length_counter = Counter(period_lengths)
dominant_length = length_counter.most_common(1)[0][0] if period_lengths else 0

# Compute cumulative metrics over non-alert periods
stable_temp_sum = 0.0
efficient_period_count = 0
for period in valid_periods:
    if len(period) == dominant_length:
        efficient_period_count += 1
        for idx in period:
            stable_temp_sum += processed_data[idx]['temp']

# Distractor: analyze pressure distribution (not used in final score)
pressure_values = [processed_data[t]['pressure'] for t in range(len(processed_data))]
pressure_freq = {}
for p in pressure_values:
    pressure_freq[p] = pressure_freq.get(p, 0) + 1
sorted_pressures = sorted(pressure_freq.items())

# Real computation path
average_stable_temp = stable_temp_sum / efficient_period_count if efficient_period_count > 0 else 0

# Secondary metric: efficiency based on stable operation duration
total_stable_cycles = sum(period_lengths)
max_possible_cycles = len(temperature_readings)
utilization_rate = total_stable_cycles / max_possible_cycles

# Final efficiency calculation
baseline_temp = 24.5
temp_deviation = abs(average_stable_temp - baseline_temp)
temp_penalty = max(0, temp_deviation * 2)

# Efficiency formula combines utilization and temperature stability
efficiency_score = int((utilization_rate * 100) - temp_penalty - (len(alerts) * 3))

# Additional red herring: sort vibration data unnecessarily
decreasing_vib = sorted(vibration_levels, reverse=True)
sum_high_vib = sum([v for v in vibration_levels if v > 8])

# Critical statement
result_code = "A" if efficiency_score > 60 else "B"

# Target result output
print(f"Result: {efficiency_score}")