import itertools

# Simulated sensor array data from environmental monitoring system
temperature_readings = [23.4, 24.1, 22.8, 25.6, 26.7, 24.3, 23.9]
humidity_readings = [45, 48, 50, 55, 60, 53, 49]
pressure_readings = [1013, 1015, 1012, 1008, 1005, 1007, 1010]

# Irrelevant auxiliary data (distractor)
sound_levels = [32, 35, 40, 38, 36, 34, 33]
lux_values = [12000, 13000, 12500, 14000, 13800, 13200, 12700]

# Data alignment and preprocessing
timestamps = list(range(len(temperature_readings)))
reading_pairs = list(zip(timestamps, temperature_readings, humidity_readings))

# Compute baseline trends (partially relevant)
temp_trend = sum(t for t in temperature_readings) / len(temperature_readings)
humi_trend = sum(h for h in humidity_readings) / len(humidity_readings)

# Anomaly detection via rolling window (core logic begins)
anomalies = []
for i in range(2, len(temperature_readings)):
    window_avg = (temperature_readings[i-2] + temperature_readings[i-1] + temperature_readings[i]) / 3
    if abs(temperature_readings[i] - window_avg) > 1.5:
        anomalies.append((i, temperature_readings[i]))

# Bit manipulation for error code simulation (red herring)
error_code = 0
for idx, val in enumerate(sound_levels):
    error_code ^= (val << 1) | (idx & 1)
error_code = error_code & 0xFF  # Mask to 8 bits

# Spurious correlation attempt between unrelated metrics (distractor)
correlation_candidate = 0
for s, l in zip(lux_values, sound_levels):
    correlation_candidate += (s // 100) % 10 == (l % 10)

# Primary diagnostic computation chain
baseline_stress = 0
for temp, humi in zip(temperature_readings, humidity_readings):
    stress_index = (temp - 20) * (humi / 100)
    if stress_index > 1.5:
        baseline_stress += stress_index

# Advanced pattern matching using itertools (relevant)
triplet_combinations = list(itertools.combinations([t for t in pressure_readings if t < 1010], 3))
pressure_variance = sum(abs(c[2] - c[0]) for c in triplet_combinations) if triplet_combinations else 0

# Decoy function that is defined but not used (dead code path)
def calculate_wind_chill(temp, wind):
    return 13.12 + 0.6215*temp - 11.37*(wind**0.16) + 0.3965*temp*(wind**0.16)

# Unused intermediate transformation (distractor)
normalized_data = [round((x - min(pressure_readings)) / (max(pressure_readings) - min(pressure_readings)), 3) 
                   for x in pressure_readings]

# Critical diagnostic flags
aggregate_score = int(baseline_stress * 10) + (pressure_variance // 10)
anomaly_count = len(anomalies)
anomaly_flag = 1 if anomaly_count > 2 else 0

correction_factor = 0
# Conditional correction based on bit count in timestamp indices (misleading but computed)
for ts in timestamps:
    bit_count = bin(ts).count('1')
    if bit_count % 3 == 0:
        correction_factor += bit_count

# Key statement with final computation
correction_factor = max(correction_factor, 5)
final_diagnostic = aggregate_score + anomaly_flag * correction_factor

# Spurious output masking real result (distractor)
print(f"System status: NOMINAL (code={error_code})")
print(f"Data points processed: {len(reading_pairs)}")

# Actual target output
Result: {final_diagnostic}