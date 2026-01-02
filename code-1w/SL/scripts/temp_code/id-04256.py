import itertools

# Simulated sensor readings from multiple radar arrays
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.0, 23.7]
humidity_readings = [45, 47, 50, 44, 46, 51, 49, 48]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017, 1013]
radiation_levels = [0.12, 0.15, 0.11, 0.13, 0.16, 0.10, 0.14, 0.12]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.05
CALIBRATION_OFFSET_B = -0.03
REFERENCE_VOLTAGE = 3.3
MAX_BUFFER_SIZE = 1024

# Misleading intermediate processing (dead path)
def legacy_calibrate(data):
    return [x * 1.02 + 0.5 for x in data]  # Unused function

# Another decoy transformation
fake_checksum = sum([int(x * 10) for x in temperature_readings[:3]]) ^ 0xFF

# Real processing begins here
combined = list(zip(temperature_readings, humidity_readings, pressure_readings, radiation_levels))

# Filter based on safety threshold: radiation < 0.13 and temp > 23.0
filtered_sensors = []
for t, h, p, r in combined:
    if r < 0.13 and t > 23.0:
        filtered_sensors.append((t, h, p, r))

# Extract only temperature and humidity for next stage
filtered_readings = [item[:2] for item in filtered_sensors]

# Decoy statistical calculation (irrelevant)
mean_humidity = sum(h for _, h in filtered_readings) / len(filtered_readings) if filtered_readings else 0
variance_proxy = sum((h - mean_humidity) ** 2 for _, h in filtered_readings) / len(filtered_readings) if filtered_readings else 0

# Auxiliary string-based identifier generation (mixed paradigm)
diagnostic_tags = ['RAD_A', 'RAD_B', 'RAD_C', 'RAD_D']
status_log = ""
for i, (temp, hum) in enumerate(filtered_readings):
    code = diagnostic_tags[i % len(diagnostic_tags)]
    flag = "NORM" if temp < 25.0 else "HIGH"
    status_log += f"{code}:{flag}-"  # String accumulation with delimiter

# Trim trailing dash
status_log = status_log.rstrip('-')

# Use of string method and enumeration (required feature)
log_entries = status_log.split('-')
enumerated_diagnostics = list(enumerate(log_entries, start=1))

# Core logic disguised among distractions
buffer = []
for idx, (temp, hum) in enumerate(filtered_readings):
    # Complex conditional with bitwise twist
    if (idx + 1) & 1:  # Only odd positions (1-indexed)
        adjusted_temp = temp * (1 + (hum / 1000))
        buffer.append(adjusted_temp)

# Secondary filter based on transformed value
refined = [val for val in buffer if val > 24.0]

# Real answer derivation hidden in data transformation chain
def process_radar_data(data):
    base = 100
    for i, (t, h) in enumerate(data):
        contribution = (t - 23) * (h / 10) * (0.95 ** i)  # Exponential decay factor
        base += contribution
    return int(base)  # Final score as integer

# Critical execution point
final_score = process_radar_data(filtered_readings)

# Red herring: fake normalization
normalized_array = [round(x / final_score * 100, 2) for x in pressure_readings]

# Output result as required
print(f"Result: {final_score}")