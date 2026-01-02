from itertools import accumulate

def find_equilibrium(weights):
    total_weight = sum(weights)
    left_sum = 0
    for i, w in enumerate(weights):
        # The torque on the right excludes current element and accumulates to the end
        right_sum = total_weight - left_sum - w
        if left_sum == right_sum:
            return i  # Return index as equilibrium point
        left_sum += w
    return -1  # No equilibrium found

# Simulate sensor weights along a beam
turbine_weights = [4, 7, 9, 3, 8, 2, 5]
left_torque = list(accumulate(turbine_weights))
right_torque = list(accumulate(reversed(turbine_weights)))

equilibrium_point = find_equilibrium(turbine_weights)

# Irrelevant auxiliary calculation (minor distraction)
avg_weight = sum(turbine_weights) / len(turbine_weights)
normalized_weights = list(map(lambda x: round(x / avg_weight, 2), turbine_weights))

print(f"Result: {equilibrium_point}")