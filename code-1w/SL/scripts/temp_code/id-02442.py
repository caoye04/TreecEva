import math

# Simulated telemetry data from satellite subsystems
telemetry_stream = [145, 273, 91, 88, 204, 117, 301, 64, 182]

# Irrelevant calibration constants (distractors)
CALIB_FACTOR_A = 0.87
CALIB_FACTOR_B = 1.03
REFERENCE_OFFSET = 42
MAX_BUFFER_SIZE = 512
TEMPORAL_DAMPING = 0.91

# Noise filter using moving window (unused in final computation)
def apply_noise_filter(signal):
    filtered = []
    for i in range(len(signal)):
        start = max(0, i - 2)
        end = min(len(signal), i + 3)
        filtered.append(sum(signal[start:end]) // (end - start))
    return filtered

# Redundant transformation function (dead code path)
def legacy_transform(x):
    return (x ** 0.5) * 2.3

# Core processing pipeline
threshold = 100
data_log = [x for x in telemetry_stream if x > 75]  # Filter valid readings

# Misleading intermediate metrics (distractors)
spike_count = 0
rolling_avg = 0
baseline_estimate = sum(data_log) / len(data_log)

# Simulated fault detection with false branches
detected_faults = []
for val in data_log:
    if val > 250 and val % 2 == 1:
        detected_faults.append(val)
        spike_count += 1  # This updates but isn't used later
    elif val < 100:
        rolling_avg += val  # Partial accumulation, misleading

# Unused diagnostic checksum
checksum = 0
for i, v in enumerate(data_log):
    checksum ^= (v + i) % 257

# Critical processing function with lambda and list comprehension
compute_weight = lambda x: math.log(x) if x > 100 else math.sqrt(x * 1.5)

# Data transformation with nested logic
transformed = [
    int(compute_weight(x) * (1.1 if x % 2 == 0 else 0.9))
    for x in data_log
]

# Conditional branching with early exit red herring
if len(transformed) > 8:
    efficiency_score = -1  # Dead branch (not taken)
else:
    temp_sum = sum(transformed[i] for i in range(len(transformed)) if i % 2 == 0)
    adjustment_factor = 1.2 if len(detected_faults) else 0.85
    
    # Core calculation buried in distractions
    raw_efficiency = temp_sum * adjustment_factor
    
    # Secondary filtering that looks important but is not
    secondary_peaks = [x for x in transformed if x > 40]
    
    # Final non-linear scaling (key step)
    normalized = raw_efficiency / math.log(baseline_estimate + 1)
    efficiency_score = int(normalized * 1.75)

# Another decoy function (never called)
def simulate_redundancy_check(data):
    return [x ^ REFERENCE_OFFSET for x in data][::-1]

# Final output assignment - key execution point
final_output = process_metrics(data_log, threshold)

# Simulate missing function with inline equivalent to avoid import
def process_metrics(log, thresh):
    filtered = [x for x in log if x > thresh]
    weights = [math.log(x) * 0.8 for x in filtered]
    score = int(sum(weights) * 2.1)
    return score

# Print target result
Result: {efficiency_score}