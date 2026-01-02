def analyze_efficiency(metrics):
    efficiency_list = [m * 1.5 for m in metrics if m > 20]
    adjusted = sum(efficiency_list) / len(efficiency_list) if efficiency_list else 0
    return round(adjusted, 2)

productivity = [85, 90, 78, 92, 88]
safety_records = [1, 0, 1, 1, 0]
days_off = 3

# Irrelevant aggregation
total_attendance = len(productivity) * 8 - days_off * 8
hourly_output = [p / 8 for p in productivity]

baseline = 80
exceeds_baseline = [p for p in productivity if p > baseline]

# Distractor: unused risk computation
temp_risk = sum(1 for s in safety_records if s == 0)
risk_factor = temp_risk * 5 if temp_risk > 0 else 0

# Semi-relevant normalization
normalized_productivity = [round(p * 0.95, 1) for p in productivity]

# Conditional adjustment based on performance spread
if max(normalized_productivity) - min(normalized_productivity) < 15:
    normalized_productivity = [p + 2 for p in normalized_productivity]

# Key state tracking
performance_set = set(round(p, 0) for p in normalized_productivity)
ideal_set = {80, 85, 90}
coverage_ratio = len(performance_set.intersection(ideal_set)) / len(ideal_set)

# Another distractor: string-based encoding of status
status_codes = ['A', 'B', 'C']
code_map = {i: status_codes[min(i // 30, 2)] for i in productivity}
summary_string = ''.join(code_map.values())
encoded_length = len(summary_string.replace('A', ''))

# Core logic disguised among other operations
def evaluate_performance(prod, risk):
    avg_prod = sum(prod) / len(prod)
    penalty = risk * 1.5
    base_score = avg_prod * 1.1
    if avg_prod >= 85:
        base_score += 10
    elif avg_prod >= 75:
        base_score += 5
    # Apply risk penalty only if risk exceeds threshold
    if risk > 3:
        base_score -= penalty
    return int(base_score)

# Critical execution point
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")