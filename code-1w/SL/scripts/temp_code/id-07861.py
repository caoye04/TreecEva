def analyze_growth_potential(temperature, moisture):
    # Irrelevant helper function with dead logic
    if temperature < 0 or moisture < 10:
        return -1
    growth_index = (temperature * 0.7) + (moisture * 0.3)
    return growth_index if growth_index > 50 else 0

# Distractor variables
unused_buffer = [0] * 100
legacy_threshold = 42.5
temp_log = {'status': 'inactive'}

soil_nutrients = {
    'nitrogen': 28,
    'phosphorus': 17,
    'potassium': 23
}

# Misleading precomputed values
phantom_baseline = sum([soil_nutrients[k] for k in soil_nutrients]) // 3
fallback_strategy = lambda x: x ** 0.5

climate_data = [22, 25, 19, 30, 27]
soil_conditions = [65, 70, 60, 80, 75]

# Decoy function that looks important but isn't used
def calculate_root_depth(temp_seq, moist_seq):
    depth = 0
    for t, m in zip(temp_seq, moist_seq):
        if t > 25 and m > 70:
            depth += 1.5
        elif t < 20:
            depth -= 0.5
    return max(depth, 0.5)

# Another red herring: unused recursive function
def predict_yield_stress(year, current=100):
    if year <= 1:
        return current
    if year % 3 == 0:
        return predict_yield_stress(year - 1, current * 0.9)
    return predict_yield_stress(year - 1, current * 1.05)

# Real computation begins here — heavily masked by noise
agri_matrix = []
for i, (temp, moist) in enumerate(zip(climate_data, soil_conditions)):
    # Compute per-index productivity score
    base_score = temp * 1.2 + moist * 1.8
    adjustment_factor = 1.0
    
    # Conditional expression with real impact
    adjustment_factor = 0.8 if temp > 26 else (1.1 if temp < 20 else 1.0)
    
    # Apply adjustment only if moisture is sufficient
    if moist >= 65:
        base_score *= adjustment_factor
    
    agri_matrix.append(base_score)

# Secondary transformation with enumerate and conditional expressions
adjusted_scores = []
for idx, score in enumerate(agri_matrix):
    modifier = 1.05 if idx % 2 == 0 else 0.95
    # Only apply modifier if score exceeds dynamic threshold
    threshold = 45 + (idx * 2)
    final_val = score * modifier if score > threshold else score * 0.8
    adjusted_scores.append(final_val)

# Core logic hidden among distractors
best_segment = -1
max_productivity = 0
for i in range(len(adjusted_scores)):
    if adjusted_scores[i] > max_productivity:
        max_productivity = adjusted_scores[i]
        best_segment = i

# Simulate nutrient absorption efficiency based on position
efficiency_map = {i: (v % 7) / 10.0 for i, v in enumerate(climate_data)}
efficiency_correction = efficiency_map.get(best_segment, 0.5)

# Real answer depends on this critical assignment
raw_harvest = sum(adjusted_scores) * (1 - efficiency_correction)

# Unused alternate path
if raw_harvest < 300:
    alternative_plan = True
    contingency = raw_harvest * 1.2  # Dead code branch

# Final optimization step using irrelevant parameters too
def optimize_harvest(temp_list, moisture_list):
    total_exposure = sum(t * 0.3 + m * 0.7 for t, m in zip(temp_list, moisture_list))
    decay_offset = len(temp_list) * 0.05
    net_effect = total_exposure - decay_offset
    
    # This line determines the actual result
    return int(net_effect * 1.08)  # Final deterministic transformation

# Critical statement
final_yield = optimize_harvest(climate_data, soil_conditions)

# Print required output
print(f"Result: {final_yield}")