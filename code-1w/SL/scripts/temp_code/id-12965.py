def analyze_efficiency(output, overhead):
    if output <= 0:
        return 0
    efficiency = (output - overhead) / output
    return efficiency if efficiency > 0 else 0

productivity = 85
risk_factor = 0.6
overhead_cost = 12
baseline = 50

# Distractor: unused variables and computations
phantom_load = 3 * baseline % 7
shadow_metric = (productivity + 4) ** 0.5

temp_diagnostic = 0
if productivity > 80:
    temp_diagnostic += 10
    for i in range(2):
        temp_diagnostic -= i

# Semi-relevant transformation
adjusted_productivity = productivity - overhead_cost if overhead_cost < 15 else productivity * 0.8

# Nested logic with conditional expression
stress_test = adjusted_productivity < 70
risk_factor = risk_factor * 1.2 if stress_test else risk_factor

# Core evaluation function
performance_index = 0
if adjusted_productivity >= 75:
    performance_index = 90
elif adjusted_productivity >= 65:
    performance_index = 70 + int(analyze_efficiency(adjusted_productivity, overhead_cost)) * 5
else:
    performance_index = 50

# Secondary adjustment based on risk
safety_buffer = 10 if risk_factor < 0.7 else 0

# Final score computation
final_score = performance_index + safety_buffer

# Print result as required
print(f"Target result: {final_score}")