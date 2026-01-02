def analyze_soil(ph_levels):
    adjusted = []
    for ph in ph_levels:
        if ph < 5.5:
            adjusted.append(ph + 0.8)
        elif ph > 7.0:
            adjusted.append(ph - 0.5)
        else:
            adjusted.append(ph)
    return adjusted

ph_data = [4.2, 5.8, 7.3, 6.1, 4.9]

# Irrelevant transformation - distractor
transformed_ph = [round(p * 1.05, 2) for p in ph_data]

soil_status = ['acidic' if p < 5.5 else 'alkaline' if p > 7.0 else 'neutral' for p in analyze_soil(ph_data)]

# Simulate rainfall impact - partially relevant but not used directly
rainfall_mm = [80, 120, 95, 110, 70]
rain_effect = [r / 100 for r in rainfall_mm]

# Core data structure: agricultural plots with yield factors
plots = [
    {'base': 120, 'adj': 1.1, 'bonus': 0},
    {'base': 95, 'adj': 0.95, 'bonus': 10},
    {'base': 130, 'adj': 1.2, 'bonus': 0},
    {'base': 110, 'adj': 1.05, 'bonus': 5},
    {'base': 85, 'adj': 0.88, 'bonus': 15}
]

# Misleading calculation - looks important but unused
theoretical_max = sum(p['base'] for p in plots) * 1.3

# Helper function to compute effective yield
def calculate_harvest(plot_list):
    total = 0
    for i, p in enumerate(plot_list):
        # Apply adjustment and conditional bonus
        adjusted_base = p['base'] * p['adj']
        # Conditional expression: extra boost if base is above threshold
        bonus_applied = p['bonus'] * 2 if p['base'] >= 110 else p['bonus']
        total += adjusted_base + bonus_applied
    return int(total)

# Secondary distractor: sorting that isn't used
sorted_plots = sorted(plots, key=lambda x: x['base'], reverse=True)

# Critical execution point
final_yield = calculate_harvest(plots)

# Output result as required
print(f"Result: {final_yield}")