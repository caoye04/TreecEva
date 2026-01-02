import math

# Simulated agricultural sensor data with noise and redundant fields
temperature_readings = [23.4, 24.1, 22.9, 25.0, 23.8, 24.5, 23.6, 24.3]
humidity_readings = [62, 58, 65, 59, 63, 60, 64, 57]
soil_moisture_raw = [1023, 987, 1045, 962, 1011, 996, 1030, 974]
ph_levels = [6.8, 6.5, 7.0, 6.4, 6.9, 6.6, 7.1, 6.3]

# Irrelevant calibration constants for unused sensors
gps_offset_x = 0.0012
gps_offset_y = -0.0034
elevation_factor = 1.07
pressure_baseline = 1013.25

# Dummy transformation (unused)
def calibrate_sensor(stream, factor=1.0):
    return [x * factor for x in stream]

# Misleading preprocessing path (dead function)
def analyze_growth_trend(data):
    trend_score = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_score += 1.5
        else:
            trend_score -= 0.8
    return trend_score  # Never used

# Distractor: fake normalization (looks important but irrelevant)
normalized_temp = [(t - 20) / 10 for t in temperature_readings]
adjusted_humidity = [(h - 50) / 100 for h in humidity_readings]

# Bit manipulation decoy (simulates low-level processing)
moisture_binary = [bin(x ^ 0b11110000)[2:] for x in soil_moisture_raw]
truncated_codes = [code[:5] if len(code) > 5 else code for code in moisture_binary]

# Unused derived metric
average_ph = sum(ph_levels) / len(ph_levels)
ph_stability = all(abs(ph - average_ph) < 0.5 for ph in ph_levels)

# Real signal extraction: focus on soil moisture trends via slicing and filtering
filtered_moisture = soil_moisture_raw[1:-1]  # Remove edge noise
moisture_diffs = [filtered_moisture[i+1] - filtered_moisture[i] for i in range(len(filtered_moisture)-1)]

# Logical masking to detect drying cycles
is_drying_cycle = [diff < -10 for diff in moisture_diffs]
valid_windows = []
for i in range(len(is_drying_cycle) - 2):
    if is_drying_cycle[i] and not is_drying_cycle[i+1] and is_drying_cycle[i+2]:
        valid_windows.append(i)

# Secondary filter using humidity correlation (only some windows qualify)
correlated_windows = []
for idx in valid_windows:
    hum_window = humidity_readings[idx+2:idx+5]
    if len(hum_window) == 3 and hum_window[0] > hum_window[1] > hum_window[2]:
        correlated_windows.append(idx)

# Data reconstruction via slice-based aggregation
aggregated_slices = []
for win in correlated_windows:
    slice_part = temperature_readings[win:win+3]
    adjusted_slice = [t * (1 + (70 - humidity_readings[win+i]) * 0.001) for i, t in enumerate(slice_part)]
    aggregated_slices.extend(adjusted_slice)

# Core calculation: harmonic mean of processed slices (true logic path)
if aggregated_slices:
    inv_sum = sum(1 / x for x in aggregated_slices)
    harmonic_base = len(aggregated_slices) / inv_sum
else:
    harmonic_base = 20.0

# Apply growth model with conditional boost
if len(correlated_windows) >= 2:
    growth_multiplier = 1.25
else:
    growth_multiplier = 0.9

potential_yield = harmonic_base * growth_multiplier

# Final adjustment using bit count from decoy array (unexpected reuse)
bit_count = sum(bit.count('1') for bit in truncated_codes)
decoy_influence = (bit_count % 7) / 100

# Key statement
final_yield = potential_yield + decoy_influence

# Target result
print(f"Result: {final_yield}")