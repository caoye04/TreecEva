import math

# Simulated sensor data processing for a biomedical diagnostic system
def collect_signals(duration):
    samples = [math.sin(t * 0.5) + 0.5 * math.cos(t * 1.3) for t in range(duration)]
    return [round(s, 3) for s in samples]

# Irrelevant helper: audio normalization (distractor)
def normalize_audio(signal):
    peak = max([abs(x) for x in signal]) if signal else 1
    return [x / peak for x in signal] if peak > 0 else signal

# Data smoothing using moving average (used)
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window + 1)
        end = i + 1
        smoothed.append(sum(signal[start:end]) / (end - start))
    return smoothed

# Noise floor estimation (distractor function - not used in main path)
def estimate_noise_floor(signal):
    return sum([x ** 2 for x in signal if abs(x) < 0.3]) / len(signal)

# Frequency domain transform (red herring - looks important but unused)
def spectral_power(signal):
    power = 0
    for i in range(len(signal)):
        phase = signal[i] * math.pi
        power += math.cos(phase) ** 2
    return round(power, 4)

# Core metric processor (used)
def compute_variability_index(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return round(math.sqrt(variance), 5)

# Secondary filter chain (partially used)
def apply_filters(data_stream):
    filtered = [x for x in data_stream if x > -0.4]  # Remove low outliers
    if len(filtered) % 2 == 0:
        filtered = filtered[:-1]
    return [x * 1.1 for x in filtered]  # Amplify

# Main processing pipeline
health_data = collect_signals(120)
decoy_signal = [math.tan(i * 0.1) for i in range(50) if abs(math.tan(i * 0.1)) < 2]
normalized_audio = normalize_audio(decoy_signal)  # Dead code path
noise_baseline = estimate_noise_floor(health_data)  # Computed but unused
spectral_analysis = spectral_power(health_data)   # Distractor metric

# Apply relevant transformations
processed_waveform = smooth_signal(health_data, window=4)
filtered_diagnostic_set = apply_filters(processed_waveform)

# Variability analysis
raw_variability = compute_variability_index(health_data)
smoothed_variability = compute_variability_index(processed_waveform)
final_variability_score = (raw_variability + 2 * smoothed_variability) / 3

# Threshold logic with conditional expression
variability_flag = 'ELEVATED' if final_variability_score > 0.6 else 'NORMAL'

# Decoy classification using lambda (unused)
assess_risk = lambda x: 'HIGH' if x > 0.8 else ('MEDIUM' if x > 0.5 else 'LOW')
risk_label = assess_risk(noise_baseline)  # Misleading intermediate result

# Aggregate features into diagnostic vector
feature_vector = [
    final_variability_score,
    len(filtered_diagnostic_set),
    sum(processed_waveform[:10]),
    math.log(len(health_data) + 1)
]

# Real-time anomaly detection (simulated state machine)
current_state = 'IDLE'
anomaly_count = 0
for val in processed_waveform[::5]:
    if current_state == 'IDLE' and val > 0.8:
        current_state = 'MONITORING'
    elif current_state == 'MONITORING':
        if val < 0.2:
            anomaly_count += 1
            current_state = 'IDLE'

# Final decision logic with list comprehension and nested conditionals
def process_metrics(data, threshold):
    # Extract key statistics
    avg = sum(data) / len(data)
    peaks = [x for x in data if x > 0.7]
    peak_ratio = len(peaks) / len(data)
    
    # Compute composite score using modular arithmetic and min/max
    cycle_metric = len(data) % 7
    adjustment_factor = 0.8 + (cycle_metric * 0.05)
    base_score = (avg * 0.3) + (peak_ratio * 0.4) + (smoothed_variability * 0.3)
    adjusted_score = base_score * adjustment_factor
    
    # Conditional override logic (never triggers due to threshold design - red herring)
    emergency_override = any(x > 1.5 for x in data)  # Impossible condition
    safety_buffer = 0.1 if emergency_override else 0.0
    
    # Final nonlinear transformation
    if adjusted_score >= threshold:
        diagnostic_value = 1000 + (adjusted_score * 100)
    else:
        diagnostic_value = 500 - (abs(adjusted_score - threshold) * 50)
        
    # Additional decoy computation (looks important)
    entropy_proxy = -sum([p * math.log(p) for p in feature_vector[:3] if p > 0])
    
    return int(round(diagnostic_value))

# Execute main diagnostic
final_diagnostic = process_metrics(health_data, threshold=0.75)
print(f"Result: {final_diagnostic}")