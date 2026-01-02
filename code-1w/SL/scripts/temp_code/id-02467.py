import math

# Simulated sensor array data (temperature readings in Celsius)
sensor_readings = [23.5, 24.1, 19.8, 22.3, 25.0, 26.7, 18.9, 20.2, 24.8, 23.7]

temperature_flags = []
anomaly_buffer = []
processed_indices = set()
baseline_reference = 22.5
smoothing_factor = 0.85
rolling_window = 3

# Irrelevant pre-processing: normalize readings (not used later)
normalized = [math.log(r + 273.15) for r in sensor_readings]

# Step 1: Identify deviations beyond threshold
deviation_map = {}
for i, temp in enumerate(sensor_readings):
    deviation = abs(temp - baseline_reference)
    deviation_map[i] = deviation
    if deviation > 2.0:
        temperature_flags.append(i)
        anomaly_buffer.append(deviation * 1.5)
    elif deviation > 1.0:
        processed_indices.add(i)

# Dead code path: unused function
def calculate_ema(data, alpha):
    ema = [data[0]]
    for x in data[1:]:
        ema.append(alpha * x + (1 - alpha) * ema[-1])
    return ema

# Unused transformation
filtered_readings = [t for t in sensor_readings if t > 20.0]

# Step 2: Compute rolling max-min over window
extremes = []
for i in range(len(sensor_readings) - rolling_window + 1):
    window = sensor_readings[i:i+rolling_window]
    extremes.append(max(window) - min(window))

# Step 3: Flag windows with high volatility
volatility_alerts = [v for v in extremes if v > 3.0]

# Step 4: Apply corrective scaling based on first and last anomalies
if temperature_flags:
    first_anom = temperature_flags[0]
    last_anom = temperature_flags[-1]
    span_correction = abs(last_anom - first_anom) * 0.1
else:
    span_correction = 0.0

# Step 5: Build aggregate metrics from multiple sources
aggregate_metrics = []
aggregate_metrics.append(len(temperature_flags))
aggregate_metrics.append(sum(anomaly_buffer) if anomaly_buffer else 0)
aggregate_metrics.append(len(volatility_alerts))
aggregate_metrics.append(span_correction)

# Distractor: complex bit manipulation with no impact
temp_state = 0b101010
for x in aggregate_metrics:
    temp_state ^= int(x) << 1
    temp_state = temp_state & 0b111111 | 0b010101

# Step 6: Compute secondary anomaly score from deviation map
weighted_deviation = 0.0
for idx, dev in deviation_map.items():
    if idx % 2 == 0:
        weighted_deviation += dev * 0.3
    else:
        weighted_deviation += dev * 0.1

anomaly_score = math.ceil(weighted_deviation)

# Step 7: Final diagnostic fusion
final_diagnostic = aggregate_metrics[-1] + anomaly_score

# Output result
print(f"Result: {final_diagnostic}")