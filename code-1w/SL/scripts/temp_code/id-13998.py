import math

# Simulated sensor data stream with metadata
data_stream = [
    {'value': 84, 'type': 'temp', 'valid': True},
    {'value': 22, 'type': 'pressure', 'valid': True},
    {'value': 15, 'type': 'temp', 'valid': False},
    {'value': 67, 'type': 'humidity', 'valid': True},
    {'value': 90, 'type': 'temp', 'valid': True}
]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_A = 0.987
CALIBRATION_OFFSET_B = -2.1
REFERENCE_VOLTAGE = 5.0

# Helper lambda for filtering valid entries
is_valid_entry = lambda x: x['valid']

# Extract and filter relevant temperature readings
temp_readings = [entry['value'] for entry in data_stream 
                if entry['type'] == 'temp' and is_valid_entry(entry)]

# Secondary processing: pressure tracking (semi-relevant but not used in final score)
pressure_readings = [entry['value'] for entry in data_stream 
                     if entry['type'] == 'pressure']

# Dummy transformation on pressure (dead code path)
adjusted_pressure = list(map(lambda p: p * CALIBRATION_FACTOR_A + CALIBRATION_OFFSET_B, pressure_readings))

# Compute rolling differences for temp (used in stability index)
if len(temp_readings) > 1:
    temp_diffs = [abs(temp_readings[i] - temp_readings[i-1]) for i in range(1, len(temp_readings))]
else:
    temp_diffs = [0]

# Stability metric: inverse of average fluctuation
stability_index = 1 / (sum(temp_diffs) / len(temp_diffs)) if sum(temp_diffs) > 0 else 1.0

# Baseline threshold check using enumerate (irrelevant count)
threshold_breaches = 0
for i, val in enumerate(temp_readings):
    if val > 85 and i % 2 == 0:  # Artificial condition
        threshold_breaches += 1

# Auxiliary computation: entropy approximation (not used)
probabilities = [val / sum(temp_readings) for val in temp_readings]
entropy_proxy = -sum(p * math.log(p) for p in probabilities if p > 0)

# Humidity presence check affects weight (semi-relevant)
humidity_detected = any(entry['type'] == 'humidity' for entry in data_stream)
weight_factor = 1.2 if humidity_detected else 1.0

# Core efficiency formula: weighted stability adjusted by mean temperature
mean_temp = sum(temp_readings) / len(temp_readings)
efficiency_score = (stability_index * weight_factor * 100) + (mean_temp / 10)

# Final aggregation step
final_output = process_metrics(data_stream) if 'process_metrics' in globals() else efficiency_score

def process_metrics(stream):
    # Re-compute same logic in a function (mirrors above)
    temps = [e['value'] for e in stream if e['type'] == 'temp' and e['valid']]
    diffs = [abs(temps[i] - temps[i-1]) for i in range(1, len(temps))] if len(temps) > 1 else [0]
    stab = 1 / (sum(diffs) / len(diffs)) if sum(diffs) > 0 else 1.0
    base_mean = sum(temps) / len(temps)
    humid = any(e['type'] == 'humidity' for e in stream)
    wf = 1.2 if humid else 1.0
    return (stab * wf * 100) + (base_mean / 10)

# Update final output
final_output = process_metrics(data_stream)

# Print result
print(f"Result: {efficiency_score}")