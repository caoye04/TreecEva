from collections import defaultdict, Counter

# Simulated health monitoring system with sensor data processing
def analyze_risk_level(value, baseline, risk_map):
    if value < baseline * 0.8:
        return 'LOW'
    elif value > baseline * 1.2:
        return 'HIGH'
    else:
        return 'NORMAL'


def apply_correction(signal, factor=1.0):
    # Irrelevant correction function (dead path)
    return [s * factor for s in signal]

# Unused helper that looks important
def compute_fourier_components(signal):
    total = 0
    for i in range(len(signal)):
        total += signal[i] * (i % 3)
    return total

# Main diagnostic engine
def extract_features(records):
    features = defaultdict(float)
    magnitude = 0
    temp_snapshot = []

    for idx, (ts, val) in enumerate(records):
        if idx % 3 == 0:
            magnitude += val ** 0.5
        if val > 50:
            temp_snapshot.append(val)

    # Distractor computation
    snapshot_stats = Counter(temp_snapshot)
    avg_high = sum(temp_snapshot) / (len(temp_snapshot) or 1)

    features['magnitude'] = magnitude
    features['high_count'] = len(temp_snapshot)

    # Real feature used later
    features['snapshot_avg'] = avg_high if temp_snapshot else 0

    return features


def evaluate_stability(metrics, history):
    score = 0
    for k, v in metrics.items():
        if k == 'magnitude':
            score += v * 0.3
        elif k == 'snapshot_avg':
            score += v * 0.7  # This will be key
    return score > 45


def aggregate_metrics(data_stream, config):
    results = []
    decoy_buffer = []

    for i, record_set in enumerate(data_stream):
        # Process each batch
        processed = extract_features(record_set)
        stable = evaluate_stability(processed, None)

        # Real logic: track only even-indexed stable results
        if i % 2 == 0 and stable:
            results.append(processed['snapshot_avg'])

        # Dead-end buffer (never used)
        decoy_buffer.append(len(decoy_buffer) + i)

    # Critical aggregation
    final_score = 0
    for j, val in enumerate(results):
        if j % 2 == 0:
            final_score += val * (j + 1)
        else:
            final_score -= val * 0.5

    # Secondary transformation
    normalized = final_score / (len(results) or 1)

    # Final thresholding
    if normalized > 30:
        return int(normalized * 1.5)
    elif normalized > 20:
        return int(normalized * 1.2)
    else:
        return int(normalized)

# Simulated input data: (timestamp, heart_rate_like_signal)
base_data = [
    [(1, 45), (2, 52), (3, 60), (4, 47), (5, 68)],
    [(6, 55), (7, 51), (8, 70), (9, 53), (10, 75)],
    [(11, 48), (12, 62), (13, 58), (14, 49), (15, 65)],
    [(16, 50), (17, 54), (18, 63), (19, 56), (20, 72)]
]

# Threshold configuration (looks important but partially unused)
alert_thresholds = {
    'critical': 70,
    'warning': 55,
    'baseline': 50
}

# Unused data structure that mimics real usage
auxiliary_logs = defaultdict(list)
for t, entries in enumerate(base_data):
    for entry in entries:
        auxiliary_logs[t].append(entry[0])

# Key execution point
intermediate_diagnostics = [extract_features(block) for block in base_data]
system_verdict = any(evaluate_stability(d, None) for d in intermediate_diagnostics)

# Final computation — this is where the answer comes from
final_diagnostic = aggregate_metrics(base_data, alert_thresholds)

# Execution output
print(f"Result: {final_diagnostic}")