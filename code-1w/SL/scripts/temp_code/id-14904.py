def calculate_efficiency(profile, loss_data):
    base_efficiency = 0.85
    adjustment_factor = 0.02
    peak_threshold = max(profile) * 0.9
    
    # Irrelevant computation: historical average (not used in final result)
    historical_avg = sum([x * 0.95 for x in profile if x < peak_threshold])
    if historical_avg > 1000:
        historical_avg /= 1.5

    # Tracking state across cycles (semi-relevant)
    cycle_count = 0
    efficiency_drops = []
    for i, (energy, loss) in enumerate(zip(profile, loss_data)):
        if energy > peak_threshold:
            cycle_count += 1
            drop = loss * adjustment_factor
            efficiency_drops.append(drop)
            if len(efficiency_drops) > 3:
                break  # Early termination

    # Real computation path
    total_energy = sum(profile)
    total_loss = sum(loss_data)
    raw_efficiency = (total_energy - total_loss) / total_energy
    
    # Apply dynamic correction based on peak behavior
    peak_corrections = [adjustment_factor * (1 - i * 0.1) for i in range(len(efficiency_drops))]
    correction = sum(peak_corrections) if peak_corrections else 0.0
    
    # Final efficiency calculation
    thermal_efficiency = base_efficiency * raw_efficiency + correction
    
    # Dead code path: never executed due to logic above
    if cycle_count == 0:
        fallback = sum(profile) / len(profile)
        thermal_efficiency = fallback * 0.01
    
    return thermal_efficiency

# Input data
energy_profile = [120, 150, 180, 200, 190, 170, 160]
losses = [12, 15, 18, 25, 20, 17, 16]

# Execution point of interest
thermal_efficiency = calculate_efficiency(energy_profile, losses)

# Output result
print(f"Result: {thermal_efficiency}")