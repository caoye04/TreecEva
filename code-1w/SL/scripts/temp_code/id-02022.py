from itertools import accumulate
import math

# Simulate time-series resource allocation under fluctuating demand
def compute_resource_allocation(base_load, fluctuations, efficiency_factor):
    adjusted_loads = [base_load * (1 + delta) for delta in fluctuations]
    
    # Apply nonlinear efficiency damping
    damped_loads = [load / (1 + efficiency_factor * i) for i, load in enumerate(adjusted_loads)]
    
    # Simulate cumulative system stress with recovery periods
    stress_levels = [max(0, load - 5) for load in damped_loads]  # Thresholded stress contribution
    recovery_impact = [stress * 0.3 for stress in reversed(stress_levels)]  # Fake backward influence (unused)
    usage_trajectory = list(accumulate(damped_loads, lambda acc, x: acc * 0.9 + x * 1.1))  # Leaky accumulation
    
    # Irrelevant secondary computation - distractor
    hypothetical_savings = sum(x for x in damped_loads if x < base_load)
    normalized_variance = sum((x - base_load)**2 for x in damped_loads) / len(damped_loads)
    transient_peaks = [x for x in usage_trajectory if x > base_load * 1.5]
    
    # Key state variables
    baseline_integral = sum(damped_loads)
    peak_capacity = max(usage_trajectory)
    stability_ratio = baseline_integral / (peak_capacity + 1e-8)
    
    # Unused complex structure - red herring
    diagnostics = {
        'total_fluctuation': sum(abs(f) for f in fluctuations),
        'coherence_index': math.exp(-normalized_variance),
        'transient_count': len(transient_peaks)
    }
    
    return peak_capacity

# Parameters
base_demand = 12.5
variation_pattern = [0.1, -0.05, 0.3, 0.15, -0.2, 0.4, 0.05, -0.1, 0.2, 0.1]
efficiency = 0.08

# Execute
result = compute_resource_allocation(base_demand, variation_pattern, efficiency)
peak_capacity = result
print(f"Result: {peak_capacity}")