from itertools import combinations

def evaluate_performance(metrics):
    base_score = sum([m * (i + 1) for i, m in enumerate(metrics)])
    adjustment = 0
    
    # Distractor: complex but unused logic involving combinations
    unused_pairs = list(combinations(metrics, 2))
    temp_sum = 0
    for a, b in unused_pairs:
        temp_sum += abs(a - b) * 0.1
    
    if len(metrics) > 3:
        adjustment = 5
    else:
        adjustment = 2
    
    return base_score + adjustment

def normalize(data):
    total = sum(data)
    return [x / total for x in data] if total != 0 else [0] * len(data)

def calculate_final_score(ranks, w):
    normalized_ranks = normalize(ranks)
    score_components = []
    
    for i, nr in enumerate(normalized_ranks):
        weight_factor = w[i] if i < len(w) else 0.5
        raw_component = nr * weight_factor * 100
        # Semi-relevant transformation
        adjusted_component = raw_component + (1 - nr) * 0.2
        score_components.append(adjusted_component)
    
    # Real computation path
    pre_score = sum(score_components)
    bonus = 0
    
    # Conditional bonus based on pattern in ranks
    sorted_ranks = sorted(ranks)
    if sorted_ranks == ranks:  # already sorted
        bonus = 10
    
    # Dead code branch — never executes due to prior sort
    if sorted_ranks != ranks and len(ranks) % 2 == 0:
        bonus += 7  # unreachable
    
    final = pre_score + bonus
    
    # Key intermediate variable that distracts but isn't used
    peak_contribution = max(score_components) if score_components else 0
    
    return final

# Main execution
metrics_data = [85, 90, 75, 95]
rankings = [40, 60, 50, 70]
weights = [0.8, 0.9, 0.7, 1.0]

# Unused helper call — red herring
performance_score = evaluate_performance(metrics_data)

# Irrelevant sorting operation
sorted_metrics = sorted(metrics_data, reverse=True)

# Actual target computation
final_score = calculate_final_score(rankings, weights)

print(f"Result: {final_score}")