import math

# Simulated sensor array diagnostics with heavy distractions
def collect_telemetry():
    raw_samples = [i * 0.7 + (i % 3) for i in range(15)]
    baseline = sum(raw_samples) / len(raw_samples)
    adjusted = [x - baseline for x in raw_samples]
    return adjusted

# Irrelevant preprocessing: signal smoothing (dead path)
def smooth_signal(data, window=3):
    if len(data) < window:
        return data
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window // 2)
        end = min(len(data), i + window // 2 + 1)
        smoothed.append(sum(data[start:end]) / (end - start))
    return smoothed

# Unused noise modeling function (decoy)
def estimate_noise_floor(signal):
    squares = [x**2 for x in signal]
    mean_square = sum(squares) / len(squares)
    rms_noise = math.sqrt(mean_square)
    return rms_noise * 0.5

# Core transformation: frequency domain approximation
def transform_to_spectral(readings):
    transformed = []
    for i in range(len(readings)):
        component = 0
        for j in range(len(readings)):
            angle = 2 * math.pi * i * j / len(readings)
            component += readings[j] * math.cos(angle)
        transformed.append(round(component, 6))
    return transformed

# Secondary filter: remove low-amplitude components (distractor logic)
def filter_peaks(components, threshold=1.5):
    filtered = [c for c in components if abs(c) > threshold]
    normalization_factor = sum([abs(x) for x in filtered]) if filtered else 1
    return [f / normalization_factor for f in filtered] if normalization_factor > 0 else []

# Misleading diagnostic chain (unused)
def compute_health_score(telemetry):
    if not telemetry:
        return 0.0
    variance = sum([(x - sum(telemetry)/len(telemetry))**2 for x in telemetry]) / len(telemetry)
    peak = max(abs(min(telemetry)), abs(max(telemetry)))
    return round((variance * 0.3) + (peak * 0.7), 4)

# Critical processing pipeline
def process_log_entries(raw_data):
    # Apply non-linear correction
    corrected = [math.log(abs(x) + 1) * math.copysign(1, x) for x in raw_data]
    
    # Introduce irrelevant intermediate
    entropy_proxy = -sum([c * math.log(abs(c) + 1e-8) for c in corrected])
    
    # Normalize to unit range
    max_val = max(abs(min(corrected)), abs(max(corrected)))
    normalized = [c / max_val for c in corrected] if max_val != 0 else corrected
    
    # Add phase distortion (relevant only in magnitude)
    modulated = []
    for i, val in enumerate(normalized):
        phase_shift = math.sin(i * 0.5)
        modulated.append(val + phase_shift * 0.1)
    
    # Final preprocessed log
    return modulated

# Main analysis function (called in key statement)
def analyze_readings(logs):
    spectral = transform_to_spectral(logs)
    
    # Distraction: unused peak analysis
    strong_peaks = [sp for sp in spectral if sp > 2.0]
    peak_count_metric = len(strong_peaks) * 10
    
    # Real computation path begins here
    magnitudes = [abs(x) for x in spectral]
    avg_magnitude = sum(magnitudes) / len(magnitudes)
    
    # Apply weighting based on index parity (hidden logic)
    weighted_sum = 0.0
    for idx, mag in enumerate(magnitudes):
        weight = 1.5 if idx % 2 == 0 else 0.5
        weighted_sum += mag * weight
    
    # Final diagnostic calculation
    diagnostic_score = weighted_sum * avg_magnitude
    return round(diagnostic_score, 6)

# Orchestration with red herrings
if __name__ == "__main__":
    # Collect raw data
    sensor_output = collect_telemetry()
    
    # Apply irrelevant smoothing (dead code branch)
    if len(sensor_output) > 10:
        smoothed_data = smooth_signal(sensor_output, window=5)
    else:
        smoothed_data = sensor_output
    
    # Compute fake health metric (distraction)
    phantom_health = compute_health_score(smoothed_data)
    
    # Real processing starts here
    processed_logs = process_log_entries(sensor_output)
    
    # Key statement
    final_diagnostic = analyze_readings(processed_logs)
    
    # Print required result
    print(f"Target result: {final_diagnostic}")