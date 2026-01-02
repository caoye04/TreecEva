import math

# Simulated sensor array data (irrelevant but plausible)
sensor_readings = [14.2, 18.7, 22.1, 19.5, 25.3, 30.0, 28.4, 26.8]
noise_floor = 1.3
calibration_sequence = [math.sin(x / 3) for x in range(len(sensor_readings))]
adjusted_readings = [r + noise_floor * c for r, c in zip(sensor_readings, calibration_sequence)]

# Data transformation pipeline (partial red herring)
filtered_data = []
for i, val in enumerate(adjusted_readings):
    if i % 2 == 0:
        filtered_data.append(val * 0.9)
    else:
        filtered_data.append(val * 1.1)

# Irrelevant statistical analysis (distractor)
mean_filtered = sum(filtered_data) / len(filtered_data)
variance = sum((x - mean_filtered) ** 2 for x in filtered_data) / len(filtered_data)
std_deviation = math.sqrt(variance)
outlier_threshold = mean_filtered + 2 * std_deviation

# System health monitoring with decoy logic
system_flags = [False, True, False, True, True]
flag_interpretation = {i: (f"ERR_{i}" if i % 2 else "OK") for i in range(5)}
active_errors = [flag_interpretation[i] for i, f in enumerate(system_flags) if f]
error_count = len(active_errors)  # Looks important, but not used later

# Core diagnostic sequence (actual relevant logic starts here)
base_metrics = [3, 7, 2, 8, 5]
running_total = 0
aggregate_metrics = []

for idx, metric in enumerate(base_metrics):
    if metric > 4:
        running_total += metric * (idx + 1)
    elif metric == 2:
        running_total += 5
    else:
        running_total -= 1
    
    # Conditional expression used (required feature)
    status_factor = 2 if running_total > 15 else 1
    intermediate = running_total * status_factor
    
    # More distractions: unused transformation
    temp_adjusted = intermediate * 1.05 if idx % 3 == 0 else intermediate * 0.98
    
    aggregate_metrics.append(intermediate)

# Secondary system state calculation (misleading path)
candidate_values = []
for x in range(3):
    candidate = (x + 1) * aggregate_metrics[x]
    candidate_values.append(candidate)

# Dead code path (never executed due to prior logic)
dummy_aggregate = []
if len(candidate_values) > 10:
    for v in candidate_values:
        dummy_aggregate.append(v // 2)

# Actual critical variables
phase_offset = 4
system_health = 0

# Determine system health using enumerate and conditional (required features)
for i, reading in enumerate(sensor_readings[:5]):
    if reading > 20 and i % 2 == 1:
        system_health += 1
    elif reading < 19 and i == 0:
        system_health -= 1

# Key computation hidden among distractions
final_diagnostic = aggregate_metrics[-1] + phase_offset * system_health

# Output required result
print(f"Result: {final_diagnostic}")