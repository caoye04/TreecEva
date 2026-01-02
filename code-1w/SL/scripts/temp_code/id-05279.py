def calculate_optimal_yield(parcel, model_func):
    base_area = len(parcel['plots'])
    shade_coverage = sum(1 for p in parcel['plots'] if p['exposure'] == 'shaded')
    premium_count = 0

    # Irrelevant computation: tracking soil pH (not used in final yield)
    avg_ph = sum(p['soil_ph'] for p in parcel['plots']) / base_area
    ph_warning_flag = avg_ph < 5.5 or avg_ph > 7.0

    # Semi-relevant transformation: adjust plot efficiency using model
    efficiencies = []
    for plot in parcel['plots']:
        base_eff = plot['fertility'] * 0.3 + plot['moisture'] * 0.7
        if plot['exposure'] == 'sunny':
            base_eff *= 1.2
        elif plot['exposure'] == 'shaded':
            base_eff *= 0.8
        efficiencies.append(round(base_eff, 3))

    # Apply growth model (lambda function usage)
    sorted_efficiencies = sorted(efficiencies, reverse=True)
    top_performers = sorted_efficiencies[:len(sorted_efficiencies)//2 or 1]

    # Distractor: unused helper logic for future expansion
    def estimate_pest_risk():
        return len([e for e in efficiencies if e < 0.4]) * 0.1

    # Actual yield calculation
    raw_yield = sum(model_func(eff) for eff in top_performers)

    # Bonus for premium plots (plots with high fertility and moisture)
    for plot in parcel['plots']:
        if plot['fertility'] > 0.8 and plot['moisture'] > 0.8:
            premium_count += 1

    bonus_multiplier = 1 + (premium_count * 0.05)

    # Final adjustment using slicing to exclude worst 10% of top half (if enough data)
    if len(top_performers) > 3:
        trimmed = top_performers[:int(-len(top_performers)*0.1) or len(top_performers)]
        adjusted_yield = sum(trimmed) * bonus_multiplier
    else:
        adjusted_yield = raw_yield * bonus_multiplier

    # Red herring: unused cost calculation
    operational_cost = base_area * 120
    maintenance_factor = 0.95 ** len(parcel.get('upgrades', []))

    final_yield = int(adjusted_yield * 100)  # Scale for reporting
    return final_yield


def growth_model(x):
    return x ** 2 + 0.1 * x

# Simulated land data
land_parcel = {
    'plots': [
        {'fertility': 0.92, 'moisture': 0.85, 'exposure': 'sunny', 'soil_ph': 6.2},
        {'fertility': 0.45, 'moisture': 0.30, 'exposure': 'shaded', 'soil_ph': 4.8},
        {'fertility': 0.88, 'moisture': 0.90, 'exposure': 'sunny', 'soil_ph': 6.8},
        {'fertility': 0.70, 'moisture': 0.65, 'exposure': 'partial', 'soil_ph': 5.9},
        {'fertility': 0.30, 'moisture': 0.25, 'exposure': 'shaded', 'soil_ph': 4.5},
        {'fertility': 0.90, 'moisture': 0.88, 'exposure': 'sunny', 'soil_ph': 7.1}
    ],
    'upgrades': ['irrigation', 'fencing']
}

# Key execution point
final_yield = calculate_optimal_yield(land_parcel, growth_model)
print(f"Result: {final_yield}")