def analyze_efficiency(metrics):
    base = sum(metrics) / len(metrics)
    adjustment = (lambda x: x ** 0.5 if x > 20 else x / 4)(base)
    return base + adjustment

productivity = [85, 90, 78, 92, 88]
overhead = [12, 15, 10, 18, 14]

# Irrelevant transformation (distractor)
decoy_metrics = [x * 1.5 for x in overhead if x > 12]

risk_factor = 0
for i, val in enumerate(productivity):
    if val >= 85:
        risk_factor += 0.1
    elif val < 80:
        risk_factor -= 0.05

    # Nested logic with partial relevance
    temp_flag = (val > 80) and (i % 2 == 0)
    if temp_flag:
        risk_factor += 0.02

# Case conversion as red herring
diagnostic_mode = "ACTIVE"
diagnostic_code = diagnostic_mode.lower() == "active"

# Unused helper function (dead code path)
def normalize_data(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Simulated auxiliary calculation (semi-relevant)
calibration = 0
for m in productivity:
    calibration += m % 10

calibration = calibration / len(productivity)

# Core evaluation logic
adjusted_productivity = analyze_efficiency(productivity)

# Misleading intermediate variables
baseline_threshold = 80
penalty_rate = 0.03

# Key computation chain
if adjusted_productivity > 85:
    performance_bonus = 5
else:
    performance_bonus = 2

# Final scoring with lambda integration
evaluate_performance = lambda prod, risk: int((prod / 10) - (risk * 100) + performance_bonus)

prod_index = adjusted_productivity
final_score = evaluate_performance(prod_index, risk_factor)

# Print result as required
print(f"Result: {final_score}")