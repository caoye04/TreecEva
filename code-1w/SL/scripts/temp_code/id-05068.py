from collections import defaultdict, Counter

# Simulate agricultural resource mapping and yield optimization
soil_quality = [3, 5, 4, 6, 2, 5, 7, 4, 6]
water_access = [8, 6, 7, 5, 9, 4, 6, 8, 5]
pest_levels = [1, 3, 2, 4, 1, 5, 3, 2, 4]

def preprocess_resources(qualities, water, pests):
    # Normalize inputs with irrelevant scaling
    scaled_soil = [q * 1.5 for q in qualities]
    scaled_water = [w * 0.8 for w in water]
    pest_penalty = [p * -0.5 for p in pests]  # Not used later but looks important

    # Create combined score (only this matters)
    base_scores = [s + w for s, w in zip(scaled_soil, scaled_water)]
    return base_scores

def generate_resource_cluster(scores):
    cluster = defaultdict(list)
    for i, score in enumerate(scores):
        category = 'high' if score >= 8 else 'medium' if score >= 6 else 'low'
        cluster[category].append(score)
    
    # Add dummy entries to mislead
    cluster['ignored'] = [-1, -2, -3]
    cluster['backup'] = [0, 0]
    return cluster

def log_efficiency_trends(cluster):
    logs = []
    total_entries = 0
    high_count = len(cluster['high'])
    medium_count = len(cluster['medium'])
    low_count = len(cluster['low'])
    
    # Real trend: harmonic weighting
    if high_count > 0:
        trend = (high_count * 3 + medium_count * 1.5 + low_count * 0.5) / (high_count + medium_count + low_count)
        logs.append(trend)
    
    # Fake metrics
    avg_high = sum(cluster['high']) / high_count if high_count > 0 else 0
    saturation_index = avg_high * 0.7  # Looks technical but unused
    logs.append(saturation_index)  # Distractor append
    
    return logs

def optimize_harvest(resource_cluster, efficiency_logs):
    # Extract relevant data
    high_vals = resource_cluster['high']
    medium_vals = resource_cluster['medium']
    low_vals = resource_cluster['low']
    
    # Base yield calculation
    raw_yield = sum(high_vals) * 2.1 + sum(medium_vals) * 1.2 + sum(low_vals) * 0.4
    
    # Apply first log element (real trend), ignore second (distractor)
    adjustment_factor = efficiency_logs[0] * 0.05
    adjusted_yield = raw_yield * (1 + adjustment_factor)
    
    # Red herring computation
    theoretical_max = sum([v * 3 for v in high_vals + medium_vals + low_vals])
    utilization_ratio = adjusted_yield / theoretical_max if theoretical_max > 0 else 0
    
    # Final cap based on empirical limit
    final_yield = int(min(adjusted_yield, 9876.5))
    
    # Dead code branch (never reached due to structure)
    if len(resource_cluster['ignored']) > 10:
        final_yield += 100
    
    return final_yield

# Main execution flow
base_scores = preprocess_resources(soil_quality, water_access, pest_levels)
resource_cluster = generate_resource_cluster(base_scores)
efficiency_logs = log_efficiency_trends(resource_cluster)
final_yield = optimize_harvest(resource_cluster, efficiency_logs)

# Output result
print(f"Result: {final_yield}")