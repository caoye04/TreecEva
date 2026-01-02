import itertools

def analyze_readings(readings):
    # Irrelevant transformation (distractor)
    normalized = [r * 0.98 + 2 for r in readings]
    filtered = [r for r in readings if 10 < r < 100]  # Only original readings used
    return sum(filtered) // len(filtered) if filtered else 0

def compute_entropy(data):
    # Dead code path - never called
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = 0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

def validate_signal(signal_str):
    # String method distractor
    if not signal_str.strip().isalnum():
        return False
    parts = signal_str.split('_')
    return len(parts) == 3 and all(p.isalpha() for p in parts[:2])

def integrate_sensor_data(raw_logs):
    # Unused complex unpacking (distractor)
    records = []
    for log in raw_logs:
        timestamp, val_str = log.split('|')
        values = list(map(float, val_str.split(',')))
        records.append((timestamp, values))
    return records

def process_metrics(data, config):
    # Core logic begins
    baseline = data['baseline']
    spikes = data['spike_series']
    
    # Distractor: irrelevant set operations
    unique_spikes = set(spikes)
    spike_outliers = {s for s in unique_spikes if s > 200}  # Not actually used in result
    
    # Real computation chain
    avg_spike = sum(spikes) / len(spikes) if spikes else 0
    adjusted_baseline = baseline * config['scale'] + config['offset']
    
    # Multiple nested conditions with red herring branches
    trend_score = 0
    if adjusted_baseline > 75:
        if avg_spike > 150:
            trend_score = 3
        elif avg_spike > 100:
            trend_score = 2
        else:
            trend_score = 1
    else:
        if avg_spike > 120:
            # Misleading branch (never reached due to outer condition)
            temp_flag = True
            trend_score = -1
        else:
            trend_score = 0
    
    # Complex but only partially relevant transformation
    moving_avg = []
    window_size = 3
    for i in range(len(spikes) - window_size + 1):
        window = spikes[i:i+window_size]
        moving_avg.append(sum(window) / window_size)
    high_moving = len([ma for ma in moving_avg if ma > 110])
    
    # Key calculation: uses high_moving as weight factor
    diagnostic_weight = high_moving or 1
    intermediate = (adjusted_baseline + avg_spike) / diagnostic_weight
    
    # Final logic step
    if trend_score >= 2:
        final_adjustment = 1.75
    else:
        final_adjustment = 0.85
    
    result = intermediate * final_adjustment
    return int(round(result))

# Main execution block
if __name__ == '__main__':
    # Simulated health monitoring system data
    health_data = {
        'baseline': 68,
        'spike_series': [95, 105, 132, 141, 99, 168, 173],  # 7 elements
        'timestamps': ['t1', 't2', 't3', 't4', 't5', 't6', 't7']  # unused
    }
    
    # Configuration with decoy keys
    thresholds = {
        'scale': 1.3,
        'offset': 8.5,
        'critical_level': 180,      # unused
        'hysteresis_window': 5,     # unused
        'sampling_rate': 10         # unused
    }
    
    # Irrelevant string processing (distractor)
    signal_tag = "ECG_LEAD_II"
    valid = validate_signal(signal_tag)
    processed_tag = signal_tag.lower().replace('_', '-')
    
    # Unused itertools example (distractor)
    combinations = list(itertools.combinations([1, 2, 3], 2))
    
    # Core call
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Print required result
    print(f"Target result: {final_diagnostic}")