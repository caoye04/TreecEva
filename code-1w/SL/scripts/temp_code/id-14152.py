def find_balance(masses, torques):
    calculate_net = lambda m, t: sum(t) - sum(m)
    adjusted_masses = [mass * 1.5 for mass in masses][1:4]
    filtered_torques = [t for t in torques if t > 20]
    net_effect = calculate_net(adjusted_masses, filtered_torques)
    equilibrium_point = abs(net_effect // 2)
    return equilibrium_point

weights = [8, 12, 15, 9, 20]
moments = [25, 18, 32, 45, 10]
equilibrium_point = find_balance(weights, moments)
print(f"Result: {equilibrium_point}")