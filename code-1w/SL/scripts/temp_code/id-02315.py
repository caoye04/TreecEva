from collections import defaultdict, Counter

# Simulated sensor fusion system for autonomous drone navigation
sensor_readings = [
    [1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 1]
]

# Irrelevant signal processing chain (red herring)
def process_signal(data):
    fft_result = []
    for d in data:
        acc = 0
        for i, x in enumerate(d):
            acc += x * (2 ** i)  # Simulate weighted frequency bin
        fft_result.append(acc % 100)
    return fft_result

signal_fragments = process_signal(sensor_readings)
filtered_signals = [x * 0.9 for x in signal_fragments if x > 5]  # Unused path
decoy_matrix = [[i*j for j in range(4)] for i in range(4)]  # Dead computation

# Core diagnostic logic with distractors
diagnostic_logs = {
    'status_codes': [200, 201, 404, 500, 200, 200, 403],
    'retry_attempts': [0, 1, 0, 2, 1, 0, 0],
    'latency_ms': [120, 250, 80, 400, 110, 95, 300]
}

temp_bias = 0.75
offset_table = {i: (i**2 % 7) * temp_bias for i in range(len(diagnostic_logs['status_codes']))}  # Distractor map

# Real metric computation buried in noise
def compute_reliability_index(logs):
    codes = logs['status_codes']
    retries = logs['retry_attempts']
    latency = logs['latency_ms']
    
    # Meaningless transformation (distractor)
    synthetic_load = sum([r * (l // 100 + 1) for r, l in zip(retries, latency)])
    
    # Actual relevant logic
    success_count = sum(1 for c in codes if c == 200)
    timeout_count = sum(1 for c in codes if c == 408 or c == 504)  # Misleading condition (never true)
    avg_retry = sum(retries) / len(retries) if retries else 0
    stable_latency = sum(1 for lt in latency if lt < 200)
    
    base_score = success_count * 10
    penalty = (avg_retry * 5) + (len(latency) - stable_latency) * 3
    return base_score - penalty

reliability_index = compute_reliability_index(diagnostic_logs)

# Decoy scoring function that looks important but is unused
def calculate_integrity_score(readings):
    flat = [bit for row in readings for bit in row]
    bit_counter = Counter(flat)
    parity_match = 1 if bit_counter[1] % 2 == bit_counter[0] % 2 else 0
    return (bit_counter[1] * 0.5) + parity_match

# Another decoy: complex but irrelevant structure
class DiagnosticBuffer:
    def __init__(self, size):
        self.data = defaultdict(list)
        self.size = size
    
    def append(self, key, val):
        if len(self.data[key]) >= self.size:
            self.data[key].pop(0)
        self.data[key].append(val)

    def get_stats(self):
        counts = {k: len(v) for k, v in self.data.items()}
        return Counter(counts)

buffer = DiagnosticBuffer(3)
for i, code in enumerate(diagnostic_logs['status_codes']):
    buffer.append('codes', code)
    buffer.append('analysis', offset_table[i])  # Feeding decoy data

# Real weight system obscured by noise
metric_weights = defaultdict(float)
metric_weights['reliability'] = 0.6
metric_weights['throughput'] = 0.2  # Unused in final calculation
metric_weights['consistency'] = 0.2

raw_outcomes = {}
raw_outcomes['reliability'] = reliability_index
raw_outcomes['throughput'] = sum(diagnostic_logs['latency_ms']) / 1000  # Distractor
raw_outcomes['consistency'] = len([x for x in diagnostic_logs['retry_attempts'] if x <= 1])

# Key computation with conditional expression and distraction
normalization_factor = 5.0 if any(x > 250 for x in diagnostic_logs['latency_ms']) else 3.0
fake_aggregation = [a*b for a, b in zip(diagnostic_logs['retry_attempts'], diagnostic_logs['latency_ms']) if a > 0]
side_metric = sum(fake_aggregation) / normalization_factor if fake_aggregation else 0  # Looks important

# Critical statement buried in logic
final_score = 0
def evaluate_performance(weights, outcomes):
    global side_metric
    temp_result = 0
    
    # Heavily nested relevance filter (3 levels deep)
    for key, weight in weights.items():
        if key in outcomes:
            if weight > 0:
                scaled_val = float(outcomes[key])
                if key == 'reliability':
                    temp_result += scaled_val * weight * 2  # Double-weighted reliability
                elif key == 'consistency':
                    adjustment = 0
                    for attempt in diagnostic_logs['retry_attempts']:
                        if attempt == 0:
                            adjustment += 0.5
                    temp_result += (scaled_val + adjustment) * weight
                # throughput ignored even though present
    
    # Final nonlinear adjustment using conditional expression
    bonus = 10 if temp_result > 40 else (5 if temp_result > 25 else 0)
    final_normalized = temp_result + bonus
    
    # Apply interference from side_metric (but it's not actually used)
    decoy_influence = side_metric * 0.1
    final_normalized = round(final_normalized - decoy_influence + 0.05, 2)  # Neutralized
    
    return int(final_normalized)

final_score = evaluate_performance(metric_weights, raw_outcomes)
print(f"Result: {final_score}")