def analyze_soil(ph_levels, moisture_data):
    avg_ph = sum(ph_levels) / len(ph_levels)
    avg_moisture = sum(moisture_data) / len(moisture_data)
    stability_score = 0
    for i in range(1, len(ph_levels)):
        stability_score += abs(ph_levels[i] - ph_levels[i-1])
    normalized_stability = stability_score / (len(ph_levels) - 1) if len(ph_levels) > 1 else 0
    return avg_ph, avg_moisture, normalized_stability


def calculate_growth_potential(base_yield, ph_factor, moisture_factor):
    adjustment = (ph_factor * 0.7 + moisture_factor * 0.3)
    potential = base_yield * adjustment
    return potential if potential > 0 else 0.1


def filter_productive_plots(plots):
    productive = []
    threshold = 85
    temp_sum = 0
    for plot in plots:
        temp_sum += plot['yield_estimate']
        if plot['yield_estimate'] >= threshold:
            productive.append(plot)
    average_estimate = temp_sum / len(plots) if plots else 0
    return productive, average_estimate


def optimize_harvest(plots):
    total_yield = 0
    efficiency_modifiers = []
    
    for plot in plots:
        size = plot['size_acres']
        ph_vals = plot['soil_ph_history']
        moisture_vals = plot['moisture_readings']
        
        # Irrelevant intermediate calculation (distractor)
        peak_moisture = max(moisture_vals) if moisture_vals else 0
        dry_spells = sum(1 for m in moisture_vals if m < 30)
        
        avg_ph, avg_moisture, stability = analyze_soil(ph_vals, moisture_vals)
        
        # Misleading computation that looks important but isn't used
        hypothetical_risk = (stability * 100) / (avg_ph + 1e-5)
        
        growth_factor = calculate_growth_potential(
            base_yield=plot['base_yield'],
            ph_factor=(7.0 / (abs(avg_ph - 6.5) + 1)),
            moisture_factor=(avg_moisture / 100)
        )
        
        expected_yield = size * growth_factor
        efficiency_modifiers.append(growth_factor)
        
        # Conditional expression (Python-specific feature)
        penalty = 0.2 if dry_spells > 2 else 0.05 if stability > 0.8 else 0
        adjusted_yield = expected_yield * (1 - penalty)
        
        total_yield += adjusted_yield
    
    # Final aggregation
    avg_efficiency = sum(efficiency_modifiers) / len(efficiency_modifiers) if efficiency_modifiers else 0
    
    # Red herring: unused complex sorting
    sorted_plots = sorted(plots, key=lambda x: x['base_yield'], reverse=True)
    cumulative_boost = 0
    for p in sorted_plots:
        if p['base_yield'] > 90:
            cumulative_boost += 0.05
    
    final_yield = int(total_yield * (1 + min(cumulative_boost, 0.2)))
    return final_yield

# Main execution
plots_data = [
    {
        'size_acres': 10,
        'base_yield': 95,
        'soil_ph_history': [6.4, 6.6, 6.5, 6.3, 6.7],
        'moisture_readings': [65, 70, 60, 55, 75, 50],
        'yield_estimate': 92
    },
    {
        'size_acres': 15,
        'base_yield': 88,
        'soil_ph_history': [6.8, 6.9, 6.7, 7.0, 6.8],
        'moisture_readings': [45, 50, 40, 35, 60],
        'yield_estimate': 87
    },
    {
        'size_acres': 8,
        'base_yield': 91,
        'soil_ph_history': [6.2, 6.1, 6.3, 6.0, 6.4],
        'moisture_readings': [70, 75, 68, 80, 72, 65, 60],
        'yield_estimate': 89
    }
]

productive_list, avg_est = filter_productive_plots(plots_data)
final_yield = optimize_harvest(plots_data)
print(f"Target result: {final_yield}")