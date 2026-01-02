from collections import defaultdict, Counter
import math

# Simulated health monitoring system with diagnostic logic

def analyze_readings(readings):
    stats = defaultdict(float)
    anomalies = []
    total = 0
    count = 0
    
    for r in readings:
        if r < 0 or r > 200:  # Invalid reading
            anomalies.append(r)
            continue
        total += r
        count += 1
        
    stats['average'] = total / count if count else 0
    stats['anomaly_count'] = len(anomalies)
    return stats

# Irrelevant helper - decoy function
def compute_bandwidth(signal):
    return sum(abs(a - b) for a, b in zip(signal, signal[1:]))

# Another red herring - unused transformation
def encrypt_data(data):
    rotated = ''.join(chr((ord(c) - 97 + 3) % 26 + 97) for c in data.lower() if c.isalpha())
    return rotated[::-1]

# Misleading preprocessing chain
def preprocess_labels(labels):
    encoded = [hash(l) % 100 for l in labels]
    sorted_encoded = sorted(encoded, reverse=True)
    filtered = [e for e in sorted_encoded if e > 10]
    return filtered[:5]

# Core processing with distractors
def extract_features(raw_data):
    features = {}
    temp_seq = []
    
    for item in raw_data:
        x = item * 1.05
        y = math.log(x + 1e-8)
        z = math.sin(x / 10) * math.cos(y / 5)
        temp_seq.append(z)
    
    # Distractor: complex but unused computation
    fft_approx = [sum(temp_seq[i::4]) for i in range(4)]
    normalized = [round(v * 2.5, 3) for v in fft_approx]
    
    # Actual relevant feature
    features['signal_power'] = sum(v**2 for v in temp_seq[-10:])
    return features

# Decoy state tracker
class MonitoringState:
    def __init__(self):
        self.timestamp = 0
        self.alerts_issued = 0
        self._cache = {}
    
    def update(self, val):
        self._cache[self.timestamp] = val

# Unused sorting path
def sort_by_priority(items):
    priority_map = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
    return sorted(items, key=lambda x: priority_map.get(x[1], 4))

# Real processing with embedded noise
def process_metrics(data, config):
    results = {}
    
    # Step 1: Analyze raw sensor values
    vital_stats = analyze_readings(data['vitals'])
    results['baseline'] = vital_stats['average']
    
    # Step 2: Extract temporal features
    extended_sequence = data['vitals'] + [data['vitals'][-1]] * 5
    derived = extract_features(extended_sequence)
    
    # Step 3: Apply threshold logic (actual decision point)
    power = derived['signal_power']
    thresh_low = config['power']['normal'][0]
    thresh_high = config['power']['normal'][1]
    
    status_flag = 0
    if power < thresh_low:
        status_flag = -1
    elif power > thresh_high:
        status_flag = 1
    else:
        status_flag = 0
    
    # Distractor: complex bit manipulation with no effect
    debug_code = 0
    for i in range(8):
        debug_code ^= (status_flag + i) << (i & 3)
    
    # Irrelevant string processing chain
    labels = ['node_A', 'node_B', 'node_C']
    processed_keys = preprocess_labels(labels)
    encrypted_key = encrypt_data('diagnostic_sync')
    
    # Critical but obscured calculation
    adjustment = len(processed_keys) * 0.1
    adjusted_power = power - adjustment
    
    # Final diagnostic - this is the actual answer
    if adjusted_power < thresh_low - 0.5:
        final_score = 42
    elif adjusted_power > thresh_high + 0.5:
        final_score = 84
    else:
        final_score = int(round(adjusted_power * 2))
    
    # Red herring assignment
    results['diagnostic_code'] = debug_code
    results['final_diagnostic'] = final_score  # This is what we need
    
    return results['final_diagnostic']

# Simulated input data
health_data = {
    'vitals': [78, 82, 76, 85, 80, 77, 83, 79, 81, 84, 75, 86, 77, 80, 79],
    'labels': ['primary', 'secondary']
}

thresholds = {
    'power': {
        'normal': [40.0, 60.0]
    }
}

# Execution point
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Target result: {final_diagnostic}")