def analyze_pattern(sequence):
    count_upper = sum(1 for c in sequence if c.isupper())
    count_lower = sum(1 for c in sequence if c.islower())
    ratio = count_upper / (count_lower + 1)
    normalized = (count_upper - count_lower) ** 2
    return ratio, normalized


def filter_noise(data, limit):
    filtered = [x for x in data if x > limit]
    excess = [x for x in data if x <= limit]  # unused
    total_energy = sum(x**2 for x in data)  # misleading computation
    return filtered


def extract_features(raw_signal):
    segments = []
    window_size = 4
    for i in range(0, len(raw_signal) - window_size + 1, 2):
        segment = raw_signal[i:i+window_size]
        segment_avg = sum(segment) / len(segment)
        peak = max(segment)
        segments.append((segment_avg, peak))
    return segments


def process_segments(segments, config):
    baseline = config['base']
    factor = config['multiplier']
    temp_results = []
    
    for avg_val, peak_val in segments:
        if peak_val > baseline * 1.5:
            adjusted = avg_val * factor + 10
        elif peak_val > baseline:
            adjusted = avg_val * factor + 5
        else:
            adjusted = avg_val * factor
        temp_results.append(adjusted)
    
    cumulative = 0
    weights = [1.0, 0.8, 0.6, 0.4][:len(temp_results)]
    for i, val in enumerate(temp_results):
        cumulative += val * weights[i]
    
    final_score = int(cumulative // 1)  # key result
    
    # Distractor block: irrelevant transformation
    inverted = [1.0 / (x + 1) for x in temp_results if x > 0]
    entropy = sum(-p * __import__('math').log(p) for p in inverted if p > 0)  # unused
    
    return final_score

# Main execution
signal_input = [3, 7, 2, 9, 4, 6, 1, 8]
thresholds = {'base': 5, 'multiplier': 3}

raw_text = "SignalDataCapture"
ratio_metric, noise_metric = analyze_pattern(raw_text)

filtered_signal = filter_noise(signal_input, limit=2)
segment_data = extract_features(filtered_signal)

final_score = process_segments(segment_data, thresholds)
print(f"Target result: {final_score}")