from itertools import accumulate

# Simulate time-series resource allocation with decay adjustments
def compute_resource_peak():
    base_load = [3, 5, -2, 7, 1, -6, 4, 8, -3, 2]
    adjustment_factors = [0.5, -1.2, 0.8, -0.3, 1.1]
    
    # Irrelevant scaling (distractor)
    dummy_scale = [x * 1.5 for x in adjustment_factors if x > 0]
    temp_buffer = sum(dummy_scale) * 0.1
    
    # Real signal generation
    amplified_load = [x * 2 for x in base_load]
    smoothed_load = list(accumulate(amplified_load, lambda a, b: a * 0.9 + b))

    # Apply conditional decay shifts (modular influence)
    shifted_load = []
    for i, val in enumerate(smoothed_load):
        if i % 4 == 0:
            shifted_load.append(val - 1.5)
        elif i % 3 == 0:
            shifted_load.append(val + 0.7)
        else:
            shifted_load.append(val)

    # Add dead code path (irrelevant branch)
    if len(shifted_load) > 50:
        fallback = sum(shifted_load) / 100
    else:
        pass  # Dead end

    # Compute rolling trend with tuple unpacking distraction
    trends = []
    for i in range(1, len(shifted_load)):
        prev, curr = shifted_load[i-1], shifted_load[i]
        trends.append(curr - prev)

    # Distractor: unused helper computation
    avg_trend = sum(trends) / len(trends) if trends else 0
    projected_next = shifted_load[-1] + avg_trend * 1.2  # Not used

    # Core logic: usage trajectory derived via conditional filtering
    usage_trajectory = [
        val for i, val in enumerate(shifted_load)
        if (i + 1) % 2 == 0 or (val > 5 and i % 3 != 0)
    ]

    # Key assignment point
    peak_capacity = max(usage_trajectory)

    # Red herring: secondary variable with similar naming
    peak_capacity_backup = max(usage_trajectory) if len(usage_trajectory) % 2 == 0 else 0

    return peak_capacity

result = compute_resource_peak()
print(f"Result: {result}")