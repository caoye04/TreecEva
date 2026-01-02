import math

# Simulated sensor array data and diagnostic system
def generate_sensor_readings():
    base_values = [i * 1.5 for i in range(10)]
    noise = [0.1, -0.2, 0.3, -0.1, 0.05, -0.15, 0.25, -0.05, 0.1, 0.0]
    return [base_values[i] + noise[i] for i in range(10)]

def apply_calibration(readings):
    calibrated = []
    factor = 1.02
    offset = -0.05
    for val in readings:
        calibrated.append((val * factor) + offset)
    # Irrelevant transformation (dead path)
    temp_result = [x ** 0.5 for x in calibrated if x > 0]
    return calibrated

def filter_outliers(data, limit=2.0):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    filtered = [x for x in data if abs(x - mean_val) <= limit * std_dev]
    # Distractor: unused computation
    outlier_count = len(data) - len(filtered)
    scaling_factor = 1.1 if outlier_count > 0 else 1.0
    return filtered

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 6)

def transform_frequency_domain(signal):
    # Simulated FFT-like transformation (simplified)
    transformed = []
    n = len(signal)
    for k in range(n):
        real = sum(signal[i] * math.cos(2 * math.pi * k * i / n) for i in range(n))
        imag = sum(-signal[i] * math.sin(2 * math.pi * k * i / n) for i in range(n))
        magnitude = (real ** 2 + imag ** 2) ** 0.5
        transformed.append(magnitude)
    # Decoy normalization (not used later)
    max_mag = max(transformed)
    normalized = [m / max_mag for m in transformed] if max_mag != 0 else transformed
    return transformed

def detect_anomalies(pattern):
    anomalies = []
    for i in range(1, len(pattern) - 1):
        if pattern[i] > pattern[i-1] and pattern[i] > pattern[i+1]:
            anomalies.append(i)
    # Unused heuristic
    suspicious_ratio = len(anomalies) / len(pattern) if pattern else 0
    return anomalies

def rolling_average(series, window=3):
    smoothed = []
    for i in range(len(series)):
        start = max(0, i - window + 1)
        end = i + 1
        avg = sum(series[start:end]) / (end - start)
        smoothed.append(avg)
    return smoothed

# Irrelevant auxiliary function (decoy)
def predict_trend(data):
    if len(data) < 2:
        return 0
    slope_sum = 0
    for i in range(1, len(data)):
        slope_sum += (data[i] - data[i-1])
    return slope_sum / (len(data) - 1)

# Core processing chain
raw_data = generate_sensor_readings()
calibrated_data = apply_calibration(raw_data)
filtered_data = filter_outliers(calibrated_data)
smoothed_data = rolling_average(filtered_data, window=2)

# Frequency analysis branch (partially relevant)
freq_components = transform_frequency_domain(smoothed_data)
entropy_score = compute_entropy(freq_components)

# Anomaly detection (distractor - result not used directly)
peaks = detect_anomalies(smoothed_data)

# Real signal processing begins here
processed_data = [round(x * 1.75, 4) for x in freq_components[:8]]  # Truncate and scale

# Lambda-based dynamic threshold
threshold_func = lambda x: 5.0 if x > 10 else (3.5 if x > 6 else 2.0)

# Misleading intermediate calculation
aggregate_metric = sum(math.sin(x) for x in processed_data) * entropy_score

# Actual analysis function with early returns and logic branching
def analyze_signal(signal, threshold_strategy):
    if not signal:
        return -1
    
    # Step 1: Normalize around median
    sorted_sig = sorted(signal)
    median = sorted_sig[len(sorted_sig)//2]
    normalized = [abs(x - median) for x in signal]
    
    # Step 2: Apply adaptive amplification
    amplified = []
    for val in normalized:
        if val < 1.0:
            amplified.append(val * 3.2)
        elif val < 3.0:
            amplified.append(val * 2.1)
        else:
            amplified.append(val * 1.5)
    
    # Step 3: Filter by dynamic threshold
    dyn_thresh = threshold_strategy(sum(amplified) / len(amplified))
    passed = [x for x in amplified if x >= dyn_thresh]
    
    # Step 4: Bit manipulation for integrity check (irrelevant but plausible)
    checksum = 0
    for x in passed:
        int_part = int(abs(x))
        checksum ^= (int_part & 0xFF)  # Use lower byte
        checksum = (checksum << 1) | (checksum >> 7)  # Rotate left
    
    # Step 5: Conditional aggregation with short-circuit logic
    if len(passed) < 3 or not passed:\
       or (len([x for x in passed if x > dyn_thresh * 1.2]) == 0):
        return 404
    
    primary_sum = sum(passed)
    adjustment = 0.0
    
    # Complex conditional adjustment
    if primary_sum > 20.0:
        if dyn_thresh > 3.0:
            adjustment = -2.5
        elif dyn_thresh > 2.0:
            adjustment = 1.8
        else:
            adjustment = 0.5
    elif primary_sum > 10.0:
        adjustment = 3.2
    else:
        adjustment = -4.0 if checksum % 2 == 0 else 4.0
    
    # Final diagnostic score
    final_score = primary_sum + adjustment
    
    # Early termination red herring (never reached due to prior logic)
    if final_score < 0:  # This won't happen given adjustments
        return 0
        extra_comp = math.log(final_score)  # Dead code
    
    return round(final_score, 4)

# Execute key statement
final_diagnostic = analyze_signal(processed_data, threshold_func)
print(f"Target result: {final_diagnostic}")