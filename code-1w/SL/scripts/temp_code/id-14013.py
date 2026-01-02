from collections import defaultdict, Counter

# Simulated bio-signal processing pipeline with diagnostic evaluation

def analyze_waveform(signal, sample_rate):
    # Irrelevant signal transformation (distractor)
    normalized = [x / max(signal) for x in signal]
    freq_domain = [abs(x * sample_rate) for x in normalized[:len(normalized)//2]]
    return sum(freq_domain) % 100

def evaluate_rhythm(peaks):
    # Misleading arrhythmia detection (dead logic path)
    intervals = [peaks[i+1] - peaks[i] for i in range(len(peaks)-1)]
    variability = sum(abs(intervals[i+1] - intervals[i]) for i in range(len(intervals)-1))
    return variability > 20

def compute_bursts(data, window_size):
    # Unused burst analysis function (decoy)
    bursts = []
    for i in range(0, len(data), window_size):
        window = data[i:i+window_size]
        if len(window) == window_size:
            bursts.append(sum(window) / len(window))
    return bursts

def filter_artifacts(readings, threshold=0.5):
    # Red herring artifact filter (not used in final path)
    clean = []
    for val in readings:
        if abs(val - sum(clean[-3:]) / max(1, len(clean[-3:]))) < threshold or not clean:
            clean.append(val)
    return clean

def extract_features(temporal_data):
    # Distractor: Spectral feature extraction (never called)
    features = defaultdict(float)
    features['kurtosis'] = sum((x - 36.6)**4 for x in temporal_data) / len(temporal_data)
    features['skew'] = sum((x - 36.6)**3 for x in temporal_data) / len(temporal_data)
    return dict(features)

def calculate_stability_index(values):
    # Seemingly important but irrelevant stability metric
    diffs = [abs(values[i+1] - values[i]) for i in range(len(values)-1)]
    return round(sum(diffs) / len(diffs), 4) if diffs else 0.0

def assess_coherence(sequence):
    # Decoy coherence analyzer
    count = 0
    for i in range(1, len(sequence)):
        if sequence[i] >= sequence[i-1]:
            count += 1
    return count / (len(sequence) - 1) if len(sequence) > 1 else 1.0

def process_metrics(data_package, config_map):
    # Core relevant logic buried among distractions
    
    # Key intermediate variables (some are red herrings)
    temp_trend = data_package.get('temperatures', [])
    hr_sequence = data_package.get('heart_rates', [])
    activity_log = data_package.get('motion_events', [])
    
    # Irrelevant preprocessing (distraction)
    baseline_shift = sum(temp_trend[:5]) / 5 - 36.6
    adjusted_temps = [t - baseline_shift for t in temp_trend]
    
    # Critical computation hidden in middle
    valid_readings = [hr for hr in hr_sequence if config_map['hr_min'] <= hr <= config_map['hr_max']]
    
    # Another distraction: simulate false correlation check
    motion_hr_correlation = 0
    if len(activity_log) > 0:
        avg_motion = sum(activity_log) / len(activity_log)
        motion_hr_correlation = abs(avg_motion - sum(hr_sequence) / len(hr_sequence))
    
    # Real logic step 1: Count sustained elevated heart rate episodes
    elevated_episodes = 0
    current_episode = 0
    for hr in hr_sequence:
        if hr > config_map['hr_elevated']:
            current_episode += 1
        else:
            if current_episode >= config_map['min_duration']:
                elevated_episodes += 1
            current_episode = 0
    if current_episode >= config_map['min_duration']:
        elevated_episodes += 1
    
    # Real logic step 2: Compute temperature deviation penalty
    temp_deviation = sum(abs(t - 36.6) for t in temp_trend)
    
    # Real logic step 3: Apply weighted diagnostic formula
    episode_weight = config_map['episode_penalty']
    temp_weight = config_map['temp_penalty']
    
    # Real logic step 4: Final diagnostic score
    raw_score = (elevated_episodes * episode_weight) + (temp_deviation * temp_weight)
    
    # Real logic step 5: Normalize using non-obvious offset
    normalization_offset = len([x for x in hr_sequence if x > 0])  # actual length
    if normalization_offset > 0:
        raw_score /= normalization_offset
    
    # Real logic step 6: Apply final activation function
    diagnostic_value = int(round(100 * (1 - (1 / (1 + raw_score)))))
    
    # Irrelevant final transformations (misleading)
    secondary_index = calculate_stability_index(adjusted_temps)
    coherence_ratio = assess_coherence(valid_readings)
    spectral_marker = analyze_waveform(hr_sequence, 256)
    
    return diagnostic_value

# Main execution block
if __name__ == '__main__':
    # Input data structure with meaningful names
    health_data = {
        'temperatures': [36.8, 37.1, 37.5, 37.3, 36.9, 37.0, 37.4, 37.6],
        'heart_rates': [72, 75, 80, 85, 92, 95, 98, 94, 88, 82, 77, 73],
        'motion_events': [0.2, 0.3, 0.1, 0.0, 0.0, 0.1, 0.4, 0.6, 0.3]
    }
    
    # Configuration map with plausible medical parameters
    threshold_map = {
        'hr_min': 50,
        'hr_max': 110,
        'hr_elevated': 85,
        'min_duration': 3,
        'episode_penalty': 15,
        'temp_penalty': 20
    }
    
    # Dead code assignments (red herrings)
    waveform_analysis = [analyze_waveform([1,2,3,4,5], 100), analyze_waveform([2,4,6,8], 200)]
    artifact_filtered = filter_artifacts(health_data['temperatures'], 0.1)
    burst_patterns = compute_bursts(health_data['heart_rates'], 4)
    temp_features = extract_features(health_data['temperatures'])
    
    # Lambda-based distractor (looks important but unused)
    severity_ranker = lambda x: 'High' if x > 75 else 'Medium' if x > 50 else 'Low'
    rankings = [severity_ranker(hr) for hr in health_data['heart_rates'] if hr > 80]
    
    # Critical execution point
    final_diagnostic = process_metrics(health_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")