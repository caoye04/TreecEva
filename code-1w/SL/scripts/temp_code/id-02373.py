from itertools import combinations

# Simulate sensor readings and validation checks
sensor_data = [12, 15, 10, 8, 20, 14]
threshold = 12
min_readings = 3

def validate_stability(data, t, min_count):
    above_threshold = [x for x in data if x > t]
    if len(above_threshold) < min_count:
        return False
    # Check variance among top readings
    top_three = sorted(above_threshold, reverse=True)[:3]
    variance = sum((x - sum(top_three)/3)**2 for x in top_three) / 3
    return variance < 15

def calculate_baseline_adjustment(data):
    # Irrelevant computation: simulates calibration drift
    total_drift = sum(x * 0.01 for x in data)
    adjustment = len(data) * 0.5 if total_drift > 0.5 else 0
    return adjustment

def compute_reliability_factor(data):
    # Useful: computes consistency using pairwise differences
    diffs = [abs(a - b) for a, b in combinations(data, 2)]
    avg_diff = sum(diffs) / len(diffs)
    return 100 / (1 + avg_diff)  # Higher score for lower variation

def adjust_for_outliers(data):
    # Semi-relevant: removes extreme values but not used in final path
    if len(data) < 5:
        return data
    sorted_data = sorted(data)
    return sorted_data[1:-1]  # Trim min and max

# Misleading intermediate calculations
raw_total = sum(sensor_data)
reading_count = len(sensor_data)
dummy_metric = raw_total * reading_count // (threshold + 1) if threshold else 0

# State tracking with red herring
system_state = 'nominal'
if raw_total > 70:
    system_state = 'elevated'
    temp_offset = 2.5
    dummy_metric += int(temp_offset)

# Actual logic begins here
stable = validate_stability(sensor_data, threshold, min_readings)
reliability = compute_reliability_factor(sensor_data)

# Conditional expression used meaningfully
baseline_adj = calculate_baseline_adjustment(sensor_data)
adjusted_reliability = reliability * 1.1 if stable else reliability * 0.9

# Final performance score calculation
base_score = 50
stability_bonus = 20 if stable else -10
efficiency_weight = 0.7 if len(sensor_data) % 2 == 0 else 1.0

# Key statement
final_score = int(base_score + stability_bonus + adjusted_reliability * efficiency_weight + baseline_adj)

# Dead code path - never executed but looks relevant
if system_state == 'critical':
    final_score -= 100

# Output result as required
print(f"Result: {final_score}")