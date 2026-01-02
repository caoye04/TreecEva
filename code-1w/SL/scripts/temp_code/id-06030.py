from collections import defaultdict, Counter
import math

# Simulated sensor network diagnostic system
def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    trend = sum(1 for i in range(1, len(sequence)) if sequence[i] > sequence[i-1])
    return trend > (len(sequence) // 2)

def validate_checksum(data_str):
    # Irrelevant checksum validation (dead logic path)
    total = 0
    for c in data_str:
        total += ord(c)
    return total % 17 == 0

def dummy_aggregator(inputs):
    # Decoy function: never actually used in critical path
    aggregate = 0
    for item in inputs:
        if isinstance(item, dict) and 'val' in item:
            aggregate += item['val'] ** 0.5
    return aggregate

def generate_metadata(tags):
    # Distractor: builds unused metadata structure
    meta = defaultdict(lambda: 'unknown')
    for t in tags:
        if t.startswith('loc_'):
            meta['location'] = t[4:]
        elif t.startswith('v_'):
            meta['version'] = t
    meta['processed'] = True
    return dict(meta)

def filter_outliers(readings, limit=50):
    # Real but partially misleading filtering
    counts = Counter(readings)
    filtered = [r for r in readings if counts[r] >= 2 or r < limit]
    # But we don't actually use frequency filtering in final logic
    return [x for x in readings if x <= limit]  # Only upper bound matters

def compute_stability_index(stream):
    if len(stream) == 0:
        return 0.0
    variance = sum((x - sum(stream)/len(stream))**2 for x in stream) / len(stream)
    return round(math.exp(-variance / 100.0), 4)

def evaluate_consistency(logs):
    # Complex but irrelevant consistency metric
    transitions = 0
    for i in range(1, len(logs)):
        if logs[i] != logs[i-1]:
            transitions += 1
    penalty = transitions * 0.05
    return max(0, 1 - penalty)

def extract_critical_band(data, low, high):
    # Actually used: extracts values in band
    return [x for x in data if low <= x <= high]

def count_anomalies(values, baseline):
    # Red herring: looks important but not used in final answer
    anomalies = 0
    ref = sum(baseline) / len(baseline) if baseline else 0
    for v in values:
        if abs(v - ref) > 15:
            anomalies += 1
    return anomalies

def process_readings(raw_data, config):
    # Core processing with hidden key logic
    
    # Irrelevant preprocessing
    raw_data.sort(reverse=True)
    stats_summary = {}
    stats_summary['peak'] = raw_data[0] if raw_data else 0
    stats_summary['floor'] = raw_data[-1] if raw_data else 0
    
    # Distractor: complex transformation not fully used
    normalized = []
    span = stats_summary['peak'] - stats_summary['floor'] or 1
    for val in raw_data:
        norm_val = (val - stats_summary['floor']) / span
        normalized.append(round(norm_val, 3))
    
    # Key branching logic based on config flags
    use_tight_filter = config.get('strict_mode', False)
    threshold_band = config.get('band', (20, 80))
    
    # Actual relevant data path begins here
    band_filtered = extract_critical_band(raw_data, *threshold_band)
    
    # Secondary filter: only keep values divisible by 3 (hidden rule)
    candidate_set = [x for x in band_filtered if x % 3 == 0]
    
    # Stability analysis is crucial
    stability = compute_stability_index(candidate_set)
    
    # Tertiary condition: must have at least 2 elements to proceed
    if len(candidate_set) < 2:
        fallback = [x for x in raw_data if x % 3 == 0 and x <= 60]
        primary_value = sum(fallback) if fallback else 0
    else:
        # The real computation: weighted combination
        base_sum = sum(candidate_set)
        weight = stability * 0.7 + 0.3  # Minimum weight 0.3
        adjusted = int(base_sum * weight)
        
        # Final twist: add length only if sum exceeds 100
        if base_sum > 100:
            adjusted += len(candidate_set)
        
        primary_value = adjusted
    
    # Dead code branch (looks like it might be used)
    if config.get('debug', False):
        debug_snapshot = {
            'input_len': len(raw_data),
            'post_band': len(band_filtered),
            'post_div3': len(candidate_set),
            'stability': stability
        }
    
    # Critical assignment
    final_diagnostic = primary_value * 2  # Final transformation
    
    # Never reached due to unconditional prior assignment
    if False:
        fallback_metrics = defaultdict(int)
        for v in raw_data:
            bucket = v // 10
            fallback_metrics[bucket] += 1
        final_diagnostic = min(fallback_metrics.values()) * 5
    
    return final_diagnostic

# Simulated input data
sensor_tags = ['loc_a7', 'v_2.1', 'diag_core', 'temp_stable']
raw_readings = [95, 42, 63, 28, 42, 78, 15, 63, 36, 88, 51, 44, 21]
thresholds = {
    'strict_mode': True,
    'band': (25, 75),
    'debug': False,
    'timeout': 300
}

# Generate unused metadata (distractor)
context_meta = generate_metadata(sensor_tags)

# Validate dummy checksum (never used)
data_id = "sensor_A7_XT"
is_valid = validate_checksum(data_id)

# Apply filters
filtered_readings = filter_outliers(raw_readings, limit=50)
signal_pattern = [63, 42, 78, 63, 36]

# Compute irrelevant metrics
pattern_score = analyze_pattern(signal_pattern)
consistency = evaluate_consistency(['A','A','B','B','B','C'])
anomaly_count = count_anomalies(raw_readings, [40, 50, 60])

# Core execution
sensor_data = raw_readings.copy()
final_diagnostic = process_readings(sensor_data, thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")