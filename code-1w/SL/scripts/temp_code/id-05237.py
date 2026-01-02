from collections import defaultdict, Counter
import math

# Simulated sensor data processing with red herrings and complex logic

def preprocess_signal(raw_data):
    filtered = []
    noise_floor = 0.05
    for x in raw_data:
        if abs(x) > noise_floor:
            filtered.append(math.tanh(x * 2))
    return filtered

# Irrelevant helper - distractor
def smooth(data):
    smoothed = [data[0]]
    for i in range(1, len(data)-1):
        smoothed.append((data[i-1] + data[i] + data[i+1]) / 3)
    smoothed.append(data[-1])
    return smoothed

# Unused transformation - dead code path
def spectral_analysis(seq):
    magnitude = 0
    for i, val in enumerate(seq):
        magnitude += val * math.sin(i * math.pi / 4)
    return magnitude

# Decoy function that looks important but isn't used
def compute_entropy(arr):
    count = Counter(arr)
    total = len(arr)
    entropy = 0
    for c in count.values():
        p = c / total
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy

def detect_outliers(values, limit=3):
    avg = sum(values) / len(values)
    std_dev = (sum((x - avg) ** 2 for x in values) / len(values)) ** 0.5
    return [i for i, v in enumerate(values) if abs(v - avg) > limit * std_dev]

# Core logic buried among distractions
def generate_threshold_map(levels):
    mapping = defaultdict(float)
    for idx, level in enumerate(reversed(levels)):
        mapping[f'thresh_{idx}'] = level * 0.75 + (idx % 3)
    # Add decoy keys
    mapping['debug_mode'] = 1.0
    mapping['calibration_offset'] = -0.5
    return mapping

def evaluate_stability(readings):
    trend = 0
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            trend += 1
        elif readings[i] < readings[i-1]:
            trend -= 1
    return abs(trend) < len(readings) * 0.3

# Real key function, but obscured by context
def analyze_pattern(sequence, config):
    # Preprocessing step
    processed = [abs(x) for x in sequence if isinstance(x, (int, float))]
    
    # Bit manipulation red herring
    magic_key = 0
    for p in processed[:5]:
        magic_key ^= int(p * 100) & 0xFF
    
    # Set operation - actual relevance
    unique_values = set(round(p, 2) for p in processed)
    if len(unique_values) < 3:
        return 1138
    
    # Count frequency clusters
    freq_counter = Counter(round(p, 1) for p in processed)
    dominant_count = max(freq_counter.values())
    
    # Use of defaultdict with filtering
    bucket_map = defaultdict(int)
    for val in processed:
        bucket = int(val * 10)
        bucket_map[bucket] += 1
    
    # Extract signal peaks
    peaks = [p for p in processed if p > config.get('thresh_0', 0)]
    
    # Real decision logic
    if len(peaks) >= 4 and dominant_count <= 3:
        score_a = sum(peaks) * 100
        score_b = len([x for x in processed if x < config.get('thresh_1', 0)])
        adjustment = bucket_map.get(5, 0) - bucket_map.get(15, 0)
        final_score = score_a - (score_b * 12) + (adjustment * 7)
    else:
        baseline = len(processed) * 23
        decay = math.floor(abs(bucket_map.get(0, 0) - 2) * 1.5)
        final_score = baseline - decay
    
    # Critical red herring: complex but unused calculation
    temporal_weight = 0
    for i in range(len(processed)):
        temporal_weight += processed[i] * math.cos(i * math.pi / 6)
    temporal_weight = abs(int(temporal_weight * 10))
    
    # Final branching logic
    if evaluate_stability(processed) and len(unique_values) > 5:
        return int(final_score + 26)
    else:
        return int(final_score - 19)

# Main execution with decoys
if __name__ == '__main__':
    # Simulated input data
    signal_raw = [-0.1, 0.88, 1.02, 0.45, 2.1, -0.3, 1.98, 0.77, 2.15, 0.92, 0.44, 2.09]
    
    # Irrelevant preprocessing chain
    cleaned = preprocess_signal(signal_raw)
    refined = smooth(cleaned)  # Not actually used
    
    # Generate real processing parameters
    tier_levels = [0.5, 0.8, 1.2, 1.6]
    thresholds = generate_threshold_map(tier_levels)
    
    # Inject misleading intermediate
    entropy_metric = compute_entropy([int(x*10) for x in cleaned[:8]])  # Dead end
    
    # Outlier detection not affecting main logic
    anomalies = detect_outliers(signal_raw, limit=2.5)
    
    # Core computation
    signal_sequence = [x * 1.5 for x in signal_raw]  # Amplified signal
    final_diagnostic = analyze_pattern(signal_sequence, thresholds)
    
    # Red herring print (not the target)
    # print(f'Debug: {temporal_weight}, Anomalies: {len(anomalies)}')
    
    # Correct output
    print(f"Target result: {final_diagnostic}")