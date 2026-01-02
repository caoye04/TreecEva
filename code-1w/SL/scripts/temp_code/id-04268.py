from itertools import combinations
from math import log

# Simulate user engagement metrics across different content types
def analyze_engagement_metrics(raw_views, raw_clicks, time_segments):
    normalized_views = [v / max(raw_views) for v in raw_views]
    normalized_clicks = [c / max(raw_clicks) for c in raw_clicks]
    
    # Misleading transformation: entropy-like computation with no real impact
    fake_entropy = 0.0
    for nv in normalized_views:
        if nv > 0:
            fake_entropy -= nv * log(nv)
    
    relevance_scores = []
    for i in range(len(time_segments)):
        score = (normalized_views[i] * 0.6) + (normalized_clicks[i] * 0.4)
        relevance_scores.append(round(score, 3))
    
    return relevance_scores

# Filter high-engagement segments based on dynamic threshold
def filter_high_impact_segments(scores, threshold_modifier=0.1):
    base_threshold = sum(scores) / len(scores)
    dynamic_threshold = base_threshold * (1 + threshold_modifier)
    
    high_impact = [s for s in scores if s >= dynamic_threshold]
    low_impact = [s for s in scores if s < dynamic_threshold]
    
    # Distractor: unused statistical moment calculations
    variance_proxy = sum((s - base_threshold) ** 2 for s in scores) / len(scores)
    skew_proxy = sum((s - base_threshold) ** 3 for s in scores) / (len(scores) * (variance_proxy ** 1.5)) if variance_proxy > 0 else 0
    
    return high_impact

# Detect optimal segment pairs using combinatorial analysis
def detect_optimal_pairs(impact_list):
    if len(impact_list) < 2:
        return [(impact_list[0], impact_list[0])] if impact_list else []
    
    candidate_pairs = list(combinations(impact_list, 2))
    best_pair = None
    highest_sum = -1
    
    for pair in candidate_pairs:
        pair_sum = sum(pair)
        if pair_sum > highest_sum:
            highest_sum = pair_sum
            best_pair = pair
    
    return [best_pair] if best_pair else []

# Final scoring with weighted contribution from optimal pairs
def calculate_final_score(optimal_pairs):
    total_contribution = 0
    for p in optimal_pairs:
        # Emphasis on synergy: product term added to sum
        synergy_bonus = p[0] * p[1]
        additive_term = sum(p)
        total_contribution += additive_term + synergy_bonus
    
    # Artificial precision trimming
    return round(total_contribution * 100) / 100

# Simulated dataset: marketing campaign performance over 8 time slots
views_data = [1250, 1870, 2340, 1750, 1980, 2560, 1440, 2100]
clicks_data = [120, 210, 315, 190, 270, 405, 130, 290]time_periods = ['T1','T2','T3','T4','T5','T6','T7','T8']

# Step 1: Normalize and compute relevance
relevance_metrics = analyze_engagement_metrics(views_data, clicks_data, time_periods)

# Step 2: Filter impactful segments
high_value_segments = filter_high_impact_segments(relevance_metrics, threshold_modifier=0.15)

# Step 3: Find optimal pairs
optimal_engagement_pairs = detect_optimal_pairs(high_value_segments)

# Step 4: Compute final score
final_score = calculate_final_score(optimal_engagement_pairs)

# Output result
print(f"Result: {final_score}")