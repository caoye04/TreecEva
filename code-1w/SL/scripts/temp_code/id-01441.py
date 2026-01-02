def analyze_workload(demand: list, thresholds: tuple) -> dict:
    peak = max(demand)
    baseline = sum(demand) / len(demand)
    volatility = (max(demand) - min(demand)) / baseline

    high_load_regions = {i for i, d in enumerate(demand) if d > thresholds[0]}
    low_load_regions = {i for i, d in enumerate(demand) if d < thresholds[1]}
    mid_range = len([d for d in demand if thresholds[1] <= d <= thresholds[0]])

    # Irrelevant transformation
    normalized = [round((d - baseline) / peak, 3) for d in demand]
    spike_count = len([n for n in normalized if n > 0.75])

    return {
        'peak': peak,
        'baseline': baseline,
        'volatility': volatility,
        'high_regions': high_load_regions,
        'low_regions': low_load_regions,
        'mid_count': mid_range
    }


def evaluate_redundancy(node_map: set, backup_ratio: float) -> int:
    # Simulated auxiliary calculation with no impact on final result
    total_nodes = len(node_map)
    redundant_nodes = int(total_nodes * backup_ratio)
    efficiency_score = (total_nodes - redundant_nodes) / total_nodes if total_nodes > 0 else 0
    return redundant_nodes  # Distractor function


def optimize_distribution(set_a: set, set_b: set) -> int:
    overlap = set_a & set_b
    exclusive_a = set_a - set_b
    exclusive_b = set_b - set_a

    balance_factor = len(exclusive_a) - len(exclusive_b)
    shift_capacity = abs(balance_factor) // 2

    adjusted_a = len(exclusive_a) - shift_capacity
    adjusted_b = len(exclusive_b) + shift_capacity

    # Dummy sorting with no effect
    temp_list = sorted([adjusted_a, adjusted_b, len(overlap)])
    
    # Final computation
    net_capacity = adjusted_a + adjusted_b + len(overlap)
    scaling_modifier = 1 if net_capacity >= 10 else 2
    final_net = net_capacity * scaling_modifier

    return final_net

# Main execution
if __name__ == "__main__":
    user_demand = [120, 85, 150, 45, 130, 90, 110, 60, 140]
    threshold_config = (100, 70)

    # Step 1: Analyze workload distribution
    analysis = analyze_workload(user_demand, threshold_config)
    
    # Extract relevant regions
    critical_zones = analysis['high_regions']
    underutilized_zones = analysis['low_regions']

    # Irrelevant redundancy check
    dummy_set = {1, 2, 3, 4, 5}
    _ = evaluate_redundancy(dummy_set, 0.3)

    # Misleading intermediate calculation
    avg_excluding_extremes = (analysis['peak'] + analysis['baseline']) / 2
    adjustment_proxy = round(avg_excluding_extremes % 10)

    # Key statement
    final_capacity = optimize_distribution(critical_zones, underutilized_zones)

    print(f"Result: {final_capacity}")