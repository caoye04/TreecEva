def main():
    base_frequency = 2.4
    network_load = {1: 'active', 3: 'idle', 4: 'active', 7: 'active', 9: 'idle'}
    peak_hours = [1, 2, 3, 7, 8, 9]

    # Irrelevant utility variable (minor distraction)
    temp_buffer = [0] * 5

    active_nodes = set(node for node, status in network_load.items() if status == 'active')
    high_demand_periods = set(peak_hours)

    overlap_count = len(active_nodes & high_demand_periods)

    scaling_factor = 1.75

    compute_intensity = lambda x: x ** 2 + 2 * x
    total_intensity = sum(compute_intensity(i) for i in range(1, overlap_count + 1))

    def calculate_efficiency(load):
        load_size = len(load)
        efficiency_score = total_intensity / (load_size + 1)
        return round(efficiency_score, 3)

    energy_threshold = calculate_efficiency(network_load)
    print(f"Result: {energy_threshold}")

if __name__ == "__main__":
    main()