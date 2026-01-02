from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_streams = [
    [142, 138, 146, 150, 135, 148, 140, 144],
    [210, 205, 198, 215, 208, 201, 207, 212],
    [95, 92, 98, 90, 94, 96, 91, 93]
]

# Irrelevant baseline reference (distractor)
baseline_patterns = {
    'A': [1, 0, 1, 1],
    'B': [0, 1, 1, 0],
    'C': [1, 1, 0, 0]
}

# Noise injection simulation (dead path)
def apply_noise(signal, level=0.05):
    return [x + random.uniform(-level, level) for x in signal]  # Unused

# Decoy function for spectral analysis (never called)
def analyze_spectrum(data):
    fft_result = []
    for i in range(len(data)):
        component = 0
        for j in range(len(data)):
            component += data[j] * math.sin(2 * math.pi * i * j / len(data))
        fft_result.append(component)
    return fft_result

# Auxiliary transformation with partial relevance
def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    variance = sum((x - mean_val) ** 2 for x in signal) / len(signal)
    std_dev = math.sqrt(variance)
    if std_dev == 0:
        return [0 for _ in signal]
    return [(x - mean_val) / std_dev for x in signal]

# Core diagnostic logic
def extract_features(streams):
    features = defaultdict(float)
    temp_cache = []
    
    for idx, stream in enumerate(streams):
        # Real computation: trend slope approximation
        slope = (stream[-1] - stream[0]) / (len(stream) - 1) if len(stream) > 1 else 0
        features[f'slope_ch{idx}'] = round(slope, 3)
        
        # Amplitude metrics
        peak_to_peak = max(stream) - min(stream)
        features[f'pp_ch{idx}'] = peak_to_peak
        
        # Distraction: dummy FFT-like binning (not used later)
        bins = [0]*4
        for val in stream:
            bin_idx = int((val % 200) // 50)
            if 0 <= bin_idx < 4:
                bins[bin_idx] += 1
        temp_cache.append(bins)
    
    # Red herring: unused statistical moment
    fourth_moment = sum((x - features['slope_ch0'])**4 for x in streams[0]) / len(streams[0])
    features['kurtosis_proxy'] = round(fourth_moment, 2)  # Not used
    
    return features

# Log processor with conditional filtering
def filter_anomalies(log_entries, threshold_map):
    anomalies = []
    severity_weights = {'minor': 1, 'major': 3, 'critical': 5}
    
    for entry in log_entries:
        lvl = entry.get('level')
        val = entry.get('value')
        ch = entry.get('channel')
        
        thresh = threshold_map.get(ch, 100)
        if val > thresh and lvl in severity_weights:
            anomalies.append({
                'ch': ch,
                'excess': val - thresh,
                'weight': severity_weights[lvl]
            })
    
    # Distractor aggregation
    debug_stats = {
        'total_anomalies': len(anomalies),
        'weighted_sum': sum(a['excess'] * a['weight'] for a in anomalies)
    }
    
    return anomalies  # Only this matters

# Main processing pipeline
def process_metrics(raw_logs, limits):
    # Step 1: Extract numerical features from raw telemetry
    extracted = extract_features(telemetry_streams)
    
    # Step 2: Generate synthetic log entries based on patterns (irrelevant channel names)
    synthetic_logs = []
    for i, s in enumerate(telemetry_streams):
        synthetic_logs.append({'channel': f'C{i}', 'value': max(s), 'level': 'major'})
        synthetic_logs.append({'channel': f'C{i}', 'value': min(s), 'level': 'minor'})
    
    # Add decoy entries
    synthetic_logs.extend([
        {'channel': 'C3', 'value': 300, 'level': 'critical'},
        {'channel': 'C4', 'value': 85, 'level': 'minor'}
    ])
    
    # Step 3: Filter anomalies above thresholds
    flagged = filter_anomalies(synthetic_logs, limits)
    
    # Step 4: Compute composite score (actual answer path)
    base_score = 0
    for item in flagged:
        base_score += int(item['excess'] // item['weight'])  # Integer division
    
    # Step 5: Apply correction using feature data (only one field used)
    slope_contribution = extracted['slope_ch1']
    adjusted = base_score + int(abs(slope_contribution))
    
    # Step 6: Final nonlinear transformation
    final_value = int(math.pow(adjusted, 2) + math.log(adjusted + 1))
    
    # Irrelevant string transformation chain (distractor)
    status_tag = "DIAG_" + "".join([chr(ord('A') + (final_value % 26)) for _ in range(3)])
    
    # Critical answer variable
    final_diagnostic = final_value
    
    # Print required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Threshold configuration (real input)
thresholds = {'C0': 140, 'C1': 200, 'C2': 95, 'C3': 250}

# Additional unused data structure (misdirection)
performance_matrix = [
    [a*b for b in range(4)] for a in range(4)
]

# Global constant that looks important but isn't used
CALIBRATION_FACTOR = sum(sum(row) for row in performance_matrix)

# Prepare log data from telemetry_streams manually
log_data = []
for i, seq in enumerate(telemetry_streams):
    log_data.append({'channel': f'C{i}', 'value': max(seq), 'level': 'major'})
    log_data.append({'channel': f'C{i}', 'value': min(seq), 'level': 'minor'})

# Execute main function
def main():
    final_diagnostic = process_metrics(log_data, thresholds)

if __name__ == '__main__':
    main()