from collections import defaultdict, Counter

# Simulated sensor network diagnostic system
def analyze_sensor_trends(raw_readings, baseline):
    trend_counter = defaultdict(int)
    volatility_index = 0
    normalized_scores = []
    
    for node_id, readings in raw_readings.items():
        if len(readings) < 3:
            continue
            
        # Real processing path
        avg_reading = sum(readings) / len(readings)
        deviation = abs(avg_reading - baseline[node_id])
        trend_counter[node_id] += 1

        # Distractor: complex but unused volatility metric
        squared_diffs = [(r - avg_reading)**2 for r in readings]
        if squared_diffs:
            volatility = sum(squared_diffs) / len(squared_diffs)
            volatility_index += volatility * 0.3

        # Normalization with slicing distraction
        windowed = readings[1:-1]  # Ignore first and last
        if windowed:
            norm_val = (sum(windowed) / len(windowed)) / (baseline[node_id] + 1e-8)
            normalized_scores.append(max(min(norm_val, 1.5), 0.5))

    return dict(trend_counter), normalized_scores


def filter_outliers(data, method='iqr'):
    # Unused advanced filtering (dead path)
    if method == 'zscore':
        return {k: v for k, v in data.items() if len(v) > 1}
    elif method == 'mad':
        return defaultdict(list)
    
    # Actual simple filter (misleading complexity above)
    filtered = {}
    for k, v in data.items():
        if not v or max(v) - min(v) > 50:  # Simple range check
            continue
        filtered[k] = v
    return filtered

# Irrelevant utility (distractor)
def compute_checksum(sequence):
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val * (i + 1)) & 0xFF
    return format(checksum, 'x')

# Decoy data structure
class DiagnosticBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0] * size
    
    def append(self, val):
        self.buffer.pop(0)
        self.buffer.append(val % 100)

# Unused recursive red herring
def binary_weight(n, acc=0):
    if n <= 0:
        return acc
    return binary_weight(n // 2, acc + (n & 1))

# Main execution
sensor_data = {
    'node_01A': [120, 125, 118, 122],
    'node_02B': [95, 105, 130, 98],
    'node_03C': [88, 85, 87],
    'node_04D': [200, 205, 198, 202, 199],
    'node_05E': [75, 73, 77, 76]
}

baseline_values = {
    'node_01A': 120,
    'node_02B': 100,
    'node_03C': 86,
    'node_04D': 200,
    'node_05E': 75
}

# Distractor variables
system_mode = 'diagnostic'
diag_buffer = DiagnosticBuffer(10)
for i in range(5):
    diag_buffer.append(i * 17)

data_integrity = compute_checksum([1, 1, 2, 3, 5, 8, 13])

# Actual processing begins here
outlier_method = 'iqr'
filtered_data = filter_outliers(sensor_data, method=outlier_method)

# Threshold map uses set operations (required feature)
valid_nodes = set(filtered_data.keys())
required_nodes = {'node_01A', 'node_02B', 'node_03C', 'node_05E'}
active_nodes = valid_nodes & required_nodes  # Intersection

threshold_map = defaultdict(lambda: 0.1)
for node in active_nodes:
    base = baseline_values[node]
    if base > 100:
        threshold_map[node] = 0.15
    else:
        threshold_map[node] = 0.08

# Core function - only this affects final answer
def process_readings(clean_data, thresholds):
    result = 0
    stats_log = []
    
    for nid, vals in clean_data.items():
        if nid not in thresholds:
            continue
            
        # Key computation
        q1, q3 = vals[len(vals)//4], vals[3*len(vals)//4]
        iqr = q3 - q1
        median = sorted(vals)[len(vals)//2]
        
        # Decision logic
        if median > baseline_values[nid]:
            adjustment = int(median * thresholds[nid])
        else:
            adjustment = -int((baseline_values[nid] - median) * 0.5)
            
        # Accumulate result
        result += adjustment * (iqr % 3 + 1)
        
        # Dead code branch (misleads traceability)
        if False:
            stats_log.append({'node': nid, 'adj': adjustment})
            
    # Final transformation
    temp_result = result * 2
    final_result = abs(temp_result) + 5
    
    # Critical assignment
    final_diagnostic = final_result + 10
    
    return final_diagnostic

# Execute key statement
trends, scores = analyze_sensor_trends(sensor_data, baseline_values)
final_diagnostic = process_readings(filtered_data, threshold_map)

print(f"Result: {final_diagnostic}")