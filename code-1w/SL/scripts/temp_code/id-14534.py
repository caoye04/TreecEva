import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 27.3, 26.0, 22.7, 20.9, 28.1, 25.4]
humidity_readings = [45, 48, 55, 43, 39, 41, 50, 52, 38, 44]
pressure_readings = [1013, 1015, 1010, 1020, 1018, 1016, 1012, 1014, 1009, 1021]

# Irrelevant auxiliary arrays (distractors)
sound_levels = [65, 63, 70, 68, 72, 66, 69, 71, 67, 64]
lux_values = [12000, 11500, 13000, 12800, 11000, 12400, 12600, 11800, 13200, 12200]

# Calibration profiles (only one is actually used)
calibration_factor = 0.987
backup_calibration = 1.013
legacy_scaling = 0.991

# Data alignment via zip (relevant)
synchronized_data = list(zip(temperature_readings, humidity_readings, pressure_readings))

# Misleading transformation chain (partly dead code)
normalized_temps = [round((t - 20) / 10, 3) for t in temperature_readings]
weighted_humidity = [(h / 100) ** 0.5 for h in humidity_readings]  # unused

# Filtering criteria with nested logic
valid_range = lambda x: 20 <= x[0] <= 28 and 40 <= x[1] <= 50
filtered_pairs = list(filter(valid_range, synchronized_data))

# Extract filtered temperatures for secondary check (red herring)
filtered_temps = [pair[0] for pair in filtered_pairs]
spike_detected = any(abs(filtered_temps[i] - filtered_temps[i-1]) > 2.0 for i in range(1, len(filtered_temps)))

# Decoy function that looks important but isn't called
def analyze_trend(data_sequence):
    differences = [data_sequence[i] - data_sequence[i-1] for i in range(1, len(data_sequence))]
    return sum(differences) / len(differences)

# Real processing begins here
index_mapping = {i: val for i, val in enumerate([x[2] for x in filtered_pairs])}
shifted_pressure = [round(p * calibration_factor, 2) for p in index_mapping.values()]

# Use of enumerate and itertools.chain to obscure actual computation path
enumerated_shifted = list(enumerate(shifted_pressure))
flat_chain = list(itertools.chain.from_iterable([(i, v) for i, v in enumerated_shifted]))

# Actual key transformation (hidden among distractors)
effective_mean = sum(flat_chain[1::2]) / len(flat_chain[1::2])  # averages only values, skips indices

def process_readings(data_chunk, factor):
    base_value = 0
    for temp, hum, pres in data_chunk:
        # Complex but deterministic transformation
        adjusted_pres = pres * factor
        contribution = (temp * 0.3) + (hum * 0.2) + (adjusted_pres * 0.001)
        base_value += contribution
    return round(base_value / len(data_chunk), 4)

# Critical statement
final_diagnostic = process_readings(filtered_pairs, calibration_factor)

# Secondary irrelevant diagnostics
anomaly_score = sum(1 for t in temperature_readings if t > 25) * len(humidity_readings)
consistency_metric = abs(effective_mean - final_diagnostic)  # misleading correlation

# Output the target result
print(f"Result: {final_diagnostic}")