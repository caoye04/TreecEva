import math

# Simulated sensor array processing with diagnostic flags
def analyze_signal_strength(signal):
    if not signal:
        return 0
    magnitude = sum([x ** 2 for x in signal]) ** 0.5
    normalized = magnitude / (len(signal) or 1)
    return round(normalized, 3)


def detect_anomalies(readings):
    anomalies = []
    baseline = sum(readings) / len(readings)
    threshold = baseline * 1.5
    for i, val in enumerate(readings):
        if val > threshold:
            anomalies.append(i)
    return anomalies if anomalies else [-1]

# Irrelevant helper - distractor function
def encrypt_data(data):
    return ''.join(chr((ord(c) + 3) % 90) for c in data)  # Caesar-like cipher, unused

# Unused transformation chain
def transform_sequence(seq):
    return [seq[i] + seq[i-1] if i > 0 else seq[0] for i in range(len(seq))]

# Decoy statistical function
def compute_entropy(values):
    total = sum(values)
    probs = [(v / total) for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs if p > 0)

# Core processing pipeline
sensor_inputs = [
    [12, 15, 14, 18, 13],
    [8, 10, 7, 11, 9],
    [25, 22, 27, 24, 26],
    [5, 6, 4, 7, 5]
]

# Dead code path: precomputed but unused
redundant_analysis = [
    analyze_signal_strength(chain) * 1.2 for chain in sensor_inputs
]

# Conditional expression and lambda usage
process_mode = 'deep' if sum(len(x) for x in sensor_inputs) > 15 else 'fast'
scoring_rule = lambda x: x ** 2 if process_mode == 'deep' else x * 1.5

# Real processing begins here
filtered_chains = []
for idx, chain in enumerate(sensor_inputs):
    strength = analyze_signal_strength(chain)
    
    # Early break red herring
    if strength < 5.0:
        continue  # This won't trigger
        break    # Dead code - unreachable
    
    anomalies = detect_anomalies(chain)
    if anomalies != [-1]:
        # Apply correction
        for a_idx in anomalies:
            if a_idx < len(chain):
                chain[a_idx] *= 0.9
    
    corrected_strength = analyze_signal_strength(chain)
    score = scoring_rule(corrected_strength)
    filtered_chains.append({'id': idx, 'score': score, 'chain': chain})

# Slicing operation with distraction
recent_scores = [entry['score'] for entry in filtered_chains[-3:]]  # uses last 3
legacy_snapshot = sensor_inputs[1:3]  # irrelevant slice

# Aggregation logic with min/max/avg
max_score = max(recent_scores)
decay_factor = 0.95 ** (len(filtered_chains) - 1)
temp_bias = sum(1 for s in recent_scores if s > 15) * 0.3  # counting heuristic

# Distractor variables
phantom_threshold = 999.9
shadow_buffer = [0] * len(sensor_inputs)  # unused tracking
sync_offset = math.sin(math.pi / 4)  # meaningless computation

# Key execution point
baseline_avg = sum(recent_scores) / len(recent_scores)
adjusted_peak = max_score * decay_factor + temp_bias

# Composite metric calculation
intermediate_metric = (baseline_avg * 0.6) + (adjusted_peak * 0.4)

# Final diagnostic computed from relevant state
final_diagnostic = round(intermediate_metric, 4)

# Print required output
print(f"Result: {final_diagnostic}")