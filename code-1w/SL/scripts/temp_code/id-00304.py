def analyze_productivity(log_data, base_efficiency):
    # Irrelevant helper: computes average line length (not used in final result)
    avg_line_length = sum(len(line) for line in log_data) / len(log_data) if log_data else 0

    # Distractor: counts occurrences of 'INFO', has no impact on output
    info_count = sum(1 for line in log_data if 'INFO' in line)

    # Real computation: extract numeric efficiency boosts
    efficiency_logs = [int(line.split()[-1]) for line in log_data if line.strip().isdigit()]
    boost_factor = sum(efficiency_logs) * 0.1 if efficiency_logs else base_efficiency

    return boost_factor


def validate_integrity(checksums, threshold=500):
    # Dead code path: never called
    total = sum(c ** 2 for c in checksums)
    return total < threshold

# Simulated system logs (mixed content)
logs = [
    'DEBUG: module load complete',
    'INFO: user session started',
    '87',
    'WARNING: low memory',
    '92',
    'INFO: data flushed',
    '88',
    'ERROR: timeout',
    '94',
    '93'
]

# Target metrics and feedback (some are distractions)
target_metrics = {
    'latency': 45,
    'throughput': 820,
    'error_rate': 0.03,
    'retry_count': 2
}

feedback_ratings = [4.2, 4.5, 3.8, 4.6, 4.1]  # User satisfaction scores

# Misleading accumulation: looks important but unused
aggregate_rating = sum(r * 10 for r in feedback_ratings) / len(feedback_ratings)

# Bitwise obfuscation: irrelevant transformation
obfuscated_key = 0
for rt in feedback_ratings:
    obfuscated_key ^= int(rt * 10)

# Secondary distractor: set operation with no downstream use
unique_scores = set(int(rt * 10) for rt in feedback_ratings)

# Core logic disguised among noise
efficiency_base = 75
growth_potential = analyze_productivity(logs, efficiency_base)

# Multiple assignment - one useful, others distracting
scaling_factor, _padding, _offset = growth_potential / 10, 0.0, 0.0

# Actual key computation chain
weighted_latency = target_metrics['latency'] * 0.3
normalized_throughput = target_metrics['throughput'] / 1000.0
adjusted_satisfaction = sum(feedback_ratings) / len(feedback_ratings) * 0.7

# Final performance score built from multiple sources
performance_component = normalized_throughput * 100 + adjusted_satisfaction * 10

# Critical statement
final_score = evaluate_performance(feedback_ratings, target_metrics)

# Helper function defined late to obscure relevance
def evaluate_performance(ratings, metrics):
    base = sum(ratings) / len(ratings)
    throughput_bonus = 10 if metrics['throughput'] > 800 else 5
    error_penalty = 8 if metrics['error_rate'] > 0.02 else 0
    
    # Use list comprehension to filter high ratings
    high_performers = [r for r in ratings if r >= 4.0]
    bonus_per_high = len(high_performers) * 2
    
    # Accumulate final score
    score = base * 10
    score += throughput_bonus
    score -= error_penalty
    score += bonus_per_high
    
    return int(score)

# Print result as required
print(f"Result: {final_score}")