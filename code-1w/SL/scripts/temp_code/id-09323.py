def calculate_harvest_efficiency(plots, cycles):
    base_efficiency = 0.85
    adjustment_factor = 0.02
    total_yield = 0.0
    efficiency_log = []

    for i, (area, soil_q, irrigated) in enumerate(plots):
        if area <= 0:
            continue

        # Simulate seasonal growth adjustments over cycles
        seasonal_boost = 0.0
        for year in range(len(cycles)):
            season_mod = (cycles[year] * (1 + 0.1 * (year % 3)))
            seasonal_boost += season_mod

        # Compute initial yield estimate
        raw_yield = area * soil_q * base_efficiency * (1 + seasonal_boost / 10)

        # Apply irrigation bonus if applicable
        if irrigated:
            raw_yield *= 1.15

        # Distractor: Track unused metrics
        unused_potential = area * 1.5 if soil_q > 0.7 else 0
        hypothetical_max = raw_yield * 1.4  # Not used in final calculation

        # Real adjustment: reduce yield if small plot with low soil quality
        if area < 5 and soil_q < 0.6:
            raw_yield *= 0.8

        total_yield += raw_yield
        efficiency_log.append(raw_yield / area if area > 0 else 0)

    # Secondary distractor loop: analyze log patterns (not affecting result)
    stable_count = 0
    for j, eff in enumerate(efficiency_log):
        if 0.9 <= eff <= 1.1:
            stable_count += 1

    # Final efficiency scaling based on consistency
    consistency_bonus = 1 + (0.05 * stable_count / len(efficiency_log)) if efficiency_log else 1

    # Actual final computation
    final_efficiency = total_yield * consistency_bonus

    # More distractions: string-based status tracking (irrelevant)
    status_flags = ['OK' if q > 0.5 else 'LOW' for _, q, _ in plots]
    flag_summary = ''.join(status_flags)
    flag_score = len(flag_summary.replace('OK', '')) * -0.01  # Unused penalty

    return final_efficiency


def main():
    # Define test input
    area_metrics = [
        (10.0, 0.85, True),
        (3.5, 0.45, False),
        (7.2, 0.78, True),
        (1.8, 0.30, False)
    ]

    growth_cycles = [0.92, 0.88, 0.95]

    # Dummy variables to increase interference
    predicted_rainfall = sum([c * 1.08 for c in growth_cycles])
    projected_costs = predicted_rainfall * 150
    irrelevant_scaling = projected_costs / (growth_cycles[0] + 1) if growth_cycles[0] != 0 else 0

    # Key execution point
    final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

    # Print result for extraction
    print(f"Result: {final_yield}")

if __name__ == "__main__":
    main()