from itertools import compress, count
import math

# Simulated industrial filtration process with multiple interfering calculations

turbidity_levels = [1.2, 0.9, 1.5, 0.7, 1.1, 1.8, 0.6]
pressure_readings = [220, 235, 210, 240, 225, 215, 230]
time_intervals = list(count(10, 5))[:7]

# Irrelevant transformation: frequency analysis (dead-end computation)
frequency_map = list(map(lambda x: math.sin(x / 100), pressure_readings))
harmonic_distortion = sum(frequency_map) * 0.01  # Distractor variable

# Misleading intermediate: apparent flow correlation (not used in final result)
apparent_flow_rate = list(filter(lambda x: x > 220, pressure_readings))
baseline_offset = len(apparent_flow_rate) * 0.05  # Red herring

# Real signal processing path
normalized_turbidity = [1 - (t / max(turbidity_levels)) for t in turbidity_levels]
valid_windows = [t > 0.8 for t in normalized_turbidity]  # High clarity intervals

# Decoy data structure: unused filtered dataset
filtered_data_stream = list(compress(pressure_readings, valid_windows))
phantom_peak = max(filtered_data_stream) if filtered_data_stream else 0  # Unused result

# Auxiliary calculation: thermal decay compensation (irrelevant)
temperature_log = [25 + i * 0.3 for i in range(7)]
thermal_decay = sum([t * 0.002 for t in temperature_log])  # Dead code path

# Core logic begins: compute net operational flow
operational_gaps = [time_intervals[i+1] - time_intervals[i] for i in range(len(time_intervals)-1)]
gap_penalty = sum([1 for g in operational_gaps if g > 6]) * 0.03  # Minor distractor

# Efficiency factor derived from valid windows and pressure stats
active_duration = sum(compress(time_intervals, valid_windows))
total_duration = sum(time_intervals)
duration_ratio = active_duration / total_duration

pressure_stability = sum(pressure_readings) / len(pressure_readings)
reference_pressure = 225

# Key efficiency computation
stability_score = 1 - abs(pressure_stability - reference_pressure) / reference_pressure
efficiency_factor = stability_score * duration_ratio  # Actual contributor

# Net flow based on harmonic mean of valid pressures (correct path)
valid_pressures = list(compress(pressure_readings, valid_windows))
if valid_pressures:
    reciprocal_sum = sum(1/p for p in valid_pressures)
    harmonic_mean = len(valid_pressures) / reciprocal_sum
else:
    harmonic_mean = 0

net_flow = harmonic_mean * 0.85  # Apply transmission efficiency

# CRITICAL STATEMENT
filtration_yield = net_flow * efficiency_factor

# Output requirement
print(f"Result: {filtration_yield}")