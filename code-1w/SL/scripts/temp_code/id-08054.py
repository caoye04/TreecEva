def analyze_metrics(data):
    base_value = sum(data) / len(data)
    adjusted = [x * 1.1 for x in data if x > base_value]
    outlier_count = len([x for x in data if x < 5])
    return base_value, adjusted, outlier_count

raw_data = [12, 15, 8, 20, 3, 17, 5]

# Preliminary analysis (some values not directly used later)
mean_val, upshifted_data, anomalies = analyze_metrics(raw_data)

threshold = 10
activation = [x for x in raw_data if x > threshold]
buffer_zone = [x for x in raw_data if x <= threshold]

scaling_factor = len(activation) / (len(buffer_zone) + 1)

# Simulate conditional adjustments
correction = 0.0
counterfactual = []
for val in upshifted_data:
    if val > 15:
        correction += 0.5
    else:
        counterfactual.append(val * 0.9)

# Dummy tracking variables (distractors)
tracking_log = {'correction_applied': correction, 'ignored_entries': len(counterfactual)}
meta_adjustment = tracking_log['correction_applied'] * 2.0

# Core logic begins here
bonus = int(mean_val // 2)
penalty = len(anomalies) * 3  # anomalies is actually an integer, but misnamed earlier

# Misleading reassignment (dead code path)
temp_result = None
if len(counterfactual) > 5:
    temp_result = sum(counterfactual)
else:
    temp_result = bonus * 2  # This always executes but temp_result unused

# Key function with conditional expression
def compute_performance(base_bonus, deduction):
    multiplier = 2 if base_bonus >= 7 else 1.5
    return int((base_bonus * multiplier) - deduction + (meta_adjustment // 1))

final_score = compute_performance(bonus, penalty)
print(f"Target result: {final_score}")