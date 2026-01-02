import math

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_data():
    raw_values = [2.1, 3.5, 4.8, 5.2, 6.0, 7.3, 8.1, 9.0, 10.5]
    timestamps = list(range(len(raw_values)))
    metadata = {'version': '2.3', 'calibrated': True}
    return list(zip(timestamps, raw_values))

def filter_outliers(data, threshold=1.5):
    values = [v for _, v in data]
    median_val = sorted(values)[len(values)//2]
    deviances = [abs(v - median_val) for v in values]
    mad = sorted(deviances)[len(deviances)//2]  # Median Absolute Deviation
    if mad == 0:
        return data
    modified_z = [abs(d / mad) for d in deviances]
    filtered = [data[i] for i in range(len(data)) if modified_z[i] <= threshold]
    return filtered

def integrate_temperature_profile(readings):
    # Trapezoidal integration of temperature over time
    if len(readings) < 2:
        return 0.0
    total_heat = 0.0
    for i in range(1, len(readings)):
        dt = readings[i][0] - readings[i-1][0]
        avg_temp = (readings[i][1] + readings[i-1][1]) / 2
        total_heat += avg_temp * dt
    return round(total_heat, 4)

def detect_anomaly_spikes(signal):
    # Detect sharp changes using finite differences
    derivatives = [signal[i+1][1] - signal[i][1] for i in range(len(signal)-1)]
    second_derivatives = [derivatives[i+1] - derivatives[i] for i in range(len(derivatives)-1)]
    spike_count = sum(1 for x in second_derivatives if abs(x) > 0.8)
    return spike_count

def generate_synthetic_baseline(n):
    # Irrelevant function: generates synthetic data not used in main flow
    return [math.sin(i * 0.5) + 2.0 for i in range(n)]
def compress_data_log(entries):
    # Irrelevant transformation: unused compression logic
    return {i: hex(int(v * 10))[2:] for i, (_, v) in enumerate(entries)}

def calculate_entropy(sequence):
    # Dead code path — looks relevant but not used in final computation
    from collections import Counter
    counts = Counter(sequence)
    total = len(sequence)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return round(entropy, 4)

def normalize_signal(readings):
    values = [v for _, v in readings]
    min_v, max_v = min(values), max(values)
    if max_v == min_v:
        return [0.0 for _ in values]
    return [(v - min_v) / (max_v - min_v) for v in values]

def compute_rolling_average(data, window=3):
    # Unused helper — distractor
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        smoothed.append(sum(data[start:i+1]) / (i - start + 1))
    return smoothed

def phase_shift_correction(readings, phase_angle=0.1):
    # Misleading preprocessing step that isn't actually used
    corrected = []
    for t, v in readings:
        adjusted = v * math.cos(phase_angle) + t * 0.01
        corrected.append((t, adjusted))
    return corrected

def process_chronological_log(log_entries):
    # Main relevant processing pipeline
    filtered_data = filter_outliers(log_entries)
    temp_integral = integrate_temperature_profile(filtered_data)
    spike_frequency = detect_anomaly_spikes(filtered_data)
    normalized_vals = normalize_signal(filtered_data)
    
    # Conditional expression (required Python feature)
    risk_level = 'high' if spike_frequency > 2 else ('medium' if temp_integral > 30.0 else 'low')
    
    # Accumulation with conditional logic
    severity_score = 0
    for val in normalized_vals:
        if val > 0.7:
            severity_score += 2
        elif val > 0.3:
            severity_score += 1
    
    # Modular arithmetic component (suggested paradigm)
    diagnostic_code = (severity_score * 7) % 11
    
    # Cross-concept combination: sets to deduplicate anomaly indices
    anomaly_indices = {i for i, v in enumerate(normalized_vals) if v > 0.75}
    if len(anomaly_indices) > 0:
        diagnostic_code = (diagnostic_code + len(anomaly_indices)) % 13
    
    return {
        'baseline_integral': temp_integral,
        'spike_count': spike_frequency,
        'risk_category': risk_level,
        'diagnostic_flag': diagnostic_code,
        'anomalies': anomaly_indices
    }

def analyze_readings(diagnostic_package):
    base_integral = diagnostic_package['baseline_integral']
    flag = diagnostic_package['diagnostic_flag']
    category = diagnostic_package['risk_category']
    anomalies = diagnostic_package['anomalies']
    
    # Complex logic chain with nesting and conditionals
    adjustment_factor = 0.0
    if category == 'high':
        if flag > 8:
            adjustment_factor = 1.75
        elif flag > 5:
            adjustment_factor = 1.25
        else:
            adjustment_factor = 0.85
    elif category == 'medium':
        adjustment_factor = 0.6 if len(anomalies) > 2 else 0.4
    else:
        adjustment_factor = 0.2
    
    # Final computation involving summation and scaling
    cumulative_index = base_integral * adjustment_factor
    
    # Early return simulation (suggested paradigm)
    if cumulative_index < 0:
        return -1.0
    
    # Final transformation
    final_value = round(cumulative_index + flag * 0.3, 4)
    
    # Decoy operation — looks like it affects result but doesn't
    temp_result = math.sqrt(final_value ** 2 + 1e-8)
    
    return final_value

# --- Execution Flow ---
sensor_logs = collect_sensor_data()
processed_logs = process_chronological_log(sensor_logs)
final_diagnostic = analyze_readings(processed_logs)

# Irrelevant variables — red herrings
baseline_prediction = generate_synthetic_baseline(10)
data_checksum = compress_data_log(sensor_logs)
theoretical_entropy = calculate_entropy([1,2,2,3,3,3,4,4,4,4])

# Critical output statement
print(f"Result: {final_diagnostic}")