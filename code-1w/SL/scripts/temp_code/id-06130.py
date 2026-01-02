from collections import defaultdict
from itertools import cycle

# Simulate sensor data stream with periodic anomalies
time_series_data = [104, 95, 110, 90, 115, 85, 120, 80, 125, 75]
pressure_readings = [205, 195, 210, 190, 215, 185, 220, 180, 225, 175]
dummy_offsets = [3, -2, 5, -1, 4]

# Track moving averages and anomalies
avg_tracker = defaultdict(float)
window_size = 3
smoothed_values = []

for i in range(len(time_series_data) - window_size + 1):
    window = time_series_data[i:i+window_size]
    avg = sum(window) // window_size
    avg_tracker[f'window_{i}'] = avg
    smoothed_values.append(avg)

# Compute trend deviation (irrelevant for final answer but adds cognitive load)
trend_deviation = 0
for j in range(1, len(smoothed_values)):
    trend_deviation += abs(smoothed_values[j] - smoothed_values[j-1])
trend_deviation = trend_deviation // 2 if trend_deviation > 50 else 0

# Simulate pressure stabilization process
pressure_cycle = cycle(pressure_readings)
accumulated_stabilization = 0
peak_pressure = max(pressure_readings)

for idx, p in enumerate(pressure_cycle):
    if idx == 10:
        break
    if p < peak_pressure - 20:
        accumulated_stabilization += p % 17
    else:
        accumulated_stabilization -= p % 11

# Dummy calculation chain with red herring variables
total_offset_impact = 0
for offset in dummy_offsets:
    temp_effect = (offset ** 2) - (offset * 3)
    if temp_effect > 0:
        total_offset_impact += temp_effect

# Core logic masked by prior distractions
baseline_reference = sum(smoothed_values[::2]) // len(smoothed_values[::2])
fluctuation_metric = abs(smoothed_values[0] - smoothed_values[-1])
net_flow = baseline_reference - fluctuation_metric

# Critical statement: equilibrium_score depends only on net_flow and peak_pressure
equilibrium_score = net_flow + (peak_pressure // 2)

print(f"Result: {equilibrium_score}")