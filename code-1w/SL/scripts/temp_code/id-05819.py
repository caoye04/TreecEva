import math

# Irrelevant utility function (dead code path)
def normalize_data(data):
    return [x / sum(data) for x in data]

# Misleading performance estimator (not used in final calculation)
def legacy_scorer(values):
    base = sum([v ** 0.5 for v in values])
    penalty = len(values) * 0.1
    return base - penalty

# Core system: Signal integrity evaluation with multiple distortions
def generate_noise_factor(level, mode='additive'):
    if mode == 'additive':
        return level * 0.03
    else:
        return level * 0.07

# Unused but plausible transformation
def encode_metrics(metrics):
    encoded = {}
    for k, v in metrics.items():
        key_encoded = ''.join([chr(ord(c)+1) for c in k])
        val_encoded = round(v * 1.23, 4)
        encoded[key_encoded] = val_encoded
    return encoded

# Distractor: complex frequency response model (never called)
class FrequencyAnalyzer:
    def __init__(self, sample_rate):
        self.rate = sample_rate
        self.filters = {'low': 0.3, 'high': 0.8}

    def compute_dft(self, signal):
        N = len(signal)
        result = [0 + 0j] * N
        for k in range(N):
            for n in range(N):
                angle = -2 * math.pi * k * n / N
                result[k] += signal[n] * (math.cos(angle) + 1j * math.sin(angle))
        return [abs(r) / N for r in result]

# Real processing begins here
signal_strength = [0.87, 0.93, 0.76, 0.88, 0.91]
avg_signal = sum(signal_strength) / len(signal_strength)

# Simulate environmental interference
interference_matrix = [
    [1.0, 0.2, 0.1],
    [0.2, 1.0, 0.3],
    [0.1, 0.3, 1.0]
]
attenuation = 0.0
for row in interference_matrix:
    for val in row:
        attenuation += val * 0.01  # Minor cumulative loss

adjusted_avg = avg_signal - attenuation

# Primary metric dictionary
metrics = {
    'throughput': 94.5,
    'latency': 12.3,
    'jitter': 0.87,
    'packet_loss': 0.04,
    'bandwidth_util': 78.2
}

# Benchmark configuration with red herring parameters
benchmark_config = {
    'thresholds': {
        'min_throughput': 80.0,
        'max_latency': 15.0,
        'critical_jitter': 1.0
    },
    'weights': {
        'throughput': 0.35,
        'latency': 0.25,
        'jitter': 0.20,
        'packet_loss': 0.15,
        'bandwidth_util': 0.05
    },
    'calibration': [0.98, 1.02, 0.99],  # unused
    'version': '2.1a',  # irrelevant
    'debug_mode': False  # decoy flag
}

# Decoy list comprehension with string methods (no effect)
dummy_analysis = [
    k.upper()[::-1].replace('T', 'X') 
    for k in metrics.keys() 
    if 't' in k and k.find('e') > 0
]

# Real scoring logic
weight_map = benchmark_config['weights']
score_components = []

# Throughput score (normalized to 100)
score_components.append((metrics['throughput'] / 100.0) * weight_map['throughput'] * 100)

# Latency score (inverse relationship)
latency_base = max(0, (benchmark_config['thresholds']['max_latency'] - metrics['latency']))
score_components.append((latency_base / benchmark_config['thresholds']['max_latency']) * weight_map['latency'] * 100)

# Jitter score
if metrics['jitter'] < benchmark_config['thresholds']['critical_jitter']:
    jitter_score = (1 - metrics['jitter']) * weight_map['jitter'] * 100
else:
    jitter_score = 0
score_components.append(jitter_score)

# Packet loss penalty
if metrics['packet_loss'] > 0:
    loss_factor = math.exp(-metrics['packet_loss'] * 10)
    packet_score = loss_factor * weight_map['packet_loss'] * 100
    score_components.append(packet_score)

# Bandwidth utilization
util_score = (metrics['bandwidth_util'] / 100.0) * weight_map['bandwidth_util'] * 100
score_components.append(util_score)

# Final aggregation using lambda and dictionary operations
total_weighted = sum(score_components)
weight_sum = sum(weight_map.values())
efficiency_ratio = (adjusted_avg + 0.1) / 1.0  # minor boost from signal

# Apply nonlinear enhancement via sigmoid-like curve
enhancement_factor = 1 + (1 / (1 + math.exp(-efficiency_ratio * 2))) * 0.1

# Critical statement
final_score = evaluate_performance(metrics, benchmark_config)

# Actual implementation of evaluate_performance (defined late to obscure flow)
def evaluate_performance(met, config):
    wc = config['weights']
    raw = 0.0
    raw += (met['throughput'] / 95.0) * wc['throughput'] * 100
    raw += ((15.0 - met['latency']) / 15.0) * wc['latency'] * 100
    raw += ((1.0 - met['jitter']) * wc['jitter'] * 100) if met['jitter'] < 1.0 else 0
    raw += (math.exp(-met['packet_loss'] * 8) * wc['packet_loss'] * 100)
    raw += (met['bandwidth_util'] / 80.0) * wc['bandwidth_util'] * 100
    return raw * (1.0 + (adjusted_avg * 0.05))  # Final adjustment based on signal quality

# Print result as required
Result: {final_score}