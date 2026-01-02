import math

# Simulated sensor array diagnostics with embedded logic chain
sensor_readings = [3.2, 4.1, 2.8, 5.6, 7.3, 6.9, 8.1, 9.4, 10.2, 8.7, 7.5, 6.3]
baseline_offset = 2.5

# Irrelevant calibration constants (distractor)
calibration_map = {"alpha": 0.98, "beta": 1.02, "gamma": 0.89, "delta": 1.11}
diagnostic_log = []

# Preprocessing stage: normalize and detect deviations
normalized = [x - baseline_offset for x in sensor_readings]
deviations = [abs(x) for x in normalized if x > 0]

# Misleading secondary path: entropy calculation (unused)
def compute_entropy(data):
    total = sum(data)
    probs = [v / total for v in data]
    return -sum(p * math.log2(p) for p in probs if p > 0)

entropy_diagnostic = compute_entropy(deviations[:5])  # Dead-end computation

# Signal windowing via slicing - relevant operation
signal_windows = [deviations[i:i+4] for i in range(0, len(deviations), 4)]
active_segments = []

for window in signal_windows:
    if len(window) >= 3:
        segment_avg = sum(window) / len(window)
        if segment_avg > 2.0:
            # Bit manipulation red herring
            encoded = 0
            for val in window:
                encoded ^= int(val * 10)  # XOR chain with no impact
            active_segments.append(segment_avg)

# Decoy function: performs complex but unused transformation
def transform_series(series):
    transformed = []
    for i, x in enumerate(series):
        phase = math.sin(i * math.pi / 4)
        transformed.append(x * phase + (i % 3))
    return [round(t, 2) for t in transformed[::-1]]

transformed_diagnostics = transform_series(active_segments)  # Computed but unused

# Core logic buried in abstraction
anomaly_series = [max(seg, default=0) for seg in signal_windows if seg]

# Threshold filter based on dynamic condition
threshold_reference = [1.8, 2.1, 1.9, 2.3]
threshold_filter = sum(threshold_reference) / len(threshold_reference)

# Primary interference: nested filtering with redundant checks
def validate_threshold(value, thresholds, tolerance=0.15):
    return any(abs(value - t) <= tolerance * t for t in thresholds)

# Heavily distracted aggregation function
def aggregate_anomalies(series, threshold):
    temp_results = []
    cumulative_shift = 0
    
    for idx, point in enumerate(series):
        # Spurious conditional branch (never triggers due to data)
        if point < 0:
            cumulative_shift -= 1
        elif point > threshold:
            # Real logic path
            adjusted = point * (1 + (idx % 3) * 0.1)
            temp_results.append(adjusted)
            
            # Fake state update
            if idx % 2 == 0:
                dummy_state = (adjusted ** 2) % 7
        else:
            # Alternate dead path
            temp_results.append(threshold * 0.5)
    
    # Final reduction using min/max/avg pattern
    if temp_results:
        peak = max(temp_results)
        floor = min(temp_results)
        average = sum(temp_results) / len(temp_results)
        # Key deterministic combination
        return round((peak + average * 2) - floor, 4)
    return 0.0

# Execution point of interest
final_diagnostic = aggregate_anomalies(anomaly_series, threshold_filter)

# Output requirement
print(f"Target result: {final_diagnostic}")