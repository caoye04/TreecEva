from itertools import combinations

def analyze_efficiency(values):
    # Irrelevant helper: computes pairwise products (not used in final result)
    pairs = list(combinations(values, 2))
    unused_products = [a * b for a, b in pairs]
    return len(pairs)

def calculate_baseline(data):
    # Distractor function: calculates average but adds noise
    total = 0
    count = 0
    for i, val in enumerate(data):
        if i % 2 == 0:
            total += val + 0.5  # Artificial offset
        count += 1
    return total / count if count else 0

def evaluate_performance(metrics, weights):
    # Core logic with distractors
    adjusted = []
    temp_offset = 0.0

    for idx, (m, w) in enumerate(zip(metrics, weights)):
        # Real transformation
        if m > 70:
            temp_offset += 1.5
        normalized = m * w + temp_offset  # Actual contribution
        adjusted.append(normalized)
    
    # Dead code branch: never executed due to data constraints
    if len(metrics) > 100:
        fallback = sum(adjusted) / 100
        return round(fallback, 2)
    
    # Semi-relevant grouping
    groups = {'high': [], 'low': []}
    for val in adjusted:
        groups['high'].append(val) if val >= 50 else groups['low'].append(val)
    
    # Actual answer computation
    raw_sum = sum(adjusted)
    penalty = len(groups['low']) * 2.5
    bonus = temp_offset * 1.2
    final_score = raw_sum - penalty + bonus
    
    # Print required at end
    return round(final_score, 4)

# Main execution block
if __name__ == "__main__":
    # Input data
    metrics = [85, 73, 91, 64, 77]
    weights = [0.2, 0.3, 0.1, 0.25, 0.15]
    
    # Irrelevant preprocessing
    scaled_metrics = [m ** 0.5 for m in metrics]
    _ = analyze_efficiency(metrics)  # Called but result ignored
    _ = calculate_baseline(scaled_metrics)  # Unused baseline
    
    # Key statement
    final_score = evaluate_performance(metrics, weights)
    print(f"Target result: {final_score}")