import itertools

# Simulated sensor data preprocessing with distractions
def collect_samples(base_freq, duration):
    samples = []
    for t in range(duration * 10):  # 10 samples per unit time
        sample = (base_freq * t) % 7 + ((t ** 2) % 3)
        samples.append(sample)
    return samples

# Irrelevant helper - decoy function
def compute_entropy(data):
    from math import log
    freq_map = {}
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

# Real processing path buried among distractions
def filter_noise(samples, threshold=4):
    cleaned = [x for x in samples if x > threshold]
    padding = [0] * (len(samples) - len(cleaned))
    return cleaned + padding  # maintains length but appends zeros

# Misleading transformation - looks important but unused in final path
def amplify_signal(data, factor=2):
    return [x * factor for x in data]

# Core analysis logic hidden among red herrings
def extract_features(data):
    features = []
    for i, val in enumerate(data):
        if i % 3 == 0 and val > 0:
            features.append(val ** 2 - i)
    return features

# Decoy statistical summary
def summarize_performance(log_data):
    avg = sum(log_data) / len(log_data)
    peak = max(log_data)
    stability = round(avg / peak, 3)
    return {'average': avg, 'peak': peak, 'stability': stability}

# Main signal analyzer - this one actually matters
def analyze_signal(data):
    temp_result = 0
    feature_set = extract_features(data)
    
    # Real computation chain
    sliced = data[::2]  # slicing every second element
    paired = list(zip(sliced, feature_set))  # using zip
    
    for idx, (raw, feat) in enumerate(paired):
        if feat > 10:
            temp_result += raw * (idx + 1)
        elif raw % 2 == 0:
            temp_result -= feat

    # Introduce controlled distraction
    dummy_calc = list(itertools.accumulate([1, 2, 1, 3]))[-1]  # equals 7, unused
    
    # Final critical calculation
    adjustment = len([x for x in data if x % 4 == 0])
    temp_result = temp_result - adjustment * 3
    
    # Secondary real operation
    offset_tracker = 0
    for a, b in itertools.pairwise(feature_set):  # pairwise from itertools
        if a < b:
            offset_tracker += 1
    
    return temp_result + offset_tracker * 2

# --- Execution with heavy interference ---

# Generate raw sensor input
initial_samples = collect_samples(base_freq=2.5, duration=6)

# Several irrelevant transformations (distractors)
entropy_value = compute_entropy(initial_samples)
summary_stats = summarize_performance(initial_samples)

# Real preprocessing step
processed_samples = filter_noise(initial_samples, threshold=3)

# Another decoy: amplitude scaling that isn't used
amplified = amplify_signal(processed_samples, factor=3)

# Key execution point buried in middle of noise
final_diagnostic = analyze_signal(processed_samples)

# More misleading post-processing
log_entry = {
    'timestamp': '2024-06-15',
    'source': 'sensor_array_A7',
    'raw_count': len(initial_samples),
    'cleaned_count': len([x for x in processed_samples if x > 0]),
    'diagnostic_flag': final_diagnostic > 0
}

# Additional red herring computations
buffer_analysis = [x for x in processed_samples if x == 0]
dead_weight = sum(buffer_analysis) * 100  # irrelevant

# Final output - must print result
print(f"Result: {final_diagnostic}")