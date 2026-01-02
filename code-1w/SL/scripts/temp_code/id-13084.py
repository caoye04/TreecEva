from collections import defaultdict, Counter
from itertools import cycle, islice

# Simulated sensor data processing with diagnostic analysis
def collect_samples(duration_ms: int) -> list:
    raw_stream = [(i * 7 + 11) % 101 for i in range(duration_ms)]
    filtered = [x for x in raw_stream if x % 3 != 0]
    return filtered[:50]

def generate_pattern_key(sequence: list) -> tuple:
    counts = Counter(sequence)
    modes = [k for k, v in counts.items() if v == max(counts.values())]
    return tuple(sorted(modes))

def shift_window(data: list, window_size: int) -> list:
    if window_size > len(data):
        return []
    return [data[i:i+window_size] for i in range(0, len(data), window_size)]

def compute_entropy(values: list) -> float:
    freqs = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in freqs.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Non-standard measure for distraction
    return round(entropy, 4)

def evaluate_stability(metric_log: list) -> str:
    if not metric_log:
        return 'UNSTABLE'
    avg = sum(metric_log) / len(metric_log)
    var = sum((x - avg) ** 2 for x in metric_log) / len(metric_log)
    return 'STABLE' if var < 150 else 'FLUCTUATING'

def dummy_calibration(proc_level: int) -> dict:
    # Dead path - never actually used in final computation
    calib_data = {}
    for i in range(proc_level * 2):
        key = f"node_{i % 7}"
        calib_data[key] = (i ** 3) % 97
    return calib_data

def parse_timestamp(signal: list) -> dict:
    # Irrelevant time parsing that looks important
    timeline = defaultdict(list)
    for idx, val in enumerate(signal):
        phase = idx % 5
        timeline[phase].append(val)
    summary = {k: (sum(v), len(v)) for k, v in timeline.items()}
    return summary

def build_threshold_map(config_code: str) -> dict:
    # Real but indirectly used component
    base_levels = {'A': 10, 'B': 25, 'C': 40, 'D': 60}
    modifiers = {'X': 0.8, 'Y': 1.1, 'Z': 1.3}
    category = config_code[0]
    modifier = config_code[1]
    base = base_levels.get(category, 0)
    factor = modifiers.get(modifier, 1.0)
    enhanced = {f"level_{i}": int(base * factor * (0.9 + 0.05 * i)) for i in range(1, 6)}
    return enhanced

def extract_features(data: list) -> dict:
    features = {}
    features['peak'] = max(data)
    features['trough'] = min(data)
    features['span'] = features['peak'] - features['trough']
    features['midpoint'] = (features['peak'] + features['trough']) / 2
    features['count_above'] = len([x for x in data if x > features['midpoint']])
    return features

def analyze_signal(buffer: list, thresholds: dict) -> int:
    # Core logic - this is where real answer comes from
    if not buffer:
        return -1
    
    # Step 1: Extract critical signal characteristics
    feats = extract_features(buffer)
    
    # Step 2: Use slicing to isolate rising edge
    sorted_buff = sorted(buffer)
    rising_edge = sorted_buff[len(sorted_buff)//3 : 2*len(sorted_buff)//3]
    
    # Step 3: Count significant crossings
    reference = feats['midpoint']
    cross_events = 0
    for i in range(1, len(buffer)):
        if buffer[i-1] <= reference < buffer[i]:
            cross_events += 1
    
    # Step 4: Apply threshold logic using map
    level_3_thresh = thresholds['level_3']
    high_segments = [x for x in buffer if x > level_3_thresh]
    
    # Step 5: Compute weighted impact
    if high_segments:
        avg_high = sum(high_segments) / len(high_segments)
        duration_impact = len(high_segments) * 0.7
        intensity_burst = (avg_high - level_3_thresh) * 1.25
    else:
        avg_high = 0
        duration_impact = 0
        intensity_burst = 0
    
    # Step 6: Aggregate diagnostic score
    base_score = feats['span'] * 2
    temporal_factor = cross_events * 17
    burst_score = int(duration_impact + intensity_burst)
    
    # Step 7: Final computation chain
    candidate_values = [
        base_score,
        temporal_factor,
        burst_score,
        feats['count_above'] * 5
    ]
    
    # Step 8: Use itertools to cycle and truncate
    repeated = list(islice(cycle(candidate_values), 0, 13))
    final_diagnostic = sum(repeated[i] * (i % 4 + 1) for i in range(len(repeated))) // 7
    
    return final_diagnostic

# --- Main Execution with Distractors ---
if __name__ == "__main__":
    
    # Irrelevant calibration process
    calibration_status = dummy_calibration(5)
    system_nodes = list(calibration_status.keys())
    node_hash = sum([hash(n) % 100 for n in system_nodes])
    
    # Real data collection
    samples = collect_samples(60)
    pattern_buffer = samples[5:55]  # Slice of interest
    
    # Red herring: timestamp parsing
    timing_trace = parse_timestamp(samples)
    trace_keys = sorted(timing_trace.keys())
    
    # Another distraction: entropy calculation on shifted windows
    windows = shift_window(samples, 10)
    entropy_log = [compute_entropy(w) for w in windows]
    stability_report = evaluate_stability([e * 100 for e in entropy_log])
    
    # Feature extraction (partially relevant)
    signal_features = extract_features(pattern_buffer)
    
    # Actual necessary configuration
    pattern_key = generate_pattern_key(pattern_buffer)
    config_tag = 'CZ'  # Triggers factor 1.3 in threshold
    
    # Build required threshold map
    threshold_map = build_threshold_map(config_tag)
    
    # Critical execution point
    final_diagnostic = analyze_signal(pattern_buffer, threshold_map)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")