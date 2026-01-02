def calculate_grid_load():
    # Simulate time-series sensor data for energy demand across zones
    timestamps = [t for t in range(0, 24, 2)]
    zone_a = [150, 170, 165, 180, 190, 210, 230, 240]
    zone_b = [130, 135, 140, 155, 170, 180, 195, 205]
    zone_c = [90, 95, 100, 110, 120, 135, 145, 150]

    # Irrelevant transformation: normalize timestamps (not used later)
    normalized_times = [(t - timestamps[0]) / (timestamps[-1] - timestamps[0]) for t in timestamps]

    # Distractor: Compute average growth rate (unused)
    growth_a = [(zone_a[i+1] - zone_a[i]) / zone_a[i] for i in range(len(zone_a)-1)]
    avg_growth_a = sum(growth_a) / len(growth_a)

    # Actual processing: compute peak-to-average ratio per zone
    peak_avg_ratios = []
    for idx, zone in enumerate([zone_a, zone_b, zone_c]):
        peak = max(zone)
        avg = sum(zone) / len(zone)
        ratio = peak / avg
        peak_avg_ratios.append(ratio)

    # Misleading intermediate: simulate temperature correlation (dead end)
    temp_readings = [22, 23, 24, 25, 26, 27, 28, 29]
    temp_zone_corr = list(zip(temp_readings, zone_a))
    dummy_weighted = sum(t * z for t, z in temp_zone_corr)  # unused

    # Key aggregation: total average demand across all zones and times
    all_demands = [sum(zones) for zones in zip(zone_a, zone_b, zone_c)]
    aggregate_demand = sum(all_demands) / len(all_demands)

    # Efficiency model based on operational hours
    operational_hours = len(timestamps)
    base_efficiency = 0.85
    degradation = 0.005 * (operational_hours - 8)
    efficiency_factor = max(0.7, base_efficiency - degradation)

    # Final computation
    final_load = aggregate_demand * efficiency_factor

    # Print result as required
    print(f"Result: {final_load}")
    return final_load

# Execute function
calculate_grid_load()