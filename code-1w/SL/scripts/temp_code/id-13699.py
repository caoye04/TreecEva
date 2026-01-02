from itertools import combinations
from math import log

# Simulate user engagement scores across multiple content types
def calculate_engagement_metrics(views, shares, dwell_time):
    base_score = views * 0.3 + shares * 0.5
    time_bonus = dwell_time * 0.02 if dwell_time > 30 else 0
    penalty = 0.1 * (views // 1000) if shares < views * 0.05 else 0
    return base_score + time_bonus - penalty

# Assess content diversity using set operations
def assess_diversity(category_stream):
    unique_categories = set(category_stream)
    repeated = len(category_stream) - len(unique_categories)
    diversity_index = len(unique_categories) / (len(category_stream) + 1e-5)
    return diversity_index, repeated

# Determine performance ranking based on composite metrics
def generate_rankings(content_data):
    raw_scores = []
    for item in content_data:
        score = calculate_engagement_metrics(item['views'], item['shares'], item['dwell'])
        diversity_factor, _ = assess_diversity(item['categories'])
        adjusted_score = score * (1 + 0.5 * diversity_factor)
        raw_scores.append(adjusted_score)
    
    # Introduce auxiliary transformation with partial relevance
    normalized = [s / (sum(raw_scores) * 0.01 + 1) for s in raw_scores]
    noise_offset = sum([log(n + 2) for n in range(len(normalized))]) * 0.01
    enhanced = [n + noise_offset for n in normalized]
    rankings = sorted(enhanced, reverse=True)
    
    # Dead computation: irrelevant to final result
    pair_combinations = list(combinations(rankings, 2))
    avg_pair_gap = sum(abs(a - b) for a, b in pair_combinations) / len(pair_combinations) if pair_combinations else 0
    
    return rankings

# Final evaluation against dynamic baseline
def evaluate_performance(rankings, baseline):
    above_baseline = sum(1 for r in rankings if r > baseline)
    below_baseline = len(rankings) - above_baseline
    performance_gap = sum(r - baseline for r in rankings if r > baseline)
    
    # Misleading intermediate calculation (not used in output)
    theoretical_max = len(rankings) * (baseline + 1)
    efficiency_ratio = performance_gap / (theoretical_max + 1e-8)
    
    # Core logic contribution
    multiplier = 2 if above_baseline >= below_baseline else 0.5
    final_score = int(performance_gap * multiplier * 100)  # Scale for integer output
    
    # Additional red herring variables
    decay_factor = 0.95 ** len(rankings)
    smoothed_score = final_score * decay_factor  # unused
    
    return final_score

# Input data setup
data_pool = [
    {'views': 1250, 'shares': 45, 'dwell': 42, 'categories': ['tech', 'ai', 'cloud', 'security']},
    {'views': 980, 'shares': 67, 'dwell': 58, 'categories': ['health', 'fitness', 'nutrition']},
    {'views': 1420, 'shares': 32, 'dwell': 26, 'categories': ['entertainment', 'celebrity']},
    {'views': 890, 'shares': 89, 'dwell': 73, 'categories': ['finance', 'crypto', 'ai', 'markets']},
    {'views': 1100, 'shares': 54, 'dwell': 35, 'categories': ['education', 'online', 'coding']}
]

rankings = generate_rankings(data_pool)
baseline = 0.45
final_score = evaluate_performance(rankings, baseline)
print(f"Target result: {final_score}")