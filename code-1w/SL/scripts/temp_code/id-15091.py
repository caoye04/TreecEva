from collections import defaultdict, Counter
import math

# Simulated sensor network data processing with diagnostic validation

# Raw sensor inputs (simulated)
sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5']
raw_readings = [
    [14, 17, 13, 21, 16],
    [9, 11, 10, 12, 8],
    [25, 27, 23, 26, 24],
    [31, 29, 33, 30, 32],
    [7, 6, 9, 8, 5]
]

# Irrelevant mapping - distractor
dummy_mapping = {sid: idx * 11 for idx, sid in enumerate(sensor_ids)}

# Initialize processing structures
calibration_factors = defaultdict(float)
reading_stats = defaultdict(list)
consistency_flags = []

# Apply fake calibration model (partly irrelevant)
for i, readings in enumerate(raw_readings):
    base = sum(readings) / len(readings)
    if i % 2 == 0:
        calibration_factors[sensor_ids[i]] = base * 0.85
    else:
        calibration_factors[sensor_ids[i]] = base * 1.15

# Real data path: compute variance and flag outliers
for i, readings in enumerate(raw_readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    reading_stats[sensor_ids[i]] = {'mean': avg, 'variance': variance}

    # Outlier detection heuristic
    high_deviation = any(abs(x - avg) > 0.5 * avg for x in readings)
    consistency_flags.append(not high_deviation)

# Compute redundancy score using zip and enumerate (core step)
redundancy_score = 0
for idx, (flag1, flag2) in enumerate(zip(consistency_flags, consistency_flags[1:])):
    if flag1 == flag2:
        redundancy_score += idx * 3
    else:
        redundancy_score -= 2

# Bit manipulation red herring
decoys = []
for i in range(5):
    val = (i << 3) | (i ^ 7)
    decoys.append(val * 19)  # Unused computation

# Hidden dependency: find dominant pattern using Counter
trend_analysis = []
for readings in raw_readings:
    rounded = [r // 5 * 5 for r in readings]  # Quantize
    counts = Counter(rounded)
    mode_class = counts.most_common(1)[0][0]
    trend_analysis.append(mode_class)

trend_shifts = 0
for a, b in zip(trend_analysis, trend_analysis[1:]):
    trend_shifts += abs(a - b) // 5

# Secondary distraction: unused recursive function
def analyze_residuals(data, level=0):
    if level >= 3 or len(data) == 1:
        return data[0] if data else 0
    mid = len(data) // 2
    left = analyze_residuals(data[:mid], level + 1)
    right = analyze_residuals(data[mid:], level + 1)
    return (left ^ right) + level

# Dead code path - never executed
temporary_fix = False
if temporary_fix:
    adjustment_log = []
    for key in sorted(calibration_factors.keys()):
        adjustment_log.append(math.log(calibration_factors[key]))

# Core logic: determine system health
valid_sensors = sum(1 for f in consistency_flags if f)
aggregate_score = 0

if valid_sensors >= 3:
    aggregate_score += 150
    
    # Use of set operations: detect unique trend classes
    early_trends = set(trend_analysis[:3])
    late_trends = set(trend_analysis[2:])
    common_trends = early_trends & late_trends
    if len(common_trends) >= 2:
        aggregate_score += 42

    # Additional condition based on variance pattern
    variances = [reading_stats[sid]['variance'] for sid in sensor_ids]
    low_var_sensors = sum(1 for v in variances if v < 10)
    if low_var_sensors >= 2:
        aggregate_score += 28

# Distractor: complex but unused bitwise aggregation
system_signature = 0
for i, v in enumerate(variances):
    system_signature ^= int(v) & (0xFF << (i % 4))

# Threshold offset computed via multiple paths (one valid)
offset_basis = len([f for f in consistency_flags if f])
threshold_offset = 0

if offset_basis == 5:
    threshold_offset = 11
elif offset_basis >= 3:
    threshold_offset = 7
else:
    threshold_offset = -5

# Critical assignment - target execution point
final_diagnostic = aggregate_score + threshold_offset

# Print result as required
print(f"Result: {final_diagnostic}")