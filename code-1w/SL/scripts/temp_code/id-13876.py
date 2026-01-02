from collections import defaultdict

# Simulate athlete performance analysis with noise and filtering
def analyze_athlete_data(raw_scores, bonus_eligible):
    score_count = defaultdict(int)
    total_points = 0
    penalty_adjustment = 0

    for score in raw_scores:
        score_count[score] += 1
        if score < 60:
            penalty_adjustment -= 5
        elif score > 90:
            total_points += score * 0.1

    # Irrelevant aggregation (distractor)
    average_frequency = sum(score_count.values()) / len(score_count) if score_count else 0

    base_performance = sum(raw_scores) + penalty_adjustment + total_points
    return base_performance, average_frequency

# Process team rankings and flag anomalies
def process_rankings(team_ranks):
    rank_shift = 0
    volatility_index = 0
    historical_trend = []

    for i in range(1, len(team_ranks)):
        change = team_ranks[i] - team_ranks[i-1]
        rank_shift += abs(change)
        volatility_index += change ** 2
        historical_trend.append(change)

    # Dead computation: not used later (distractor)
    smoothed_trend = [historical_trend[i] for i in range(len(historical_trend)) if i % 2 == 0]

    consistency_bonus = 10 if rank_shift < 15 else 0
    return volatility_index, consistency_bonus

# Main scoring logic
def calculate_final_score(ranks, flags):
    base, _ = analyze_athlete_data([85, 92, 78, 92, 88], flags)
    index, bonus = process_rankings(ranks)

    # Key intermediate variables with some irrelevant ones
    adjustment_factor = 1.0
    if flags['streak'] and ranks[0] < 5:
        adjustment_factor *= 1.1

    # Multiple assignments (relevant and misleading)
    temp_debug_1, temp_debug_2 = 0, 0
    debug_sum = sum([temp_debug_1, temp_debug_2])  # Unused

    # Core calculation
    raw_score = base + bonus
    scaled_score = raw_score * adjustment_factor

    # Noise injection (some doesn't affect outcome)
    outlier_buffer = 0
    for _ in range(3):
        outlier_buffer += 7  # Accumulates but unused

    final_score = int(scaled_score)  # This is the actual answer
    return final_score

# Input data
rankings = [3, 5, 4, 6, 7]
performance_flags = {
    'streak': True,
    'injury_free': False,
    'bonus_lock': False
}

# Execution point of interest
final_score = calculate_final_score(rankings, performance_flags)
print(f"Result: {final_score}")