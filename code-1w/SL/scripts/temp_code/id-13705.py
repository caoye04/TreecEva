import math

# Simulated sensor data processing for a climate monitoring system
def collect_sensor_data():
    raw_readings = [23.4, 25.1, 19.8, 24.3, 20.2, 26.7, 22.9, 18.5, 27.1, 21.6]
    calibration_offset = 1.2
    adjusted = [x + calibration_offset for x in raw_readings]
    outliers = {x for x in adjusted if x > 28 or x < 19}
    filtered = [x for x in adjusted if x not in outliers]
    return filtered

# Auxiliary function - appears important but only used once
def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)

# Red herring: unused function that looks relevant
def predict_trend(data):
    trend_score = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend_score += (data[i] - data[i-1]) * 1.5
        elif data[i] < data[i-1]:
            trend_score -= (data[i-1] - data[i]) * 0.8
    return trend_score

# Misleading transformation chain
def apply_filters(signal):
    processed = []
    noise_floor = 20.5
    for val in signal:
        if val > noise_floor:
            processed.append(val * 0.95)
        else:
            processed.append(val * 1.05)
    # Double filtering illusion
    secondary = list(map(lambda x: x + 0.3 if x < 22 else x - 0.2, processed))
    return secondary  # Never actually called

# Core analysis logic
def analyze_readings(metrics):
    base_threshold = 21.7
    high_vals = list(filter(lambda x: x > base_threshold, metrics))
    low_vals = [x for x in metrics if x <= base_threshold]
    
    # Distractor computation with intermediate variables
    avg_high = sum(high_vals) / len(high_vals) if high_vals else 0
    avg_low = sum(low_vals) / len(low_vals) if low_vals else 0
    
    deviation_score = 0
    for val in metrics:
        if val > avg_high:
            deviation_score += (val - avg_high) * 1.1
        elif val < avg_low:
            deviation_score -= (avg_low - val) * 0.9
    
    # Complex conditional expression with nested logic
    status_flag = 'ELEVATED' if len(high_vals) > len(low_vals) else 'NORMAL'
    adjustment_factor = 1.3 if status_flag == 'ELEVATED' else 0.8
    
    # Decoy bit manipulation (looks cryptic but deterministic)
    bit_mask = 0b1101
    masked_deviation = int(abs(deviation_score)) & bit_mask
    
    # Critical path: destructuring and tuple unpacking
    summary_stats = (len(metrics), sum(metrics), round(avg_high, 2))
    count, total, peak_avg = summary_stats
    
    # Final diagnostic calculation - depends on multiple prior steps
    baseline = total / count if count > 0 else 0
    final_diagnostic = baseline + (masked_deviation * adjustment_factor)
    
    # Unused dead-end branch with misleading print
    if final_diagnostic > 100:
        overflow_correction = math.log(final_diagnostic)
        final_diagnostic -= overflow_correction  # Never executed
    
    return final_diagnostic

# Irrelevant global constants
MAX_BUFFER_SIZE = 1024
RETRY_LIMIT = 3
TIMEOUT_SEC = 30

# Data flow orchestration
sensor_metrics = collect_sensor_data()
entropy_value = compute_entropy(sensor_metrics)  # Computed but not used in main logic

# Apply false processing path
processed_signal = []
for reading in sensor_metrics:
    if reading > 22.0:
        processed_signal.append(reading * 1.02)
    else:
        processed_signal.append(reading * 0.98)

# Actual key execution point
final_diagnostic = analyze_readings(sensor_metrics)

# Output result as required
print(f"Target result: {final_diagnostic}")