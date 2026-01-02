from collections import defaultdict
from itertools import combinations

# Simulate survey response aggregation with bias correction
def preprocess_survey(raw_responses):
    cleaned = [r for r in raw_responses if 1 <= r <= 10]
    outlier_count = sum(1 for r in cleaned if r < 3 or r > 8)
    stats = defaultdict(int)
    for val in cleaned:
        stats['sum'] += val
        stats['count'] += 1
        if val > 5:
            stats['positive'] += 1
    
    # Irrelevant distractor computation
    temp_pairs = list(combinations(cleaned, 2))
    pair_sum = sum(a + b for a, b in temp_pairs)  # Not used later
    
    return dict(stats)

# Apply weighting and normalization
def compute_baseline(sums, total_count):
    raw_avg = sums / total_count
    normalized = (raw_avg - 3.0) * 1.5
    return max(normalized, 1.0)

# Main aggregation with adjustment logic
def compute_aggregate(data, adj):
    result = preprocess_survey(data)
    base = compute_baseline(result['sum'], result['count'])
    
    # Dummy conditional branch (always false in this case)
    extra_weight = 0
    if len(data) > 1000:  # Never true
        extra_weight = 0.5
    
    # Core logic
    positivity_ratio = result['positive'] / result['count']
    boost = 2.0 * positivity_ratio if positivity_ratio > 0.6 else 0.5
    
    # Multiple intermediate steps with some red herrings
    temp_debug = {'base': base, 'boost': boost, 'adj': adj}  # Unused tracking
    adjusted_base = base * adj
    final_score = adjusted_base + boost + extra_weight
    
    # Additional irrelevant set operation
    unique_vals = set(data)
    completeness_check = len(unique_vals.intersection({1,2,3,4,5,6,7,8,9,10}))  # Distractor
    
    return round(final_score, 4)

# Simulated input data
survey_data = [5, 7, 6, 8, 9, 4, 7, 6, 5, 8, 7, 6, 10, 3, 7, 6, 5, 8, 7, 6]
adjustment_factor = 1.2

# Execute main logic
final_score = compute_aggregate(survey_data, adjustment_factor)
print(f"Result: {final_score}")