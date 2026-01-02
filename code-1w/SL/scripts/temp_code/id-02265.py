from itertools import combinations

# Simulate agricultural yield analysis across regions with noise filtering
region_data = [
    {'name': 'north', 'soil_quality': 0.8, 'rainfall': 120, 'crops': ['wheat', 'barley']},
    {'name': 'south', 'soil_quality': 0.5, 'rainfall': 60, 'crops': ['maize']},
    {'name': 'east', 'soil_quality': 0.9, 'rainfall': 200, 'crops': ['rice', 'sugarcane', 'maize']},
    {'name': 'west', 'soil_quality': 0.6, 'rainfall': 90, 'crops': ['wheat', 'maize']}
]

# Irrelevant helper: computes string lengths of crop names (distractor)
def analyze_crop_naming(crop_list):
    return [len(crop) for crop in crop_list]

# Misleading metric: unused biodiversity score
def calculate_biodiversity_score(region_list):
    total_pairs = 0
    for region in region_list:
        pairs = list(combinations(region['crops'], 2))
        total_pairs += len(pairs)
    return total_pairs

# Noise filter: removes high-rainfall outliers above threshold (semi-relevant)
def filter_high_rainfall(regions, threshold=150):
    return [r for r in regions if r['rainfall'] <= threshold]

# Core logic: compute weighted harvest efficiency
# Weighted by soil quality and normalized rainfall (optimal at 100mm)
def compute_harvest_efficiency(regions):
    filtered_regions = filter_high_rainfall(regions)
    efficiency_scores = []
    
    for r in filtered_regions:
        base_efficiency = r['soil_quality'] * 100
        rainfall_factor = min(r['rainfall'] / 100.0, 1.2)  # capped at 1.2
        adjusted_efficiency = base_efficiency * rainfall_factor
        efficiency_scores.append(adjusted_efficiency)
    
    avg_efficiency = sum(efficiency_scores) / len(efficiency_scores)
    
    # Bonus for regions with more than 2 crops (only east qualifies pre-filter)
    rich_crop_count = sum(1 for r in filtered_regions if len(r['crops']) > 2)
    if rich_crop_count >= 1:
        avg_efficiency *= 1.1  # 10% bonus
    
    return round(avg_efficiency, 4)

# Dead code path: unused normalization function
def normalize_data(data, key):
    values = [item[key] for item in data]
    m = min(values)
    M = max(values)
    return [(v - m) / (M - m) for v in values] if M > m else [0] * len(values)

# Extract crop names for slicing demo (irrelevant to final result)
all_crops = []
for region in region_data:
    all_crops.extend(region['crops'])

crop_name_lengths = analyze_crop_naming(all_crops)
median_length = sorted(crop_name_lengths)[len(crop_name_lengths)//2]

# Compute biodiversity (computed but not used)
biodiversity_index = calculate_biodiversity_score(region_data)

# Key execution point
final_yield = compute_harvest_efficiency(region_data)

# Print result as required
print(f"Result: {final_yield}")