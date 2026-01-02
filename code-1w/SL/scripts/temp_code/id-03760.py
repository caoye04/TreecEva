from collections import defaultdict

# Simulate thermal dynamics in a multi-zone reactor core
def main():
    zone_temperatures = [320, 345, 370, 335, 358]
    energy_input = 125000
    time_steps = 18
    damping_factor = 0.88

    # Irrelevant acoustic resonance tracking (distractor)
    acoustic_modes = defaultdict(int)
    for i in range(3):
        acoustic_modes[f'mode_{i}'] += i * 1.5

    # Core energy profile computation
    energy_profile = []
    for t in range(time_steps):
        cycle_energy = energy_input * (damping_factor ** t)
        if t % 3 == 0:
            cycle_energy *= 1.1  # Pulse injection
        energy_profile.append(cycle_energy)
    
    # Dummy signal processing (dead code path - distractor)
    filtered_signal = []
    for val in energy_profile:
        if val > 50000:
            filtered_signal.append(val * 0.95)
        else:
            continue  # Misleading: never reached due to logic

    # Loss mechanisms
    conduction_loss = sum([t * 0.15 for t in zone_temperatures])
    radiation_loss = energy_input * 0.12
    fluctuation_loss = (energy_profile[5] - energy_profile[10]) * 0.05
    losses = [conduction_loss, radiation_loss, fluctuation_loss]

    # Efficiency calculation with conditional expression
    def calculate_efficiency(profile, loss_components):
        total_available = sum(profile) * 0.67  # Usable fraction
        total_loss = sum(loss_components)
        base_efficiency = (total_available - total_loss) / total_available
        
        # Conditional adjustment based on profile stability
        stability_score = sum([
            abs(energy_profile[i] - energy_profile[i+1]) 
            for i in range(len(energy_profile)-1)
        ]) / len(energy_profile)
        
        # Slicing to analyze mid-phase behavior (relevant use)
        mid_phase = energy_profile[5:12]
        peak_ratio = max(mid_phase) / sum(mid_phase) if mid_phase else 0
        
        # Final efficiency with conditional expression
        return base_efficiency * (1.05 if stability_score < 1500 and peak_ratio < 0.25 else 0.93)

    # Critical execution point
    thermal_efficiency = calculate_efficiency(energy_profile, losses)
    
    # Additional irrelevant state tracking (distractor)
    status_log = []
    for temp in zone_temperatures:
        status_log.append(f"Zone stable at {temp}K")

    print(f"Result: {thermal_efficiency}")

if __name__ == "__main__":
    main()