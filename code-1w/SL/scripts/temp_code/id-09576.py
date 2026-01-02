import itertools

# Simulated sensor array data and calibration parameters
def collect_sensor_data():
    raw_readings = [127, 255, 192, 64, 80, 95, 130]
    scaling_factor = 0.75
    adjusted = [r * scaling_factor for r in raw_readings]
    filtered = [val for val in adjusted if val > 70]
    return filtered

def generate_hamming_sequence(n):
    # Irrelevant function: generates bit parity sequence
    seq = []
    for i in range(n):
        bits = bin(i).count('1')
        seq.append(1 if bits % 2 == 0 else 0)
    return seq

def compute_checksum(data):
    # Unused checksum logic (distractor)
    chk = 0
    for d in data:
        chk ^= int(d)
    return chk << 2

def extract_features(signal):
    # Real feature extraction: computes peak-to-peak variation
    if not signal:
        return 0
    max_val = min_val = signal[0]
    for s in signal:
        if s > max_val:
            max_val = s
        if s < min_val:
            min_val = s
    ptp = max_val - min_val
    avg = sum(signal) / len(signal)
    return round(ptp * (avg / 100), 4)

def validate_frame(frame):
    # Misleading validation with early returns
    if len(frame) < 5:
        return False
    if sum(frame) % 2 == 0:
        return True  # Red herring: looks important
    return False

def build_index_mapping(keys):
    # Dead code path: builds unused index map
    mapping = {}
    for idx, k in enumerate(keys):
        mapping[k] = (idx ** 2) % 7
    return mapping

def analyze_pattern(signals, key):
    # Core analysis logic (nested, with distractors)
    baseline = sum(signals) / len(signals)
    deviations = [abs(s - baseline) for s in signals]
    threshold = 1.5 * (sum(deviations) / len(deviations))
    
    # Use set operations to filter significant deviations
    high_dev_indices = {i for i, d in enumerate(deviations) if d > threshold}
    low_dev_indices = {i for i, d in enumerate(deviations) if d <= threshold / 2}
    overlap_check = high_dev_indices & low_dev_indices  # Always empty, but looks meaningful
    
    # Apply transformation using itertools
    rolling_pairs = list(itertools.pairwise(signals))
    trend_scores = []
    for a, b in rolling_pairs:
        if b > a:
            trend_scores.append(1)
        elif b < a:
            trend_scores.append(-1)
        else:
            trend_scores.append(0)
    
    # Aggregate score based on pattern transitions
    trend_changes = 0
    for i in range(1, len(trend_scores)):
        if trend_scores[i] != trend_scores[i-1]:
            trend_changes += 1
    
    # Decoy logic block (never used)
    anomaly_clusters = []
    temp_cluster = []
    for td in trend_scores:
        if td == 0:
            if temp_cluster:
                anomaly_clusters.append(temp_cluster)
                temp_cluster = []
        else:
            temp_cluster.append(td)
    if temp_cluster:
        anomaly_clusters.append(temp_cluster)
    
    # Final diagnostic calculation
    feature_metric = extract_features(signals)
    change_intensity = sum(abs(ts) for ts in trend_scores)
    stability_ratio = (len(signals) - trend_changes) / len(signals)
    
    # Critical computation
    final_diagnostic = int((feature_metric * change_intensity) - (trend_changes * 10) + (stability_ratio * 100))
    
    # Distractor assignment (no effect)
    diagnostic_log = {
        'raw_length': len(signals),
        'checksum': compute_checksum(signals),
        'validation_passed': validate_frame(signals),
        'index_map': build_index_mapping(['A','B','C'])
    }
    
    return final_diagnostic

# Main execution flow
collected_signals = collect_sensor_data()
system_key = [0, 1, 1, 0]  # Hamming-related key (misleading)

# Irrelevant data generation
noise_profile = [x ^ 255 for x in collected_signals if x < 100]
sync_sequence = generate_hamming_sequence(8)

# Key statement
final_diagnostic = analyze_pattern(collected_signals, system_key)

print(f"Target result: {final_diagnostic}")