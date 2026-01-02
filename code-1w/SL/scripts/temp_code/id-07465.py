def evaluate_performance(entries, importance_factors):
    # Preprocessing: extract top performers based on weighted ranking
    sorted_entries = sorted(entries, key=lambda x: sum(a * b for a, b in zip(x[1:], importance_factors)), reverse=True)

    # Secondary metric: calculate spread of top 3 scores (distractor computation)
    top_3_scores = [sum(a * b for a, b in zip(e[1:], importance_factors)) for e in sorted_entries[:3]]
    score_variance = sum((s - sum(top_3_scores)/3) ** 2 for s in top_3_scores)  # unused distraction

    # Determine performance decay across quartiles
    chunk_size = max(1, len(sorted_entries) // 4)
    quartile_peaks = []
    for i in range(4):
        start = i * chunk_size
        end = start + chunk_size if i < 3 else len(sorted_entries)
        if start < len(sorted_entries):
            segment = sorted_entries[start:end]
            peak = max(sum(a * b for a, b in zip(e[1:], importance_factors)) for e in segment)
            quartile_peaks.append(peak)

    # Decay analysis - how much does performance drop?
    decay_trend = [quartile_peaks[i] - quartile_peaks[i+1] for i in range(3)]
    avg_decay = sum(decay_trend) / len(decay_trend)

    # Core logic: compute final score using only first and last quartile peak
    stability_bonus = 1 if quartile_peaks[0] - quartile_peaks[-1] < 15 else 0
    base_score = int(quartile_peaks[0] * 2 - quartile_peaks[-1] + avg_decay)

    # Apply bonus and clamp
    final_result = base_score + stability_bonus

    # Irrelevant tracking variables (distraction)
    entry_count_log = {i: len([e for e in entries if e[0][0] == chr(65+i)]) for i in range(5)}  # counts by group A-E
    outlier_flags = [abs(e[1] - e[2]) > 10 for e in entries]  # not used

    return final_result

# Input data: (team_id, metric1, metric2, metric3, metric4)
data_pool = [
    ('A1', 8, 12, 9, 14),
    ('B2', 7, 10, 13, 11),
    ('C3', 9, 14, 8, 10),
    ('D4', 6, 11, 12, 13),
    ('E5', 10, 9, 11, 12),
    ('F6', 8, 13, 10, 9),
    ('G7', 7, 12, 14, 8),
    ('H8', 9, 10, 11, 11)
]

# Weights for evaluation criteria
weights = [0.25, 0.30, 0.20, 0.25]

# Misleading preprocessing (semi-relevant but not critical)
normalized_data = [[round(val * 0.1, 2) for val in row[1:]] for row in data_pool]  # scaled down
summary_stats = {
    'max_metric': max(max(row[1:]) for row in data_pool),
    'min_metric': min(min(row[1:]) for row in data_pool)
}

# Key execution point
final_score = evaluate_performance(data_pool, weights)
print(f"Result: {final_score}")