from itertools import accumulate

def find_equilibrium(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i, val in enumerate(arr):
        # Check if left sum equals right sum (excluding current element)
        right_sum = total_sum - left_sum - val
        if left_sum == right_sum:
            return i  # Return index as equilibrium point
        left_sum += val
    return -1  # No equilibrium found

# Sensor weight calibration data
weights = [4, 7, 3, 8, 5, 2]

# Irrelevant auxiliary variable (minor distraction)
calibration_offset = 0.0

# Compute equilibrium point in the weight distribution
equilibrium_point = find_equilibrium(weights)

# Print result in required format
print(f"Result: {equilibrium_point}")