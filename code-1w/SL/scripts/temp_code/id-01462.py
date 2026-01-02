from collections import defaultdict, Counter
from itertools import combinations, cycle

# Simulated sensor network diagnostic system
def collect_sensor_readings():
    raw_streams = {
        'temp': [23.1, 24.5, 19.8, 25.6, 26.7, 22.4, 20.1, 27.3],
        'pressure': [101.3, 102.1, 99.8, 103.4, 100.2, 101.8, 98.7, 104.5],
        'humidity': [45, 52, 38, 61, 47, 55, 40, 67]
    }

    # Irrelevant transformation - red herring
    normalized = {}
    for k, v in raw_streams.items():
        mean_val = sum(v) / len(v)
        normalized[k] = [x - mean_val for x in v]

    # Actual relevant data extraction
    readings = []
    for i in range(len(raw_streams['temp'])):
        composite_index = (raw_streams['temp'][i] * 0.5 + 
                          raw_streams['pressure'][i] * 0.3 + 
                          raw_streams['humidity'][i] * 0.2)
        readings.append((i, composite_index))

    return raw_streams, readings

# Decoy function - never called
def analyze_failure_modes(data):
    critical_events = 0
    for val in data['temp']:
        if val > 25 and abs(val - 25) < 3:
            critical_events += 1
    return critical_events

# Unused utility - distractor
bitmask_patterns = [0b1010, 0b1100, 0b0110, 0b1111]
active_mask = bitmask_patterns[2] ^ 0b1010 & 0b0111

# Main processing pipeline
def filter_anomalies(raw_data, indices):
    # Extract high-risk time windows
    risk_flags = []
    for idx, score in indices:
        temp_dev = abs(raw_data['temp'][idx] - 24.0)
        press_dev = abs(raw_data['pressure'][idx] - 101.5)
        humid_dev = abs(raw_data['humidity'][idx] - 50)
        
        total_deviation = temp_dev * 0.4 + press_dev * 0.35 + humid_dev * 0.25
        
        # This condition is actually irrelevant - misleading
        if total_deviation > 8.0:
            risk_flags.append((idx, 'CRITICAL'))
        elif total_deviation > 5.0:
            risk_flags.append((idx, 'WARNING'))
    
    # But we only care about specific index pattern
    valid_indices = [i for i, s in indices if i % 2 == 1]  # Only odd positions
    filtered = [(i, raw_data['temp'][i]) for i in valid_indices]
    
    # Dead code branch - unreachable
    if False:
        emergency_override = sum(x[1] for x in filtered) * 0.1
        return emergency_override

    return filtered

# Threshold configuration (real logic uses this)
def build_threshold_map():
    config = defaultdict(dict)
    config['temp']['warning'] = 24.0
    config['temp']['fault'] = 26.0
    config['cycles'] = list(cycle([1, 2, 3]))[:10]  # unused portion
    config['version'] = 2.1
    
    # Real thresholds used later
    limits = {
        'low_risk': 23.5,
        'moderate_risk': 25.0,
        'high_risk': 26.5
    }
    
    # Add decoy entries
    config['debug'] = {k: hash(str(v)) % 1000 for k, v in limits.items()}
    
    return limits

# Core analysis function
def process_readings(data_points, thresholds):
    accumulator = 0
    
    # Generate all possible pairs for correlation check (not actually used)
    pairs = list(combinations(data_points, 2))
    correlation_shadow = len(pairs) % 7  # misleading intermediate
    
    # Real logic: classify and aggregate
    classifications = []
    for index, temp_val in data_points:
        if temp_val < thresholds['low_risk']:
            classifications.append(1)
        elif temp_val < thresholds['moderate_risk']:
            classifications.append(2)
        elif temp_val < thresholds['high_risk']:
            classifications.append(3)
        else:
            classifications.append(4)
    
    # Count distribution (used)
    freq = Counter(classifications)
    
    # Complex weighting calculation with red herrings
    weights = {1: 0.1, 2: 0.3, 3: 0.7, 4: 1.2}
    weighted_score = 0
    
    # Irrelevant bitwise manipulation
    magic_seed = 0b101010
    shift_key = (magic_seed >> 3) & 0b111
    salt_value = shift_key ^ 0b101
    
    # Actual scoring
    for cls, count in freq.items():
        contribution = count * weights[cls] * (cls + salt_value)  # salt_value = 5
        weighted_score += contribution
    
    # Final adjustment using correct path
    baseline = len(data_points) * 2.5
    final_score = weighted_score - baseline
    
    # Multiple return candidates - but only one used
    debug_snapshot = {
        'entries': len(data_points),
        'score_raw': weighted_score,
        'baseline': baseline,
        'salt': salt_value
    }
    
    # The actual answer flows here
    final_diagnostic = int(round(final_score * 10))  # Scale and truncate
    
    # Never reached - dead code
    if final_diagnostic < 0:
        fallback = sum(freq.values()) << 2
        return fallback
        
    return final_diagnostic

# Execution sequence
if __name__ == '__main__':
    raw_data, indexed_scores = collect_sensor_readings()
    
    # Irrelevant data structure
    metadata_tree = {
        'nodes': [
            {'id': 'A1', 'type': 'sensor', 'depth': 1},
            {'id': 'B2', 'type': 'aggregator', 'depth': 2}
        ]
    }
    
    # Filtering step
    filtered_data = filter_anomalies(raw_data, indexed_scores)
    
    # Threshold setup
    threshold_map = build_threshold_map()
    
    # Critical computation
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")