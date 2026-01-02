import math

# Simulated sensor data acquisition and analysis with extensive distractors
def acquire_raw_sensor_data():
    # Real signal embedded in noise
    base_signal = [math.sin(x * 0.1) + 0.5 * math.cos(x * 0.3) for x in range(100)]
    noise_floor = [0.1 * (hash(str(i)) % 100) / 100.0 for i in range(100)]  # Irrelevant noise model
    return [base_signal[i] + noise_floor[i] for i in range(100)]

def filter_artifacts(data):
    # Apply moving average to clean data (relevant)
    filtered = []
    for i in range(len(data)):
        start = max(0, i - 2)
        end = min(len(data), i + 3)
        window_avg = sum(data[start:end]) / (end - start)
        filtered.append(round(window_avg, 6))
    
    # Distractor: unused transformation path
    fft_magnitude = [abs(d * math.exp(2j * math.pi * 0.1)) for d in data]  # Dead code branch
    normalized_fft = [m / max(fft_magnitude) if max(fft_magnitude) != 0 else 0 for m in fft_magnitude]
    
    return filtered

def extract_features(signal):
    # Feature extraction with red herring calculations
    peaks = []
    troughs = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(signal[i])
        elif signal[i] < signal[i-1] and signal[i] < signal[i+1]:
            troughs.append(signal[i])
    
    avg_peak = sum(peaks) / len(peaks) if peaks else 0
    avg_trough = sum(troughs) / len(troughs) if troughs else 0
    
    # Distractor variables
    synthetic_envelope = [max(p, 0.1) for p in peaks]  # Unused envelope
    dummy_phase_shift = sum([hash(f'phase_{i}') % 10 for i in range(5)])  # Meaningless computation
    
    feature_vector = {
        'amplitude_modulation': avg_peak - avg_trough,
        'zero_crossings': sum(1 for i in range(1, len(signal)) if signal[i-1] < 0 <= signal[i]),
        'spectral_entropy': -sum((p / sum(peaks)) * math.log(p / sum(peaks)) for p in peaks if p > 0),
        'dummy_flag': False
    }
    
    return feature_vector

def calculate_calibration_offset(signal_chunk):
    # Complex but irrelevant calibration logic
    offset = 0
    for val in signal_chunk:
        if val > 0.5:
            offset += int(abs(val * 10)) & 7  # Bitwise operation as distraction
        else:
            offset -= int(abs(val * 5)) | 3
    return offset % 1000  # Never used

def generate_diagnostic_report(features):
    # Elaborate reporting structure that's not actually used
    report_template = """
    Diagnostic Summary:
    AM Index: {am:.4f}
    Zero Crossings: {zc}
    Entropy: {ent:.4f}
    """
    filled_report = report_template.format(
        am=features['amplitude_modulation'],
        zc=features['zero_crossings'],
        ent=features['spectral_entropy']
    )
    checksum = sum(ord(c) for c in filled_report if c.isalpha()) % 97
    return {'report': filled_report, 'checksum': checksum}  # Ignored return

def analyze_signal(processed_features):
    # Core diagnostic logic buried in distractions
    mod_index = processed_features['amplitude_modulation']
    cross_count = processed_features['zero_crossings']
    entropy_val = abs(processed_features['spectral_entropy'])
    
    # Red herring control flow
    temp_state = {'stage': 'initial', 'value': 0}
    if mod_index > 0.8:
        temp_state['stage'] = 'high'
        temp_state['value'] = 999
    elif entropy_val > 1.5:
        temp_state['stage'] = 'chaotic'
        temp_state['value'] = -888
    else:
        temp_state['stage'] = 'stable'
        temp_state['value'] = 42  # Misleading constant
    
    # Actual computation path
    raw_score = (mod_index * 150) + (cross_count * 7.3) - (entropy_val * 20.1)
    adjustment = 0
    if cross_count > 10:
        adjustment += 50
    if mod_index > 0.6:
        adjustment += 25
    if entropy_val < 0.8:
        adjustment += 15
    
    final_score = raw_score + adjustment
    
    # Final transformation
    final_diagnostic = int(round(math.pow(final_score, 1.1) % 10000))
    
    # Decoy output
    debug_trace = [final_score >> i for i in range(3)]  # Bit shift distraction
    
    return final_diagnostic

# Orchestration with multiple irrelevant steps
if __name__ == '__main__':
    # Step 1: Acquire raw data
    raw_data = acquire_raw_sensor_data()
    
    # Step 2: Filter artifacts (relevant)
    cleaned_data = filter_artifacts(raw_data)
    
    # Step 3: Extract meaningful features (relevant)
    extracted_features = extract_features(cleaned_data)
    
    # Step 4: Spurious calibration calculation (distractor)
    calibration = calculate_calibration_offset(raw_data[::10])
    
    # Step 5: Generate unused report (distractor)
    report_obj = generate_diagnostic_report(extracted_features)
    
    # Step 6: Core analysis (where answer is determined)
    final_diagnostic = analyze_signal(extracted_features)
    
    # Step 7: Print result (required)
    print(f"Result: {final_diagnostic}")