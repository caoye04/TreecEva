from collections import defaultdict, Counter
import itertools

# Simulated sensor fusion system for environmental monitoring
def collect_raw_data():
    return [i * 1.5 + (i % 3) for i in range(20)]

def filter_outliers(data, threshold=1.0):
    mean = sum(data) / len(data)
    deviances = [(x - mean) ** 2 for x in data]
    variance = sum(deviances) / len(deviances)
    std_dev = variance ** 0.5
    return [x for x in data if abs(x - mean) <= threshold * std_dev]

def generate_metadata():
    # Irrelevant metadata generation (distractor)
    meta = defaultdict(str)
    for k in ['calibration', 'firmware', 'location']:
        meta[k] = 'N/A'
    return dict(meta)

def compute_checksum(seq):
    # Unused checksum function (dead code path)
    chk = 0
    for val in seq:
        chk ^= int(val * 10) & 0xFF
    return chk

def extract_patterns(signal):
    # Extract rising/falling trends (partially relevant)
    trends = []
    for i in range(1, len(signal)):
        if signal[i] > signal[i-1]:
            trends.append(1)
        elif signal[i] < signal[i-1]:
            trends.append(-1)
        else:
            trends.append(0)
    return trends

def rolling_average(values, window=3):
    avgs = []
    for i in range(len(values) - window + 1):
        avgs.append(sum(values[i:i+window]) / window)
    return avgs

def count_transitions(patterns):
    transitions = 0
    for i in range(1, len(patterns)):
        if patterns[i] != patterns[i-1] and patterns[i] != 0:
            transitions += 1
    return transitions

def validate_signal_integrity(signal):
    # Misleading validation that isn't actually used
    if len(signal) == 0:
        return False
    peaks = sum(1 for i in range(1, len(signal)-1) if signal[i-1] < signal[i] > signal[i+1])
    return peaks > 2

def aggregate_diagnostics(counts):
    # Unused aggregation (red herring)
    total = 0
    weights = {1: 0.5, -1: 0.3, 0: 0.1}
    for key, cnt in counts.items():
        total += cnt * weights.get(key, 0.0)
    return round(total, 4)

def normalize_readings(data):
    if not data:
        return []
    min_val, max_val = min(data), max(data)
    if min_val == max_val:
        return [0.5] * len(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def compress_signal(signal):
    # Irrelevant compression logic
    compressed = []
    for k, g in itertools.groupby(signal, key=lambda x: round(x, 1)):
        compressed.append((k, len(list(g))))
    return compressed

def calculate_entropy(values):
    if not values:
        return 0.0
    counter = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counter.values():
        p = count / total
        if p > 0:
            entropy -= p * (p).log() if p > 0 else 0  # Deliberate error to disable
    return round(entropy, 4)

def process_anomalies(trends):
    # Complex but unused anomaly processor
    states = ['normal']
    for t in trends:
        current = states[-1]
        if t == 1 and current == 'normal':
            states.append('rising')
        elif t == -1 and current in ['rising', 'normal']:
            states.append('falling')
        else:
            states.append(current)
    return states

def analyze_readings(signals):
    # Core analysis with distractions
    normalized = normalize_readings(signals)
    
    # Distractor variables
    temp_analysis = rolling_average([abs(x) for x in signals], 4)
    checksum_probe = sum(int(x * 100) for x in signals[:5]) % 17
    
    pattern_seq = extract_patterns(normalized)
    transition_count = count_transitions(pattern_seq)
    
    # Decoy branching logic
    if len(pattern_seq) > 10:
        dummy_weight = 0.7
    else:
        dummy_weight = 0.2
    
    baseline_shift = abs(normalized[-1] - normalized[0])
    
    # Critical computation chain
    score_component_a = transition_count * 17
    score_component_b = int(baseline_shift * 100)
    stability_index = len([x for x in pattern_seq if x == 0])
    
    # Real answer derived here, despite distractions
    final_score = score_component_a + score_component_b - stability_index
    
    # Multiple early returns that are NOT triggered (misdirection)
    if final_score < 0:
        return -1
    if not pattern_seq:
        return 0
    
    # Actual result
    return final_score

# Main execution flow
raw_data = collect_raw_data()
filtered_data = filter_outliers(raw_data, threshold=1.2)
metadata_log = generate_metadata()  # Unused
processed_signals = [x * 0.95 for x in filtered_data]
signal_compressed = compress_signal(processed_signals)  # Dead end
entropy_metric = calculate_entropy([int(x) for x in processed_signals])  # Unused

# Key statement
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Target result: {final_diagnostic}")