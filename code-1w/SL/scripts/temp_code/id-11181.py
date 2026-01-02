def analyze_resource_allocation():
    # Simulated system resource tracker
    resource_map = {
        'cpu': 4, 'memory': 16, 'storage': 512,
        'bandwidth': 100, 'gpu': 1, 'latency': 20
    }

    # Historical usage patterns (in hours)
    usage_log = [
        {'resource': 'cpu', 'usage': 3.2, 'priority': 1},
        {'resource': 'memory', 'usage': 12.1, 'priority': 1},
        {'resource': 'storage', 'usage': 412.5, 'priority': 2},
        {'resource': 'bandwidth', 'usage': 89.3, 'priority': 2},
        {'resource': 'gpu', 'usage': 0.8, 'priority': 1}
    ]

    # Irrelevant auxiliary data (distractor)
    performance_metrics = []
    for i in range(len(usage_log)):
        record = usage_log[i]
        score = (record['usage'] * (5 - i)) / (record.get('priority') + 1)
        performance_metrics.append(round(score, 3))

    # Misleading intermediate calculation (dead path)
    avg_performance = sum(performance_metrics) / len(performance_metrics) if performance_metrics else 0
    threshold = 6.5
    compliance_flag = avg_performance > threshold

    # Auxiliary function for efficiency computation
    def calculate_utilization(rsrc, used):
        if rsrc == 'latency':
            return 100.0 / used if used > 0 else 0
        elif rsrc in ['cpu', 'gpu']:
            return (used / resource_map[rsrc]) * 100
        else:
            return (used / resource_map[rsrc]) * 90  # Artificial reduction factor

    # Complex logic with distractors
    total_weighted_usage = 0.0
    total_capacity_score = 0
    priority_adjustment = 0

    for entry in usage_log:
        res = entry['resource']
        used = entry['usage']
        priority = entry['priority']

        # Real contribution to result
        utilization = calculate_utilization(res, used)
        total_weighted_usage += utilization * priority

        # Distractor: accumulates but not used directly
        total_capacity_score += resource_map.get(res, 0)

        # Semi-relevant adjustment (only priority matters in weight)
        if priority == 1:
            priority_adjustment += 1

    # Another distraction: unused set operations
    available_resources = set(resource_map.keys())
    used_resources = set(entry['resource'] for entry in usage_log)
    idle_set = available_resources - used_resources
    fallback_modes = {f"backup_{r}" for r in idle_set if r in ['storage', 'memory']}

    # Dictionary-based transformation (irrelevant)
    backup_config = {}
    for r in idle_set:
        backup_config[f"standby_{r}"] = resource_map[r] * 0.5

    # Core calculation: efficiency ratio
    efficiency_ratio = 0
    if len(usage_log) > 0:
        base_efficiency = total_weighted_usage / len(usage_log)
        penalty_factor = 0.95 if priority_adjustment < 3 else 1.0
        efficiency_ratio = base_efficiency * penalty_factor

    # Final red herring: unused conditional mutation
    if 'latency' in resource_map and efficiency_ratio > 50:
        adjusted_latency = resource_map['latency'] * 0.85
        efficiency_ratio -= adjusted_latency / 10

    # Critical execution point
    efficiency_ratio = calculate_efficiency(resource_map, usage_log)

    return efficiency_ratio


def calculate_efficiency(resources, log):
    # Independent helper function
    total_load = 0.0
    count = 0

    for item in log:
        r = item['resource']
        u = item['usage']
        cap = resources.get(r, 1)
        load_percent = (u / cap) * 100
        total_load += load_percent
        count += 1

    average_load = total_load / count if count > 0 else 0
    bonus = 10 if len(log) >= 4 else 0
    return round(average_load - 5 + bonus, 4)

# Execute and print result
efficiency_ratio = analyze_resource_allocation()
print(f"Result: {efficiency_ratio}")