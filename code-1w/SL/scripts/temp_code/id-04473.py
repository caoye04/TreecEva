def analyze_growth_pattern(sequence):
    """ Misleading helper: analyzes string patterns but not used in final calculation. """
    if not sequence:
        return 0
    count = 0
    for char in sequence:
        if char.lower() in 'aeiou':
            count += 1
    return count

# Simulated agricultural field data
temp_readings = [22, 25, 19, 30, 27]
humidity_levels = {"morning": 65, "afternoon": 45, "night": 80}
field_data = [
    {"soil_ph": 6.5, "temp": 25, "yield_potential": 800},
    {"soil_ph": 5.8, "temp": 27, "yield_potential": 700},
    {"soil_ph": 6.2, "temp": 24, "yield_potential": 850}
]

# Configuration with red herring parameters
config = {
    "optimal_ph_range": (5.5, 6.5),
    "growth_factor": 1.08,
    "decay_threshold": 7,
    "bonus_multiplier": 1.2,
    "legacy_mode": False,
    "debug_level": 99
}

# Distractor variables - unused in core logic
baseline_score = sum(temp_readings) / len(temp_readings)
seasonal_adjustment = humidity_levels["afternoon"] * 0.3
placeholder_result = analyze_growth_pattern("Photosynthesis")
intermediate_flag = False

# Core state tracking
active_fields = 0
yield_accumulator = 0
penalty_deduction = 0

for entry in field_data:
    # Primary condition: check soil pH within optimal range
    if config["optimal_ph_range"][0] <= entry["soil_ph"] <= config["optimal_ph_range"][1]:
        yield_accumulator += entry["yield_potential"]
        active_fields += 1
    else:
        # Apply decay penalty for suboptimal pH
        penalty_deduction += entry["yield_potential"] * 0.15

# Secondary adjustment based on temperature consistency
temp_variance = max(temp_readings) - min(temp_readings)
if temp_variance > 10:
    yield_accumulator *= 0.9  # 10% reduction for high variance

# Tuple unpacking - relevant operation
base_yield, modifiers = yield_accumulator, []

# Simulate recursive depth adjustment (simple recursion)
def adjust_for_elevation(yield_val, depth=2):
    if depth <= 0:
        return yield_val
    return adjust_for_elevation(yield_val * 1.02, depth - 1)

adjusted_yield = adjust_for_elevation(base_yield)

# Final efficiency calculation
if active_fields >= 2:
    modifiers.append(config["bonus_multiplier"])

final_multiplier = 1.0
for mod in modifiers:
    final_multiplier *= mod

final_yield = int((adjusted_yield - penalty_deduction) * final_multiplier)

# Dead code path - never executed but adds distraction
if config["legacy_mode"]:
    fallback = {"result": 0, "status": "inactive"}
    final_yield = fallback["result"]

# Print result as required
print(f"Result: {final_yield}")