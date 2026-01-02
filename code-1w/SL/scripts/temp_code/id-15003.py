from collections import defaultdict

# Simulate agricultural plot data with growth cycles
def simulate_growth_cycles(season_data):
    growth_trend = defaultdict(int)
    noise_offset = 0
    temp_accumulator = 0

    for week, values in season_data.items():
        weekly_total = sum(values)
        growth_trend[week] = weekly_total * 0.85  # Apply efficiency factor

        # Irrelevant noise tracking (distractor)
        noise_offset += (weekly_total % 7)
        temp_accumulator += noise_offset % 4

    return growth_trend

# Analyze soil nutrient balance (semi-relevant preprocessing)
def analyze_nutrient_balance(nutrients):
    balance_score = 0
    excess_tracker = 0

    for nutrient, level in nutrients.items():
        if level > 50:
            excess_tracker += 1
        balance_score += max(0, 100 - level)  # Inverse weighting

    # Dead computation: not used later
    final_warning = "Stable" if excess_tracker < 3 else "Unbalanced"

    return balance_score

# Core function to compute harvest efficiency
def calculate_harvest_efficiency(plots, threshold):
    efficiency_log = []
    cumulative_index = 0
    penalty_counter = 0

    for plot_id, data in plots.items():
        base_yield = sum(data['cycles'])
        size_factor = data['size']

        # Compute effective yield with size scaling
        effective_yield = base_yield * (size_factor / 10.0)

        # Apply conditional bonus or penalty
        if base_yield > threshold:
            bonus = (base_yield * 0.1) if size_factor > 8 else 0
            effective_yield += bonus
        else:
            penalty_counter += 1
            effective_yield *= 0.9  # 10% penalty

        efficiency_log.append(effective_yield)

        # Tracking unused metric (distractor)
        cumulative_index += int(effective_yield % 5)

    # Final adjustment based on statistical spread
    mean_yield = sum(efficiency_log) / len(efficiency_log)
    variance_proxy = sum((y - mean_yield) ** 2 for y in efficiency_log) / len(efficiency_log)
    stability_bonus = 10 * (variance_proxy < 200)  # Binary bonus for low variance

    final_yield = int(mean_yield + stability_bonus)

    # Extra red herring: slicing irrelevant portion
    sorted_yields = sorted(efficiency_log)
    mid_section = sorted_yields[1:-1]  # Unused slice
    avg_mid = sum(mid_section) / len(mid_section) if mid_section else 0

    return final_yield

# Main execution
if __name__ == "__main__":
    # Input data: agricultural plots
    plots = {
        'p1': {'cycles': [120, 135, 110, 145], 'size': 9},
        'p2': {'cycles': [95, 105, 90, 115], 'size': 12},
        'p3': {'cycles': [160, 155, 170, 165], 'size': 7},
        'p4': {'cycles': [80, 85, 75, 90], 'size': 10}
    }

    nutrients = {
        'nitrogen': 58, 'phosphorus': 45, 'potassium': 62, 'calcium': 33
    }

    threshold = 400

    # Preprocessing steps with side effects (some irrelevant)
    season_data = {
        'week1': [120, 95], 'week2': [135, 105], 'week3': [110, 90], 'week4': [145, 115]
    }
    growth_trend = simulate_growth_cycles(season_data)
    nutrient_score = analyze_nutrient_balance(nutrients)

    # Key statement
    final_yield = calculate_harvest_efficiency(plots, threshold)

    print(f"Result: {final_yield}")