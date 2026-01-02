def analyze_efficiency(output, overhead):
    efficiency = (output - overhead) / (output + 1)
    adjusted_efficiency = efficiency * 0.9 if efficiency > 0.7 else efficiency * 1.1
    return adjusted_efficiency

output_volume = 450
overhead_cost = 80
efficiency_metric = analyze_efficiency(output_volume, overhead_cost)

productivity = efficiency_metric * output_volume

# Simulate risk adjustment based on volatility index
dummy_tracker = [i**2 for i in range(5)]  # Irrelevant computation
baseline_risk = 100
volatility_index = 2.3
risk_factor = baseline_risk / (volatility_index + 0.7)
risk_factor += sum({1, 2, 3}.intersection({2, 3, 4}))  # Semi-relevant: adds 5

# Distractor block: dead logic path
if False:
    phantom_value = 999
    temp_result = phantom_value * 2

# Core evaluation with conditional expression and set usage
def evaluate_performance(prod, risk):
    base_score = prod / 10
    penalty = 15 if risk > 50 else 5
    # Additional irrelevant intermediate calculation
    shadow_buffer = [x for x in range(3)]
    offset = len(shadow_buffer)  # Always 3, but adds noise
    final = base_score - penalty + offset
    return final

intermediate_debug = efficiency_metric * 2  # Unused debugging remnant

final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")