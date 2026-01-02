def analyze_efficiency(values):
    filtered = [v for v in values if v > 0]
    weighted = sum([filtered[i] * (i + 1) for i in range(len(filtered))])
    return weighted // len(filtered) if filtered else 0

productivity = [85, 90, -5, 75, 0, 80]
overhead = [3, 1, 4, 1, 5]
dummy_calc = sum(x ** 2 for x in overhead)  # Distractor

# Simulate system load impact on performance
load_factors = {1: 0.95, 2: 0.88, 3: 0.91, 4: 0.85, 5: 0.82}
system_load = len(overhead)
adjusted_productivity = [p * load_factors.get(i % 5 + 1, 1.0) for i, p in enumerate(productivity)]

# Hidden normalization step
normalized = set(int(p // 5 * 5) for p in adjusted_productivity)  # Round down to nearest 5
baseline = sum(normalized) / len(normalized)

# Risk assessment based on variance
variance_proxy = sum((p - baseline) ** 2 for p in adjusted_productivity) / len(adjusted_productivity)
risk_factor = 1.0 if variance_proxy < 100 else 1.15

aux_data = [10, 20, 30]
aux_sum = sum(aux_data)  # Irrelevant computation

intermediate_result = analyze_efficiency(adjusted_productivity)

# Core evaluation logic
if risk_factor > 1.1:
    final_score = int(intermediate_result * 0.85)
else:
    final_score = int(intermediate_result * 1.1) - 5

# Additional red herring: unused function
def debug_state():
    return {"status": "ok", "code": 200}

# Unused list comprehension with side-effect-free operations
_ = [x * x for x in range(5) if x % 2 == 0]

Result: final_score