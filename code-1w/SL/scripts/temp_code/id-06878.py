from collections import defaultdict, Counter
import math

# Simulated sensor readings with noise and redundant data
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.5, 26.2, 24.8, 23.5, 27.0, 25.5]
humidity_readings = [45, 47, 46, 50, 52, 45, 48, 50, 55, 45]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1013, 1014, 1016, 1007, 1013]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8', 'I9', 'J10']
device_status = {code: 'active' if i % 2 == 0 else 'standby' for i, code in enumerate(legacy_codes)}

def analyze_outliers(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    return [x for x in data if abs(x - mean) > 2 * std_dev]

# Misleading function that appears important but isn't used in final computation
def deprecated_normalization(arr):
    min_val, max_val = min(arr), max(arr)
    return [(x - min_val) / (max_val - min_val) for x in arr]

# Core processing pipeline
def extract_modes(readings_list):
    freq = Counter(readings_list)
    max_freq = max(freq.values())
    return sorted([k for k, v in freq.items() if v == max_freq])

def rolling_average(data, window=3):
    if len(data) < window:
        return [sum(data)/len(data)]
    return [sum(data[i:i+window]) / window for i in range(len(data) - window + 1)]

def detect_stable_phases(values, threshold=0.5):
    roll_avg = rolling_average(values)
    fluctuations = [abs(roll_avg[i+1] - roll_avg[i]) for i in range(len(roll_avg)-1)]
    stable_count = sum(1 for f in fluctuations if f < threshold)
    return stable_count

# Distractor: complex bit manipulation with no effect on result
def scramble_code(base_id):
    code = 0
    for c in base_id:
        code ^= ord(c)
        code = (code << 1) | (code >> 7)
        code &= 0xFF
    return code

diagnostic_flags = defaultdict(bool)
diagnostic_flags['outlier_free'] = False
diagnostic_flags['stable_pressure'] = True
diagnostic_flags['humidity_spike'] = any(h > 50 for h in humidity_readings)

# Real-time stream simulation (unused path - dead code)
current_stream_index = 0
temp_buffer = []
while current_stream_index < 5:
    temp_buffer.append(temperature_readings[current_stream_index])
    current_stream_index += 1

# Key analysis functions actually used
primary_modes = extract_modes(temperature_readings)
secondary_modes = extract_modes(humidity_readings)

temp_stability = detect_stable_phases(temperature_readings, threshold=0.8)
humid_stability = detect_stable_phases(humidity_readings, threshold=3.0)

# Aggregation logic with red herrings
baseline_ref = math.floor(sum(primary_modes) / len(primary_modes))
penalty_factor = 0
if len(primary_modes) > 1:
    penalty_factor += 0.25
if temp_stability < 3:
    penalty_factor += 0.15

# Decoy calculation involving pressure (not actually affecting final score)
pressure_mode = max(set(pressure_readings), key=pressure_readings.count)
pressure_drift = max(pressure_readings) - min(pressure_readings)

# Unused transformation (distractor)
sorted_with_index = list(enumerate(sorted(temperature_readings, reverse=True)))
indexed_map = {idx: val for idx, val in sorted_with_index}

# Final aggregation using only temperature and humidity stability
raw_score = (temp_stability * 10) + (humid_stability * 7)
adjusted_score = raw_score * (1 - penalty_factor)

# Secondary adjustment based on mode consistency
mode_bonus = 5 if primary_modes[0] in [23.5, 24.0, 24.5] else 0

# Final computation
final_score = int(adjusted_score + mode_bonus)

# Additional irrelevant operations to increase interference
checksum = 0
for i, temp in enumerate(temperature_readings):
    checksum ^= int(temp * 10) ^ (i << 2)

# Dummy zip usage with unrelated data (satisfies language feature requirement)
for temp, humid, press in zip(temperature_readings, humidity_readings, pressure_readings):
    if humid > 50:
        diagnostic_flags['high_humidity_phase'] = True

# Output the target variable
print(f"Result: {final_score}")