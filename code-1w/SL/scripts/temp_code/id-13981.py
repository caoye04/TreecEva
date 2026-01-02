import math

# Simulated biomedical signal processing pipeline
# Contains multiple layers of data transformation with red herrings

def analyze_waveform(signal):
    if not signal:
        return 0
    peak = max(signal)
    baseline = sum(signal) / len(signal)
    amplitude = peak - baseline
    # Distractor: irrelevant frequency calculation
    freq_domain = [math.sin(x * 0.1) for x in range(len(signal))]
    normalized_amp = round(amplitude * 1.75, 3)
    return normalized_amp

def compute_envelope(data):
    envelope = []
    for i in range(1, len(data) - 1):
        val = (data[i-1] + data[i] + data[i+1]) / 3
        envelope.append(val)
    # Dead code path - never used
    smoothed = [x * 0.9 for x in envelope if x > 0.5]
    return envelope

def evaluate_stability(rhythm):
    variations = [abs(rhythm[i] - rhythm[i-1]) for i in range(1, len(rhythm))]
    avg_variation = sum(variations) / len(variations)
    stability_score = 100 * math.exp(-avg_variation)
    return stability_score

def extract_features(raw_readings):
    # Real processing step
    filtered = [x for x in raw_readings if 40 < x < 160]
    # Distractor variables
    outlier_count = len([x for x in raw_readings if x <= 40 or x >= 160])
    compression_ratio = len(filtered) / len(raw_readings) if raw_readings else 0
    mean_val = sum(filtered) / len(filtered) if filtered else 0
    variance = sum((x - mean_val) ** 2 for x in filtered) / len(filtered) if filtered else 0
    std_deviation = math.sqrt(variance)
    # Key derived metric (used later)
    quality_index = round(mean_val / (std_deviation + 1), 4)
    return quality_index, len(filtered)

def process_metrics(data, config):
    # Core logic hidden among distractions
    alpha = config['alpha_threshold']
    beta = config['beta_limit']
    gamma = config['gamma_scale']
    
    # Irrelevant preprocessing chain
    temp_buffer = ''.join(str(int(x)) for x in data[:5])
    checksum = sum(int(c) for c in temp_buffer)
    token = list(map(lambda x: chr(ord('a') + (x % 26)), data[:3]))
    token_str = ''.join(token).upper()
    
    # Actual critical computation branch
    feature_score, valid_count = extract_features(data)
    waveform_analysis = analyze_waveform(data)
    rhythm_pattern = compute_envelope(data)
    rhythm_score = evaluate_stability(rhythm_pattern) if rhythm_pattern else 0
    
    # Decoy conditional that looks important but is bypassed
    if len(data) > 1000 and checksum > 20:
        emergency_override = True
        fallback_mode = math.log(checksum, 10)
    else:
        emergency_override = False
        fallback_mode = None
    
    # Real decision logic
    if valid_count < 3:
        return -1
    
    # Final integration of key metrics
    base_metric = feature_score * 2.3
    adjustment = (waveform_analysis / 10) * (rhythm_score / 100)
    final_diagnostic = int(base_metric + adjustment)
    
    # Unused complex structure
    report_summary = {
        'version': '2.1',
        'metrics': {
            'quality': feature_score,
            'amplitude': waveform_analysis,
            'stability': rhythm_score
        },
        'status': 'processed' if final_diagnostic > 0 else 'failed'
    }
    
    return final_diagnostic

# Main execution context
if __name__ == '__main__':
    # Simulated patient data stream
    health_data = [
        78, 85, 82, 79, 88, 90, 87, 83, 80, 77,
        75, 73, 78, 81, 84, 86, 89, 91, 85, 82,
        79, 76, 74, 77, 80, 83, 85, 88, 90, 87
    ]
    
    # Configuration with misleading parameters
    thresholds = {
        'alpha_threshold': 0.75,
        'beta_limit': 120,
        'gamma_scale': 3.14159,
        'debug_mode': False,
        'log_level': 'VERBOSE'
    }
    
    # Distractor operations
    buffer_copy = health_data.copy()
    sorted_copy = sorted(buffer_copy, reverse=True)
    median_val = sorted_copy[len(sorted_copy)//2]
    quartile_1 = sorted_copy[len(sorted_copy)//4]
    
    # String manipulation red herring
    tag_sequence = "BIOMED|V3|" + "DATA".lower() + f"|{len(health_data)}"
    tags = tag_sequence.split('|')
    code_hash = sum(ord(c) for c in tags[-1])
    
    # Critical execution point
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")