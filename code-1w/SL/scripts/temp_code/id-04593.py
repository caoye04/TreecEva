from itertools import groupby
from math import log

# Simulate agricultural yield optimization with noise filtering and efficiency scoring
def analyze_soil_samples(samples):
    sorted_samples = sorted(samples, key=lambda x: x['ph'])
    clusters = [list(g) for k, g in groupby(sorted_samples, key=lambda x: round(x['ph'], 1))]
    
    # Irrelevant transformation (distractor)
    transformed_data = []
    for cluster in clusters:
        avg_moisture = sum(s['moisture'] for s in cluster) / len(cluster)
        for s in cluster:
            transformed_data.append({
                'id': s['id'],
                'stability_score': abs(s['ph'] - avg_moisture) * 0.7
            })
    
    # Relevant computation path
    cluster_metrics = []
    for cluster in clusters:
        ph_pivot = cluster[0]['ph']
        base_yield = sum(s['nutrients'] for s in cluster)
        size_factor = len(cluster) ** 0.5
        decay = log(1 + base_yield / (ph_pivot + 1))
        efficiency = base_yield * size_factor * decay
        cluster_metrics.append({'ph_group': round(ph_pivot, 1), 'efficiency': efficiency})
    
    return cluster_metrics

# Main processing pipeline
def calculate_harvest_efficiency(cluster_scores, adj_factor):
    if not cluster_scores:
        return 0.0
    
    # Sort by efficiency for ranking (semi-relevant)
    ranked = sorted(cluster_scores, key=lambda x: x['efficiency'], reverse=True)
    top_three = ranked[:3]
    
    # Apply adjustment factor (critical step)
    adjusted_total = sum(item['efficiency'] * adj_factor for item in top_three)
    
    # Distractor: unused normalization
    max_raw = max(item['efficiency'] for item in cluster_scores)
    normalized = [item['efficiency'] / max_raw for item in ranked]
    smoothness = sum(abs(normalized[i] - normalized[i-1]) for i in range(1, len(normalized))) if len(normalized) > 1 else 0
    
    return round(adjusted_total, 4)

# Simulated sensor data from field grid
raw_samples = [
    {'id': 1, 'ph': 6.8, 'moisture': 32, 'nutrients': 18},
    {'id': 2, 'ph': 6.9, 'moisture': 34, 'nutrients': 22},
    {'id': 3, 'ph': 6.9, 'moisture': 33, 'nutrients': 20},
    {'id': 4, 'ph': 7.2, 'moisture': 29, 'nutrients': 15},
    {'id': 5, 'ph': 7.2, 'moisture': 30, 'nutrients': 17},
    {'id': 6, 'ph': 7.2, 'moisture': 31, 'nutrients': 19},
    {'id': 7, 'ph': 5.4, 'moisture': 40, 'nutrients': 10},
    {'id': 8, 'ph': 5.4, 'moisture': 38, 'nutrients': 12}
]

# Secondary distractor: unused historical average
historical_avg_yield = 142.6
projected_growth_rate = 1.08
baseline_projection = historical_avg_yield * projected_growth_rate

# Noise threshold filter (dead code - never used)
valid_ids = [s['id'] for s in raw_samples if s['moisture'] > 25]
filtered_samples = [s for s in raw_samples if s['nutrients'] > 9]

# Core execution path
analysis_results = analyze_soil_samples(filtered_samples)
adjustment_factor = 1.15
final_yield = calculate_harvest_efficiency(analysis_results, adjustment_factor)

# Final output
print(f"Result: {final_yield}")