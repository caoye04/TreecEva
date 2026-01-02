from collections import defaultdict
import itertools

# Simulate sensor data processing with noise filtering and performance scoring
def collect_diagnostics(raw_readings):
    diagnostics = defaultdict(int)
    temp_buffer = []
    anomaly_count = 0  # irrelevant counter for distraction

    for val in raw_readings:
        if val < 0:
            diagnostics['negative'] += 1
        elif val > 100:
            diagnostics['overload'] += 1
            anomaly_count += 1  # red herring
        else:
            temp_buffer.append(val)

    filtered = [x for x in temp_buffer if x % 2 == 1]  # keep only odd values
    diagnostics['valid_odds'] = len(filtered)
    return dict(diagnostics)


def compute_envelope(signal):
    envelope = 0
    phase_shift = 0.0
    for i, s in enumerate(signal):
        envelope += (s ** 2) * (i % 3 + 1)
        if i % 5 == 0:
            phase_shift += s / (i + 1)
    return envelope  # decoy function, not used in final logic


def generate_baseline_profile(shape):
    profile = []
    for i in range(len(shape)):
        profile.append((shape[i] + i) ** 0.5)
    return profile  # unused, misleading


def extract_features(data_stream):
    feature_map = {}
    segment = data_stream[::2]  # every other element

    running_total = 0
    for idx, item in enumerate(segment):
        if idx == 0:
            continue
        diff = abs(item - segment[idx-1])
        running_total += diff

    feature_map['drift'] = running_total
    feature_map['length'] = len(segment)

    # Irrelevant transformation chain
    transformed = list(map(lambda x: (x * 2) % 7, segment))
    paired = list(itertools.combinations(transformed, 2))
    feature_map['complexity'] = len(paired) if len(paired) > 10 else 0

    return feature_map


def evaluate_performance(metrics, base):
    score = 0
    penalty = 0

    if 'valid_odds' in metrics:
        score += metrics['valid_odds'] * 17

    if 'drift' in metrics:
        score += int(metrics['drift'])

    if metrics.get('complexity', 0) > 5:
        score += 50

    # Deliberately misleading branches
    if base.get('peak', 0) > 50:
        penalty += 100

    # Actual logic: only valid_odds and drift contribute
    return score - penalty

# Main execution flow
raw_input = [12, -5, 103, 45, 68, 89, 107, 33, 72, 91, 54, 21]

# Step 1: Collect diagnostics
diag_results = collect_diagnostics(raw_input)

# Step 2: Extract additional features
feature_set = extract_features(raw_input)

# Step 3: Merge relevant metrics
metrics = {}
metrics.update(diag_results)
metrics.update(feature_set)

# Baseline (irrelevant fields included as distractors)
baseline = {
    'peak': 120,
    'window': 5,
    'threshold': 0.8
}

# Critical statement
final_score = evaluate_performance(metrics, baseline)

print(f"Result: {final_score}")