def transform_sequence(seq, mode=0):
    if mode == 0:
        return [x ** 2 - x for x in seq if x % 2 == 1]
    elif mode == 1:
        return [x + 10 for x in seq if x < 50]
    else:
        return [x for x in seq if x > 0]

# Sensor simulation data (irrelevant path)
sensor_log = [12, 15, 18, 21, 24, 27, 30]
calibration_offset = sum([x for x in sensor_log if x % 3 == 0]) // len(sensor_log)
adjusted_readings = [x - calibration_offset for x in sensor_log]

# Legacy system diagnostics (dead code path)
def legacy_diagnostics(data):
    total = 0
    for item in data:
        if item > 20:
            total += item * 0.75
    return int(total // 2)

# Unused diagnostic function
def compute_health_score(metrics):
    base = sum(metrics) / len(metrics)
    penalty = 0
    for val in metrics:
        if val < 10:
            penalty += 5
    return max(0, base - penalty)

# Real processing begins here
raw_data = [8, 12, 5, 19, 3, 11, 14, 7]
filtered_data = [x for x in raw_data if x > 6]
sorted_data = sorted(filtered_data, reverse=True)
doubled_pairs = [(x, x * 2) for x in sorted_data]

# Misleading transformation chain
shadow_copy = doubled_pairs[:]
for i in range(len(shadow_copy)):
    a, b = shadow_copy[i]
    shadow_copy[i] = (a + 1, b - 1)

# Actual relevant computation
processed_data = transform_sequence(sorted_data, mode=0)

# Decoy set operations with irrelevant analysis
temp_set_1 = {x % 7 for x in raw_data}
temp_set_2 = {x % 5 for x in filtered_data}
decoys = temp_set_1.symmetric_difference(temp_set_2)
side_analysis = len(decoys) * 3 + sum(temp_set_1.intersection(temp_set_2))

# Threshold logic using set
threshold_set = {2, 6, 12, 56, 72}
backup_thresholds = {10, 20, 30}  # unused

# Core analysis function
def analyze_readings(readings, limits):
    count = 0
    history = []
    for val in readings:
        transformed = (val * 3) + 1
        if transformed > 20:
            history.append(transformed)
        if val in limits:
            count += 1
    # Secondary condition check
    result = 0
    for h in history:
        if h % 4 == 0:
            result += h // 4
        else:
            result += h % 7
    return result + count

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_set)
print(f"Target result: {final_diagnostic}")