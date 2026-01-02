import math

# Simulate a scientific data processing pipeline with intermediate scoring

def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if x > 0]
    normalized = [math.log(val) for val in filtered]
    return [round(n, 3) for n in normalized]

# Irrelevant helper: computes variance but not used in final path
def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Core processing function with distractors
def calculate_ranking(dataset):
    base_weight = 0.85
    penalty_factor = 0.92
    bonus_threshold = 2.0

    # Misleading intermediate calculation (not affecting final logic)
    shadow_score = sum([d ** 0.5 for d in dataset if d < 1.5]) * 0.1

    # Actual scoring logic
    significant_entries = list(filter(lambda x: x > bonus_threshold, dataset))
    bonus_points = len(significant_entries) * 3

    base_score = sum(dataset) * base_weight
    adjustment = 0
    for val in dataset:
        if val > 1.0:
            adjustment += 0.5
        elif val <= 0.5:
            adjustment -= 0.2

    # Another red herring: calculated but unused
    outlier_count = len([v for v in dataset if v > 3.0])
    temp_correction = outlier_count * -0.7 if outlier_count > 2 else 0

    final_rank = base_score + adjustment + bonus_points
    return round(final_rank, 2)

# Entry point data
sensor_data = [0.1, 1.2, 2.3, 0.5, 3.1, 2.7, 0.9, 4.4, 1.8, 2.9]
processed_data = preprocess_readings(sensor_data)

# Unused but plausible computation to increase cognitive load
data_mean = sum(processed_data) / len(processed_data)
dispersion_metric = max(processed_data) - min(processed_data)

# Key statement
final_score = calculate_ranking(processed_data)

print(f"Result: {final_score}")