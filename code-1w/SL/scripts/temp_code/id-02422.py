def generate_baseline(size):
    return [i * 0.5 for i in range(size)]

# Irrelevant data generation (distractor)
baseline_data = generate_baseline(100)
scaling_factor = 2.718
offset_correction = sum([x ** 0.5 for x in baseline_data[:10]])

# Real input setup
sensor_readings = [12, 8, 15, 3, 9, 11, 7]
calibration_sequence = list(map(lambda x: (x + 1) ** 2 % 13, sensor_readings))

# Misleading transformation chain (dead path)
transformed = []
for val in calibration_sequence:
    temp = val * scaling_factor
    if temp > 20:
        transformed.append(int(temp) // 2)
    else:
        transformed.append(int(temp) + 3)

# Decoy function that's never called
def analyze_anomaly(seq):
    anomalies = 0
    for i in range(len(seq)):
        if seq[i] ^ i == 0:
            anomalies += 1
    return anomalies

# Actual processing begins here
threshold_mask = [1 if x > 5 else 0 for x in calibration_sequence]

# Bit manipulation red herring
bit_accumulator = 0
for i, val in enumerate(threshold_mask):
    bit_accumulator |= (val << i)  # Unused result

# Conditional filtering with slicing distraction
active_segments = calibration_sequence[::2]  # Every other element

# Linear search disguised as validation
def find_first_exceeding(seq, limit):
    for i in range(len(seq)):
        if seq[i] > limit:
            return i
    return -1

limit_check_1 = find_first_exceeding(calibration_sequence, 10)
limit_check_2 = find_first_exceeding(calibration_sequence, 15)

# Core logic hidden among noise
rolling_window = []
for i in range(len(active_segments) - 1):
    rolling_window.append(active_segments[i] * active_segments[i + 1])

# String-based decoy (uses string method)
status_log = "System nominal"
status_flags = status_log.upper().split()  # Distracting use of string methods

# More irrelevant state
checksum = 0
for ch in status_log:
    checksum ^= ord(ch)

# Actual diagnostics calculation
def compute_health_score(seq):
    score = 0
    for x in seq:
        if x % 3 == 0:
            score += x // 3
        elif x % 2 == 0:
            score -= x // 4
        else:
            score += x % 5
    return score

# Diagnostics built from filtered data
diagnostics = compute_health_score(active_segments)

# Key computation buried in abstraction
final_diagnostic = process_metrics(calibration_sequence, diagnostics)

# True definition of process_metrics (was not defined earlier)
def process_metrics(seq, base_diag):
    weighted_sum = 0
    for i, val in enumerate(seq):
        if i % 2 == 0 and val < 12:
            weighted_sum += val * (i + 1)
        elif val >= 12:
            weighted_sum -= (val % 10) * 2
    return base_diag + weighted_sum // 2

# Recompute final_diagnostic correctly now that function is defined
final_diagnostic = process_metrics(calibration_sequence, diagnostics)
print(f"Result: {final_diagnostic}")