from collections import defaultdict, Counter
import math

# Simulated system log analyzer with performance metrics and distractors
def analyze_log_integrity(raw_logs):
    if not raw_logs:
        return False
    
    # Distractor: checksum validation (never used in final logic)
    checksum = sum(len(log) for log in raw_logs) % 7
    temp_data = [log.strip('[]') for log in raw_logs if 'ERROR' not in log]
    
    # Red herring: nested structure that isn't used
    metadata_tree = {}
    for i, entry in enumerate(temp_data):
        if i % 5 == 0:
            metadata_tree[f'node_{i}'] = {'depth': i // 3, 'flag': False}
    
    return len(temp_data) > 3

# Irrelevant auxiliary function (dead code path)
def compute_entropy(data_list):
    freq = {}
    for item in data_list:
        freq[item] = freq.get(item, 0) + 1
    total = len(data_list)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 4)

# Decoy transformation function
def transform_legacy_format(old_logs):
    mapping = defaultdict(int)
    for log in old_logs:
        parts = log.split(':')
        if len(parts) > 1:
            mapping[parts[0]] += 1
    return dict(mapping)

# Real logic begins here — subtle signal among noise
def extract_metrics(entries, baseline=0.85):
    scores = []
    anomalies = set()
    
    for entry in entries:
        if 'TRACE' in entry:
            # Valid path: extract duration and normalize
            try:
                duration_str = entry.split('duration=')[1].split(',')[0]
                duration = float(duration_str)
                normalized = duration * 0.77
                scores.append(normalized)
            except (IndexError, ValueError):
                anomalies.add(entry)
    
    # Distractor: unused statistical summary
    mean_score = sum(scores) / len(scores) if scores else 0
    stdev = (sum((x - mean_score) ** 2 for x in scores) / (len(scores) or 1)) ** 0.5
    
    # Another red herring: outlier detection (not influencing output)
    filtered = [s for s in scores if abs(s - mean_score) <= 2 * stdev]
    
    return scores  # Actual return used downstream

# Core aggregation with multiple concepts
def aggregate_performance(logs, threshold):
    # Parse and filter logs
    parsed = [line for line in logs if line.startswith('LOG')]
    
    # Use of Counter — relevant feature
    level_counts = Counter()
    for line in parsed:
        if 'LEVEL' in line:
            lvl = line.split('LEVEL=')[1][0]
            level_counts[lvl] += 1
    
    # Extract durations using real logic
    durations = extract_metrics(logs, baseline=threshold)
    
    # Fake model weights (distractor)
    weights = defaultdict(float)
    for k in 'ABCDE':
        weights[k] = 0.1 * ord(k) % 0.9
    
    # Accumulation with integer division and rounding
    base_accum = 0
    for val in durations:
        if val > 0.5:
            base_accum += int(val * 100) // 3  # Integer division
    
    # Set operations as required feature
    high_dur = {int(d * 10) for d in durations if d > 0.6}
    low_dur = {int(d * 10) for d in durations if d <= 0.6}
    overlap = high_dur & low_dur  # Empty, but plausible
    
    # Real computation path
    adjustment = len(high_dur) - len(overlap)
    raw_total = sum(durations) * 1000
    
    # Final score influenced by multiple factors
    scaling_factor = 1.0
    if analyze_log_integrity(logs):  # This returns True, used subtly
        scaling_factor += 0.25
    
    intermediate = raw_total + base_accum
    
    # Critical statement
    final_score = int(intermediate / (1 + threshold)) * adjustment
    
    # Dead code below (never reached due to return)
    if final_score < 0:
        fallback = compute_entropy([str(int(d)) for d in durations])
        return fallback
        
    return final_score

# Simulated input logs — mix of signal and noise
log_data = [
    'LOG:TRACE id=001,duration=1.23,LEVEL=A',
    'INFO: system ready',
    'LOG:TRACE id=002,duration=0.89,LEVEL=B',
    'ERROR: disk full',
    'LOG:TRACE id=003,duration=1.51,LEVEL=A',
    'METADATA: node=alpha',
    'LOG:TRACE id=004,duration=0.45,LEVEL=C',
    'LOG:TRACE id=005,duration=1.72,LEVEL=A',
    'DEBUG: tracing enabled',
    'LOG:TRACE id=006,duration=0.93,LEVEL=B'
]

user_threshold = 0.65

# Execution point of interest
final_score = aggregate_performance(log_data, user_threshold)

print(f"Result: {final_score}")