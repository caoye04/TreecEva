import math

# Simulated sensor data processing for a biomedical device
def preprocess_readings(raw_signals):
    filtered = [x for x in raw_signals if abs(x) > 0.1]
    baseline = sum(filtered) / len(filtered) if filtered else 0.0
    return [x - baseline for x in filtered]

# Irrelevant auxiliary function (distractor)
def compute_fft_magnitude(signal):
    n = len(signal)
    if n == 0:
        return 0.0
    real_part = sum(signal[i] * math.cos(2 * math.pi * i / n) for i in range(n))
    imag_part = sum(signal[i] * math.sin(2 * math.pi * i / n) for i in range(n))
    return math.sqrt(real_part**2 + imag_part**2)

# Noise reduction using moving average (partially relevant)
def reduce_noise(data, window=3):
    if len(data) < window:
        return data[:]
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        end = i + 1
        smoothed.append(sum(data[start:end]) / (end - start))
    return smoothed

# Outlier detection (red herring - not used in final path)
def detect_outliers(values, factor=1.5):
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [v for v in values if v < lower_bound or v > upper_bound]

# Data normalization (used but with distraction)
def normalize_range(values, target_min=-1, target_max=1):
    if not values:
        return []
    min_val, max_val = min(values), max(values)
    if min_val == max_val:
        return [0 for _ in values]
    return [target_min + (v - min_val) * (target_max - target_min) / (max_val - min_val) for v in values]

# Core diagnostic logic
thresholds = {
    'critical_level': 0.75,
    'warning_band': 0.45,
    'recovery_zone': 0.25
}

health_data = [
    0.88, 0.91, 0.43, 0.77, 0.66, 0.55, 0.32, 0.29, 0.18, 0.21,
    0.53, 0.61, 0.72, 0.81, 0.44, 0.39, 0.25, 0.28, 0.63, 0.74
]

# Decoy variables (dead code paths)
baseline_offset = 0.02
aggregation_factor = 1.8
scaling_exponent = 2.1

# Unused transformation chain (misleading)
transformed_data = [math.tanh(x * scaling_exponent) for x in health_data]
fft_component = compute_fft_magnitude(transformed_data)
dummy_metric = fft_component * aggregation_factor

# Real processing path begins here
filtered_data = [x for x in health_data if x > thresholds['recovery_zone']]
suppressed_noise = reduce_noise(filtered_data, window=2)
normalized_signal = normalize_range(suppressed_noise, 0, 1)

# Secondary filtering based on dynamic threshold
adaptive_threshold = 0.6 * thresholds['warning_band'] + 0.4 * thresholds['critical_level']
stable_segments = [x for x in normalized_signal if x <= adaptive_threshold]

# Calculate risk score (intermediate distractor)
risk_score = 0.0
for val in normalized_signal:
    if val > thresholds['critical_level']:
        risk_score += 2
    elif val > thresholds['warning_band']:
        risk_score += 1

# Auxiliary tracking (irrelevant counter)
event_counter = {"high": 0, "moderate": 0, "low": 0}
for v in health_data:
    if v > 0.7:
        event_counter["high"] += 1
    elif v > 0.4:
        event_counter["moderate"] += 1
    else:
        event_counter["low"] += 1

# Final analysis function combining multiple concepts
def analyze_metrics(metrics, config):
    # Nested logic with conditional expressions
    primary_risk = sum(1 for m in metrics if m > config['critical_level']) > 2
    secondary_indicator = sum(m for m in metrics if m > config['warning_band'])
    
    # Bit manipulation as red herring (not affecting output directly)
    flag_state = 0b1010
    if len(metrics) % 2 == 0:
        flag_state ^= 0b1100
    encoded_status = flag_state & 0b0111  # unused
    
    # Complex conditional expression
    trend_weight = 1.5 if len(stable_segments) > len(metrics) // 2 else 0.8
    
    # Destructuring assignment (tuple unpacking)
    avg_metric = sum(metrics) / len(metrics) if metrics else 0
    peak = max(metrics) if metrics else 0
    _, _, base_influence = (0.1, 0.3, avg_metric * 0.6)
    
    # Composite calculation with dictionary lookup
    category = 'severe' if primary_risk else 'moderate' if secondary_indicator > 1.5 else 'mild'
    severity_map = {'mild': 1, 'moderate': 2, 'severe': 3}
    base_score = severity_map[category]
    
    # Final diagnostic computation (this determines the answer)
    adjustment = math.log(peak + 1) if peak > 0 else 0
    final_value = int((base_score * trend_weight + adjustment + base_influence) * 100)
    
    # Dead code block (never executed)
    if False:
        fallback = sum(transformed_data) / len(transformed_data)
        final_value = int(fallback * 1000)
    
    return final_value

# Execution point of interest
final_diagnostic = analyze_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")