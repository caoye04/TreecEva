from itertools import accumulate
import math

def analyze_workload(pattern, base_load=10):
    # Simulate fluctuating system workload over time
    adjustments = [int(math.sin(t) * 5) for t in range(len(pattern))]
    
    # Irrelevant transformation (distractor)
    encrypted = ''.join(chr(ord(c) ^ 3) for c in pattern)
    entropy = sum(math.log(ord(c)) for c in pattern if ord(c) > 32)
    
    # Core logic: derive workload from character frequency and phase shifts
    char_impact = [base_load + ord(c) % 7 - 3 for c in pattern]
    phased_changes = [delta * 2 if i % 3 == 0 else delta for i, delta in enumerate(adjustments)]
    
    # Combine via lambda-based weighting (semi-relevant)
    weight_fn = lambda x, y: x + (y // 2)
    combined = [weight_fn(char_impact[i], phased_changes[i]) for i in range(len(char_impact))]
    
    # Build usage trajectory with accumulation (relevant)
    usage_trajectory = list(accumulate(combined, lambda acc, x: acc + x if acc + x > 5 else 5))
    
    # Dead code path - never executed (distractor)
    if False:
        buffer_waste = [math.ceil(val / 7) for val in usage_trajectory]
        base_load = sum(buffer_waste) % 1000
    
    # Key computation point
    peak_capacity = max(usage_trajectory)
    
    # Extra irrelevant calculations to increase cognitive load
    avg_cycle = sum(abs(phased_changes[i] - phased_changes[(i+1)%len(phased_changes)]) for i in range(len(phased_changes)))
    stability_index = len(pattern) / (1 + entropy / 100)
    
    return peak_capacity, usage_trajectory, encrypted, stability_index

# Main execution
work_pattern = "alphaSync_2024"
scale_factor = 12

result_tuple = analyze_workload(work_pattern, base_load=scale_factor)
peak_capacity = result_tuple[0]

# Secondary distraction: process unused components
if len(result_tuple[1]) > 10:
    smoothed = list(map(lambda x: round(x, 1), result_tuple[1][::2]))
    peak_capacity += len(smoothed) - 10  # Minor adjustment based on length

# Final output
print(f"Result: {peak_capacity}")