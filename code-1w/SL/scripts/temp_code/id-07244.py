def calculate_harvest_yield(climate_data):
    # Irrelevant transformation (distractor)
    normalized_data = {k: v * 1.05 for k, v in climate_data.items() if v > 0}

    # Semi-relevant preprocessing
    filtered_readings = [val for val in climate_data.values() if 10 <= val <= 40]
    adjustment_factor = 0.85 if len(filtered_readings) > 3 else 1.1

    # Misleading intermediate calculation (not used in final result)
    outlier_count = sum(1 for v in climate_data.values() if v < 5 or v > 50)
    dummy_score = outlier_count * 10 + 5

    # Core logic begins
    base_yield = 0
    for temp in climate_data.values():
        if temp < 15:
            base_yield += 2
        elif 15 <= temp <= 35:
            base_yield += 5
        else:
            base_yield += 3

    # Use of lambda for dynamic threshold (relevant)
    quality_boost = (lambda x: x * 0.2 if x > 4 else x * 0.1)(base_yield)

    # Conditional expression affecting final yield
    stress_penalty = 7 if any(v > 45 for v in climate_data.values()) else 0

    # Destructuring assignment (tuple unpacking) - relevant
    (min_val, max_val) = (min(climate_data.values()), max(climate_data.values()))
    range_bonus = 10 if max_val - min_val < 20 else 4

    # Final composition with distractors present but not dominating
    final_yield = base_yield + quality_boost - stress_penalty + range_bonus

    return final_yield

# Simulated sensor data from agricultural zones (realistic context)
climate_data = {
    "zone_A": 18,
    "zone_B": 33,
    "zone_C": 12,
    "zone_D": 41,
    "zone_E": 25,
    "zone_F": 19
}

# Extraneous unused variable (dead code path - distractor)
baseline_projection = sum(climate_data.values()) / len(climate_data)

# Key execution point
final_yield = calculate_harvest_yield(climate_data)

# Output result as required
print(f"Result: {final_yield}")