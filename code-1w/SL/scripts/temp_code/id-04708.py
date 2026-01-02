from collections import defaultdict

# Simulate agricultural yield optimization under weather uncertainty
def calculate_base_yield(area, fertility):
    return area * (fertility + 0.5) * 0.8

def adjust_for_rainfall(base_yield, rainfall):
    if rainfall < 20:
        return base_yield * 0.6
    elif rainfall > 80:
        return base_yield * 0.75
    else:
        return base_yield

def apply_pest_control(yield_value, severity):
    reduction_factor = {1: 0.95, 2: 0.85, 3: 0.65}.get(severity, 1.0)
    return yield_value * reduction_factor

def simulate_growth_stress(base_yield, temperature_anomaly):
    stress_ratio = max(0, min(1, (temperature_anomaly - 2) / 10))
    return base_yield * (1 - stress_ratio)

def optimize_harvest(plot_data, forecast):
    total_yield = 0
    stress_tests = []
    temp_buffer = []

    # Misleading pre-computation (distractor)
    hypothetical_yields = defaultdict(float)
    for name, data in plot_data.items():
        area, fert = data['area'], data['fertility']
        base = calculate_base_yield(area, fert)
        hypothetical_yields[name] = base * 1.2  # Not used later

    # Core logic with nested conditions and distractors
    for name, data in plot_data.items():
        area = data['area']
        fertility = data['fertility']
        rainfall = forecast.get(name, {}).get('rain', 50)
        pest_level = forecast.get(name, {}).get('pests', 1)
        temp_dev = forecast.get(name, {}).get('temp_dev', 0)

        # Irrelevant intermediate tracking (distractor)
        if temp_dev > 5:
            temp_buffer.append(temp_dev * area)

        # Key computation chain
        yield_val = calculate_base_yield(area, fertility)
        yield_val = adjust_for_rainfall(yield_val, rainfall)
        
        # Simulate conditional treatment (semi-relevant path)
        treated_yield = apply_pest_control(yield_val, pest_level)
        if pest_level >= 2:
            yield_val = treated_yield  # Only applies sometimes

        # Additional environmental stress adjustment
        stressed_yield = simulate_growth_stress(yield_val, temp_dev)
        stress_tests.append(stressed_yield - yield_val)  # Logged but not critical

        total_yield += stressed_yield

    # Secondary processing with red herring variables
    avg_stress_impact = sum(stress_tests) / len(stress_tests) if stress_tests else 0
    buffer_sum = sum(temp_buffer)

    # Final adjustment using unused components (misdirection)
    adjustment_proxy = abs(avg_stress_impact) * 0.1 + buffer_sum * 0.01
    final_optimized = total_yield - adjustment_proxy  # Minor correction

    # Critical assignment point
    final_yield = int(round(final_optimized))

    # Extraneous post-processing (dead code path)
    outlier_count = 0
    for val in hypothetical_yields.values():
        if val > 500:
            outlier_count += 1

    return final_yield

# Input data
plots = {
    'north_field': {'area': 40, 'fertility': 6.2},
    'south_orchard': {'area': 25, 'fertility': 7.0},
    'east_meadow': {'area': 30, 'fertility': 5.8},
    'west_paddock': {'area': 35, 'fertility': 6.5}
}

forecast = {
    'north_field': {'rain': 75, 'pests': 2, 'temp_dev': 3},
    'south_orchard': {'rain': 85, 'pests': 1, 'temp_dev': 1},
    'east_meadow': {'rain': 60, 'pests': 3, 'temp_dev': 6},
    'west_paddock': {'rain': 45, 'pests': 2, 'temp_dev': 2}
}

# Execution point
final_yield = optimize_harvest(plots, forecast)
print(f"Result: {final_yield}")