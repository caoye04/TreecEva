def analyze_efficiency(values):
    adjusted = [v * 1.1 for v in values if v > 50]
    return sum(adjusted) // len(adjusted) if adjusted else 0

productivity = [85, 90, 78, 65, 45, 92]

# Simulate team performance metrics with distractors
team_size = 6
temp_multiplier = 1.05
dummy_calc = [x * temp_multiplier for x in productivity]
dummy_total = sum(dummy_calc)

baseline = sum(productivity) / len(productivity)
device_count = 3

# Red herring: irrelevant hardware simulation
sensor_readings = [device_count * 2 + i for i in range(4)]
hardware_offset = max(sensor_readings) - min(sensor_readings)

# Risk assessment based on volatility
volatility = [abs(productivity[i] - productivity[i-1]) for i in range(1, len(productivity))]
avg_volatility = sum(volatility) / len(volatility)
risk_factor = 1 if avg_volatility < 15 else 1.2

# Efficiency bonus calculation (unused distractor)
efficiency_bonus = analyze_efficiency(productivity)
scale_factor = 0.9  # Unused scaling hint

# Core logic: performance evaluation with conditional adjustment
def evaluate_performance(perf_list, risk):
    base_score = sum(p ** 0.5 for p in perf_list)  # Emphasis on balanced high performance
    penalty = 0
    for val in perf_list:
        if val < 70:
            penalty += 5
    adjusted_score = base_score - penalty
    if risk == 1.2:
        adjusted_score *= 0.95
    return round(adjusted_score)

intermediate_result = evaluate_performance(productivity, 1)  # Distractor call

# Key execution point
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")