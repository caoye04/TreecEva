from collections import defaultdict, Counter
import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings(raw_samples):
    processed = []
    for val in raw_samples:
        if val < 0:
            val = abs(val)
        processed.append(round(math.log(val + 1e-5) * 100, 2))
    return processed

def compute_checksum(data):
    # Irrelevant checksum function (dead code path)
    chk = 0
    for d in data:
        chk = (chk + int(d * 10)) % 257
    return chk

def generate_histogram(values):
    hist = defaultdict(int)
    for v in values:
        bucket = int(v // 5)
        hist[bucket] += 1
    return hist

def extract_outliers(scores, limit=3):
    sorted_vals = sorted(scores, reverse=True)
    return sorted_vals[:limit]

def calculate_entropy(counts):
    total = sum(counts.values())
    entropy = 0.0
    for freq in counts.values():
        p = freq / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def filter_anomalies(log_data, baseline):
    anomalies = []
    for entry in log_data:
        if abs(entry - baseline) > 15:
            anomalies.append(entry)
    return anomalies  # Unused in final logic

def derive_key_metrics(entries):
    metrics = {}
    metrics['peak'] = max(entries)
    metrics['trough'] = min(entries)
    metrics['spread'] = metrics['peak'] - metrics['trough']
    metrics['midpoint'] = (metrics['peak'] + metrics['trough']) / 2
    return metrics

def evaluate_stability(measurements):
    diffs = [abs(measurements[i+1] - measurements[i]) for i in range(len(measurements)-1)]
    avg_change = sum(diffs) / len(diffs)
    return avg_change < 2.5

def analyze_patterns(signal, criteria):
    # Core logic hidden among distractors
    signal_counts = Counter([int(s) for s in signal if s > 0])
    entropy = calculate_entropy(signal_counts)
    
    # Distractor: complex but unused structure
    profile = {}
    for k, v in signal_counts.items():
        profile[k] = {
            'freq': v,
            'weight': v * math.sin(k),
            'flagged': v > 4 and k % 2 == 0
        }
    
    # Real decision path
    valid_entries = [k for k, v in signal_counts.items() if v >= criteria['min_freq']]
    score_basis = [k * v for k, v in signal_counts.items() if k in valid_entries]
    base_score = sum(score_basis)
    
    # Secondary transformation
    adjusted_score = base_score
    if len(valid_entries) > 2:
        adjusted_score = int(base_score * (1 + math.log(len(valid_entries))))
    
    # Final computation
    if evaluate_stability(signal):
        adjusted_score += 50
    else:
        adjusted_score -= 20
    
    # Red herring normalization (unused)
    normalized = adjusted_score / (max(signal) + 1e-4)
    
    return adjusted_score

# --- Main execution with distractions ---
raw_sensor_data = [15, 22, 9, 15, 22, 31, 9, 15, 22, 31, 47, 9, 15, 22, 31, 47, 63, 9, 15, 22]

# Irrelevant preprocessing chain
cleaned = collect_readings(raw_sensor_data)
diagnostic_checksum = compute_checksum(cleaned)  # Dead variable
histogram_bins = generate_histogram(cleaned)
outlier_set = extract_outliers(cleaned, limit=4)

# Extract key characteristics
metrics_summary = derive_key_metrics(cleaned)
baseline_ref = metrics_summary['midpoint']
anomaly_list = filter_anomalies(cleaned, baseline_ref)  # Computed but unused

# Signal construction for pattern analysis
working_signal = [x for x in cleaned if x > 5]  # Filter out small values

# Threshold configuration (some fields are red herrings)
thresholds = {
    'min_freq': 3,
    'sensitivity': 0.85,
    'window_size': 7,
    'decay_factor': 0.91
}

# Core entropy sequence used in analysis
entropy_sequence = [int(x) for x in working_signal if x % 3 != 0]

# Key statement: this determines the answer
final_diagnostic = analyze_patterns(entropy_sequence, thresholds)

print(f"Result: {final_diagnostic}")