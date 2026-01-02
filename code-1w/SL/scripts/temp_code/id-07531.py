def analyze_performance(metrics):
    # Irrelevant transformation
    adjusted = [x * 1.05 for x in metrics if x > 80]
    offset = sum(adjusted) / len(adjusted) if adjusted else 0

    # Distractor computation
    peak = max(metrics) if metrics else 0
    trough = min(metrics) if metrics else 0
    volatility = (peak - trough) / peak if peak != 0 else 0

    # Semi-relevant normalization
    normalized = [(x - 70) / 30 for x in metrics]
    return normalized


def compute_trend(data):
    trend_values = []
    for i, val in enumerate(data):
        if i == 0:
            trend_values.append(0)
        else:
            diff = data[i] - data[i-1]
            trend_values.append(1 if diff >= 0 else -1)
    
    # Misleading smoothing (not used later)
    smoothed = [sum(trend_values[max(0, i-2):i+1]) / (i+1) for i in range(len(trend_values))]
    
    return trend_values


def calculate_rankings(scores):
    sorted_pairs = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    rankings = [0] * len(scores)
    for rank, (idx, _) in enumerate(sorted_pairs):
        rankings[idx] = rank + 1
    return rankings


def calculate_final_score(ranks, trends):
    weighted_sum = 0
    for i, (rank, trend) in enumerate(zip(ranks, trends)):
        if trend == 1:  # Positive trend
            contribution = (10 - rank) * 1.2
        else:
            contribution = (10 - rank) * 0.8
        weighted_sum += contribution
    
    # Extra processing that doesn't affect outcome
    ceiling_check = min(weighted_sum, 100)
    floor_check = max(ceiling_check, 0)
    bonus_adjustment = 0
    for _ in range(3):
        bonus_adjustment += 0.1  # Dead-end distraction
    
    # Final score determined here
    final_score = round(weighted_sum, 2)
    return final_score

# Main execution
performance_metrics = [85, 92, 78, 88, 95, 83, 90, 87]

# Step 1: Normalize metrics (some irrelevant steps inside)
normalized_metrics = analyze_performance(performance_metrics)

# Step 2: Compute trend from original metrics (important)
trend_analysis = compute_trend(performance_metrics)

# Step 3: Rank based on raw metrics
rankings = calculate_rankings(performance_metrics)

# Step 4: Calculate final score using rankings and trend
definitive_trend = trend_analysis  # Rename for clarity
final_score = calculate_final_score(rankings, definitive_trend)

print(f"Result: {final_score}")