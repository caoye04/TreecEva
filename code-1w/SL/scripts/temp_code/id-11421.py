from collections import defaultdict, Counter
import itertools

# Simulated sensor data stream with metadata
data_stream = [
    {'type': 'temp', 'value': 23.5, 'sensor_id': 'T001', 'status': 'ok'},
    {'type': 'pressure', 'value': 1013.25, 'sensor_id': 'P001', 'status': 'ok'},
    {'type': 'temp', 'value': 24.1, 'sensor_id': 'T002', 'status': 'ok'},
    {'type': 'humidity', 'value': 45.0, 'sensor_id': 'H001', 'status': 'ok'},
    {'type': 'temp', 'value': 22.8, 'sensor_id': 'T001', 'status': 'ok'},
    {'type': 'pressure', 'value': 1012.9, 'sensor_id': 'P001', 'status': 'ok'},
    {'type': 'temp', 'value': 24.3, 'sensor_id': 'T002', 'status': 'fault'},  # Faulty reading
    {'type': 'humidity', 'value': 46.2, 'sensor_id': 'H001', 'status': 'ok'}
]

# Configuration map (some entries are red herrings)
config = {
    'thresholds': {
        'temp': (20.0, 30.0),
        'pressure': (950.0, 1050.0),
        'humidity': (30.0, 70.0)
    },
    'weights': {
        'temp': 0.5,
        'pressure': 0.3,
        'humidity': 0.2
    },
    'aggregation': 'weighted_mean',
    'debug_mode': True,
    'log_level': 'verbose',
    'sampling_rate': 100,
    'buffer_size': 1024
}

# Irrelevant helper (dead code path)
def validate_checksum(data):
    return sum(ord(c) for c in str(data)) % 256

# Misleading preprocessing function that is never called
def normalize_readings(stream):
    normed = []
    for item in stream:
        if item['type'] == 'temp':
            normed.append({**item, 'value': (item['value'] - 20) / 10})
        elif item['type'] == 'pressure':
            normed.append({**item, 'value': (item['value'] - 1000) / 50})
        else:
            normed.append(item)
    return normed

# Decoy statistical function
def compute_entropy(values):
    counter = Counter(values)
    total = len(values)
    entropy = 0
    for count in counter.values():
        p = count / total
        entropy -= p * __import__('math').log2(p)
    return entropy

# Main processing pipeline
def collect_by_type(stream):
    grouped = defaultdict(list)
    status_log = defaultdict(int)
    
    for entry in stream:
        t = entry['type']
        v = entry['value']
        s = entry['status']
        status_log[t] += 1
        
        # Only include valid status readings
        if s == 'ok':
            grouped[t].append(v)
    
    # Distractor: unused transformation
    flattened = list(itertools.chain.from_iterable(grouped.values()))
    
    return grouped, status_log

def filter_outliers(data_dict, thresholds):
    filtered = {}
    outlier_count = 0
    
    for key, values in data_dict.items():
        low, high = thresholds[key]
        valid = [v for v in values if low <= v <= high]
        outlier_count += len(values) - len(valid)
        filtered[key] = valid
    
    # Red herring variable
    avg_outliers = outlier_count / len(data_dict) if data_dict else 0
    
    return filtered

def aggregate_data(data_dict, method='mean'):
    results = {}
    
    for k, v in data_dict.items():
        if not v:
            results[k] = 0.0
            continue
        
        if method == 'mean':
            results[k] = sum(v) / len(v)
        elif method == 'median':
            sorted_v = sorted(v)
            mid = len(sorted_v) // 2
            results[k] = sorted_v[mid] if len(sorted_v) % 2 else (sorted_v[mid-1] + sorted_v[mid]) / 2
    
    return results

def apply_weighting(values, weights):
    total_weighted = 0.0
    total_weight = 0.0
    
    for key, val in values.items():
        if key in weights:
            total_weighted += val * weights[key]
            total_weight += weights[key]
    
    return total_weighted / total_weight if total_weight else 0.0

def detect_trend(series):
    if len(series) < 3:
        return 'stable'
    diffs = [series[i+1] - series[i] for i in range(len(series)-1)]
    pos = sum(1 for d in diffs if d > 0)
    neg = sum(1 for d in diffs if d < 0)
    return 'increasing' if pos > neg else 'decreasing' if neg > pos else 'stable'

def process_segments(raw_data, cfg):
    # Step 1: Group data by type, filtering only 'ok' status
    collected_data, logs = collect_by_type(raw_data)
    
    # Step 2: Apply threshold-based outlier filtering
    cleaned_data = filter_outliers(collected_data, cfg['thresholds'])
    
    # Step 3: Aggregate each sensor type
    aggregated = aggregate_data(cleaned_data, method='mean')
    
    # Step 4: Detect trend in temperature (distractor usage)
    temp_trend = detect_trend(collected_data.get('temp', []))
    
    # Step 5: Apply weighted fusion only on aggregated values
    fused_value = apply_weighting(aggregated, cfg['weights'])
    
    # Step 6: Additional correction based on pressure trend (unused)
    pressure_values = collected_data.get('pressure', [])
    pressure_trend = detect_trend(pressure_values)
    
    # Step 7: Final adjustment using bit manipulation (red herring)
    adjusted_int = int(fused_value * 100)
    masked = adjusted_int & 0xFF  # Keep only lower 8 bits
    final_decimal = masked / 100.0
    
    # Step 8: Use character counting from sensor IDs as offset (irrelevant)
    all_ids = ''.join(entry['sensor_id'] for entry in raw_data)
    char_freq = Counter(all_ids)
    offset = char_freq.get('0', 0) - char_freq.get('1', 0)  # Likely zero
    
    # Step 9: Real computation — combine final_decimal with offset (but offset is negligible)
    final_output = final_decimal + offset
    
    # Step 10: Print intermediate distractors (for confusion)
    debug_info = {
        'temp_trend': temp_trend,
        'pressure_trend': pressure_trend,
        'outlier_estimate': logs['temp'] - len(cleaned_data.get('temp', [])),
        'entropy_test': compute_entropy([1,1,2,2,3,3])  # Constant call
    }
    
    return final_output

# Execution flow
if __name__ == '__main__':
    collected_data, _ = collect_by_type(data_stream)
    final_output = process_segments(data_stream, config)
    print(f"Target result: {final_output}")