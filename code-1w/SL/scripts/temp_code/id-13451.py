def analyze_contributions(values, thresholds):
    contributions = []
    for i, val in enumerate(values):
        if val > thresholds[i % len(thresholds)]:
            contributions.append((i, val ** 0.5))
        else:
            contributions.append((i, val / 2))
    return contributions


def filter_anomalies(records):
    seen = set()
    filtered = []
    for r in records:
        if r[0] not in seen:
            seen.add(r[0])
            if r[1] > 0:
                filtered.append(r)
    return filtered


def compute_entropy(data):
    from math import log2
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 6)


def transform_sequence(seq, keymap):
    mapped = [keymap[x % 5] for x in seq]
    shifted = [m << 1 if i % 2 == 0 else m >> 1 for i, m in enumerate(mapped)]
    return [s ^ 3 for s in shifted]


def calculate_baseline(reference):
    base = 0
    for r in reference:
        base += r * 2 if r % 2 == 0 else r * 3
    return base // len(reference)


def integrate_feedback(scores, feedback_flags):
    adjusted = []
    for score, flag in zip(scores, feedback_flags):
        if flag == 'critical':
            adjusted.append(score * 1.5)
        elif flag == 'minor':
            adjusted.append(score * 0.9)
        else:
            adjusted.append(score)
    return [round(a, 2) for a in adjusted]


def evaluate_performance(weights, outcomes):
    weighted_sum = 0
    for w, o in zip(weights, outcomes):
        weighted_sum += w * (o if o < 50 else 50)
    penalty = 0
    for o in outcomes:
        if o > 75:
            penalty += o // 10
    return int(weighted_sum - penalty)

# Irrelevant initialization block (distractor)
initial_metrics = [88, 72, 91, 65, 83]
dummy_thresholds = [70, 75, 80]
raw_contributions = analyze_contributions(initial_metrics, dummy_thresholds)
entropy_value = compute_entropy([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

# Unused data structures (red herring)
signal_chain = [1, 3, 2, 4, 0]
key_mapping = {0: 5, 1: 3, 2: 7, 3: 2, 4: 8}
transformed = transform_sequence(signal_chain, key_mapping)
baseline_ref = [10, 20, 30, 40]
baseline_calc = calculate_baseline(baseline_ref)

# Real input data
metric_weights = [0.2, 0.3, 0.1, 0.25, 0.15]
raw_outcomes = [85, 92, 45, 78, 67]
feedback_types = ['minor', 'critical', 'none', 'none', 'minor']

# Process relevant data
adjusted_outcomes = integrate_feedback(raw_outcomes, feedback_types)

# Core evaluation (key statement)
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Print result
print(f"Target result: {final_score}")