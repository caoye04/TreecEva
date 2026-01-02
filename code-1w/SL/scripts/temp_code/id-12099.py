from itertools import combinations

def analyze_growth_patterns(data, factor):
    temp_results = []
    for i in range(2, len(data) + 1):
        for combo in combinations(data, i):
            product = 1
            for val in combo:
                product *= val
            temp_results.append(product % factor)
    return temp_results

# Simulate environmental stress factors across zones
stress_factors = [3, 7, 5, 11, 13]
dummy_analysis = [x ** 2 + 2*x + 1 for x in stress_factors if x % 2 == 1]

# Actual crop cluster health scores (key data)
cluster_scores = [4, 8, 6, 2, 10]

# Irrelevant transformation - distractor
mapped_zones = list(map(lambda z: (z * 3 + 1) // 2, stress_factors))

# Secondary analysis with no impact on final result
trend_pairs = [(a, b) for a, b in zip(stress_factors, stress_factors[1:]) if a < b]
adjusted_trends = [t[1] - t[0] for t in trend_pairs]

threshold = 7

# Core logic hidden among distractions
def calculate_harvest_efficiency(clusters, limit):
    valid_clusters = [c for c in clusters if c >= limit]
    if not valid_clusters:
        return 0
    
    # Compute pairwise synergies
    synergy_pairs = list(combinations(valid_clusters, 2))
    total_synergy = 0
    for p1, p2 in synergy_pairs:
        total_synergy += abs(p1 - p2)
    
    base_yield = sum(valid_clusters)
    efficiency_bonus = len(synergy_pairs) * 0.5 if total_synergy > 0 else 0
    
    # Dummy conditional branch - dead path
    if len(valid_clusters) > 10:
        efficiency_bonus += 5  # Never reached
    
    return base_yield + efficiency_bonus

# Execution point of interest
final_yield = calculate_harvest_efficiency(cluster_scores, threshold)

print(f"Result: {final_yield}")