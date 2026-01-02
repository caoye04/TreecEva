from itertools import combinations

# Simulate sensor readings from a distributed environmental monitoring system
temperature_readings = [23.4, 24.1, 22.7, 25.3, 26.0, 24.8]
humidity_readings = [56, 59, 52, 61, 58, 60]
pressure_readings = [1013, 1015, 1012, 1016, 1018, 1014]

# Misleading intermediate processing: irrelevant smoothing filter
def apply_filter(data):
    smoothed = [data[0]]
    for i in range(1, len(data)):
        smoothed.append(0.7 * data[i] + 0.3 * smoothed[-1])
    return smoothed

temp_filtered = apply_filter(temperature_readings)  # Distractor
humidity_filtered = apply_filter([float(x) for x in humidity_readings])  # Distractor

# Real processing begins: compute derived indices
heat_index = []
for t, h in zip(temperature_readings, humidity_readings):
    hi = t + 0.5555 * (6.11 * (1.8 * t + 32 + 273.15) * (h / 100) - 10)
    heat_index.append(round(hi, 2))

# Compute pressure trends (first differences)
pressure_trend = [pressure_readings[i] - pressure_readings[i-1] for i in range(1, len(pressure_readings))]

# Flag anomalous combinations using itertools
anomaly_pairs = []
for idx_a, idx_b in combinations(range(len(heat_index)), 2):
    if abs(heat_index[idx_a] - heat_index[idx_b]) > 3.0 and abs(pressure_trend[idx_a % len(pressure_trend)] - pressure_trend[idx_b % len(pressure_trend)]) > 1:
        anomaly_pairs.append((idx_a, idx_b))

# Baseline adjustment based on anomaly count
baseline_adjustment = len(anomaly_pairs) * 2

# Compute weighted flow index (relevant computation)
flow_weights = [0.3, 0.5, 0.7, 0.4, 0.6, 0.8]
weighted_flow = 0.0
for i, (hi_val, w) in enumerate(zip(heat_index, flow_weights)):
    weighted_flow += hi_val * w

# Secondary distractor: unused correlation matrix
unused_corr_matrix = [[0 for _ in range(6)] for _ in range(6)]
for i in range(6):
    for j in range(6):
        unused_corr_matrix[i][j] = round(abs(temperature_readings[i] - temperature_readings[j]) * 0.1, 2)

# Net flow calculation
net_flow_components = []
for i, val in enumerate(heat_index):
    trend_idx = i % len(pressure_trend)
    component = (val - 25) * pressure_trend[trend_idx] * (0.5 if i % 2 == 0 else -0.5)
    net_flow_components.append(component)

net_flow = int(sum(net_flow_components))

# Threshold logic with distractor variables
threshold = 5
buffer_zone = 2  # Unused in final logic
scaling_factor = 1.0  # Distractor: defined but not used

# Key statement
equilibrium_score = net_flow if abs(net_flow) > threshold else baseline_adjustment

# Irrelevant enumeration block (dead-end logic)
status_log = []
for idx, reading in enumerate(temperature_readings):
    status = "HIGH" if reading > 24 else "NORMAL"
    timestamp = f"T{idx+1}"
    status_log.append((timestamp, status))

# Output result
Result: equilibrium_score