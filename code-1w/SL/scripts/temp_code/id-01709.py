import itertools

def analyze_pattern(sequence):
    # Irrelevant function: analyzes bit patterns but not used in final calculation
    count = 0
    for a, b in itertools.pairwise(sequence):
        if (a + b) % 3 == 0:
            count += 1
    return count

def validate_checksum(data):
    # Dead-end function: looks important but unused
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= (val * (i + 1)) % 255
    return checksum == 42

def transform_features(raw_inputs):
    # Distractor transformation with red herring logic
    transformed = []
    for x in raw_inputs:
        temp_val = (x ** 2 + 3 * x + 1) % 100
        if temp_val > 50:
            transformed.append(temp_val // 2)
        else:
            transformed.append(temp_val)
    return transformed[::-1]  # Reversed order – never consumed

def compute_rankings(elements):
    # Unused ranking logic that seems relevant
    ranked = sorted(elements, reverse=True)
    ranks = {}
    for idx, val in enumerate(ranked):
        ranks[val] = idx + 1
    return {v: k for k, v in ranks.items()}  # Mapping rank to value

def filter_outliers(dataset, threshold=1.5):
    # Looks statistically meaningful but irrelevant
    mean = sum(dataset) / len(dataset)
    std_dev = (sum((x - mean) ** 2 for x in dataset) / len(dataset)) ** 0.5
    return [x for x in dataset if abs(x - mean) <= threshold * std_dev]

def evaluate_performance(metrics, weights):
    # Core logic hidden among distractions
    weighted_sum = 0
    max_possible = 0
    for i in range(len(metrics)):
        if i % 2 == 0:
            # Only even indices contribute; odd ones are decoys
            weighted_sum += metrics[i] * weights[i]
        max_possible += weights[i]  # Max weight sum for normalization
    
    # Real computation path
    normalized = weighted_sum / max_possible
    bonus = 0
    
    # Conditional bonus based on combinatorial condition
    combinations = list(itertools.combinations([1, 2, 3, 4], 3))
    combo_count = len(combinations)  # 4 combinations
    
    if combo_count >= 4 and normalized > 0.7:
        bonus = 12
    
    base_score = int(normalized * 100)
    final_score = base_score + bonus
    
    # Many variables defined but only final_score matters
    debug_info = f'Score components: base={base_score}, bonus={bonus}'
    log_entry = {'timestamp': 123456, 'score': final_score, 'status': 'processed'}
    temp_result = (base_score * 2 + bonus) % 1000
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Input data with misleading extra values
    raw_metrics = [85, 92, 78, 63, 91, 45, 88, 73]  # Only even indices used: 85,78,91,88
    importance_weights = [0.2, 0.3, 0.15, 0.1, 0.1, 0.05, 0.05, 0.05]  # Weights aligned

    # Irrelevant preprocessing steps (distractors)
    cleaned_data = filter_outliers(raw_metrics, threshold=1.8)
    features = transform_features(raw_metrics)
    rankings_map = compute_rankings(raw_metrics)
    pattern_insight = analyze_pattern([1, 2, 4, 8, 16])

    # Actual critical call
    final_score = evaluate_performance(raw_metrics, importance_weights)
    
    # Print required output
    print(f"Result: {final_score}")