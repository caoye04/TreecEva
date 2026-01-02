def analyze_performance(metrics, thresholds):
    alert_count = 0
    normalized = []
    for i, val in enumerate(metrics):
        if val > thresholds[i % len(thresholds)]:
            alert_count += 1
        norm_val = (val - min(metrics)) / (max(metrics) - min(metrics) + 1e-8)
        normalized.append(round(norm_val, 4))
    return normalized, alert_count

metrics = [89, 92, 78, 96, 85, 83]
thresholds = [80, 85, 90]

# Irrelevant transformation
transformed_metrics = [x ** 0.5 * 1.5 for x in metrics]
dummy_pairs = list(zip(transformed_metrics, ['A', 'B', 'C', 'D', 'E', 'F']))

norm_vals, alerts = analyze_performance(metrics, thresholds)

# Simulate ranking with tie-breaking logic
rank_data = []
for idx, score in enumerate(norm_vals):
    rank_data.append((score, -idx, f'Item_{idx+1}'))  # Use negative index for reverse tiebreak

# Sort by score descending, then by reverse index (to favor later items on ties)
rank_data.sort(key=lambda x: (x[0], x[1]), reverse=True)

rankings = [item[2] for item in rank_data]
score_ranks = [i+1 for i, _ in enumerate(rank_data)]

# Weight assignment with distractor logic
base_weights = [10, 8, 6, 4, 3, 2]
dynamic_weights = [w * (1 + 0.1 * alerts) for w in base_weights]

# Introduce irrelevant set operation
unique_letters = set(''.join(rankings))
dropped_items = set(['Item_3', 'Item_5'])
filtered_ranks = [r for r in rankings if r not in dropped_items]

# Unused helper function (dead code path)
def experimental_reweight(ranks, factor=1.1):
    return [f * factor for f in dynamic_weights[:len(ranks)]]

# Core calculation obscured by context
position_bonus = {i+1: 5-i for i in range(6)}  # Bonus decreases with position

# Distractor: complex nested loop that computes unused metric
aggregate_shift = 0
for i, (rank, orig_score) in enumerate(zip(rankings, norm_vals)):
    shift = 0
    for j, entry in enumerate(rank_data):
        if entry[2] == rank:
            shift = abs(i - j)
            break
    aggregate_shift += shift

# Final scoring logic
weights = [dynamic_weights[rank-1] for rank in score_ranks]
raw_scores = []
for i, name in enumerate(rankings):
    pos = i + 1
    base = norm_vals[i] * weights[i]
    bonus = position_bonus[pos] if pos <= 5 else 0
    raw_scores.append(base + bonus)

# Secondary adjustment based on initial metric order (misleading dependency)
index_map = {name: i for i, name in enumerate(rankings)}
correction_factor = 0
for i, orig_name in enumerate([f'Item_{j+1}' for j in range(6)]):
    if orig_name in index_map:
        correction_factor += abs(i - index_map[orig_name])

corrected_scores = [score - 0.2 * correction_factor for score in raw_scores]

final_score = sum(corrected_scores) // 1  # Floor to nearest int

print(f"Result: {final_score}")