def analyze_risk_profile(inputs):
    # Irrelevant risk analysis (distractor)
    risk_score = sum([x ** 0.5 for x in inputs if x > 5])
    normalized = [round(x / max(inputs), 3) for x in inputs]
    return risk_score

# Simulate environmental exposure levels over time
exposure_levels = [x * 1.5 for x in range(8, 16)]
stress_factors = [abs((i - 4) * 1.2) for i in range(len(exposure_levels))]

# Dead code path - never executed but adds confusion
if len(stress_factors) < 5:
    stress_factors.append(999)

# Auxiliary calculation with misleading intermediate
baseline_shift = 0
for val in exposure_levels[:4]:
    baseline_shift += val * 0.1

# Destructuring assignment - relevant only partially
primary, secondary = exposure_levels[0], stress_factors[0]

# Complex list comprehension with filtering and transformation
adjusted_levels = [
    (exp * (1 + stress) - 2) 
    for exp, stress in zip(exposure_levels, stress_factors)
    if exp >= 10
]

# Set operation to remove potential duplicates (though unlikely)
filtered_adjusted = list(set(adjusted_levels))
sorted_adjusted = sorted(filtered_adjusted, reverse=True)

# Dummy function call that does nothing to final result
analyze_risk_profile(stress_factors)

# State-tracking variable with incremental updates
accumulated_loss = 0
for i, val in enumerate(sorted_adjusted):
    if i % 2 == 0:
        accumulated_loss += val * 0.05

# Core computation: simulate yield based on adjusted exposure
harvest_results = lambda exps, stresses: sum(
    [e * (0.8 - s * 0.1) for e, s in zip(exps, stresses) if e > 12]
)

# Key assignment point
final_yield = harvest_results(exposure_levels, stress_factors)

print(f"Result: {final_yield}")