from itertools import combinations

# Simulate agricultural yield optimization across microclimate zones
def analyze_microclimate_stability(temperature_log, rainfall_data):
    stability_score = 0
    fluctuation_penalty = 0
    
    for i in range(1, len(temperature_log)):
        diff = abs(temperature_log[i] - temperature_log[i-1])
        if diff > 5:
            fluctuation_penalty += diff * 0.3
    
    # Irrelevant smoothing pass (distractor)
    smoothed = [temperature_log[0]]
    for t in temperature_log[1:]:
        smoothed.append(smoothed[-1] * 0.8 + t * 0.2)
    
    base_stability = sum(rainfall_data) * 0.1
    return base_stability - fluctuation_penalty

# Identify optimal planting cluster configurations
def generate_cluster_configurations(field_size):
    configs = []
    for r in range(2, min(5, field_size//3 + 1)):
        configs.extend(combinations(range(field_size), r))
    
    # Dead code path - never used (distractor)
    if len(configs) > 100:
        return configs[:100]
    
    return configs[:50]  # Limit for computational feasibility

# Calculate harvest efficiency based on cluster performance and growth cycles
def calculate_harvest_efficiency(cluster_scores, growth_cycles):
    efficiency = 0.0
    decay_factor = 0.95
    
    for cycle in range(growth_cycles):
        cycle_boost = 1 + (cycle * 0.05)  # Incremental improvement per cycle
        max_score = max(cluster_scores) * cycle_boost
        efficiency += max_score * (decay_factor ** cycle)
        
        # Update scores with simulated pollination spread (semi-relevant)
        new_scores = []
        for i, score in enumerate(cluster_scores):
            neighbor_influence = 0
            if i > 0:
                neighbor_influence += cluster_scores[i-1] * 0.1
            if i < len(cluster_scores) - 1:
                neighbor_influence += cluster_scores[i+1] * 0.1
            new_scores.append(score * 0.8 + neighbor_influence)
        cluster_scores = new_scores
    
    return round(efficiency, 4)

# Main execution
field_temperature = [22, 25, 19, 26, 30, 28, 24, 20]
rainfall_pattern = [120, 80, 150, 200, 90, 60, 130, 180]

# Step 1: Assess environmental baseline
env_stability = analyze_microclimate_stability(field_temperature, rainfall_pattern)
baseline_risk = sum(1 for t in field_temperature if t < 20 or t > 28)

# Step 2: Generate planting configurations (uses itertools)
config_options = generate_cluster_configurations(len(field_temperature))
config_count = len(config_options)

# Step 3: Simulate initial cluster productivity
cluster_base_productivity = [abs(t * 0.4 + r * 0.01) for t, r in zip(field_temperature, rainfall_pattern)]

# Step 4: Apply stress adjustment (distractor computation)
stress_factors = []
for temp, rain in zip(field_temperature, rainfall_pattern):
    stress = 0
    if temp < 20 or temp > 30:
        stress += 0.2
    if rain < 70 or rain > 180:
        stress += 0.15
    stress_factors.append(stress)
adjusted_productivity = [p * (1 - s) for p, s in zip(cluster_base_productivity, stress_factors)]

# Step 5: Determine final cluster scores using raw base (bypassing adjusted)
cluster_scores = [p * (1 + env_stability * 0.01) for p in cluster_base_productivity]
growth_cycles = 6

# Key statement
final_yield = calculate_harvest_efficiency(cluster_scores, growth_cycles)

print(f"Result: {final_yield}")