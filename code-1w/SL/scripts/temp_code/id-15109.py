from collections import defaultdict

# Simulate agricultural yield optimization across variable growth cycles
def analyze_crop_performance(plots):
    efficiency_map = defaultdict(lambda: 0)
    temp_results = []
    base_rainfall = 120
    evaporation_rate = 0.07
    phantom_yield = 0  # distractor variable

    for plot_id, data in plots.items():
        soil_health = data['soil']
        sunlight_hours = data['sun']
        water_supply = base_rainfall + data.get('irrigation', 0)
        adjusted_evap = water_supply * evaporation_rate
        net_water = water_supply - adjusted_evap

        # Irrelevant calculation - dead computation path
        for _ in range(2):
            phantom_yield += net_water * 0.01  # not used later

        # Compute growth potential
        growth_potential = (soil_health * 0.4) + (sunlight_hours * 0.35) + (net_water * 0.25)
        efficiency_map[plot_id] = round(growth_potential, 3)

        # Semi-relevant filtering (only some results are used)
        if growth_potential > 95:
            temp_results.append((plot_id, growth_potential))

    # Distractor: unused aggregation
    avg_temp = sum(val for _, val in temp_results) / len(temp_results) if temp_results else 0
    high_yield_ids = [pid for pid, _ in temp_results]

    return efficiency_map, high_yield_ids


def calculate_harvest_efficiency(metrics, cycles):
    total_efficiency = 0.0
    cycle_factor = 1.0
    debug_offset = 0.05  # misleading variable

    for i in range(cycles):
        noise_adjustment = (i % 3) * 0.02
        cycle_factor *= (1 + 0.08 + noise_adjustment)  # compound-like effect

    # Apply cycle amplification to metrics
    amplified_values = map(lambda x: x * cycle_factor, metrics.values())
    total_efficiency = sum(amplified_values)

    # Extra logic that doesn't alter final result
    final_checklist = [x for x in amplified_values if x > 100]  # empty re-evaluation
    consistency_flag = len(final_checklist) > 0

    scaling_constant = 0.91  # red herring parameter
    dummy_consistency_score = len(metrics) * debug_offset * scaling_constant

    return int(total_efficiency)  # deterministic integral output

# Main execution
if __name__ == "__main__":
    field_data = {
        'F1': {'soil': 92, 'sun': 88, 'irrigation': 30},
        'F2': {'soil': 96, 'sun': 94, 'irrigation': 20},
        'F3': {'soil': 89, 'sun': 90, 'irrigation': 35},
        'F4': {'soil': 95, 'sun': 85, 'irrigation': 25}
    }

    # Step 1: Analyze per-plot efficiency
    efficiencies, selected_plots = analyze_crop_performance(field_data)

    # Step 2: Track auxiliary statistics (distractor)
    total_plots = len(field_data)
    active_plots = len(selected_plots)
    utilization_ratio = round(active_plots / total_plots, 3) if total_plots else 0

    # Step 3: Simulate multi-season accumulation
    growth_cycles = 6
    area_metrics = efficiencies  # passed as metric values

    # Key statement
    final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

    print(f"Result: {final_yield}")