from collections import defaultdict

# Simulate agricultural yield analysis across multiple growth cycles and soil clusters
def analyze_crop_performance():
    # Initialize cluster-specific data
    cluster_ids = ['C1', 'C2', 'C3']
    soil_ph_levels = {'C1': 6.2, 'C2': 5.8, 'C3': 6.5}
    base_moisture = [0.38, 0.41, 0.39]

    # Growth cycle parameters (days)
    growth_cycles = [28, 32, 35, 29]
    temperature_fluctuations = [-1.2, 0.5, 2.1, -0.8]

    # Simulated biomass accumulation per cycle (kg/m²)
    biomass_data = [
        [2.1, 1.9, 2.3],
        [2.4, 2.0, 2.5],
        [2.6, 2.2, 2.7],
        [2.3, 1.8, 2.4]
    ]

    # Irrelevant auxiliary calculation (distractor)
    avg_temperature = sum([22 + t for t in temperature_fluctuations]) / len(temperature_fluctuations)
    normalized_ph = {cid: round(ph * 10) / 10 for cid, ph in soil_ph_levels.items()}

    # Track cluster-specific metrics
    cluster_metrics = defaultdict(dict)
    for i, cid in enumerate(cluster_ids):
        moisture = base_moisture[i]
        ph = soil_ph_levels[cid]
        
        # Compute growth potential index (GPI)
        gpi = (moisture * 100) + (ph * 5) + 10
        
        # Simulate pest resistance score (not used in final result)
        pest_score = (7 - abs(ph - 6.0)) * 15
        
        # Store relevant and semi-relevant metrics
        cluster_metrics[cid]['gpi'] = gpi
        cluster_metrics[cid]['pest_resistance'] = pest_score  # distractor
        cluster_metrics[cid]['base_moisture'] = moisture

    # Secondary distractor: unused transformation
    transformed_cycles = [cycle + 2 if cycle < 30 else cycle - 1 for cycle in growth_cycles]

    def calculate_harvest_efficiency(clusters, cycles):
        efficiency = 0.0
        adjustment_factor = 0.85

        for idx, cycle in enumerate(cycles):
            cycle_weight = cycle / sum(cycles)
            
            # Harvest boost from length but capped at 35 days
            day_bonus = min(cycle, 35) * 0.02
            
            for cid in clusters:
                gpi = clusters[cid]['gpi']
                moisture = clusters[cid]['base_moisture']
                
                # Core efficiency contribution
                contribution = (gpi * 0.3) + (moisture * 50) + day_bonus
                efficiency += contribution * cycle_weight * adjustment_factor
        
        # Apply arbitrary field loss (constant)
        efficiency *= 0.93
        
        # Dead code path (never executed)
        if False:
            efficiency -= 5.0  # unreachable
            efficiency = max(efficiency, 0)

        return efficiency

    # Execute main computation
    final_yield = calculate_harvest_efficiency(cluster_metrics, growth_cycles)
    
    # Additional irrelevant aggregation (distractor)
    total_biomass = sum(sum(row) for row in biomass_data)
    peak_cycle_index = max(range(len(biomass_data)), key=lambda i: sum(biomass_data[i]))
    
    print(f"Result: {final_yield}")
    return final_yield

# Run simulation
analyze_crop_performance()