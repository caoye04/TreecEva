import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 19.0, 25.8, 21.3, 18.7, 26.1, 20.9, 24.4, 22.6, 19.8]
humidity_readings = [45, 52, 48, 60, 55, 43, 58, 50, 53, 57]
pressure_readings = [1013, 1015, 1011, 1016, 1012, 1014, 1010, 1013, 1015, 1012]

# Irrelevant auxiliary data (distractor)
sound_levels = [32, 45, 38, 50, 42, 36, 48, 41, 39, 44]  # Decoy sensor data
light_intensity = [800, 950, 870, 1020, 930, 820, 980, 890, 910, 960]  # Unused

# Data transformation pipeline with red herrings
smoothed_temps = [round((t + temperature_readings[i-1] + temperature_readings[(i+1) % len(temperature_readings)]) / 3, 2) 
                   for i, t in enumerate(temperature_readings)]

# Misleading intermediate calculation (dead path)
avg_sound_pressure = sum(sound_levels) / len(sound_levels) if sound_levels else 0
unused_feature = ''.join(chr(int(65 + (l // 10) % 26)) for l in light_intensity[:5])

# Conditional filtering based on dynamic thresholds
operational_thresholds = {
    'temp_low': 20.0,
    'temp_high': 25.0,
    'humidity_range': (45, 58)
}

# Distractor: unused complex structure
diagnostic_matrix = [[math.sin(i * j * 0.1) for j in range(5)] for i in range(5)]

# Real processing begins here — non-obvious due to noise
valid_indices = []
for i in range(len(temperature_readings)):
    temp_ok = operational_thresholds['temp_low'] <= temperature_readings[i] <= operational_thresholds['temp_high']
    humid_ok = operational_thresholds['humidity_range'][0] <= humidity_readings[i] <= operational_thresholds['humidity_range'][1]
    if temp_ok and humid_ok:
        valid_indices.append(i)

filtered_data = [(temperature_readings[i], humidity_readings[i], pressure_readings[i]) for i in valid_indices]

# Threshold map includes decoy keys to mislead
threshold_map = {
    'critical_temp': 25.5,
    'warning_humid': 60,
    'ignored_param_x': 1234,  # Red herring
    'decoy_flag': True,         # Meaningless flag
    'scale_factor': 1.75       # Not used in final logic
}

# Core analysis function with lambda and slicing
analyze_readings = lambda data, config: (
    sum(
        int(tr * 10) + (hr // 2) - (pr // 100)  # Composite diagnostic score
        for tr, hr, pr in data[-5:]  # Only last 5 valid entries matter
    ) * int(config.get('critical_temp') < 26)  # Condition disables multiplier if false
)

# Secondary irrelevant transformation (distractor)
compressed = list(map(lambda x: round(x[0] * math.log(x[1] + 1), 1), filtered_data))

# Key statement containing the answer
temp_snapshot = smoothed_temps[::2]  # Unused slice
final_diagnostic = analyze_readings(filtered_data, threshold_map)

# Output the target result
print(f"Target result: {final_diagnostic}")