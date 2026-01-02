def analyze_efficiency(metrics):
    base_efficiency = sum(metrics) / len(metrics)
    adjustment = lambda x: x ** 0.5 if x > 5 else x * 0.8
    return adjustment(base_efficiency)

metrics_data = [7, 6, 8, 9, 5]
raw_efficiency = analyze_efficiency(metrics_data)

# Distractor: Irrelevant transformation chain
temp_weights = [1.1, 0.9, 1.0, 1.2, 0.8]
scaled_metrics = [m * w for m, w in zip(metrics_data, temp_weights)]
avg_scaled = sum(scaled_metrics) / len(scaled_metrics)
adjusted_avg = avg_scaled * 0.95  # Dead computation path

# Real logic begins
productivity = raw_efficiency * 1.3
risk_factor = 0.0

if productivity > 7:
    risk_factor += 0.1
    secondary_check = [x for x in metrics_data if x >= 7]
    if len(secondary_check) >= 3:
        risk_factor += 0.05

# Misleading complex expression with no effect
dummy_calc = (lambda a, b: (a + b) // 2)(len(metrics_data), 10) % 3
dummy_state = {"flag": False, "count": dummy_calc}

# Core evaluation with semi-relevant string processing
evaluation_notes = "High performance recorded this quarter"
caps_count = sum(1 for c in evaluation_notes if c.isupper())
modifier = 0.1 if caps_count > 3 else 0.05

# Final scoring logic
def evaluate_performance(p, r):
    base = p * (1 - r)
    bonus = 2.0 if p >= 8 else (1.0 if p >= 7 else 0.0)
    # String-based condition affecting score
    words = evaluation_notes.split()
    if any(len(w) > 7 for w in words):
        bonus += modifier
    return int(base + bonus)

# Key assignment point
dummy_state["result"] = evaluate_performance(productivity, risk_factor)  # Red herring usage
final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")