from collections import defaultdict

# Simulate energy grid load distribution across sectors
def compute_energy_distribution(demand_data, thresholds):
    base_load = 185.7
    peak_multiplier = 1.35
    off_peak_discount = 0.82
    temp_storage = []
    sector_adjustments = defaultdict(float)
    
    for sector, demand in demand_data.items():
        if demand > thresholds['high']:
            adjusted_demand = demand * peak_multiplier
        elif demand < thresholds['low']:
            adjusted_demand = demand * off_peak_discount
        else:
            adjusted_demand = demand
        
        # Irrelevant aggregation (distractor)
        temp_storage.append(adjusted_demand ** 0.5)
        sector_adjustments[sector] = round(adjusted_demand, 2)

    # Secondary computation with partial relevance
    total_base = sum(demand_data.values())
    total_adj = sum(sector_adjustments.values())
    stability_ratio = total_adj / total_base if total_base else 0

    # Red herring: unused complex calculation
    volatility_index = 0
    if stability_ratio > 1.1:
        volatility_index = sum((v - base_load) ** 2 for v in sector_adjustments.values()) / len(sector_adjustments)
    elif stability_ratio < 0.9:
        volatility_index = -1 * sum(v for v in temp_storage if v > 5)

    # Core logic path
    flow_capacity = 975
    maintenance_factor = 0.93
    operational_days = 28
    scheduled_downtime = 3

    available_days = operational_days - scheduled_downtime
    raw_flow = flow_capacity * available_days
    adjusted_flow = raw_flow * maintenance_factor  # Key intermediate value

    # Efficiency model
    efficiency_logs = [stability_ratio * 0.75]
    if volatility_index > 0:
        efficiency_logs.append(0.68)
    else:
        efficiency_logs.append(0.91)
    
    # Logical combination with distractors
    initial_efficiency = efficiency_logs[-1]
    degradation_rate = 0.003 * operational_days
    efficiency_factor = initial_efficiency - degradation_rate

    # Final assignment - key execution point
    final_flux = adjusted_flow * efficiency_factor

    # Unrelated logging (dead code)
    debug_snapshot = {
        'timestamp': '2024-06-15',
        'volatility': volatility_index,
        'base': base_load,
        'readings': [round(x, 2) for x in temp_storage[::3]]
    }

    print(f"Result: {final_flux}")

# Inputs
demand_profile = {
    'industrial': 210,
    'residential': 160,
    'commercial': 195,
    'agricultural': 80
}
threshold_settings = {
    'high': 200,
    'low': 100
}

compute_energy_distribution(demand_profile, threshold_settings)