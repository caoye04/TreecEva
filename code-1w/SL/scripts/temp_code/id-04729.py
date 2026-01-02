def analyze_workload(servers, maintenance_mode):
    base_load = 80
    threshold = 90
    overload_count = 0
    temp_buffer = []
    usage_levels = []

    for idx, server in enumerate(servers):
        load = base_load + (idx * 3) % 7

        if server in maintenance_mode:
            adjusted_load = max(load - 20, 10)
        else:
            adjusted_load = min(load + 5, 100)

        # Simulate fluctuating network impact
        network_spike = (idx + 1) * 1.5
        effective_load = min(adjusted_load + network_spike, 105)

        # Irrelevant transformation
        encoded = ''.join([chr(ord('A') + int(i % 26)) for i in [effective_load]])
        temp_buffer.append(encoded)

        # Only every second server's load is actually recorded
        if idx % 2 == 0:
            usage_levels.append(int(effective_load))

        # Dead code branch - never affects final result
        if load > threshold:
            overload_count += 1  # Not used later

    # Secondary processing: filtering out low usage
    filtered_levels = [level for level in usage_levels if level >= 85]

    # Spurious list creation
    shadow_copy = usage_levels[:]
    shadow_copy.sort(reverse=True)

    # Key statement
    peak_capacity = max(usage_levels)

    # Extra distraction: unused aggregation
    avg_filtered = sum(filtered_levels) / len(filtered_levels) if filtered_levels else 0

    # Output the target result
    print(f"Result: {peak_capacity}")

# Input data
server_names = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
maintenance_list = ['beta', 'delta']

# Execute function
def run():
    analyze_workload(server_names, maintenance_list)

run()