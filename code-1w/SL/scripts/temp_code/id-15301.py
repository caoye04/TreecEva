from itertools import accumulate
def find_equilibrium(weights, moments):
    total_weight = sum(weights)
    total_moment = sum(moments)
    if total_weight == 0:
        return 0.0
    center_of_mass = total_moment / total_weight
    running_weight = 0
    for i, w in enumerate(weights):
        running_weight += w
        if running_weight >= total_weight / 2:
            balance_index = i
            break
    cumulative_moment_left = sum(moments[:balance_index+1])
    cumulative_moment_right = sum(moments[balance_index:])
    equilibrium_point = abs(cumulative_moment_left - cumulative_moment_right)
    return equilibrium_point

# System parameters
turbine_blade_weights = [12, 18, 23, 15, 32]
turbine_blade_moments = [144, 216, 345, 225, 480]
equilibrium_point = find_equilibrium(turbine_blade_weights, turbine_blade_moments)
print(f"Result: {equilibrium_point}")