def analyze_readings(readings):
    cumulative_score = 0
    temp_offset = 0.0
    for i, val in enumerate(readings):
        if i % 3 == 0:
            cumulative_score += val * 1.1
        elif i % 3 == 1:
            cumulative_score -= val * 0.2
        else:
            cumulative_score += abs(val) // 2
    return int(cumulative_score)


def validate_sequence(seq):
    # Irrelevant validation logic (dead path)
    checksum = sum(seq[i] * (i + 1) for i in range(len(seq)) if i % 2 == 0)
    normalized = [x / (checksum + 1e-6) for x in seq]
    return all(x < 0.5 for x in normalized)


def compute_fragments(data):
    # Distractor computation with slicing and zip
    segments = [data[i:i+3] for i in range(0, len(data), 3)]
    fragment_scores = []
    for seg in segments:
        if len(seg) == 3:
            a, b, c = seg
            score = (a ^ b) & (c | 10)  # Bit manipulation red herring
            fragment_scores.append(score)
    return fragment_scores


def filter_anomalies(values, limit=100):
    # Unused filtering function (decoy)
    anomalies = set()
    for idx, v in enumerate(values):
        if v > limit or v < -limit:
            anomalies.add(idx)
    return anomalies


def extract_features(dataset):
    # Complex but irrelevant feature extraction
    features = {}
    even_vals = dataset[::2]
    odd_vals = dataset[1::2]
    paired = list(zip(even_vals, odd_vals))
    
    magnitude = sum(abs(a - b) for a, b in paired)
    coherence = sum(1 for a, b in paired if (a > 0) == (b > 0))
    features['magnitude'] = magnitude
    features['coherence'] = coherence
    features['ratio'] = coherence / (len(paired) + 1e-8)
    
    # Fake intermediate diagnostic
    dummy_diagnostic = (magnitude * coherence) % 77
    return features, dummy_diagnostic


def process_metrics(data, config):
    base_result = analyze_readings(data)
    
    # Real transformation chain
    adjusted = [x - config.get('baseline', 0) for x in data]
    windowed = [sum(adjusted[i:i+4]) for i in range(len(adjusted) - 3)]
    peak_response = max(windowed) if windowed else 0
    
    # Critical calculation: uses slicing and enumerate
    trend_scores = []
    for j, win in enumerate(windowed):
        if j % 2 == 0:
            trend_scores.append(win * 0.7)
        else:
            trend_scores.append(win * 0.3)
    
    aggregated_trend = sum(trend_scores)
    
    # Real answer path
    stability_index = aggregated_trend - abs(base_result)
    final_diagnostic = int(stability_index * config.get('sensitivity', 1.0))
    
    # Decoy variables (misleading intermediates)
    phantom_metric = (base_result ^ int(aggregated_trend)) & 0xFFFF
    fallback_value = (phantom_metric * 3) % 999
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Input data (simulated sensor readings)
    health_data = [12, -5, 8, 19, 3, -11, 7, 14, 6, 9, 2, 5, 13, -3]
    
    # Configuration map (mixed relevant and irrelevant keys)
    thresholds = {
        'baseline': 4,
        'sensitivity': 2.5,
        'tolerance': 0.8,
        'damping_factor': 1.05,
        'window_size': 4
    }
    
    # Dead code path invocation (no effect)
    _ = validate_sequence(health_data)
    _ = compute_fragments(health_data)
    
    # Extract features (used only to create distraction)
    features, dummy = extract_features(health_data)
    
    # Key assignment: this produces the actual answer
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")