from itertools import accumulate

# Simulate daily energy reserve adjustment over a deployment cycle
def compute_operational_capacity():
    base_reserves = [3, -1, 4, -2, 5, -3, 2]
    fluctuation_scale = 2
    adjusted_flow = [x * fluctuation_scale for x in base_reserves]

    # Irrelevant transformation: reverse scaling attempt (not used)
    inverse_test = [x / (fluctuation_scale + 1) for x in adjusted_flow]

    # Apply cumulative usage under variable load
    usage_trajectory = list(accumulate(adjusted_flow))

    # Dummy peak detection with offset (semi-relevant but not final)
    transient_peaks = [x for x in usage_trajectory if x > 4]
    average_peak = sum(transient_peaks) / len(transient_peaks) if transient_peaks else 0

    # Key computation step
    peak_capacity = max(usage_trajectory)

    # Red herring: unused capacity margin calculation
    safety_margin = 1.2
    theoretical_max = peak_capacity * safety_margin

    # Dead code path: never executed due to fixed condition
    debug_mode = False
    if debug_mode:
        print('Debug info:', usage_trajectory)

    return peak_capacity

result = compute_operational_capacity()
print(f'Result: {result}')