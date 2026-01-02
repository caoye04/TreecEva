from collections import defaultdict, Counter

# Simulate agricultural yield analysis with noise and irrelevant computations
def analyze_crop_performance(fields):
    results = defaultdict(float)
    for field_id, crops in fields.items():
        base_yield = 0
        bonus_factor = 1.0
        penalty = 0

        # Irrelevant seasoning calculation (distractor)
        seasoning_index = sum([len(crop) for crop in crops]) % 7
        if seasoning_index > 4:
            bonus_factor *= 1.05

        for crop in crops:
            if 'wheat' in crop:
                base_yield += 23
            elif 'corn' in crop:
                base_yield += 19
            elif 'rice' in crop:
                base_yield += 21
            # Distractor: unused mutation
            adjusted_name = crop[::-1].lower().replace('e', '3')

        # Fake normalization (never used later)
        normalized = round(base_yield / (len(crops) + 1), 3) if crops else 0
        results[field_id] = base_yield * bonus_factor - penalty

    return results

# Dead function - looks related but unused in final logic
def predict_rainfall_impact(logs):
    impact_score = 0
    for entry in logs:
        parts = entry.split(':')
        if len(parts) > 1:
            value = float(parts[1].strip())
            impact_score += abs(value) * 0.3
    return max(impact_score, 10.5)

# Another red herring: soil nutrient simulation
def compute_nutrient_depletion(field_map):
    depletion_grid = [[0]*5 for _ in range(5)]
    total_loss = 0.0
    for i in range(len(depletion_grid)):
        for j in range(len(depletion_grid[i])):
            if i % 2 == 0:
                depletion_grid[i][j] = (i + j) * 0.7
                total_loss += depletion_grid[i][j]
    return round(total_loss, 4)

# Core relevant logic buried among distractions
def calculate_harvest_efficiency(data, weather):
    efficiency = 0
    crop_counter = Counter()

    # Parse field data and extract key metrics
    for field_record in data:
        field_crops = field_record.get('crops', [])
        size_acres = field_record.get('size', 1)
        
        # Count all crops
        for crop in field_crops:
            crop_counter[crop] += 1
            # Relevant transformation
            if 'wheat' in crop and 'early' in crop:
                efficiency += 4.2 * size_acres
            elif 'corn' in crop and 'hybrid' in crop:
                efficiency += 3.8 * size_acres
            elif 'rice' in crop and 'drought' not in crop:
                efficiency += 3.5 * size_acres

    # Weather adjustment factor — only certain conditions matter
    valid_conditions = 0
    for log_entry in weather:
        if 'temp:' in log_entry:
            temp_val = float(log_entry.split(':')[1].strip())
            if 18 <= temp_val <= 27:
                valid_conditions += 1

    # Final efficiency depends on both crop type and stable temperatures
    adjustment_factor = valid_conditions / len(weather) if weather else 1
    efficiency *= adjustment_factor

    # Real answer derived here
    final_value = int(efficiency + 0.5)  # Round to nearest integer

    # Irrelevant slicing operation (meets language feature requirement)
    history_snapshot = weather[1:-1]
    avg_len = sum(len(entry) for entry in history_snapshot) / len(history_snapshot) if history_snapshot else 0

    return final_value

# Input data setup
field_data = [
    {'id': 'F1', 'crops': ['wheat_early_variety', 'corn_standard'], 'size': 2},
    {'id': 'F2', 'crops': ['wheat_early_variety', 'rice_regular'], 'size': 3},
    {'id': 'F3', 'crops': ['corn_hybrid_strain', 'wheat_local'], 'size': 1}
]

weather_log = [
    'temp: 22.1', 'temp: 19.5', 'temp: 28.3', 'temp: 25.0', 'temp: 17.9', 'temp: 20.4'
]

# Execute main logic
initial_analysis = analyze_crop_performance({
    'F1': ['wheat_early_variety', 'corn_standard'],
    'F2': ['rice_regular', 'wheat_local']
})

# Unused nutrient computation (distraction)
nutrient_loss = compute_nutrient_depletion([[1,2],[3,4]])

# Critical statement — this produces the answer
final_yield = calculate_harvest_efficiency(field_data, weather_log)

# Output result as required
print(f"Result: {final_yield}")