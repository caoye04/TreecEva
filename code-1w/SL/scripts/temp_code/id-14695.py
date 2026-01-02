def analyze_performance(metrics, thresholds):
    above_threshold = []
    for i, val in enumerate(metrics):
        if val > thresholds[i % len(thresholds)]:
            above_threshold.append((i, val))
    return above_threshold

metrics = [85, 90, 76, 88, 92, 73, 81]
thresholds = [80, 85, 70]

# Misleading computation - not used in final result
distorted_metrics = [m * 1.05 for m in metrics]
adjusted = list(zip(distorted_metrics, [t * 0.95 for t in thresholds]))

# Simulate ranking with auxiliary scoring
raw_ranks = []
for idx, score in enumerate(metrics):
    rank_val = (score - 70) * (idx + 1)
    raw_ranks.append(rank_val)

# Secondary distraction: sorting irrelevant data
decorated_pairs = sorted(enumerate(raw_ranks), key=lambda x: x[1], reverse=True)
rank_positions = {item[0]: pos for pos, item in enumerate(decorated_pairs)}

# Weight assignment with modular arithmetic
weights = []
for i in range(len(metrics)):
    base_weight = (i * i + 3) % 7 + 1
    adjusted_weight = base_weight * 0.8 if i % 2 == 0 else base_weight * 1.1
    weights.append(round(adjusted_weight, 2))

# Actual computation path
rankings = [item[1] for item in decorated_pairs]  # Extract ordered scores

# Red herring function call (no side effects)
def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

variance_proxy = compute_variance([w * 100 for w in weights])  # Unused beyond this point

# Core logic buried among distractions
def calculate_final_score(ranks, w):
    cumulative = 0
    for i, r in enumerate(ranks):
        modifier = 1.2 if i % 3 == 0 else 0.9
        weighted_contribution = r * w[i] * modifier
        if weighted_contribution > 200:  # Threshold filter
            cumulative += int(weighted_contribution // 10)
    return cumulative + (len(ranks) % 5)

final_score = calculate_final_score(rankings, weights)
print(f"Result: {final_score}")