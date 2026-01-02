import math

# Simulated sensor data and diagnostic system for a spacecraft subsystem
sensor_a = 5.7
sensor_b = 3.2
sensor_c = 8.9

# Irrelevant calibration constants (distractors)
calib_x = 0.987
kalman_factor = 1.023
temp_offset = -0.45
voltage_gain = 2.1
baseline_drift = 0.003

# Data preprocessing with red herring transformations
preprocessed_a = round(sensor_a ** 1.5, 4)
preprocessed_b = abs(sensor_b * math.sin(math.pi / 6))
preprocessed_c = max(0, sensor_c - 7.1)

# Decoy health check function (never called)
def legacy_health_check(data):
    return sum(data) / len(data) if data else 0

# Unused intermediate arrays (dead code paths)
historical_readings = [4.5, 5.1, 5.7, 6.0, 5.8]
anomaly_flags = [False] * 5
rolling_average = 5.42

# Real-time anomaly detection using modular arithmetic and thresholds
def detect_anomalies(s_a, s_b, s_c):
    score_a = int((s_a * 10) % 7)
    score_b = int((s_b * 10) % 5)
    score_c = int((s_c * 10) % 9)
    
    # Logical evaluation with short-circuiting (critical path)
    if score_a < 3 and score_b > 1 or not (score_c == 0):
        return True
    return False

# Complex lambda-based transformation chain (core logic)
data_normalizer = lambda x: x if x <= 7 else 7 + (x - 7) / 2
normalized_a = data_normalizer(sensor_a)
normalized_b = data_normalizer(sensor_b)
normalized_c = data_normalizer(sensor_c)

# Bitwise interference pattern analysis (mixed paradigm)
interference_code = int.from_bytes(b'INT', 'big')
modulated_signal = interference_code ^ int(normalized_a * 100)
checksum = (modulated_signal >> 3) & 0xFF

# Distractor: fake fusion algorithm
fusion_weight = 0.67
dummy_fusion = (normalized_a * 0.3 + normalized_b * 0.3 + normalized_c * 0.4) * fusion_weight

# Health metric computation – only this matters
health_metrics = [
    round(normalized_a, 3),
    round(normalized_b, 3),
    round(normalized_c, 3)
]

# Core analyzer function with early returns and nested logic
def system_status_analyzer(metrics):
    if not metrics:
        return -999

    m1, m2, m3 = metrics

    # First-level checks
    if m1 < 4.0 or m2 < 2.0:
        return 101

    # Second-level composite logic
    base_risk = 0
    if m1 > 5.5:
        base_risk += 3
    if m2 > 3.0:
        base_risk += 2
    if m3 > 7.5:
        base_risk += 4

    # Third-level: modular arithmetic dependency
    adjustment = (int(m1 * 10) + int(m2 * 10)) % 6

    # Fourth-level: logical combination with bit flag
    flags = 0
    if m1 + m2 > 8.0:
        flags |= 1
    if m2 + m3 > 10.0:
        flags |= 2
    if m1 + m3 > 12.0:
        flags |= 4

    # Final computation – critical execution point
    if flags & 1 and adjustment > 3:
        final_score = (base_risk * 17) + adjustment
    elif flags & 4:
        final_score = (base_risk * 12) - adjustment
    else:
        final_score = (base_risk * 15)

    # Additional transformation via lambda (used)
    scaler = lambda x: x * 1.25 if x < 50 else x * 1.1
    return int(scaler(final_score))

# Execution point of interest
final_diagnostic = system_status_analyzer(health_metrics)

# Print result as required
print(f"Target result: {final_diagnostic}")