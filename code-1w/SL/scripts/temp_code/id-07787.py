def analyze_productivity(hours_logged, efficiency_factor):
    base_output = sum([h * 0.8 for h in hours_logged if h > 0])
    penalty = 0
    if len(hours_logged) > 5:
        underperforming_days = [h for h in hours_logged if h < 6]
        penalty = len(underperforming_days) * 0.5
    adjusted_output = max(base_output - penalty, 0)
    return adjusted_output * efficiency_factor

hours_data = [8, 7.5, 5, 9, 4.5, 6.5, 8]
efficiency = 1.2
temporary_result = analyze_productivity(hours_data, efficiency)

# Irrelevant computation block (distractor)
redundant_calc = 0
for i in range(3):
    redundant_calc += i ** 3
snapshot_log = f"Checkpoint at {redundant_calc} units"

# Core assessment data
assessments = {
    'planning': 85,
    'execution': 92,
    'review': 78,
    'adaptability': 88,
    'collaboration': 90
}

weights = {
    'planning': 0.2,
    'execution': 0.3,
    'review': 0.15,
    'adaptability': 0.25,
    'collaboration': 0.1
}

# Auxiliary function with minor side path
def validate_assessment_range(values):
    out_of_bounds = []
    for k, v in values.items():
        if v < 0 or v > 100:
            out_of_bounds.append(k)
    return len(out_of_bounds) == 0

is_valid = validate_assessment_range(assessments)

# Actual aggregation logic
weighted_total = 0
for key in assessments:
    if key in weights:
        weighted_total += assessments[key] * weights[key]

# Secondary adjustment based on productivity proxy
temp_adjustment = temporary_result / 10.0
final_score = int(weighted_total + min(temp_adjustment, 5))

# Dead code path (distractor)
if final_score > 100:
    final_score = 100

# Output result
print(f"Result: {final_score}")