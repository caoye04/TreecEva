def analyze_signal(samples, threshold=0.75):
    filtered = [s for s in samples if abs(s) > threshold]
    power = sum(x**2 for x in filtered)
    normalized = [x / (power**0.5 + 1e-9) for x in filtered]
    return normalized


def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * __import__('math').log2(p + 1e-9)
    return round(entropy, 6)

# Irrelevant helper function (dead code path)
def predict_trend(values):
    if len(values) < 3:
        return 0
    trend = all(values[i] <= values[i+1] for i in range(len(values)-1))
    return 1 if trend else -1

# Decoy variables and computations
baseline_offset = 42
reference_map = {i: (i * 17) % 97 for i in range(20)}
symbol_table = ['A', 'B', 'C', 'D', 'E']
lookup_mask = [1, 0, 1, 1, 0]

# Core data structures with distractors
metrics = {
    'throughput': 89.4,
    'latency': 12.7,
    'jitter': 3.2,
    'packet_loss': 0.05,
    'reliability': 0.998,
    'bandwidth_usage': 67.3
}

benchmark_weights = {
    'throughput': 0.25,
    'latency': 0.20,
    'jitter': 0.15,
    'packet_loss': 0.10,
    'reliability': 0.20,
    'bandwidth_usage': 0.10
}

# Misleading intermediate calculation
adjusted_metrics = {}
for k in metrics:
    if k == 'latency':
        adjusted_metrics[k] = 100 - metrics[k]  # Inverted scale
    elif k == 'packet_loss':
        adjusted_metrics[k] = (1 - metrics[k]) * 100
    else:
        adjusted_metrics[k] = metrics[k]

# Simulated signal data (distractor)
signal_samples = [0.1, 0.8, -0.9, 0.2, 0.76, -0.85, 0.3, 0.05]
analyzed_signal = analyze_signal(signal_samples)

# Red herring: entropy computation on sliced symbol data
sliced_symbols = symbol_table[1:4:1]
encoded_sequence = []
for ch in sliced_symbols:
    encoded_sequence.extend([ord(ch)] * 2)
sequence_entropy = compute_entropy(encoded_sequence)

# Real logic begins here — weighted performance evaluation
weight_sum = 0
score_sum = 0

for key in metrics:
    weight = benchmark_weights.get(key, 0)
    if weight > 0:
        raw_value = metrics[key]
        
        # Normalize each metric to a 0-100 scale (except reliability which is already high)
        if key == 'latency':
            normalized_val = max(0, 100 - (raw_value * 2))  # Lower latency = better
        elif key == 'jitter':
            normalized_val = max(0, 100 - (raw_value * 10))
        elif key == 'packet_loss':
            normalized_val = (1 - raw_value) * 100
        elif key == 'reliability':
            normalized_val = raw_value * 100
        else:
            normalized_val = min(100, raw_value)  # Cap at 100
            
        contribution = normalized_val * weight
        score_sum += contribution
        weight_sum += weight

# Final aggregation
if weight_sum > 0:
    preliminary_score = score_sum / weight_sum
else:
    preliminary_score = 0

# Secondary adjustment based on entropy (unused red herring)
adjustment_factor = sequence_entropy / 10.0 if sequence_entropy > 0 else 0.0

# Final performance score — this is the actual answer
final_score = round(preliminary_score + baseline_offset * 0.0, 3)  # No real adjustment

# Output target result
print(f"Result: {final_score}")