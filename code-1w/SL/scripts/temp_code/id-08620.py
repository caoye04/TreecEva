def analyze_growth_factors(conditions):
    # Irrelevant processing: normalize light and humidity (not used in final result)
    normalized_light = [min(max(val, 0), 100) for val in conditions.get('light', [])]
    humidity_score = sum([1 for h in conditions.get('humidity', []) if 40 < h < 80])

    # Distractor: complex but unused transformation
    processed_ph = {k: round((v * 1.2) + 0.5, 2) for k, v in conditions.get('ph_levels', {}).items()}

    # Relevant computation: temperature viability filter
    viable_temps = [t for t in conditions.get('temperature', []) if 18 <= t <= 30]
    temp_stability = len(viable_temps) / len(conditions.get('temperature', [])) if conditions.get('temperature') else 0

    return temp_stability


def calculate_soil_richness(profiles):
    richness_scores = []n    for zone, profile in profiles.items():
n        base_nutrients = profile.get('nitrogen', 0) + profile.get('phosphorus', 0)
        organic_matter = profile.get('organic_matter', 0)
        depth_factor = min(profile.get('depth_cm', 0) / 100, 1)

        # Semi-relevant: this score is partially overwritten later
        preliminary_score = (base_nutrients * 0.6) + (organic_matter * 0.4)
        adjusted_score = (preliminary_score * depth_factor) + (organic_matter * 0.1)  # minor adjustment

        richness_scores.append(adjusted_score)

    # Dead code path: never used
    if len(richness_scores) > 10:
        smoothed = [sum(richness_scores[i:i+3])/3 for i in range(len(richness_scores)-2)]
    else:
        smoothed = None

    return sum(richness_scores) / len(richness_scores) if richness_scores else 0

# Main data structures
dataset_snapshot = {
    'season': 'monsoon',
    'temperature': [22, 25, 19, 31, 27, 18, 24],  # one out of bounds
    'humidity': [85, 60, 75, 90, 55],
    'light': [95, 105, 80, 70],
    'ph_levels': {'A1': 6.2, 'A2': 5.8, 'B1': 7.1}
}

soil_profiles = {
    'A1': {'nitrogen': 12, 'phosphorus': 8, 'organic_matter': 3.2, 'depth_cm': 45},
    'A2': {'nitrogen': 10, 'phosphorus': 9, 'organic_matter': 2.8, 'depth_cm': 60},
    'B1': {'nitrogen': 14, 'phosphorus': 7, 'organic_matter': 4.0, 'depth_cm': 30}
}

# Misleading preprocessing step (slice-based filtering that's not ultimately decisive)
temp_window = dataset_snapshot['temperature'][1:5]  # [25, 19, 31, 27]
cleaned_temps = [t for t in temp_window if t <= 30]  # removes 31

# Key state tracking with distractors
tracking_log = []
stability_ratio = analyze_growth_factors(dataset_snapshot)
base_richness = calculate_soil_richness(soil_profiles)

# Composite index with red herring calculation
potential_boost = 0
if stability_ratio > 0.6:
    potential_boost += 5
if base_richness > 10:
    potential_boost += 3  # This won't trigger

# Real logic hidden among distractions
weight_stability = 0.4
weight_richness = 0.6

initial_potential = (stability_ratio * weight_stability + base_richness * weight_richness)

decay_factor = 0.9
adjusted_potential = initial_potential * decay_factor

# Final calculation using slicing to extract key subset for refinement
refinement_slice = dataset_snapshot['temperature'][-3:]  # last three: [31, 27, 18]
penalty_points = sum([1 for t in refinement_slice if t < 20 or t > 30])  # only 31 and 18 qualify

penalty_rate = penalty_points * 0.05
final_yield = round(adjusted_potential * (1 - penalty_rate), 4)

# Print required output
print(f"Target result: {final_yield}")