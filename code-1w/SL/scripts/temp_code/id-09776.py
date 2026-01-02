from collections import defaultdict

# Simulate distributed sensor network load analysis
sensor_readings = [14, 18, 22, 19, 25, 30, 28, 20, 17, 23]
baseline_threshold = 20
redundancy_nodes = 3
system_load = 0
fluctuation_log = defaultdict(int)

temp_offset = 0
for reading in sensor_readings:
    if reading > baseline_threshold:
        system_load += reading * 0.85
    else:
        temp_offset += reading * 0.1

    # Logging fluctuations for diagnostic purposes (not used in final result)
    fluctuation_level = 'high' if reading > 22 else 'low'
    fluctuation_log[fluctuation_level] += 1

# Irrelevant transformation - simulates calibration drift compensation
adjusted_offsets = list(map(lambda x: x ** 0.5, sensor_readings[:3]))
calibration_shift = sum(adjusted_offsets) / 3 if adjusted_offsets else 0

# Secondary loop analyzing node distribution (partially relevant)
node_weights = []
for i in range(redundancy_nodes):
    weight = (i + 1) * 0.6
    if i % 2 == 0:
        weight *= 1.2
    node_weights.append(weight)

aggregated_weight = sum(node_weights)
effective_redundancy = aggregated_weight / redundancy_nodes

# Core calculation chain
base_capacity = system_load * 1.2
scaling_factor = len(fluctuation_log) * 0.1
intermediate_capacity = base_capacity + (base_capacity * scaling_factor)

# Redundancy adjustment based on effective node contribution
redundancy_factor = effective_redundancy / 2.0

# Key statement
final_adjustment = system_load * (1 + redundancy_factor)
peak_capacity = int(intermediate_capacity + final_adjustment)

# Dead code path - never executed but adds cognitive load
if False:
    debug_trace = [x * 2 for x in node_weights]
    peak_capacity -= sum(debug_trace)

# Print final result as required
print(f"Result: {peak_capacity}")