def analyze_growth_conditions(temp_list, hum_list):
    growth_score = 0
    penalty = 0
    bonus = 0
    temp_adjustments = []
    hum_adjustments = []

    for i, (t, h) in enumerate(zip(temp_list, hum_list)):
        if t < 20 or t > 35:
            penalty += 5
            temp_adjustments.append((i, t))
        else:
            growth_score += 3

        if h < 40 or h > 80:
            penalty += 3
            hum_adjustments.append((i, h))
        else:
            bonus += 2

        # Irrelevant computation: tracking adjustment counts even if unused
        if len(temp_adjustments) > len(hum_adjustments):
            bonus -= 1

    # Dead code path: never executed due to logic, but looks relevant
    if penalty > 100:
        growth_score = max(0, growth_score - 10)

    return growth_score, bonus, penalty


def calculate_optimal_yield(temps, hums):
    score, extra_bonus, deductions = analyze_growth_conditions(temps, hums)
    
    # Secondary processing with some red herring variables
    efficiency_map = {i: val * 0.1 for i, val in enumerate(temps)}
    stability_index = 0
    fluctuation_count = 0
    
    for i in range(1, len(temps)):
        diff = abs(temps[i] - temps[i-1])
        if diff > 5:
            fluctuation_count += 1
            stability_index -= diff * 0.5
        else:
            stability_index += 1
    
    # Another distraction: complex string-based state tracking
    state_log = ""
    for t, h in zip(temps, hums):
        if t > 30 and h < 50:
            state_log += 'X'
        elif t < 25 and h > 70:
            state_log += 'Y'
        else:
            state_log += 'Z'
    
    # Core yield formula – depends only on score, extra_bonus, and stability_index
    base_yield = score * 10 + extra_bonus * 5
    adjusted_yield = base_yield + stability_index
    
    # Final irrelevant scaling
    if 'XX' in state_log:
        adjusted_yield *= 0.95

    final_yield = int(adjusted_yield)
    return final_yield

# Input data
temperature_data = [22, 25, 31, 19, 27, 33, 24]
humidity_data = [60, 85, 45, 30, 70, 88, 75]

# Execution point
final_yield = calculate_optimal_yield(temperature_data, humidity_data)
print(f"Target result: {final_yield}")