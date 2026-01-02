import itertools

# Simulated system telemetry data with mixed signal types
def collect_signals(duration):
    signals = []
    for t in range(0, duration * 10, 1):
        raw = (t * 2.718) % 5 + (t % 7)
        filtered = raw if raw > 3 else 3
        signals.append({'time': t, 'value': round(filtered, 2), 'type': 'primary'})
    return signals

# Legacy function - unused but looks relevant
def deprecated_analysis(data):
    total = 0
    for item in data:
        if 'legacy' in item:
            total += item['legacy'] * 1.5
    return total

# Misleading auxiliary calculation with decoy variables
temp_offset = 127
calibration_map = {i: i * 0.91 for i in range(100)}
reference_checksum = sum(calibration_map.values()) // 10

# Core processing pipeline
def extract_features(signals):
    timestamps = [s['time'] for s in signals]
    values = [s['value'] for s in signals]
    
    # Compute rolling window stats (3-point windows)
    rolling_avg = []
    for i in range(2, len(values)):
        window = values[i-2:i+1]
        rolling_avg.append(sum(window) / 3)
    
    # Detect anomalies above dynamic threshold
    base_level = sum(values) / len(values)
    anomaly_threshold = base_level * 1.4
    anomalies = [v for v in values if v > anomaly_threshold]
    
    # Generate feature vector
    return {
        'count': len(values),
        'base': base_level,
        'spikes': len(anomalies),
        'stability': len(values) - len(anomalies),
        'entropy': len(set(round(v, 1) for v in values))
    }

# Advanced correlation engine using itertools
def find_correlations(features_list):
    keys = ['base', 'spikes', 'stability', 'entropy']
    combinations = list(itertools.combinations(keys, 2))
    correlations = {}
    for a, b in combinations:
        correlations[f'{a}_vs_{b}'] = abs(features_list[0].get(a, 0) - features_list[0].get(b, 0))
    return correlations

# Data enrichment with red herring transformations
def enrich_log_entry(entry):
    entry['checksum'] = sum(ord(c) for c in str(entry)) % 1000
    entry['flags'] = []
    if entry.get('spikes', 0) > 5:
        entry['flags'].append('HIGH_ACTIVITY')
    if entry.get('base', 0) < 4:
        entry['flags'].append('LOW_BASELINE')
    # Unused field generation (distractor)
    entry['deprecated_score'] = entry.get('stability', 0) * 0.7 + entry.get('entropy', 0) * 0.3
    return entry

# Main metric processor with conditional logic and early exits
def process_metrics(entries, threshold):
    if not entries:
        return 0
    
    # Filter valid entries
    valid_entries = [e for e in entries if e.get('count', 0) > threshold // 2]
    
    if len(valid_entries) == 0:
        return -1
    
    # Prioritize entry with highest stability
    sorted_entries = sorted(valid_entries, key=lambda x: x.get('stability', 0), reverse=True)
    primary = sorted_entries[0]
    
    # Early exit condition (rarely triggered - misleading path)
    if primary.get('entropy', 0) > 30 and threshold < 5:
        return sum(primary.values()) % 100
    
    # Critical computation path
    spike_ratio = primary.get('spikes', 0) / primary.get('count', 1)
    normalized_stability = primary.get('stability', 0) / (primary.get('count', 1) + 1)
    
    # Weighted diagnostic score
    weight_a = 0.6
    weight_b = 0.4
    if spike_ratio > 0.2:
        weight_a, weight_b = weight_b, weight_a  # Dynamic weight shift
    
    # Final computation
    diagnostic_score = weight_a * spike_ratio + weight_b * normalized_stability
    
    # Integer conversion for system compatibility
    final_score = int(diagnostic_score * 1000)
    
    # Dead code branch (never reached due to prior logic)
    if final_score < 0:
        fallback = 0
        for k in calibration_map:
            if k % 7 == 0:
                fallback += calibration_map[k]
        final_score = int(fallback % 100)
    
    return final_score

# Global constants that look important but are only partially used
criticality_levels = {'low': 1, 'medium': 2, 'high': 3}
system_threshold = 8
sample_duration = 50

# Data generation pipeline
raw_signals = collect_signals(sample_duration)
features = extract_features(raw_signals)
log_entries = [enrich_log_entry(features)]

# Correlation analysis (computed but not used - distractor)
correlations = find_correlations([features])
decoy_result = deprecated_analysis([{'legacy': 42}])

# Key execution point
final_diagnostic = process_metrics(log_entries, system_threshold)
print(f"Result: {final_diagnostic}")