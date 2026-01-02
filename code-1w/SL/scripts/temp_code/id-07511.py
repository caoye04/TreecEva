from collections import defaultdict, Counter

def analyze_field_patterns(temperatures, rainfall, crop_types):
    # Irrelevant aggregation - distractor
    temp_stats = defaultdict(float)
    for t in temperatures:
        temp_stats['sum'] += t
        temp_stats['count'] += 1
    temp_stats['avg'] = temp_stats['sum'] / temp_stats['count'] if temp_stats['count'] else 0

    # Semi-relevant: count crop distribution (used later)
    crop_counter = Counter(crop_types)

    # Simulate microclimate zones - mostly irrelevant
    microclimates = []
    for i, (t, r) in enumerate(zip(temperatures, rainfall)):
        zone = 'arid' if t > 30 and r < 100 else 'temperate' if 20 <= t <= 30 else 'cool'
        microclimates.append(zone)
    
    # Misleading efficiency metric (never used in final result)
    fake_efficiency = sum(1 for z in microclimates if z == 'temperate') * 0.7

    return crop_counter, microclimates, temp_stats


def calculate_harvest_efficiency(yields, crop_data, thresholds):
    # Key variable initialization
    base_multiplier = 1.0
    adjustment_factor = 0.0
    total_crops = sum(crop_data.values())

    # Distractor: unused growth stages
    growth_stages = ['germination', 'vegetative', 'flowering', 'maturation']
    stage_map = {i+1: stage for i, stage in enumerate(growth_stages)}

    # Real logic begins: filter valid yields using threshold
    valid_yields = [y for y in yields if y >= thresholds.get('min_yield', 0)]

    # Intermediate transformation with lambda - actual use
    normalized = list(map(lambda x: x / max(valid_yields), valid_yields))

    # Weighted efficiency calculation
    weighted_sum = 0.0
    for i, val in enumerate(normalized):
        if i % 2 == 0:
            weighted_sum += val * 1.1
        else:
            weighted_sum += val * 0.95

    # Another red herring: simulate pest resistance (unused)
    pest_resistance_score = 0
    for crop, count in crop_data.items():
        if 'wheat' in crop or 'barley' in crop:
            pest_resistance_score += count * 0.3
        elif 'corn' in crop:
            pest_resistance_score += count * 0.6

    # Core formula - determines answer
    raw_efficiency = sum(valid_yields) / len(valid_yields) if valid_yields else 0
    adjustment_factor = len([v for v in rainfall_data if v > 150]) * 0.02  # depends on outer scope
    final_efficiency = raw_efficiency * (base_multiplier + adjustment_factor) * (weighted_sum / len(normalized) if normalized else 1)

    return int(round(final_efficiency))

# Main execution context
if __name__ == '__main__':
    # Input data
    temperature_data = [25, 28, 32, 26, 24, 35, 29]
    rainfall_data = [120, 180, 90, 200, 110, 80, 160]
    crop_distribution = ['wheat_spring', 'corn_yellow', 'wheat_winter', 'soybean', 'barley', 'corn_white', 'wheat_spring']
    yield_records = [450, 520, 300, 580, 410, 540, 470]
    
    # Thresholds configuration (some fields unused)
    config_thresholds = {
        'min_yield': 300,
        'max_temp': 40,
        'ignore_below_rain': 50
    }

    # Call analysis (partially used)
    counts, zones, stats = analyze_field_patterns(temperature_data, rainfall_data, crop_distribution)

    # Critical computation
    final_yield = calculate_harvest_efficiency(yield_records, counts, config_thresholds)

    print(f"Result: {final_yield}")