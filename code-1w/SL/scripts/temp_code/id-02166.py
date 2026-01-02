import math

# Simulated sensor data stream with embedded patterns
def generate_raw_stream():
    return [i * 1.5 + math.sin(i / 3) for i in range(120)]

def segment_data(stream):
    # Slice into overlapping windows of size 20 with step 5
    segments = [stream[i:i+20] for i in range(0, len(stream)-20, 5)]
    normalization_factor = sum([len(s) for s in segments]) / len(segments)
    normalized_segments = [[val / normalization_factor for val in s] for s in segments]
    return normalized_segments

def calculate_entropy(values):
    # Dummy entropy calculation for distraction
    hist = {}
    for v in values:
        bin_val = int(v * 10)
        hist[bin_val] = hist.get(bin_val, 0) + 1
    total = sum(hist.values())
    return -sum((count/total) * math.log2(count/total) for count in hist.values())

def apply_noise_filter(data_block, strength=0.95):
    # Irrelevant noise suppression function (dead path)
    return [x * strength for x in data_block]

def extract_peaks(signal):
    # Another red herring: finds local maxima but unused later
    peaks = []
    for i in range(1, len(signal)-1):
        if signal[i-1] < signal[i] > signal[i+1]:
            peaks.append(signal[i])
    return sorted(peaks, reverse=True)[:5]

def rolling_average(values, window=3):
    smoothed = []
    for i in range(len(values) - window + 1):
        smoothed.append(sum(values[i:i+window]) / window)
    return smoothed

def compute_skewness(data):
    n = len(data)
    mean_val = sum(data) / n
    variance = sum((x - mean_val)**2 for x in data) / n
    if variance == 0:
        return 0.0
    std_dev = math.sqrt(variance)
    if std_dev == 0:
        return 0.0
    skew = sum(((x - mean_val) / std_dev)**3 for x in data) * (1/n)
    return round(skew, 6)

def build_threshold_map(metrics):
    # Creates a mapping that appears important but only one key matters
    base_thresholds = {
        'rms': metrics.get('rms', 0.0) * 0.75,
        'kurtosis': metrics.get('kurtosis', 0.0) + 0.2,
        'purity': max(0.1, min(0.9, metrics.get('entropy', 0.5)))
    }
    base_thresholds['adjusted_purity'] = base_thresholds['purity'] * 1.1
    return base_thresholds

def process_sequence(segments, factor):
    processed = []n    stats_log = []
    for idx, seg in enumerate(segments):
        # Real computation path begins
        filtered_seg = [x * factor for x in seg]  # Apply scaling
        avg_val = sum(filtered_seg) / len(filtered_seg)
        deviation_sq = [(x - avg_val)**2 for x in filtered_seg]
        variance = sum(deviation_sq) / len(deviation_sq)
        rms = math.sqrt(variance)
        
        # Decoy computations
        peak_values = extract_peaks(filtered_seg)
        smoothed_signal = rolling_average(filtered_seg)
        skewness = compute_skewness(smoothed_signal)
        entropy = calculate_entropy(filtered_seg)
        
        # Only these are actually used later
        purity_metric = abs(avg_val) / (rms + 1e-8)
        
        segment_summary = {
            'id': idx,
            'avg': avg_val,
            'rms': rms,
            'skew': skewness,  # unused
            'entropy': entropy,  # unused
            'purity': purity_metric,
            'size': len(filtered_seg)
        }
        stats_log.append(segment_summary)
        processed.append(segment_summary)
    
    # Secondary transformation (only some fields propagate)
    transformed = []
    for entry in processed:
        new_entry = {
            'ref': entry['id'],
            'quality': entry['purity'] * entry['avg'],  # irrelevant
            'stability': entry['rms'] / (entry['avg'] + 1e-8),
            'valid': entry['size'] >= 15
        }
        transformed.append(new_entry)
    
    return {'results': processed, 'summary': transformed, 'count': len(processed)}

def validate_purity(full_output, thresholds):
    results = full_output['results']
    total_weighted_score = 0.0
    total_contribution = 0
    
    # Critical logic: aggregate based on purity above adjusted threshold
    adj_threshold = thresholds['adjusted_purity']
    
    for res in results:
        raw_purity = res['purity']
        weight = abs(res['avg']) + 1  # ensure positive weight
        
        # Actual decision point
        if raw_purity >= adj_threshold:
            contribution = raw_purity * weight
            total_weighted_score += contribution
            total_contribution += weight
    
    # Dead code branches (distractors)
    outlier_count = len([r for r in results if r['rms'] > 5.0])
    if outlier_count > 10:
        total_weighted_score *= 0.9  # never reached due to data range
    
    stability_index = sum([s['stability'] for s in full_output['summary'] if s['valid']], 0)
    adjustment_factor = math.tanh(stability_index / 100)  # computed but not used
    
    final_score = total_weighted_score / (total_contribution + 1e-8)
    return round(final_score, 6)

# --- Execution Block ---
if __name__ == '__main__':
    raw_stream = generate_raw_stream()
    
    # Irrelevant preprocessing chain
    cleaned_stream = [x for x in raw_stream if -10 < x < 10]
    inverted_stream = [-x for x in cleaned_stream]
    reversed_segment = inverted_stream[::-1]
    sliced_view = reversed_segment[10:80:2]  # slicing operation used
    
    # Calibration using dummy metric
    calibrate_base = sum(sliced_view) / len(sliced_view)
    calibration_factor = abs(calibrate_base) / (math.pi / 4)
    
    # Key processing pipeline
    segmented = segment_data(raw_stream)
    processed_result = process_sequence(segmented, calibration_factor)
    
    # Build threshold map from mixed statistics (only one field matters)
    all_avgs = [r['avg'] for r in processed_result['results']]
    avg_of_avgs = sum(all_avgs) / len(all_avgs)
    rms_list = [r['rms'] for r in processed_result['results']]
    mean_rms = sum(rms_list) / len(rms_list)
    
    summary_metrics = {
        'rms': mean_rms,
        'kurtosis': compute_skewness(rms_list),
        'entropy': calculate_entropy(all_avgs)
    }
    
    threshold_map = build_threshold_map(summary_metrics)
    
    # CORE STATEMENT: this determines the answer
    filtration_score = validate_purity(process_sequence(segment_data(raw_stream), calibration_factor), threshold_map)
    
    print(f"Target result: {filtration_score}")