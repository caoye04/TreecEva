import itertools

# System configuration parameters (many are red herrings)
base_voltage = 230
core_count = 8
thermal_threshold = 75.5
cooling_rate = 0.68
voltage_fluctuation = 12.4
efficiency_factor = 0.87
redundancy_nodes = 5

# Simulated thermal sensor readings over time (relevant data)
sensor_a = [68.2, 71.3, 74.1, 73.9, 76.5, 77.3, 75.0]
sensor_b = [69.0, 70.1, 72.8, 74.5, 78.2, 77.0, 74.3]
sensor_c = [67.5, 70.8, 73.2, 75.1, 76.9, 75.8, 73.7]

# Irrelevant network metrics
tx_packets = [1203, 1187, 1255, 1198]
rx_errors = [0, 1, 0, 0]
latency_ms = [23.4, 25.1, 24.8, 26.2]

# Combine sensor streams using itertools (relevant)
all_readings = list(itertools.chain(sensor_a, sensor_b, sensor_c))

# Apply moving average filter (partially relevant transformation)
smoothed = []
for i in range(2, len(all_readings)):
    avg = (all_readings[i-2] + all_readings[i-1] + all_readings[i]) / 3
    smoothed.append(round(avg, 2))

# Compute derived metrics (some irrelevant)
variance_pool = [abs(smoothed[i+1] - smoothed[i]) for i in range(len(smoothed)-1)]
avg_variance = sum(variance_pool) / len(variance_pool)
spike_count = sum(1 for v in variance_pool if v > 1.0)

# Critical system load modeling (core logic)
thermal_loads = [val * 1.08 for val in smoothed if val > thermal_threshold]

# Dead code path - never executed (distractor)
if cooling_rate > 1.0:
    thermal_loads = [load * 0.9 for load in thermal_loads]

# Hardware degradation adjustment (irrelevant - condition false)
hw_age_years = 7
device_type = 'gen2'
if hw_age_years > 5 and device_type == 'gen1':
    efficiency_factor *= 0.92

# Power modulation logic (contains early return red herring)
def apply_modulation(loads, factor):
    result = []
    for load in loads:
        adjusted = load * factor
n        if adjusted > 95:  # unreachable due to data range
            return [0] * len(loads)  # dead return
        result.append(adjusted)
    return result

# Unused function - decoy (never called)
def calculate_redundancy_margin(nodes, threshold=0.8):
    import math
    return math.comb(nodes + 2, 2) * threshold

# Final capacity assessment
baseline_peak = max(thermal_loads)

# Key assignment statement
peak_capacity = max(thermal_loads) * efficiency_factor

# Secondary irrelevant calculation
normalized_index = (peak_capacity / base_voltage) * 100

# Output the target result
print(f"Result: {peak_capacity}")