def analyze_workload(servers, maintenance_mode):
    # Simulate a data center workload analysis with interference
    base_load = [s['cores'] * s['utilization'] for s in servers]
    adjusted_load = [load * 1.1 if load < 50 else load * 0.95 for load in base_load]

    # Irrelevant preprocessing: normalize names (distractor)
    server_names = [s['name'].upper() for s in servers]
    name_lengths = [len(name) for name in server_names]
    avg_name_length = sum(name_lengths) / len(name_lengths) if name_lengths else 0

    # State tracking with enumerate (required feature)
    usage_tracker = []
    overload_count = 0
    for i, load in enumerate(adjusted_load):
        if i in maintenance_mode:
            adjusted_load[i] = load * 0.3  # Reduced capacity during maintenance
        if adjusted_load[i] > 85:
            overload_count += 1
        usage_tracker.append(round(adjusted_load[i], 2))

    # Secondary computation on labels (mostly irrelevant)
    labels = [f'SRV-{i}' for i in range(len(servers))]
    valid_labels = [lbl for lbl in labels if lbl.endswith('0') or lbl.endswith('5')]

    # Complex filtering using zip and set operations (required features)
    status_map = list(zip(server_names, usage_tracker, [s['region'] for s in servers]))
    high_usage_regions = {region for name, usage, region in status_map if usage > 75}
    critical_regions = {r for r in high_usage_regions if r.startswith('US')}

    # Dead code path (misleading)
    if overload_count > 100:  # This will never trigger
        fallback = sum(usage_tracker) // len(usage_tracker)
        usage_tracker.append(fallback)

    # Core logic step embedded in noise
    temp_result = [val for val in usage_tracker if val > 0]
    normalized_total = sum(temp_result) / len(temp_result) if temp_result else 0

    # Key assignment with required operation
    peak_capacity = max(usage_tracker)

    # Additional red herring computations
    weighted_score = 0
    for idx, val in enumerate(usage_tracker):
        if idx % 3 == 0:
            weighted_score += val * 0.1
    final_diagnostic = weighted_score * (1 + avg_name_length * 0.01)

    print(f"Result: {peak_capacity}")
    return peak_capacity

# Input data
server_fleet = [
    {'name': 'alpha', 'cores': 8, 'utilization': 6.2, 'region': 'US-East'},
    {'name': 'beta', 'cores': 12, 'utilization': 7.1, 'region': 'EU-West'},
    {'name': 'gamma', 'cores': 16, 'utilization': 5.5, 'region': 'US-West'},
    {'name': 'delta', 'cores': 8, 'utilization': 9.8, 'region': 'US-East'},
    {'name': 'epsilon', 'cores': 12, 'utilization': 6.7, 'region': 'AP-South'}
]

maintenance_schedule = {1, 3}

# Execute
result = analyze_workload(server_fleet, maintenance_schedule)