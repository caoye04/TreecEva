import math

# Simulated sensor data stream from industrial monitoring system
temperature_readings = [23.5, 24.1, 25.3, 26.0, 27.8, 28.2, 29.0, 30.5, 31.0, 32.1]
humidity_readings = [45, 47, 50, 52, 55, 58, 60, 63, 65, 67]
pressure_readings = [1013, 1012, 1015, 1010, 1008, 1005, 1003, 1001, 999, 997]

# Irrelevant auxiliary data (distractor)
event_log_ids = ['E001', 'E002', 'E003', 'E004', 'E005', 'E006', 'E007', 'E008', 'E009', 'E010']
user_access_times = [1623456789, 1623456845, 1623456901, 1623456967, 1623457033]

# Data processing pipeline
smoothed_temps = []
for i, temp in enumerate(temperature_readings):
    if i == 0:
        smoothed_temps.append(temp)
    else:
        smoothed_temps.append(0.7 * temp + 0.3 * smoothed_temps[i-1])

# Humidity trend analysis (partially relevant but not critical)
humidity_trend = 0
for i in range(1, len(humidity_readings)):
    if humidity_readings[i] > humidity_readings[i-1]:
        humidity_trend += 1
    elif humidity_readings[i] < humidity_readings[i-1]:
        humidity_trend -= 1

# Pressure-based anomaly detection (red herring)
critical_pressure_events = []
for j, p in enumerate(pressure_readings):
    if p < 1000 and j % 2 == 0:
        critical_pressure_events.append(j)

# Compute derived features
rate_of_change = []
for k in range(1, len(smoothed_temps)):
    rate_of_change.append(smoothed_temps[k] - smoothed_temps[k-1])

# Fallback baseline calculation (dead code path)
baseline_avg = sum(smoothed_temps) / len(smoothed_temps)
if baseline_avg < 0:
    baseline_avg = 25.0  # Impossible condition, never executed

# Anomaly scoring using temperature derivative
anomalies = []
for roc in rate_of_change:
    if roc > 1.0:
        anomalies.append(roc * 2)
    elif roc < 0.3:
        anomalies.append(roc * 0.5)
    else:
        anomalies.append(roc)

# Simulate diagnostic thresholds (irrelevant computations)
normal_threshold = 0.8
warning_threshold = 1.5
alert_threshold = 2.2

status_flags = []
for a in anomalies:
    if a > alert_threshold:
        status_flags.append('ALERT')
    elif a > warning_threshold:
        status_flags.append('WARNING')
    else:
        status_flags.append('NORMAL')

# Dummy classification model (decoy function)
def classify_status(val):
    if val > 2.0:
        return 'CRITICAL'
    elif val > 1.0:
        return 'ELEVATED'
    else:
        return 'STABLE'

# Apply decoy function to irrelevant list
fake_classification = [classify_status(x) for x in pressure_readings[:5]]

# Core metric computation chain
weighted_anomalies = []
for idx, (i, v) in enumerate(zip(range(len(anomalies)), anomalies)):
    weight = 1 + 0.1 * idx  # Increasing importance over time
    weighted_anomalies.append(v * weight)

# Aggregate across multiple dimensions (sets and lists)
anomaly_set_1 = set(round(x, 1) for x in weighted_anomalies if x > 1.0)
anomaly_set_2 = set(round(x, 1) for x in anomalies if x > 0.8)
common_anomalies = anomaly_set_1.intersection(anomaly_set_2)

# Primary metric accumulation
aggregate_metrics = []
cumulative = 0.0
for wa in weighted_anomalies:
    cumulative += wa
    aggregate_metrics.append(round(cumulative, 3))

# Secondary indirect measurement (misleading intermediate)
total_fluctuation = sum(abs(rate_of_change[i] - rate_of_change[i-1]) for i in range(1, len(rate_of_change)))

# Final adjustment factors
scaling_factor = len(common_anomalies) * 0.5

# Spurious correlation check (distractor logic)
correlation_score = 0
for t, h in zip(temperature_readings, humidity_readings):
    if t > 25 and h > 50:
        correlation_score += 1

# Actual final computation (depends only on specific path)
anomaly_score = len([x for x in anomalies if x > 1.2])

# Key statement: this determines the answer
final_diagnostic = aggregate_metrics[-1] + anomaly_score * scaling_factor

print(f"Result: {final_diagnostic}")