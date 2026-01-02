def analyze_efficiency(metrics):
    efficiency = sum(metrics) / len(metrics)
    adjusted = efficiency * 0.9
    return adjusted

metrics_data = [85, 90, 78, 92, 88]
baseline = 80

# Irrelevant computation - distractor
shadow_metrics = [m * 1.05 for m in metrics_data]
temporary_sum = sum(shadow_metrics)

efficiency_score = analyze_efficiency(metrics_data)

# Risk assessment using set operations
critical_thresholds = {75, 80, 85, 90}
met_thresholds = {m for m in metrics_data if m >= 80}
risk_factor = len(critical_thresholds - met_thresholds) + 2

productivity = efficiency_score + 5

# Lambda-based transformation - not directly used but plausible
transform = lambda x: x ** 1.1
augmented_productivity = transform(productivity)

# Dead code path - misleading
if False:
    productivity *= 0.8
    risk_factor += 10

# Core logic embedded in distraction
def evaluate_performance(prod, risk):
    if prod > baseline:
        return prod - (risk * 1.5)
    else:
        return prod + risk

final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")