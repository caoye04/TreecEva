import itertools

def analyze_trends(values):
    trend_scores = []
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend_scores.append(1)
        elif values[i] < values[i-1]:
            trend_scores.append(-1)
        else:
            trend_scores.append(0)
    return sum(trend_scores)

def compute_volatility(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return variance ** 0.5

def compute_final_score(ranks, weights):
    base_score = 0
    adjustment_factor = 0.85
    
    # Real computation path
    sorted_ranks = sorted(ranks.items(), key=lambda x: x[1])
    rank_order = [item[0] for item in sorted_ranks]
    
    # Distractor: volatility analysis on irrelevant transformation
    transformed = [ranks[k] * 2 + 3 for k in ['A', 'B', 'C'] if k in ranks]
    _ = compute_volatility(transformed)  # Dead use
    
    # Real contribution: weighted bonus based on rank order
    bonus = 0
    for idx, key in enumerate(rank_order):
        if key in weights:
            bonus += weights[key] * (len(rank_order) - idx)
    
    # Distractor: unused permutation logic
    perm_count = 0
    for _ in itertools.permutations([1, 2, 3]):
        perm_count += 1  # Always 6, irrelevant
    
    # Real base score calculation
    for key, rank in ranks.items():
        if rank <= 3:
            base_score += 10
        elif rank <= 6:
            base_score += 5

    # Apply bonus with adjustment
    final_score = int(base_score + (bonus * adjustment_factor))
    
    # Distractor: redundant dictionary copy
    shadow_copy = {k: v for k, v in ranks.items()}
    for k in shadow_copy:
        shadow_copy[k] *= -1  # Never used
    
    return final_score

def main():
    # Input data
    rank_data = {'A': 2, 'B': 5, 'C': 1, 'D': 7, 'E': 3}
    bonus_weights = {'A': 2, 'C': 3, 'E': 1}
    
    # Irrelevant preprocessing
    normalized = {k: v / sum(rank_data.values()) for k, v in rank_data.items()}
    entropy = 0
    for p in normalized.values():
        if p > 0:
            entropy -= p * __import__('math').log(p)
    
    # Key statement
    final_score = compute_final_score(rank_data, bonus_weights)
    
    # Output result
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()