from collections import defaultdict, Counter
import math

# Simulated sensor readings over time (temperature in Celsius)
sensor_data = [
    {'time': 0, 'temp': 20.1, 'sensor_id': 'T1'},
    {'time': 1, 'temp': 22.5, 'sensor_id': 'T1'},
    {'time': 2, 'temp': 19.8, 'sensor_id': 'T2'},
    {'time': 3, 'temp': 25.3, 'sensor_id': 'T1'},
    {'time': 4, 'temp': 24.1, 'sensor_id': 'T2'},
    {'time': 5, 'temp': 27.6, 'sensor_id': 'T3'},
    {'time': 6, 'temp': 26.2, 'sensor_id': 'T1'},
    {'time': 7, 'temp': 28.9, 'sensor_id': 'T3'},
    {'time': 8, 'temp': 23.4, 'sensor_id': 'T2'},
    {'time': 9, 'temp': 30.1, 'sensor_id': 'T1'}
]

# Irrelevant auxiliary data (distractor)
diagnostic_logs = [
    {'level': 'INFO', 'msg': 'System boot'},
    {'level': 'WARN', 'msg': 'High load'},
    {'level': 'DEBUG', 'msg': 'Sensor T2 recalibrated'}
]

# Misleading transformation (dead path)
def legacy_calibrate(value):
    return (value * 1.02) + 0.5  # Not used in main logic

# Unused helper (red herring)
def rolling_average(data, window=3):
    result = []
    for i in range(len(data)):
        if i < window - 1:
            result.append(None)
        else:
            result.append(sum(data[i - window + 1:i + 1]) / window)
    return result

# Decoy function that looks important but isn't called
def analyze_failure_modes(logs):
    counts = Counter([entry['level'] for entry in logs])
    return {k: v * 100 for k, v in counts.items()}

# Real processing begins here
sensor_groups = defaultdict(list)
for record in sensor_data:
    sensor_groups[record['sensor_id']].append(record['temp'])

# Compute growth trends per sensor (some irrelevant)
growth_rates = {}
for sid, temps in sensor_groups.items():
    if len(temps) > 1:
        growth = sum(temps[i+1] - temps[i] for i in range(len(temps)-1))
        growth_rates[sid] = round(growth / (len(temps) - 1), 3)
    else:
        growth_rates[sid] = 0.0

# Fallback calibration map (partially used distractor)
calibration_offset = {'T1': 0.2, 'T2': -0.1, 'T3': 0.0, 'T4': 0.5}

# Primary transformation pipeline
filtered_readings = []
for record in sensor_data:
    temp = record['temp']
    sensor_id = record['sensor_id']
    # Only apply offset to T1 (others ignored - subtle detail)
    if sensor_id == 'T1':
        temp += calibration_offset[sensor_id]
    filtered_readings.append(temp)

# Secondary feature extraction
mean_temp = sum(filtered_readings) / len(filtered_readings)
peak_temp = max(filtered_readings)
temp_range = peak_temp - min(filtered_readings)

# Statistical moment calculation (distraction)
variance = sum((t - mean_temp) ** 2 for t in filtered_readings) / len(filtered_readings)
skewness = sum(((t - mean_temp) / (variance ** 0.5)) ** 3 for t in filtered_readings) / len(filtered_readings)

# Composite health score (irrelevant)
health_score = 100 - (variance * 2) + (skewness * 5)

# Actual core logic disguised among noise
def extract_phase_shift(readings):
    # Simulate frequency domain shift (bitwise obfuscation)
    total = 0
    for i, val in enumerate(readings):
        shifted = int(val * 10) << 1
        masked = shifted & 0xFF
        total ^= masked  # Use XOR to combine
    return total

phase_key = extract_phase_shift(filtered_readings)

# Real metric computation chain
baseline = mean_temp * 1.8 + 32  # Convert to Fahrenheit as base
adjustment_factor = (peak_temp - mean_temp) / 10
normalized_span = temp_range / (mean_temp + 0.1)

# Weighted combination with hidden priority
weights = [0.6, 0.3, 0.1]
weighted_metric = (
    weights[0] * baseline + 
    weights[1] * (adjustment_factor * 100) + 
    weights[2] * (normalized_span * 50)
)

# Final transformation using phase key (critical step)
final_hash = (phase_key ^ int(weighted_metric)) & 0xFFFF

# Main calculation function (appears complex but deterministic)
def calculate_thermal_metric(readings):
    raw_sum = sum(r * 1.1 for r in readings)
    count_T1 = sum(1 for rec in sensor_data if rec['sensor_id'] == 'T1')
    penalty = 0
    if count_T1 > 3:
        penalty = 15.5
    adjusted_sum = raw_sum - penalty
    # Incorporate final_hash as non-linear modulator
    modulation = (final_hash % 25) / 10.0
    return (adjusted_sum / len(readings)) + modulation

# Execute main statement
thermal_capacity = calculate_thermal_metric(processed_readings=[f + 0.5 for f in filtered_readings])

Result: {thermal_capacity}