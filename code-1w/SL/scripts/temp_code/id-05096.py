from collections import defaultdict

# Simulate agricultural yield prediction with noise filtering and state tracking
def preprocess_climate_data(raw_data):
    processed = []
    moving_avg = 0
    count = 0
    for val in raw_data:
        if val < 0:  # Invalid reading
            continue
        moving_avg = (moving_avg * count + val) / (count + 1) if count > 0 else val
        count += 1
        if val > 25:
            processed.append(val * 0.9)  # Heat stress adjustment
    return processed if processed else [20]


def evaluate_soil_health(profiles):
    health_scores = defaultdict(int)
    total_nutrients = 0
    for key, values in profiles.items():
        base_score = len(values) * 1.5
        nutrient_level = sum(values) / len(values) if values else 0
        total_nutrients += nutrient_level
        degradation_penalty = 0
        for v in values:
            if v < 2:
                degradation_penalty += 1
        health_scores[key] = base_score + nutrient_level - degradation_penalty
    
    # Distractor computation: unused summary
    avg_score = sum(health_scores.values()) / len(health_scores) if health_scores else 0
    dummy_normalization = avg_score * 0.85
    
    return dict(health_scores)


def calculate_harvest_potential(climate_input, soil_input):
    climate_clean = preprocess_climate_data(climate_input)
    soil_metrics = evaluate_soil_health(soil_input)
    
    # Intermediate calculations with some irrelevant ones
    temp_baseline = sum(climate_clean) / len(climate_clean)
    growth_factor = temp_baseline / 20.0
    buffer_reserve = temp_baseline * 0.1  # Unused in final result
    
    yield_components = []
    for region, score in soil_metrics.items():
        potential = score * growth_factor
        if potential > 30:
            potential *= 0.85  # Sustainability cap
        yield_components.append(potential)
    
    # Irrelevant aggregation
    max_potential = max(yield_components) if yield_components else 0
    min_potential = min(yield_components) if yield_components else 0
    range_potential = max_potential - min_potential
    
    final_yield = int(sum(yield_components))
    
    # Additional red herring variables
    projected_loss_rate = 0.03
    adjusted_projection = final_yield * (1 - projected_loss_rate)
    
    return final_yield

# Input data
climate_readings = [22, 26, -2, 30, 24, 28, -1, 27]
soil_profiles = {
    'north_field': [4, 5, 4],
    'south_field': [3, 2, 3, 4],
    'east_field': [5, 5, 6]
}

# Key execution point
final_yield = calculate_harvest_potential(climate_readings, soil_profiles)

print(f"Result: {final_yield}")