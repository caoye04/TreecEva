def monitor_system_integrity(base_offset, thresholds):
    operational_modes = {1: 'nominal', 2: 'elevated', 3: 'critical'}
    diagnostic_log = []
    temp_cache = []

    for i in range(len(thresholds)):
        if thresholds[i] > base_offset:
            diagnostic_log.append((i, operational_modes[2]))
            temp_cache.append(i * 2)
        elif thresholds[i] == base_offset:
            diagnostic_log.append((i, operational_modes[1]))
            temp_cache.append(i + 1)
        else:
            diagnostic_log.append((i, operational_modes[1]))
            temp_cache.append(-1)  # placeholder

    # Irrelevant transformation
    reversed_cache = [x for x in reversed(temp_cache)]
    sum_check = sum(reversed_cache[:3]) if len(reversed_cache) > 3 else 0

    status_flags = set()
    for entry in diagnostic_log:
        phase_id, mode = entry
        if mode == 'critical':
            status_flags.add(phase_id)

    # Decoy calculation with no impact
    decoy_aggregate = 0
    for x in temp_cache:
        decoy_aggregate += x ** 2
        if decoy_aggregate > 1000:
            decoy_aggregate = 0

    return status_flags


def compute_calibration_sequence(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq[-1] if n > 1 else 0

# Unused helper function (red herring)
def validate_phase_integrity(*args):
    total = 0
    for arg in args:
        total += arg % 7
    return total // 2

# Simulated sensor readings (distraction data)
sensor_readings = [45, 67, 89, 34, 78]
baseline_adjustment = 65

# Real execution begins here
config_matrix = [
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0]
]

# Irrelevant matrix transformation
transposed = [[config_matrix[j][i] for j in range(len(config_matrix))] for i in range(len(config_matrix[0]))]
determinant_approx = transposed[0][0] * transposed[1][1] - transposed[0][1] * transposed[1][0]

# Core logic disguised among distractions
active_thresholds = [50, 70, 65, 80, 60]
base_reference = 65

# Key intermediate structure
phase_interlocks = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5
}

# Misleading aggregation
interlock_sum = 0
for key, val in phase_interlocks.items():
    interlock_sum += ord(key.lower()) % val

# Actual relevant call chain
detected_anomalies = monitor_system_integrity(base_reference, active_thresholds)

# Complex dummy loop with side effects that don't matter
history_buffer = []
for anomaly in detected_anomalies:
    shifted = (anomaly + 5) % 8
    history_buffer.append(shifted)
    if shifted > 4:
        history_buffer.append(shifted // 2)

# Core assignment - the real answer builds here
operational_phases = list(detected_anomalies)

# Secondary irrelevant computation
fibonacci_diagnostic = compute_calibration_sequence(10)

# Set-based analysis with meaningful but non-obvious logic
def analyze_status(phases):
    expected_phases = {0, 1, 2, 3, 4}
    missing_phases = expected_phases - set(phases)
    anomaly_count = len(phases)
    completeness_score = len(expected_phases.intersection(set(phases)))

    # Modular arithmetic used meaningfully
    hash_value = 0
    for p in phases:
        hash_value = (hash_value * 7 + p) % 13

    # Critical computation path
    score_factor = 1
    if len(missing_phases) >= 3:
        score_factor = -2
    elif len(missing_phases) == 0:
        score_factor = 3
    else:
        score_factor = 2

    # Dead branch - never reached due to logic above
    if completeness_score > 10:  # Impossible condition
        score_factor *= 10

    # Final result derived from multiple reasoning steps
    final_score = (anomaly_count * 100) + (hash_value * score_factor) + len(missing_phases)

    # Decoy variable
    temp_result = (completeness_score ** 2) + fibonacci_diagnostic

    return final_score

# Execution point of interest
final_diagnostic = analyze_status(operational_phases)

# Print required output
print(f"Result: {final_diagnostic}")