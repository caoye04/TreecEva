def analyze_structural_loads(load_profile):
    total_load = sum(load_profile)
    cumulative_load = 0
    equilibrium_index = -1
    tolerance = 1e-4
    max_load = max(load_profile)
    min_load = min(load_profile)
    normalized_profile = [load / max_load for load in load_profile]
    filtered_loads = [load for load in load_profile if load > min_load * 2]

    temp_sum = 0
    for i in range(len(normalized_profile)):
        temp_sum += normalized_profile[i]

    dummy_shift = load_profile[::2]  
    reversed_profile = load_profile[::-1]

    secondary_balance = 0
    backup_pivot = -1
    for j in range(1, len(reversed_profile)):
        secondary_balance += reversed_profile[j]
        if secondary_balance > total_load * 0.3:
            backup_pivot = j
            break

    for pivot_point in range(len(load_profile)):
        left_span = load_profile[:pivot_point]
        right_span = load_profile[pivot_point + 1:]

        left_torque = sum(i * load for i, load in enumerate(left_span))
        right_torque = sum(i * load for i, load in enumerate(right_span))

        left_total = sum(left_span)
        right_total = sum(right_span)

        net_moment = abs(left_torque - right_torque)
        net_force = abs(left_total - right_total)

        inertial_factor = pivot_point ** 2 if pivot_point > 0 else 0
        damping_effect = inertial_factor * 0.01

        if net_force < tolerance and net_moment < tolerance:
            equilibrium_index = pivot_point if net_force < tolerance else -1
            break

    diagnostic_code = 200 if equilibrium_index != -1 else 404
    status_message = "Stable" if diagnostic_code == 200 else "Unstable"

    return equilibrium_index

loads = [1.2, 2.4, 3.6, 2.4, 1.2]
equilibrium_index = analyze_structural_loads(loads)
print(f"Result: {equilibrium_index}")