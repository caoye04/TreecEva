import math

# Simulated dataset: (timestamp, temperature, humidity, pressure)
data_log = [
    (1623456000, 25.3, 60.1, 1013.2),
    (1623456060, 26.1, 58.7, 1012.9),
    (1623456120, 27.5, 55.2, 1012.4),
    (1623456180, 28.3, 53.8, 1011.8),
    (1623456240, 27.9, 54.5, 1012.1),
    (1623456300, 26.7, 57.3, 1012.7),
    (1623456360, 25.8, 59.8, 1013.0),
    (1623456420, 24.9, 61.2, 1013.4),
    (1623456480, 25.4, 59.9, 1013.1),
    (1623456540, 26.0, 58.4, 1012.8)
]

# Irrelevant sensor calibration offsets (distractor)
offsets = {'temp': -0.5, 'humidity': 1.2, 'pressure': 0.3}

calibrated = []
for entry in data_log:
    ts, t, h, p = entry
    # Apply fake calibration (not actually used later)
    calibrated.append((ts, t + offsets['temp'], h + offsets['humidity'], p + offsets['pressure']))

# Extract only temperature for anomaly detection (real processing path starts here)
temperatures = [entry[1] for entry in data_log]

# Compute moving average with window size 3
moving_avg = []
for i in range(len(temperatures)):
    if i < 2:
        moving_avg.append(None)
    else:
        avg = sum(temperatures[i-2:i+1]) / 3
        moving_avg.append(round(avg, 2))

# Flag anomalies where temperature deviates by more than 1.0 from moving average
anomalies = []
for i, temp in enumerate(temperatures):
    if moving_avg[i] is not None:
        if abs(temp - moving_avg[i]) > 1.0:
            anomalies.append((i, temp))

# Decoy function: looks important but unused
def analyze_pressure_trend(log):
    pressures = [entry[3] for entry in log]
    trend = 0
    for i in range(1, len(pressures)):
        trend += pressures[i] - pressures[i-1]
    return trend

# Unused clustering attempt (dead code path)
clusters = {}
for idx, temp in enumerate(temperatures):
    key = int(temp // 5) * 5
    if key not in clusters:
        clusters[key] = []
    clusters[key].append(idx)

# Real processing: compute volatility score using pairwise differences
volatility = 0.0
for i in range(1, len(temperatures)):
    volatility += abs(temperatures[i] - temperatures[i-1])

# Normalize volatility to a 0-100 scale
normalized_volatility = (volatility / len(temperatures)) * 10

# Use enumerate and zip together in meaningful transformation
indexed_data = list(enumerate(data_log))
prev_temps = temperatures[:-1]
curr_temps = temperatures[1:]
temp_changes = [round(c - p, 2) for p, c in zip(prev_temps, curr_temps)]
change_with_index = list(enumerate(temp_changes, 1))

# Secondary scoring based on change magnitude
change_magnitude_score = sum([abs(change) * 2 for change in temp_changes])

# Combine scores: normalized volatility (weighted 0.6) + change magnitude (weighted 0.4)
combined_instability = (normalized_volatility * 0.6) + (change_magnitude_score * 0.4)

# Final score derived from instability (inverse relationship)
final_score = int(100 - combined_instability)

# Distractor print statements (no impact)
_ = [print(f'Intermediate {i}: {v}') for i, v in enumerate(moving_avg) if v]

dummy_lookup = {i: math.sin(i) for i in range(1, 20)}
decoy_value = sum(dummy_lookup.values())

# Critical execution point
def calculate_final_score(score):
    # Additional adjustment based on number of anomalies
    adjustment = len(anomalies) * 2
    return score - adjustment

final_score = calculate_final_score(final_score)

print(f"Result: {final_score}")