import math

# Simulated sensor data processing pipeline for environmental monitoring
data_stream = [14, 19, 25, 36, 41, 52, 63, 74, 85, 96]
baseline = {i: val % 13 for i, val in enumerate(data_stream)}
anomaly_threshold = 3.14159

# Irrelevant auxiliary data (distractor)
calendar_events = {'Q1': 3, 'Q2': 5, 'Q3': 7, 'Q4': 11}
event_weights = [x ** 0.5 for x in calendar_events.values()]
scaling_factor = sum(event_weights) / len(event_weights)

# Data transformation with red herring operations
temp_offset = 273.15
transformed_data = []
for val in data_stream:
    kelvin = val + temp_offset
    transformed = int(kelvin / 2) % 17
    if transformed > 10:
        transformed = 10
    transformed_data.append(transformed)

# Decoy function that is never called (dead code path)
def legacy_calibrate(x):
    return (x * 1.07) - 4 if x > 20 else x * 0.92

# Bit manipulation distraction block
bit_flags = 0b101010
flag_shift = (bit_flags << 3) & 0b11110000
flag_check = bin(flag_shift ^ 0b11000000).count('1')

# Set operations (required feature) - some are irrelevant
observed_readings = set(transformed_data)
expected_range = set(range(0, 13))
deviant_readings = observed_readings - expected_range  # Always empty, but looks important
consistency_check = len(observed_readings & expected_range) > 8

# Lambda function (required feature): used in filtering, but also has decoy usage
integrity_filter = lambda x: x != 0 and (x & (x - 1)) == 0  # Power of two check
filtered_diagnostics = list(filter(integrity_filter, transformed_data))

# Unused but plausible-looking diagnostic
redundant_metric = sum(1 for x in transformed_data if x in [2, 4, 8])

# Core logic buried among distractions
def process_metrics(data, base_map):
    cumulative = 0
    for idx, val in enumerate(data):
        deviation = abs(val - base_map[idx])
        if deviation > 0:
            cumulative += deviation * (idx + 1)
    return cumulative // 3

# Secondary computation with misleading intermediate
rolling_buffer = [transformed_data[i] ^ transformed_data[-i-1] for i in range(len(transformed_data)//2)]
anomaly_contributions = [abs(x - 5) for x in rolling_buffer if x != 5]
anomaly_score = 0
if anomaly_contributions:
    raw_anomaly = sum(anomaly_contributions) / len(anomaly_contributions)
    if raw_anomaly > anomaly_threshold:
        anomaly_score = math.floor(raw_anomaly * 2)
    else:
        anomaly_score = math.ceil(raw_anomaly)

# Dead assignment - looks like it does something
status_flag = 'NORMAL' if consistency_check else 'ALERT'

# Key statement: this computes the final result
final_diagnostic = process_metrics(transformed_data, baseline) + anomaly_score

# Output the result as required
print(f"Target result: {final_diagnostic}")