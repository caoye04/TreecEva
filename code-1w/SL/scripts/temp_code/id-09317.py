def analyze_soil(ph_levels):
    # Irrelevant analysis
    avg_ph = sum(ph_levels) / len(ph_levels)
    stability_score = 0
    for i in range(1, len(ph_levels)):
        stability_score += abs(ph_levels[i] - ph_levels[i-1])
    normalized_stability = 1 / (1 + stability_score)
    return normalized_stability

soil_samples = [6.2, 6.4, 6.3, 6.5, 6.6, 6.4, 6.3]

# Distractor: soil health computation that isn't used later
soil_health = analyze_soil(soil_samples)

field_data = [
    {'crop': 'wheat', 'area': 120, 'yield_per_hectare': 3.2, 'moisture': 0.45},
    {'crop': 'corn', 'area': 85, 'yield_per_hectare': 4.1, 'moisture': 0.38},
    {'crop': 'barley', 'area': 200, 'yield_per_hectare': 2.8, 'moisture': 0.52},
    {'crop': 'oats', 'area': 90, 'yield_per_hectare': 3.6, 'moisture': 0.41}
]

# Filter fields with adequate moisture using lambda
suitable_fields = list(filter(lambda f: f['moisture'] < 0.5, field_data))

# Intermediate calculations with distractors
baseline_adjustment = 0.95
bonus_factor = 1.0
penalty_applied = False

# Accumulate total potential yield from suitable fields
raw_total = 0
adjusted_total = 0
for field in suitable_fields:
    raw_total += field['area'] * field['yield_per_hectare']
    if field['crop'] == 'wheat':
        bonus_factor = 1.1  # Bonus only if wheat is present
        penalty_applied = True  # Misleading flag update

# Apply adjustment (bonus only if wheat was found)
adjusted_total = raw_total * bonus_factor

# Simulate processing loss unrelated to final logic
processing_loss_rate = 0.03
net_after_processing = adjusted_total * (1 - processing_loss_rate)

# Additional irrelevant state tracking
inspection_log = []
for field in suitable_fields:
    inspection_log.append(f"{field['crop'].upper()}: PASSED")

# Processed fields: extract area and adjusted yield per hectare
processed_fields = []
for field in suitable_fields:
    adjusted_yield = field['yield_per_hectare'] * bonus_factor
    processed_fields.append({'area': field['area'], 'adjusted_yield': adjusted_yield})

# Final calculation function
def calculate_harvest(fields):
    total_yield = 0
    for f in fields:
        total_yield += f['area'] * f['adjusted_yield']
    return total_yield

# Key statement
final_yield = calculate_harvest(processed_fields)

# Print result as required
print(f"Target result: {final_yield}")