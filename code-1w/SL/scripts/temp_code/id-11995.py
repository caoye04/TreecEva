def analyze_signal(data, threshold=0.5):
    filtered = [x for x in data if abs(x) > threshold]
    return sum(filtered) / len(filtered) if filtered else 0.0

signal_data = [0.1, -0.3, 0.7, -1.2, 0.9, 0.0, -0.4]
noise_floor = 0.25

# Distractor: Irrelevant signal processing branch
def process_audio(signal):
    return [s ** 2 for s in signal if s > 0.5]

audio_features = process_audio(signal_data)

# Real computation begins here
baseline = sum([abs(x) for x in signal_data]) / len(signal_data)
adjusted = [x * 1.5 if x > 0 else x * 0.5 for x in signal_data]

# Distractor: Unused transformation chain
decay_weights = [0.9 ** i for i in range(len(signal_data))]
tapered_signal = [adjusted[i] * decay_weights[i] for i in range(len(adjusted))]

# Key metric calculations with red herrings
metrics = {
    'amplitude': abs(analyze_signal(adjusted)),
    'stability': len([x for x in adjusted if -0.6 < x < 0.6]),
    'drift': adjusted[-1] - adjusted[0],
    'complexity': len(adjusted) - len(set(round(x, 1) for x in adjusted))
}

# Distractor: Decoy metrics and unused functions
def calculate_entropy(vals):
    from math import log
    counts = {}
    for v in vals:
        rounded = round(v, 1)
        counts[rounded] = counts.get(rounded, 0) + 1
    total = len(vals)
    return -sum((count/total) * log(count/total) for count in counts.values())

entropy_proxy = calculate_entropy(adjusted)  # Dead end

# Another decoy path
if metrics['drift'] > 0:
    temp_correction = metrics['stability'] * 0.3
    shadow_score = (metrics['amplitude'] + temp_correction) * 1.2  # Not used

weights = {
    'amplitude': 0.4,
    'stability': 0.3,
    'drift': -0.1,  # Negative weight
    'complexity': 0.2
}

# Distractor: Fake normalization block
normalization_factor = sum(abs(w) for w in weights.values())
scaled_metrics = {k: v / (1 + abs(v)) for k, v in metrics.items()}

# Core logic buried in distractions
intermediate_values = []
for key in ['amplitude', 'stability', 'drift', 'complexity']:
    if key in weights and abs(weights[key]) > 0:
        intermediate_values.append(metrics[key] * weights[key])

aggregated = sum(intermediate_values)

# Final scoring with conditional adjustment
penalty = 0
if metrics['complexity'] > 2:
    penalty += 1.5
if metrics['stability'] < 3:
    penalty += 0.8

final_score = aggregated - penalty

# Distractor: Unused alternate scoring
backup_score = sum(scaled_metrics[k] * weights[k] for k in weights) if all(k in scaled_metrics for k in weights) else 0

# Red herring: Additional irrelevant output
auxiliary_result = [x for x in adjusted if x > baseline]

print(f"Result: {final_score}")