import math

# Simulated sensor array data with noise and calibration offsets
data_stream = [14, 17, 23, 19, 12, 27, 31, 16, 28, 21]

calibration_factor = 0.89
noise_floor = 2.1
baseline_offset = 15

# Irrelevant auxiliary metrics (distractors)
system_uptime = 1278  # seconds
packet_loss_rate = 0.0034
redundant_checksum = sum([len(str(x)) for x in data_stream])

# Misleading intermediate transformation (dead path)
def deprecated_normalization(arr):
    return [x / max(arr) for x in arr]

# Unused but plausible helper function (decoy)
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

# Core processing pipeline
filtered_data = [x for x in data_stream if x > baseline_offset]
adjusted_readings = [(x - baseline_offset) * calibration_factor for x in filtered_data]

# Bit manipulation for error detection (partially relevant red herring)
error_flags = 0
for val in data_stream:
    error_flags ^= int(val)  # Cumulative XOR (looks important)
    error_flags = error_flags & 0xFF  # Clamp to 8 bits

# Simulated diagnostic thresholds
warning_level = 8.5
critical_level = 12.0

# Counting logic with grouping by severity
mild_anomalies = 0
severe_anomalies = 0
for reading in adjusted_readings:
    if warning_level <= reading < critical_level:
        mild_anomalies += 1
    elif reading >= critical_level:
        severe_anomalies += 1

# Higher-order function for dynamic threshold filtering (lambda use)
adaptive_filter = lambda threshold: [x for x in adjusted_readings if x > threshold]

# Apply filter above critical level to isolate significant events
significant_events = adaptive_filter(critical_level)

# Composite health score (misleading metric)
health_score = len(significant_events) * 3.7 + (10 - severe_anomalies)

# Auxiliary timing simulation (irrelevant)
timing_intervals = [0.23, 0.18, 0.21, 0.25]
latency_jitter = sum([(t - 0.2)**2 for t in timing_intervals])

# Primary analysis function (core logic)
def analyze_readings(readings):
    if not readings:
        return 0.0
    
    # Nested logic with multiple steps
    squared_sum = sum([x**2 for x in readings])
    mean_square = squared_sum / len(readings)
    rms_value = math.sqrt(mean_square)
    
    # Additional transformation
    log_enhanced = math.log(rms_value + 1) * 4.2
    
    # Final nonlinear mapping
    diagnostic_index = (log_enhanced ** 1.5) - 6.3
    
    return diagnostic_index

# Data preprocessing step
processed_data = []
for val in adjusted_readings:
    processed_data.append(abs(val) + noise_floor)

# Critical execution point
final_diagnostic = analyze_readings(processed_data)

# Print result as required
print(f"Target result: {final_diagnostic}")