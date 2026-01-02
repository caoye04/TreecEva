def analyze_segments(ranges, thresholds):
    coverage_set = set()
    overlap_count = {}

    for start, end in ranges:
        for point in range(start, end + 1):
            coverage_set.add(point)
            overlap_count[point] = overlap_count.get(point, 0) + 1

    max_overlap = max(overlap_count.values())

    redundant_points = {p for p, cnt in overlap_count.items() if cnt > 1}
    unique_coverage = coverage_set - redundant_points

    efficiency_score = len(unique_coverage) / len(coverage_set) if coverage_set else 0

    return max_overlap, efficiency_score


def calculate_threshold_metrics(data, baseline):
    squared_errors = [(x - baseline) ** 2 for x in data]
    mean_sq_error = sum(squared_errors) / len(data) if data else 0
    rmse = mean_sq_error ** 0.5

    threshold_deviation = abs(baseline - sum(data) / len(data)) if data else 0

    return rmse, threshold_deviation


def aggregate_resources(capacities, constraints):
    resource_pool = []
    temp_buffer = []

    for cap in capacities:
        if cap <= 0:
            continue
        adjusted = cap * 0.9
        if adjusted > constraints['limit']:
            adjusted = constraints['limit']
        resource_pool.append(adjusted)
        temp_buffer.append(adjusted * 1.1)  # unused distractor

    total_available = sum(resource_pool)
    avg_resource = total_available / len(resource_pool) if resource_pool else 0

    high_yield = [r for r in resource_pool if r > avg_resource]
    yield_rate = len(high_yield) / len(resource_pool) if resource_pool else 0

    return resource_pool, yield_rate


def optimize_allocation(max_overlap, pool):
    scaling_factor = 1.0 / (max_overlap + 1e-8)
    scaled = [p * scaling_factor for p in pool]
    adjustment = sum(scaled) * 0.1
    final_capacity = int(sum(scaled) - adjustment)

    # Distractor calculations
    hypothetical = [p * 2 for p in scaled if p > 5]
    noise_offset = len(hypothetical) * 0.05

    return final_capacity


# Main execution
if __name__ == "__main__":
    time_ranges = [(10, 15), (12, 18), (14, 16), (20, 25)]
    demand_thresholds = {'min': 5, 'limit': 12}
    usage_data = [8, 10, 7, 13, 9]
    base_level = 9

    # Step 1: Analyze temporal segment overlaps
    max_overlap, efficiency = analyze_segments(time_ranges, demand_thresholds)

    # Step 2: Compute statistical metrics on usage
    rmse, deviance = calculate_threshold_metrics(usage_data, base_level)

    # Step 3: Aggregate and preprocess resource capacities
    raw_capacities = [10, 15, 8, 20, 12]
    resources, yield_ratio = aggregate_resources(raw_capacities, demand_thresholds)

    # Step 4: Optimize final allocation based on overlap and pooled resources
    final_capacity = optimize_allocation(max_overlap, resources)

    print(f"Result: {final_capacity}")