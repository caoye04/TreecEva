import math

# Sensor simulation and health diagnostics system
def generate_signals(baseline, noise_level, count):
    return [baseline + math.sin(i) * noise_level for i in range(count)]

# Irrelevant utility: converts numeric severity to string (never used)
def severity_label(level):
    labels = {1: 'Low', 2: 'Medium', 3: 'High'}
    return labels.get(level, 'Unknown')

# Dummy transformation — looks important but unused in final path
def legacy_normalize(data_list):
    max_val = max(data_list)
    return [x / max_val for x in data_list] if max_val != 0 else data_list

# Core processing pipeline
def filter_outliers(readings, threshold=2.5):
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    std_dev = math.sqrt(variance)
    # Only include values within threshold standard deviations
    return [x for x in readings if abs(x - mean_val) <= threshold * std_dev]

# Transform sensor data into diagnostic metrics
def extract_features(cleaned_data):
    peak = max(cleaned_data)
    trough = min(cleaned_data)
    volatility = sum(abs(cleaned_data[i+1] - cleaned_data[i]) for i in range(len(cleaned_data)-1))
    return {
        'amplitude': peak - trough,
        'trend_stability': volatility / len(cleaned_data) if cleaned_data else 0,
        'centroid': sum(cleaned_data) / len(cleaned_data) if cleaned_data else 0
    }

# Additional red herring: complex frequency analysis (never called)
def spectral_analysis(signal):
    fft_result = []
    for k in range(len(signal)):
        real_part = sum(signal[n] * math.cos(2 * math.pi * k * n / len(signal)) for n in range(len(signal)))
        imag_part = sum(-signal[n] * math.sin(2 * math.pi * k * n / len(signal)) for n in range(len(signal)))
        fft_result.append(math.sqrt(real_part**2 + imag_part**2))
    dominant_freq = fft_result.index(max(fft_result)) if fft_result else 0
    return {'dominant_frequency': dominant_freq, 'spectrum_complexity': len([f for f in fft_result if f > 1.0])}

# Recursive smoothing function with limited actual use
def smooth_recursive(values, factor=0.3, depth=0):
    if depth >= 2 or len(values) < 2:
        return values[:]
    smoothed = [values[0]]
    for i in range(1, len(values)):
        smoothed.append(factor * values[i] + (1 - factor) * smoothed[i-1])
    return smooth_recursive(smoothed, factor, depth + 1)

# Main diagnostic engine
def analyze_readings(metrics):
    # Simulate multi-factor decision matrix
    risk_score = 0
    
    if metrics['amplitude'] > 1.8:
        risk_score += 3
    elif metrics['amplitude'] > 1.2:
        risk_score += 2
    else:
        risk_score += 1
        
    if metrics['trend_stability'] > 0.6:
        risk_score += 2
    elif metrics['trend_stability'] > 0.3:
        risk_score += 1

    if metrics['centroid'] > 0.7:
        risk_score += 2
    elif metrics['centroid'] < 0.3:
        risk_score -= 1  # Negative impact only in low centroid

    # Hidden adjustment: if amplitude high AND unstable, apply penalty
    if metrics['amplitude'] > 1.5 and metrics['trend_stability'] > 0.5:
        risk_score += 1  # Counterintuitive boost due to calibration offset

    return int(risk_score * 100)  # Scale for precision reporting

# Unused backup logic for fallback scenarios
def emergency_threshold_check(stream):
    critical_count = sum(1 for x in stream if x > 2.0)
    return critical_count > 5

# Simulated raw input from sensors
def main():
    raw_readings = generate_signals(baseline=0.5, noise_level=1.2, count=50)
    
    # Apply filtering to remove anomalies
    filtered_readings = filter_outliers(raw_readings, threshold=2.2)
    
    # Smooth the data using recursive method (modifies signal slightly)
    smoothed_signal = smooth_recursive(filtered_readings, factor=0.4)
    
    # Extract key features for diagnostic evaluation
    processed_metrics = extract_features(smoothed_signal)
    
    # DEAD CODE PATH: example of misleading usage
    # if len(smoothed_signal) > 40:
    #    alt_metrics = extract_features(smoothed_signal[:25])
    #    fallback_score = analyze_readings(alt_metrics)
    #    processed_metrics['backup_risk'] = fallback_score
    
    # UNUSED variable assignment — distractor
    temp_normalization = legacy_normalize(smoothed_signal)
    spectral_diag = spectral_analysis(smoothed_signal)  # Computed but not used
    
    # Final diagnostic computation — this is the key execution point
    final_diagnostic = analyze_readings(processed_metrics)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Execute main function
main()