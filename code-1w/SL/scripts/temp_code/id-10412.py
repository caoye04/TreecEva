from collections import defaultdict, Counter

# Simulated sensor data stream with noise and redundant channels
def generate_noisy_signals():
    base_signal = [i * 2 + (-1)**i for i in range(20)]
    noise = [i % 3 for i in range(20)]
    return [base_signal[i] + noise[i] for i in range(20)]

def apply_filter(x):
    return (x >> 1) + (x & 1)

def transform_buffer(buffer):
    # Irrelevant transformation path
    temp = [apply_filter(b) for b in buffer]
    shifted = temp[3:] + temp[:3]
    return shifted

def compute_checksum(arr):
    # Unused decoy function
    return sum(x ^ (x << 1) for x in arr) % 1000

def evaluate_stability(index, value):
    if index < 10:
        return value + 5
    else:
        return value - 3

def analyze_peaks(signal):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > signal[i-1] and signal[i] > signal[i+1]:
            peaks.append(i)
    return peaks

def extract_features(data):
    # Distractor: complex feature extraction that isn't fully used
    features = defaultdict(int)
    features['length'] = len(data)
    features['avg'] = sum(data) / len(data)
    features['max'] = max(data)
    features['min'] = min(data)
    features['range'] = features['max'] - features['min']
    
    # Red herring computation
    temp_stats = [abs(x - features['avg']) for x in data]
    features['deviation_sum'] = sum(temp_stats)
    
    return features

def build_processing_chain(raw):
    chain = {}
    chain['raw'] = raw[:]
    chain['filtered'] = [x for x in raw if x % 2 == 0]
    chain['corrected'] = [evaluate_stability(i, x) for i, x in enumerate(chain['filtered'])]
    chain['shifted'] = chain['corrected'][2:] + chain['corrected'][:2]  # slicing
    chain['clipped'] = [min(max(x, 10), 25) for x in chain['shifted']]
    
    # Dead code branch - never accessed
    if False:
        chain['reversed'] = chain['clipped'][::-1]
        for i in range(len(chain['reversed'])):
            chain['reversed'][i] = chain['reversed'][i] ^ 7
    
    return chain

def collect_diagnostics(chain):
    diagnosis = {}
    diagnosis['node_count'] = len(chain['corrected'])
    diagnosis['peak_positions'] = analyze_peaks(chain['clipped'])
    diagnosis['value_counts'] = Counter(chain['clipped'])  # Using Counter
    
    # Misleading intermediate calculation
    dummy_agg = 0
    for k, v in diagnosis['value_counts'].items():
        if k > 15:
            dummy_agg += k * v
    diagnosis['high_freq_contribution'] = dummy_agg
    
    # Actual relevant metric
    diagnosis['baseline_drift'] = chain['clipped'][0] - chain['filtered'][0] if chain['filtered'] else 0
    
    return diagnosis

def aggregate_metrics(chain, diag):
    metric = 0
    metric += len(chain['filtered']) * 3
    metric += diag['node_count'] * 2
    metric -= diag['baseline_drift']
    
    # Multiple layers of irrelevant additions
    extra = 0
    for val in chain['clipped']:
        if val in diag['value_counts'] and diag['value_counts'][val] > 1:
            extra += val // 4
    metric += extra
    
    # Key distractor: looks important but unused in final logic
    fake_dependency = sum(diag['value_counts'].keys()) * len(diag['peak_positions'])
    
    return metric

# Main execution flow
sensor_data = generate_noisy_signals()
features = extract_features(sensor_data)  # Computed but only partially used

# Irrelevant data transformation
buffer_snapshot = sensor_data[5:15]  # slicing
transformed = transform_buffer(buffer_snapshot)

# Core processing path
processing_chain = build_processing_chain(sensor_data)
diagnostics = collect_diagnostics(processing_chain)

# Critical statement
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

# Print result as required
print(f"Result: {final_diagnostic}")