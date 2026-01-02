def main():
    base_power = 120
    overload_factor = 1.75
    efficiency_ratio = 0.88

    # Calculate dynamic load based on environmental conditions
    temperatures = [22, 25, 27, 30, 33]
    adjusted_loads = [base_power * (1 + (t - 25) * 0.02) for t in temperatures]

    current_load = adjusted_loads[3]  # Load at 30°C

    peak_capacity = 150
    system_age = 3

    # Determine degradation factor using conditional expression
    degradation = 0.95 if system_age < 5 else 0.85

    def calculate_efficiency(load, peak, ratio, degrade):
        normalized = load / peak
        effective_efficiency = ratio * degrade
        return int(normalized * 100) * effective_efficiency  # Discretized efficiency score

    energy_threshold = calculate_efficiency(current_load, peak_capacity, efficiency_ratio, degradation)
    
    # Irrelevant tracking variable (minor distraction - intervention level 4)
    status_log = ['OK'] * 3
    
    print(f"Result: {energy_threshold}")

if __name__ == "__main__":
    main()