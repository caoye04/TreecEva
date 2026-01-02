import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 20.4, 21.9]
humidity_readings = [45, 52, 58, 61, 49, 55, 60, 50]
co2_levels = [410, 415, 420, 430, 425, 418, 435, 428]

# Irrelevant auxiliary data (distractor)
pollutant_names = ['PM2.5', 'O3', 'NO2', 'SO2']
sensor_ids = ['S001', 'S002', 'S003', 'S004', 'S005']
location_grid = [(0,0), (0,1), (1,0), (1,1)]

# Misleading preprocessing functions (dead paths)
def normalize_data(data):
    max_val = max(data)
    return [x / max_val for x in data]  # Not actually used

def shift_values(arr, offset=1):
    return [x + offset for x in arr]  # Unused function

def calculate_entropy(values):
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * math.log(p) for p in probs if p > 0)  # Red herring

# Core processing pipeline
filtered_temps = [t for t in temperature_readings if 20 <= t <= 25]
avg_temp = sum(filtered_temps) / len(filtered_temps) if filtered_temps else 0

humidity_binary = [1 if h > 50 else 0 for h in humidity_readings]
humidity_runs = ''.join(map(str, humidity_binary))
consecutive_high = max(len(run) for run in humidity_runs.split('0')) if '1' in humidity_runs else 0

# Bit manipulation on CO2 data (relevant but disguised)
co2_ints = [int(x) for x in co2_levels]
shifted_co2 = [(val << 1) ^ 0xFF for val in co2_ints]  # Transform but only one value matters
key_co2_metric = shifted_co2[2] & 0xFFFF  # Extract unsigned-like value

# Decoy statistical analysis
mean_co2 = sum(co2_levels) / len(co2_levels)
co2_variance = sum((x - mean_co2) ** 2 for x in co2_levels) / len(co2_levels)
co2_skew = (sum((x - mean_co2) ** 3 for x in co2_levels) / len(co2_levels)) / (co2_variance ** 1.5) if co2_variance > 0 else 0

# Simulated log entries with timestamps and statuses (complex structure)
raw_logs = [
    '2023-08-01T08:00:00Z|TEMP|OK|23.5',
    '2023-08-01T08:05:00Z|HUMID|WARN|52',
    '2023-08-01T08:10:00Z|CO2|OK|410',
    '2023-08-01T08:15:00Z|TEMP|ALERT|19.8',
    '2023-08-01T08:20:00Z|HUMID|OK|49',
    '2023-08-01T08:25:00Z|CO2|OK|415'
]

# Parse logs using string operations
parsed_logs = []
for log in raw_logs:
    parts = log.split('|')
    timestamp = parts[0].split('T')[1].split(':')[0]  # Hour only
    sensor_type = parts[1]
    status = parts[2]
    value_str = parts[3]
    try:
        value = float(value_str)
    except ValueError:
        value = 0
    parsed_logs.append((timestamp, sensor_type, status, value))

# Extract hourly pattern counts
hourly_stats = {}
for hour, s_type, stat, val in parsed_logs:
    key = (hour, s_type)
    hourly_stats[key] = hourly_stats.get(key, 0) + 1

# Filter logs by condition
processed_logs = [
    (h, t, v) for h, t, s, v in parsed_logs 
    if s == 'OK' or (t == 'TEMP' and v > 20)
]

# Unused complex transformation (distractor)
log_summary = {
    hour: list(map(lambda x: x[1], filter(lambda y: y[0] == hour, processed_logs)))
    for hour in set(h for h, _, _ in processed_logs)
}

# Critical diagnostic computation chain
base_score = sum(int(t[0]) for t in processed_logs)  # Sum of hours (8+8+8+8+8 = 40)
weight_factor = len([p for p in processed_logs if p[1] == 'CO2'])  # Count CO2 entries = 2
adjustment = key_co2_metric % 17  # 420 << 1 = 840; 840 ^ 255 = 615; 615 & 0xFFFF = 615; 615 % 17 = 6

intermediate_diag = (base_score * weight_factor) + adjustment  # (40 * 2) + 6 = 86

# Secondary correction based on temperature consistency
temp_stability = int(avg_temp) if avg_temp > 0 else 0  # int(22.25) = 22
final_diagnostic = intermediate_diag - temp_stability + consecutive_high  # 86 - 22 + 1 = 65

# Print result for evaluation
print(f"Result: {final_diagnostic}")