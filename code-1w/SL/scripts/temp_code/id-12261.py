from collections import defaultdict, Counter

# Simulated sensor array data processing with diagnostic validation
sensor_data = [78, 85, None, 92, 74, 88, None, 95, 82, 73]
threshold = 80
anomaly_flags = []
running_total = 0
valid_count = 0

# Irrelevant statistical placeholder (distractor)
mean_placeholder = 0
weighting_curve = [0.1, 0.3, 0.5, 0.7, 0.9]

# Primary data cleaning and anomaly detection
for reading in sensor_data:
    if reading is not None:
        running_total += reading
        valid_count += 1
        if reading < threshold:
            anomaly_flags.append(True)
        else:
            anomaly_flags.append(False)

# Compute baseline metrics
if valid_count > 0:
    mean_placeholder = running_total / valid_count  # Not used later (red herring)

# Simulate historical anomaly patterns (unused legacy path - dead code)
historical_trend = defaultdict(int)
for i, flag in enumerate(anomaly_flags):
    historical_trend[i % 3] += 1  # Distractor computation

# Anomaly clustering analysis (misleading intermediate)
cluster_analysis = Counter()
for i in range(len(anomaly_flags)):
    cluster_key = 'low' if anomaly_flags[i] else 'normal'
    cluster_analysis[cluster_key] += 1

# Unused normalization factor (decoy)
normalization_bias = sum(weighting_curve) / 5

# Critical signal conditioning
active_anomalies = sum(anomaly_flags)
baseline_reference = running_total // valid_count  # Integer division for discrete scaling

# Secondary system health check (irrelevant subsystem)
system_health_log = [{'status': 'OK', 'code': 200} for _ in range(5)]
decoy_aggregate = 0
for entry in system_health_log:
    if entry['code'] == 200:
        decoy_aggregate += 10

# Tertiary calibration sequence (fake dependency)
calibration_chain = [x * 0.5 for x in weighting_curve if x > 0.2]
offset_correction = len(calibration_chain) * 2

# Core logic disguised among distractors
aggregate_score = baseline_reference * 100  # Scale base performance

# Conditional adjustment based on anomaly density
if active_anomalies > 2:
    correction_factor = -5
else:
    correction_factor = 3

# Weighted impact model (key path)
anomaly_weight = len(anomaly_flags) - active_anomalies

# DEAD CODE PATH: Legacy fallback (never executed)
legacy_mode = False
if legacy_mode:
    final_diagnostic = 999
else:
    # This is the actual execution path
    final_diagnostic = aggregate_score + correction_factor * anomaly_weight

# Print result as required
print(f"Target result: {final_diagnostic}")