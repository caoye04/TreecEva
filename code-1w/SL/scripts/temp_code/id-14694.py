from itertools import combinations

def preprocess_data(entries):
    # Irrelevant preprocessing step with side effects
    normalized = [e / sum(entries) for e in entries]
    smoothed = [normalized[i] + 0.01 for i in range(len(normalized))]
    return smoothed

def compute_pairwise_metrics(data):
    # Distractor function: computes unused metrics
    results = []
    for a, b in combinations(data, 2):
        diff = abs(a - b)
        ratio = max(a, b) / (min(a, b) + 1e-8)
        results.append((diff, ratio))
    return results

def rank_elements(values):
    indexed = list(enumerate(values))
    sorted_indexed = sorted(indexed, key=lambda x: x[1], reverse=True)
    ranks = [0] * len(values)
    for rank, (idx, val) in enumerate(sorted_indexed):
        ranks[idx] = rank + 1
    return ranks

def calculate_weighted_sum(ranks, weights):
    weighted_sum = 0
    for i in range(len(ranks)):
        weighted_sum += ranks[i] * weights[i % len(weights)]
    return weighted_sum

def calculate_final_score(ranks, weights):
    temp_scores = []
    for r in ranks:
        if r % 2 == 0:
            temp_scores.append(r ** 2)
        else:
            temp_scores.append(r + 1)
    
    # Real computation path
    base_score = calculate_weighted_sum(ranks, weights)
    adjustment = 0
    for i, score in enumerate(temp_scores):
        if i % 3 == 0:
            adjustment += score // 4
    
    # Secondary distractor: unused transformation
    transformed_ranks = [r * 1.5 for r in ranks if r < 5]
    dummy_aggregate = sum(transformed_ranks) / (len(transformed_ranks) + 1)
    
    final_score = base_score + adjustment - 2  # Final deterministic result
    return final_score

# Main execution block
if __name__ == "__main__":
    raw_input_data = [12, 15, 8, 23, 17, 4]
    processed_data = preprocess_data(raw_input_data)
    
    # Unused metric collection (distractor)
    metrics = compute_pairwise_metrics(raw_input_data)
    avg_metric = sum(m[0] for m in metrics) / len(metrics)
    
    rankings = rank_elements(raw_input_data)
    weights = [3, 1, 4, 1, 5]
    
    # Key statement
    final_score = calculate_final_score(rankings, weights)
    
    # Additional irrelevant tracking
    status_log = {}
    for idx, r in enumerate(rankings):
        status_log[f"item_{idx}"] = "high" if r <= 3 else "low"
    
    print(f"Result: {final_score}")