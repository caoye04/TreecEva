import itertools

def analyze_soil_quality(plots):
    # Irrelevant analysis that computes unused metrics
    ph_levels = [plot['ph'] for plot in plots]
    avg_ph = sum(ph_levels) / len(ph_levels)
    variance = sum((p - avg_ph) ** 2 for p in ph_levels) / len(ph_levels)
    return avg_ph  # Not actually used later

def simulate_growth_cycles(plot, rain):
    # Simulate crop yield over multiple growth cycles with diminishing returns
    base_yield = plot['fertility'] * 10
    stress_factor = 0.0
    peak_yield = 0
    
    # Distractor loop: simulates cycles but only last cycle matters
    for cycle in range(1, 4):
        if rain < 30:
            stress_factor += 0.2
        elif rain > 80:
            stress_factor += 0.15
        else:
            stress_factor = max(0.0, stress_factor - 0.1)
        
        current_yield = base_yield * (0.95 ** cycle) * (1 - stress_factor)
        if current_yield > peak_yield:
            peak_yield = current_yield
    
    return current_yield  # Only final cycle returned

def compute_optimal_harvest(plots, rainfall):
    total_yield = 0.0
    bonus_applied = False
    
    # Real computation: accumulate yields based on rainfall
    for plot in plots:
        if plot['crop_type'] == 'wheat' and rainfall > 50:
            raw_yield = simulate_growth_cycles(plot, rainfall)
            total_yield += raw_yield
        elif plot['crop_type'] == 'corn' and rainfall >= 40:
            raw_yield = simulate_growth_cycles(plot, rainfall)
            if raw_yield > 75 and not bonus_applied:
                total_yield += raw_yield * 1.1  # 10% bonus once
                bonus_applied = True
            else:
                total_yield += raw_yield
    
    # Red herring: complex grouping with itertools that does nothing
    grouped = itertools.groupby(plots, key=lambda x: x['crop_type'])
    group_count = sum(1 for _, g in grouped)  # Unused
    
    adjustment_factor = 0.98  # Minor correction
    final_yield = total_yield * adjustment_factor
    
    # Dead code path - never executed due to logic above
    if len(plots) > 100:
        final_yield = max(final_yield, 50)
        
    return final_yield

# Main execution
plots = [
    {'fertility': 7.2, 'crop_type': 'wheat', 'ph': 6.5},
    {'fertility': 6.8, 'crop_type': 'wheat', 'ph': 5.9},
    {'fertility': 8.0, 'crop_type': 'corn', 'ph': 7.0},
    {'fertility': 5.5, 'crop_type': 'corn', 'ph': 6.1},
    {'fertility': 9.0, 'crop_type': 'wheat', 'ph': 6.3}
]

rainfall = 55
soil_analysis = analyze_soil_quality(plots)  # Computed but not used
final_yield = compute_optimal_harvest(plots, rainfall)
print(f"Target result: {final_yield}")