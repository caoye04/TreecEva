import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.1, 23.7]
humidity_readings = [45, 48, 50, 44, 52, 49, 47, 51]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017, 1013]

# Irrelevant calibration coefficients (distractor)
calibration_map = {'gain': 1.02, 'offset': -0.5, 'scale_factor': 2.1}
adjusted_temps = [t * calibration_map['gain'] + calibration_map['offset'] for t in temperature_readings]

# Misleading intermediate diagnostic (dead path)
system_health_flag = 'OK'
if sum(humidity_readings) > 400:
    system_health_flag = 'WARNING'
else:
    system_health_flag = 'CRITICAL'

# Bit manipulation for checksum simulation (partially relevant)
def compute_checksum(values):
    checksum = 0
    for val in values:
        truncated = int(val * 10) if isinstance(val, float) else val
        checksum ^= truncated
        checksum = (checksum << 1) & 0xFFFF
    return checksum

# Spurious transformation chain (red herring)
transformed_humidity = []
for h in humidity_readings:
    h_str = str(h)
    if h_str.startswith('4'):
        transformed_humidity.append(h ** 1.5)
    else:
        transformed_humidity.append(h + 10)

# Real processing begins: detect anomalies in temperature
baseline_temp = sum(temperature_readings) / len(temperature_readings)
anomalies = []
for i, temp in enumerate(temperature_readings):
    if abs(temp - baseline_temp) > 1.0:
        anomalies.append(i)

# Cross-reference with pressure fluctuations
pressure_trend = []
for i in range(1, len(pressure_readings)):
    pressure_trend.append(pressure_readings[i] - pressure_readings[i-1])

significant_pressure_shifts = list(itertools.compress(range(1, len(pressure_readings)), 
                                                      [abs(x) >= 2 for x in pressure_trend]))

# Correlate anomaly timing across systems
correlated_events = []
for event_time in anomalies:
    if event_time in significant_pressure_shifts:
        correlated_events.append(event_time)

# Compute composite risk score (core logic)
raw_risk_score = 0
for idx in correlated_events:
    temp_deviation = abs(temperature_readings[idx] - baseline_temp)
    pressure_spike = abs(pressure_trend[idx-1])
    raw_risk_score += temp_deviation * pressure_spike * 10

# Secondary distraction: entropy calculation on stringified data (irrelevant)
data_stream = ''.join([f'{t}{h}' for t, h in zip(temperature_readings, humidity_readings)])
entropy_chars = set(data_stream)
shannon_entropy = sum(-(data_stream.count(c) / len(data_stream)) * 
                      ((data_stream.count(c) / len(data_stream)) and (data_stream.count(c) / len(data_stream)).__log__()) 
                      for c in entropy_chars)

# Final aggregation with thresholding (key statement)
def aggregate_threshold(score, events, threshold=25.0):
    if len(events) == 0:
        return 0
    adjusted = score / len(events)
    if adjusted > threshold:
        return int(adjusted * 2.5)
    else:
        return int(adjusted)

final_diagnostic = aggregate_threshold(raw_risk_score, correlated_events)

# Print result as required
print(f"Result: {final_diagnostic}")