import math
from collections import defaultdict

def compute_quarterly_adjustments(performances):
    if len(performances) <= 1:
        return performances
    mid = len(performances) // 2
    left = compute_quarterly_adjustments(performances[:mid])
    right = compute_quarterly_adjustments(performances[mid:])
    return merge_performance_segments(left, right)

def merge_performance_segments(left_seg, right_seg):
    merged = []
    i = j = 0
    while i < len(left_seg) and j < len(right_seg):
        if left_seg[i] >= right_seg[j]:
            merged.append(left_seg[i])
            i += 1
        else:
            merged.append(right_seg[j])
            j += 1
    merged.extend(left_seg[i:])
    merged.extend(right_seg[j:])
    return merged

# Portfolio performance data (logarithmic returns)
portfolio_logs = [0.02, -0.01, 0.03, -0.005, 0.015, -0.02, 0.025, 0.01]

# Process performance data using divide and conquer
sorted_performances = compute_quarterly_adjustments(portfolio_logs)

# Calculate adjustment weights
weight_map = {i: math.exp(return_val) for i, return_val in enumerate(sorted_performances)}
total_weight = sum(weight_map.values())
normalized_weights = {k: v / total_weight for k, v in weight_map.items()}

# Compute adjustment factor
adjustment_powers = {k: math.log(v + 1) for k, v in normalized_weights.items()}
composite_factor = sum(adjustment_powers.values()) / len(adjustment_powers)

final_adjustment_factor = round(composite_factor * 1000000)
print(f"Result: {final_adjustment_factor}")