def analyze_performance(logs):
    # Irrelevant helper: counts debug entries (distractor)
    debug_count = sum(1 for entry in logs if 'DEBUG' in entry)
    warning_count = sum(1 for entry in logs if 'WARN' in entry)
    return warning_count

# Simulated system performance data
timestamps = [1623456000, 1623456060, 1623456120, 1623456180]
errors = ['None', 'Timeout', 'None', 'Crash']
performance_logs = [
    'INFO: System online',
    'WARN: High latency detected',
    'DEBUG: Memory usage at 62%',
    'WARN: Retrying connection',
    'INFO: Recovery initiated'
]

# Rankings from three evaluation modules
module_a_ranking = [85, 90, 78, 92]
module_b_ranking = [88, 87, 80, 90]
module_c_ranking = [84, 91, 76, 93]

rankings = list(zip(module_a_ranking, module_b_ranking, module_c_ranking))

# Auxiliary computation: average per module (semi-relevant)
avg_a = sum(module_a_ranking) / len(module_a_ranking)
avg_b = sum(module_b_ranking) / len(module_b_ranking)
avg_c = sum(module_c_ranking) / len(module_c_ranking)

# Misleading normalization (not actually used in final score)
normalized_ranks = []
for rank_tuple in rankings:
    normalized = tuple(r * 0.95 for r in rank_tuple)
    normalized_ranks.append(normalized)

# Core logic disguised among distractions
effective_warnings = analyze_performance(performance_logs)
penalty_factor = 0 if effective_warnings < 2 else 0.1

# Primary aggregation: weighted consensus score
total_consensus = 0
consensus_weights = [0.4, 0.35, 0.25]  # Decreasing priority

for i, (a, b, c) in enumerate(rankings):
    sorted_ranks = sorted([a, b, c])
    # Use median as robust estimator
    median_rank = sorted_ranks[1]
    weight = consensus_weights[i % len(consensus_weights)]
    total_consensus += median_rank * weight

# Secondary adjustment based on trend
rank_deltas = [module_a_ranking[i+1] - module_a_ranking[i] for i in range(len(module_a_ranking)-1)]
improvement_trend = sum(1 for d in rank_deltas if d > 0)
trend_bonus = 2 if improvement_trend >= 2 else 0

# Final calculation obscured by context
baseline_score = total_consensus + trend_bonus
final_score = int(baseline_score - (baseline_score * penalty_factor))

# Print result as required
print(f"Result: {final_score}")