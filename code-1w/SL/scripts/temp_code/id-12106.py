def analyze_growth_factor(conditions):
    base = conditions['temperature'] * 0.8
    bonus = 1.2 if conditions['rainfall'] > 50 else 0.7
    penalty = 0.9 if conditions['pests'] else 1.0
    # Irrelevant calculation (distractor)
    hypothetical_loss = base * 0.15
    adjusted = base * bonus * penalty
    return adjusted

# Simulate agricultural yield across regions
total_regions = 4
region_data = [
    {'name': 'north', 'temperature': 25, 'rainfall': 60, 'pests': True, 'soil_quality': 'high'},
    {'name': 'south', 'temperature': 30, 'rainfall': 40, 'pests': False, 'soil_quality': 'medium'},
    {'name': 'east', 'temperature': 20, 'rainfall': 70, 'pests': True, 'soil_quality': 'low'},
    {'name': 'west', 'temperature': 35, 'rainfall': 45, 'pests': False, 'soil_quality': 'high'}
]

accumulated_scores = []
buffer_zone = []  # Unused list (distractor)

for data in region_data:
    score = analyze_growth_factor(data)
    multiplier = 2 if data['soil_quality'] == 'high' else (1.5 if data['soil_quality'] == 'medium' else 1)
    final_score = score * multiplier
    accumulated_scores.append(final_score)

    # Dead code path (distractor)
    if len(buffer_zone) > 10:
        buffer_zone.clear()

# Intermediate aggregation (semi-relevant)
avg_base_yield = sum(accumulated_scores) / len(accumulated_scores)

# Apply seasonal adjustment using conditional expression
season_factor = 1.3 if avg_base_yield < 25 else 0.95
adjusted_total = avg_base_yield * season_factor

# Compute harvest index based on combinatorics of viable regions
viable_regions = [s for s in accumulated_scores if s > 20]
combination_count = 0
for i in range(len(viable_regions)):
    for j in range(i + 1, len(viable_regions)):
        combination_count += 1

# Auxiliary calculation with dictionary operations
growth_summary = {f'region_{i}': s for i, s in enumerate(accumulated_scores)}
growth_summary['combination_potential'] = float(combination_count)

# Final computation chain
def calculate_harvest_potential(data_list):
    base = adjusted_total
    offset = combination_count * 0.4
    # Conditional expression used here
    boost = 1.1 if len(viable_regions) >= 2 else 0.9
    noise_floor = 0.05 * sum([len(d['name']) for d in data_list])  # Slight distraction
    result = base + offset * boost - noise_floor
    return int(result)  # Deterministic integer output

final_yield = calculate_harvest_potential(region_data)
print(f"Result: {final_yield}")