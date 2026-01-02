from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'sensor': 'temp', 'value': 72.3, 'status': 'OK', 'node': 'A1'},
    {'sensor': 'pressure', 'value': 101.8, 'status': 'OK', 'node': 'A2'},
    {'sensor': 'temp', 'value': 75.1, 'status': 'WARN', 'node': 'A1'},
    {'sensor': 'flow', 'value': 12.5, 'status': 'OK', 'node': 'B1'},
    {'sensor': 'temp', 'value': 88.9, 'status': 'ALERT', 'node': 'A3'},
    {'sensor': 'pressure', 'value': 95.4, 'status': 'WARN', 'node': 'A2'},
    {'sensor': 'flow', 'value': 8.3, 'status': 'ALERT', 'node': 'B2'}
]

# Irrelevant helper that counts character frequencies in sensor names (distraction)
def analyze_labels(data):
    label_text = ''.join(d['sensor'] for d in data)
    return Counter(label_text)

# Misleading metric: computes average but on non-numeric status (dead end)
def bogus_aggregate(data):
    statuses = [d['status'] for d in data]
    if not statuses:
        return 0
    # Nonsensical conversion
    return sum(len(s) for s in statuses) / len(statuses)

# Decoy function: appears useful but unused in final path
def legacy_calibrate(values):
    adjusted = []
    for v in values:
        if v < 50:
            adjusted.append(v * 1.2)
        elif v > 90:
            adjusted.append(v * 0.85)
        else:
            adjusted.append(v)
    return adjusted

# Real processing begins here
def extract_readings(telemetry, sensor_type):
    return [entry['value'] for entry in telemetry if entry['sensor'] == sensor_type]

def compute_entropy(values):
    if not values or len(values) == 0:
        return 0.0
    freq = defaultdict(int)
    total = len(values)
    for v in values:
        freq[round(v)] += 1  # Discretize for frequency
    entropy = 0.0
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def validate_nodes(telemetry):
    node_health = defaultdict(list)
    for entry in telemetry:
        node_health[entry['node']].append(entry['status'])
    
    health_score = 0
    for node, statuses in node_health.items():
        for s in statuses:
            if s == 'ALERT':
                health_score -= 3
            elif s == 'WARN':
                health_score -= 1
            else:
                health_score += 1
    return health_score

# Auxiliary transformation with partial relevance
def transform_log(telemetry):
    log_matrix = defaultdict(list)
    for entry in telemetry:
        log_matrix[entry['sensor']].append(entry['value'])
    
    # Compute z-scores for each sensor group (some distraction)
    normalized = {}
    for sensor, vals in log_matrix.items():
        mean = sum(vals) / len(vals)
        variance = sum((v - mean) ** 2 for v in vals) / len(vals)
        std_dev = math.sqrt(variance) if variance > 0 else 1
        normalized[sensor] = [(v - mean) / std_dev for v in vals]
    
    # But only return raw transformed temp for actual use
    return normalized.get('temp', [])

# Main processing pipeline
def process_metrics(log_data, system_mode):
    # Step 1: Extract temperature readings
    temps = extract_readings(log_data, 'temp')
    
    # Step 2: Compute entropy of temperature distribution
    temp_entropy = compute_entropy(temps)
    
    # Step 3: Get node validation score
    node_score = validate_nodes(log_data)
    
    # Step 4: Transform log and get normalized temp deviations
    norm_devs = transform_log(log_data)
    
    # Step 5: Aggregate deviation magnitude (only used if mode is 'strict')
    dev_magnitude = sum(abs(d) for d in norm_devs)
    
    # Step 6: Apply conditional weighting based on system mode
    if system_mode == 'diagnostic':
        base = temp_entropy * 100
        penalty = abs(node_score) * 10
        # Only use dev_magnitude if any ALERT exists
        alert_count = sum(1 for d in log_data if d['status'] == 'ALERT')
        if alert_count > 0:
            base += dev_magnitude * 5
        result = int(base - penalty)
    else:
        result = int(temp_entropy * 50)
    
    # Step 7: Final adjustment via bit manipulation (obscure but deterministic)
    result = (result ^ 0xAAAA) & 0xFFFF  # XOR mask then truncate to 16 bits
    result = (result * 3) // 7  # Nonlinear scaling
    
    return result

# Irrelevant global constants (distractors)
MAX_BUFFER_SIZE = 8192
PROTOCOL_VERSION = '2.1.7'
DEBUG_FLAGS = {'io': False, 'memory': True, 'timing': False}

# Simulated system state
system_state = 'diagnostic'

# Execute key transformations
char_freq = analyze_labels(telemetry_stream)  # Dead-end analysis
bogus_metric = bogus_aggregate(telemetry_stream)  # Misleading scalar
legacy_adjusted = legacy_calibrate(extract_readings(telemetry_stream, 'flow'))  # Unused correction

# Core execution point
final_diagnostic = process_metrics(telemetry_stream, system_state)

# Output the target result
print(f"Target result: {final_diagnostic}")