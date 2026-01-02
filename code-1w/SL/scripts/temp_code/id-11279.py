from collections import defaultdict, Counter

# Simulated sensor data ingestion with noise
def fetch_raw_sensor_data():
    return [0.45, 0.67, None, 0.89, -0.12, 0.44, None, 0.91, 0.56, 0.67, 0.45]

def apply_noise_filter(data):
    # Irrelevant transformation: amplifies values (not actually used in final path)
    amplified = [x * 1.5 for x in data if x is not None]
    baseline_shift = sum(amplified) / len(amplified)
    shifted = [x + baseline_shift for x in amplified]
    return shifted  # Dead end

def clean_and_threshold(data, threshold=0.4):
    # Correct processing path: remove nulls and filter by threshold
    cleaned = [x for x in data if x is not None and x >= threshold]
    return sorted(cleaned, reverse=True)

def generate_frequency_map(data):
    # Distractor: computes frequencies but not used in final logic
    freq = defaultdict(int)
    for val in data:
        freq[round(val, 1)] += 1
    return dict(freq)

def compute_moving_average(data, window=2):
    # Red herring function: looks important but unused
    if len(data) < window:
        return [0.0]
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    return averages

def evaluate_signal_stability(data):
    # Misleading intermediate metric
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    stability_score = sum(1 for d in diffs if d < 0.1)
    return stability_score > 2

def extract_peaks(data):
    # Another distractor — finds local maxima, never called
    peaks = []
    for i in range(1, len(data)-1):
        if data[i-1] < data[i] > data[i+1]:
            peaks.append(data[i])
    return peaks

def calculate_entropy(data):
    # Complex but irrelevant calculation
    from math import log2
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def normalize_values(data):
    # Looks useful but is a decoy
    min_val, max_val = min(data), max(data)
    if min_val == max_val:
        return [0.5] * len(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def process_signals(data, config):
    # Core logic hidden among distractions
    segment_size = config.get('segment_size', 3)
    segments = [data[i:i+segment_size] for i in range(0, len(data), segment_size)]
    
    # Apply transformations only on first two valid segments
    processed = []
    for seg in segments[:2]:
        squared = [x ** 2 for x in seg]
        adjusted = [y + config['offset'] for y in squared]
        processed.extend(adjusted)
    
    # Final aggregation
    raw_sum = sum(processed)
    correction_factor = config['correction']
    final_value = int((raw_sum * correction_factor))
    return final_value

# Irrelevant global tracking
system_log = []
system_log.append('START')

# Main execution flow
raw_data = fetch_raw_sensor_data()

# Distraction: multiple unused transformations
_ = apply_noise_filter(raw_data)
freq_map = generate_frequency_map(raw_data)
mov_avg = compute_moving_average(raw_data)  # Computed but unused
entropy_metric = calculate_entropy(raw_data)  # Logged but irrelevant

# Actual signal path
filtered_data = clean_and_threshold(raw_data, threshold=0.45)

# Another red herring: stability check not influencing logic
stability = evaluate_signal_stability(filtered_data)

config = {
    'segment_size': 2,
    'offset': 0.8,
    'correction': 2.5,
    'mode': 'aggressive'
}

# Key assignment point
final_output = process_signals(filtered_data, config)

# Decoy normalization
normalized = normalize_values(filtered_data)

# Output result as required
print(f"Target result: {final_output}")