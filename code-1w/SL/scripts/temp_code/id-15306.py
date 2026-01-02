import itertools

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7]
humidity_readings = [55, 57, 60, 53, 50, 48, 52, 56]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1007, 1009, 1011]

# Irrelevant transformation: normalize humidity (not used in final calculation)
normalized_humidity = [h / 100 for h in humidity_readings]

# Distractor function: analyzes pressure trends but returns unused result
def analyze_pressure_trend(pressures):
    trend = []
    for i in range(1, len(pressures)):
        if pressures[i] > pressures[i-1]:
            trend.append(1)
        elif pressures[i] < pressures[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    return sum(trend)  # This result is never used

# Call but don't use
pressure_analysis_score = analyze_pressure_trend(pressure_readings)

# Real processing begins: detect temperature anomalies
baseline_temp = sum(temperature_readings[:4]) / 4
anomalies = []
for temp in temperature_readings:
    if abs(temp - baseline_temp) > 1.5:
        anomalies.append(temp)

# Compute rolling average over 3-day window
rolling_averages = []
for i in range(len(temperature_readings) - 2):
    window_avg = sum(temperature_readings[i:i+3]) / 3
    rolling_averages.append(round(window_avg, 2))

# Apply false correction: this looks important but is discarded later
raw_correction = sum(rolling_averages) / len(rolling_averages)
discarded_adjustment = raw_correction * 0.97

# Critical path: generate diagnostic metrics using itertools
windowed_data = list(itertools.pairwise(rolling_averages))
fluctuations = [abs(pair[1] - pair[0]) for pair in windowed_data]

# Simulate redundant backup calculation (unused)
backup_fluctuations = []
for i in range(1, len(rolling_averages)):
    delta = abs(rolling_averages[i] - rolling_averages[i-1])
    backup_fluctuations.append(delta)

# Aggregate primary metrics
aggregate_metrics = [
    len(anomalies),
    int(sum(fluctuations)),
    int(baseline_temp),
    len(rolling_averages)
]

# Dead code path: complex bitwise logic that computes unused flag
status_flag = 0
for val in pressure_readings:
    status_flag ^= int(val)
    status_flag <<= 1
    if status_flag > 10000:
        status_flag >>= 4
status_flag &= 0xFF  # Unused diagnostic flag

# Red herring: fake correction chain
temp_deviation = temperature_readings[-1] - temperature_readings[0]
risk_estimate = temp_deviation ** 2 / 10.0
penalty_factor = risk_estimate * 0.3  # Never applied

# Key variables for final computation
correction_factor = len(list(itertools.combinations([x for x in anomalies if x > baseline_temp], 2)))
safety_margin = abs(rolling_averages[-1] - rolling_averages[-2])

# Critical statement
final_diagnostic = aggregate_metrics[-1] + correction_factor * safety_margin

# Print result as required
print(f"Result: {final_diagnostic}")