def analyze_component(signal, threshold=0.5):
    """Irrelevant helper function for signal analysis (dead code path)."""
    return [x for x in signal if abs(x) > threshold]


def preprocess_data(raw):
    """Unrelated data preprocessing (distractor)."""
    return sorted([x % 100 for x in raw], reverse=True)[:10]

# Simulated sensor metrics (some relevant, some misleading)
sensor_metrics = [0.82, 0.45, 0.91, 0.67, 0.33, 0.76, 0.54, 0.29]

# Irrelevant transformations
decoy_signal = [((x * 3) + 7) % 1 for x in range(8)]
processed_decoy = preprocess_data([int(x*1000) for x in decoy_signal])

# Actual weights for evaluation (only these matter)
weights = [0.2, 0.3, 0.1, 0.25, 0.15]  # Sum = 1.0

# Misleading alternate weight sets (red herrings)
alt_weights_v1 = [0.1, 0.1, 0.1, 0.1, 0.6]
alt_weights_v2 = [0.5, 0.5, 0, 0, 0]

# Core metric components (key data)
latency_ms = 45
throughput_ops = 1200
error_rate = 0.02
consistency_score = 0.88
recovery_time = 3.4

# Distractor calculations
fake_metric_1 = (latency_ms * 0.7) + (error_rate * 100)
fake_metric_2 = throughput_ops / (recovery_time * 10)

# Real metric normalization (critical path)
normalized_metrics = [
    max(0, min(1, (50 - latency_ms) / 50)),           # lower latency → higher score
    max(0, min(1, throughput_ops / 2000)),            # capped at 2000 ops
    max(0, min(1, 1 - error_rate * 5)),               # error penalty
    consistency_score,
    max(0, min(1, (5 - recovery_time) / 5))           # faster recovery → better
]

# Bitwise interference (seemingly complex but irrelevant)
config_flag = 0b1011
mask = 0b1101
obfuscated = (config_flag ^ mask) & 0b1111

# Decoy scoring using slicing (looks important but unused)
slice_backup = normalized_metrics[::2]
temp_scores = [x * 0.5 for x in slice_backup]

# Another red herring: sorting decoy
sorted_distract = sorted(temp_scores, key=lambda x: -x)

# Key function that computes the actual result
def evaluate_performance(metrics, w):
    """Compute weighted performance score."""
    base = sum(m * w[i] for i, m in enumerate(metrics[:len(w)]))
    bonus = 0.05 if metrics[0] > 0.8 and metrics[1] > 0.6 else 0
    penalty = 0.1 if metrics[2] < 0.5 or metrics[4] < 0.6 else 0
    return round(base + bonus - penalty, 6)

# Critical execution point
final_score = evaluate_performance(normalized_metrics, weights)

# Print required output
print(f"Result: {final_score}")