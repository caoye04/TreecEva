from itertools import combinations

def analyze_performance(metrics):
    avg = sum(metrics) / len(metrics)
    variance = sum((x - avg) ** 2 for x in metrics) / len(metrics)
    return avg, variance

def extract_top_pairs(data, threshold=0.8):
    pairs = []
    for i, j in combinations(range(len(data)), 2):
        if (data[i] + data[j]) / 2 > threshold:
            pairs.append((i, j))
    return pairs

def calculate_final_score(ranks, wts):
    normalized_ranks = [r / max(ranks) for r in ranks]
    weighted_sum = sum(r * w for r, w in zip(normalized_ranks, wts))
    penalty = 0.0
    for i in range(1, len(ranks)):
        if ranks[i] < ranks[i-1]:
            penalty += 0.01
    adjustment = 1.0 - penalty
    return weighted_sum * adjustment

def main():
    # Simulated model evaluation metrics (higher is better)
    accuracy_scores = [0.88, 0.92, 0.85, 0.94, 0.87]
    latency_impact = [0.1, 0.15, 0.08, 0.2, 0.12]  # Lower is better
    memory_footprint = [1024, 1300, 950, 1500, 1100]  # Lower is better

    # Irrelevant transformation (distractor)
    efficiency_ratings = [a / (l + 0.05) for a, l in zip(accuracy_scores, latency_impact)]
    
    # Normalize and invert negative metrics
    inverted_latency = [1 - l for l in latency_impact]
    inverted_memory = [1 - (m / 2000) for m in memory_footprint]

    # Compute composite rankings (main logic)
    composite_metrics = [
        acc * 0.6 + lat * 0.2 + mem * 0.2
        for acc, lat, mem in zip(accuracy_scores, inverted_latency, inverted_memory)
    ]

    # Extract indices sorted by performance
    sorted_indices = sorted(range(len(composite_metrics)), key=lambda i: composite_metrics[i], reverse=True)
    rankings = [0] * len(composite_metrics)
    for rank, idx in enumerate(sorted_indices):
        rankings[idx] = rank + 1

    # Weight vector for final scoring
    weights = [0.4, 0.3, 0.15, 0.1, 0.05]

    # Distractor: unused combination analysis
    high_performers = extract_top_pairs(composite_metrics, threshold=0.85)
    perf_avg, perf_var = analyze_performance(composite_metrics)

    # Key computation
    final_score = calculate_final_score(rankings, weights)

    # Print result
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()