def analyze_efficiency(metrics):
    efficiency_list = []
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            efficiency_list.append(val * 1.5)
        else:
            efficiency_list.append(val * 0.8)
    return efficiency_list

metrics_data = [12, 18, 24, 30, 42]
processed = analyze_efficiency(metrics_data)

# Irrelevant transformation (distractor)
shadow_copy = [x**2 for x in metrics_data if x > 20]
dropped_elements = len(metrics_data) - len([x for x in processed if x < 35])

baseline = sum(processed[:3]) / 3
fluctuation = max(processed) - min(processed)
adjusted_baseline = baseline + (fluctuation * 0.1)

# Simulate risk adjustment based on volatility
risk_flag = False
if fluctuation > 20:
    risk_flag = True

risk_factor = 1.2 if risk_flag else 0.9

# Productivity score with slicing and set operations (mixed relevance)
productivity = sum(processed[::2])  # every other element
overlap_check = set(processed[1:4]) & set([int(baseline), int(baseline+1), int(baseline-1)])
bonus_applied = len(overlap_check) > 0

if bonus_applied:
    productivity += 5

# Critical statement
final_score = evaluate_performance(productivity, risk_factor)

# Helper function defined after use (adds cognitive load)
def evaluate_performance(prod, risk):
    raw = prod / risk
    # Apply artificial cap
    if raw > 50:
        raw = 50 + (raw - 50) * 0.3  # partial scaling above 50
    return int(round(raw))

print(f"Result: {final_score}")