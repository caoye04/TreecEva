def analyze_growth_cycle(data):
    total_cycles = len(data)
    growth_scores = []
    temp_offset = 0

    for i, entry in enumerate(data):
        base = entry['temp'] * entry['moisture']
        if entry['light'] > 50:
            base *= 1.2
        growth_scores.append(base + temp_offset)

    avg_score = sum(growth_scores) / len(growth_scores) if growth_scores else 0
    return avg_score


def calculate_harvest_efficiency(plots, conditions):
    efficiency_list = []
    penalty_factor = 0.9
    dummy_sum = 0

    for i, (plot, cond) in enumerate(zip(plots, conditions)):
        area = plot['size']
        soil_q = plot['soil_quality']
        temp = cond['temperature']
        moisture = cond['humidity']

        # Core calculation
        base_yield = area * soil_q * (temp / 20.0)
        if moisture < 40:
            base_yield *= 0.7
        elif moisture > 80:
            base_yield *= 0.85

        # Irrelevant accumulation (distractor)
        dummy_sum += i * 2

        # Conditional expression (required feature)
        adjustment = 1.1 if soil_q > 0.7 else 0.95
        adjusted_yield = base_yield * adjustment

        efficiency_list.append(adjusted_yield)

    # Final result computation
    final_yield = int(sum(efficiency_list) / len(efficiency_list)) if efficiency_list else 0

    # Extra unused computation (interference)
    outlier_count = sum(1 for y in efficiency_list if y < 50)
    consistency_check = outlier_count < 2

    return final_yield

# Input data
plots = [
    {'size': 10, 'soil_quality': 0.8},
    {'size': 15, 'soil_quality': 0.6},
    {'size': 12, 'soil_quality': 0.9},
    {'size': 8,  'soil_quality': 0.5}
]

conditions = [
    {'temperature': 25, 'humidity': 60},
    {'temperature': 18, 'humidity': 35},
    {'temperature': 22, 'humidity': 85},
    {'temperature': 20, 'humidity': 70}
]

# Analyze growth cycle (distractor call)
dummy_score = analyze_growth_cycle(conditions)

# Main computation
final_yield = calculate_harvest_efficiency(plots, conditions)

print(f"Result: {final_yield}")