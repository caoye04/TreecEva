from collections import defaultdict, Counter
from itertools import combinations, cycle
import math

# Simulated sensor array data from autonomous drone navigation system
telemetry_stream = [
    {'time': 0.1, 'x': 1.0, 'y': 2.0, 'z': 3.0, 'temp': 22.5, 'voltage': 4.1},
    {'time': 0.2, 'x': 1.3, 'y': 2.4, 'z': 3.2, 'temp': 22.6, 'voltage': 4.0},
    {'time': 0.3, 'x': 1.7, 'y': 2.9, 'z': 3.8, 'temp': 22.7, 'voltage': 3.9},
    {'time': 0.4, 'x': 2.2, 'y': 3.5, 'z': 4.5, 'temp': 22.8, 'voltage': 3.8},
    {'time': 0.5, 'x': 2.8, 'y': 4.2, 'z': 5.3, 'temp': 22.9, 'voltage': 3.7}
]

# Irrelevant calibration lookup (distractor)
calibration_map = defaultdict(lambda: 0)
for i in range(10):
    for j in range(i + 1, 10):
        calibration_map[(i, j)] = (i * j) % 7

# Unused path planner stub (dead code path)
def plan_route_legacy(nodes):
    if len(nodes) < 2:
        return []
    route = [nodes[0]]
    while len(route) < len(nodes):
        remaining = set(nodes) - set(route)
        next_node = min(remaining, key=lambda x: (x[0] - route[-1][0])**2 + (x[1] - route[-1][1])**2)
        route.append(next_node)
    return route

# Red herring function with misleading name (does not affect final result)
def compute_thermal_drift(logs):
    total_drift = 0.0
    for entry in logs:
        temp = entry['temp']
        voltage = entry['voltage']
        drift = math.sin(temp) * (voltage - 3.5)
        total_drift += abs(drift)
    return total_drift * 1000  # unused result

# Real processing begins here — extract trajectory points
trajectory_points = [(entry['x'], entry['y'], entry['z']) for entry in telemetry_stream]

# Compute displacement vectors between consecutive points
vectors = []
for i in range(1, len(trajectory_points)):
    prev = trajectory_points[i-1]
    curr = trajectory_points[i]
    dx = curr[0] - prev[0]
    dy = curr[1] - prev[1]
    dz = curr[2] - prev[2]
    vectors.append((dx, dy, dz))

# Calculate vector magnitudes and cumulative direction change
magnitudes = [math.sqrt(dx**2 + dy**2 + dz**2) for dx, dy, dz in vectors]
total_length = sum(magnitudes)
direction_changes = []
for i in range(1, len(vectors)):
    v1, v2 = vectors[i-1], vectors[i]
    dot = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
    norm_v1 = math.sqrt(v1[0]**2 + v1[1]**2 + v1[2]**2)
    norm_v2 = math.sqrt(v2[0]**2 + v2[1]**2 + v2[2]**2)
    if norm_v1 == 0 or norm_v2 == 0:
        angle = 0
    else:
        cos_angle = max(-1, min(1, dot / (norm_v1 * norm_v2)))
        angle = math.acos(cos_angle)
    direction_changes.append(angle)

total_direction_change = sum(direction_changes)

# Simulate optimization pass (finds smoothed path)
optimized_path = []
cursor = 0
smoothing_window = 2
while cursor < len(trajectory_points):
    window_slice = trajectory_points[cursor:cursor+smoothing_window+1]
    avg_x = sum(p[0] for p in window_slice) / len(window_slice)
    avg_y = sum(p[1] for p in window_slice) / len(window_slice)
    avg_z = sum(p[2] for p in window_slice) / len(window_slice)
    optimized_path.append((avg_x, avg_y, avg_z))
    cursor += smoothing_window

# Distractor: unused combinatorial analysis of sensor pairs
sensor_pairs = list(combinations(['temp', 'voltage', 'x', 'y', 'z'], 2))
pair_correlations = defaultdict(float)
for pair in sensor_pairs:
    val1_sum = sum(entry[pair[0]] for entry in telemetry_stream)
    val2_sum = sum(entry[pair[1]] for entry in telemetry_stream)
    pair_correlations[pair] = (val1_sum * val2_sum) % 100

# Another red herring: cyclic iterator over dummy commands
command_cycle = cycle(['IDLE', 'ARM', 'TAKEOFF', 'NAV', 'LOITER', 'LAND'])
command_sequence = [next(command_cycle) for _ in range(len(telemetry_stream))]

# Telemetry log enriched with derived fields
telemetry_log = []
for i, entry in enumerate(telemetry_stream):
    new_entry = entry.copy()
    if i > 0:
        speed = magnitudes[i-1] / 0.1  # delta_t = 0.1
        new_entry['speed'] = speed
    else:
        new_entry['speed'] = 0.0
    new_entry['regime'] = 'CRUISE' if new_entry.get('speed', 0) > 3.0 else 'HOVER'
    telemetry_log.append(new_entry)

# Critical function that computes final diagnostic metric
def analyze_metrics(path, log):
    # Metric 1: Path efficiency (actual distance vs straight-line)
    total_opt_path = 0.0
    for i in range(1, len(path)):
        dx = path[i][0] - path[i-1][0]
        dy = path[i][1] - path[i-1][1]
        dz = path[i][2] - path[i-1][2]
        total_opt_path += math.sqrt(dx**2 + dy**2 + dz**2)
    
    start = path[0]
    end = path[-1]
    direct_distance = math.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2 + (end[2]-start[2])**2)
    
    if direct_distance == 0:
        efficiency = 1.0
    else:
        efficiency = direct_distance / total_opt_path
    
    # Metric 2: System stability based on voltage variance
    voltages = [entry['voltage'] for entry in log]
    mean_voltage = sum(voltages) / len(voltages)
    variance = sum((v - mean_voltage)**2 for v in voltages) / len(voltages)
    stability = 1 / (1 + variance * 10)  # higher variance → lower stability
    
    # Metric 3: Navigation complexity from direction changes in original
    complexity = total_direction_change * 10
    
    # Final weighted diagnostic score
    diagnostic_score = (efficiency * 0.5) + (stability * 0.3) - (complexity * 0.01)
    
    # Apply nonlinear correction based on number of optimization segments
    segment_count = len(optimized_path)
    correction_factor = math.tanh(segment_count / 5.0)
    
    final_score = diagnostic_score * correction_factor
    
    # Distractor: update unused global
    global calibration_map
    calibration_map['diagnostic_run'] += 1
    
    return round(final_score * 100000) / 100000  # normalize to 5 decimal places

# Execute critical statement
final_diagnostic = analyze_metrics(optimized_path, telemetry_log)
print(f"Target result: {final_diagnostic}")