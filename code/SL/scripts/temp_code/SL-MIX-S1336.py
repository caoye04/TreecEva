from collections import defaultdict
import math

def compute_segment_fee(segment):
    if len(segment) <= 1:
        return sum(segment) * 0.01
    mid = len(segment) // 2
    left_fee = compute_segment_fee(segment[:mid])
    right_fee = compute_segment_fee(segment[mid:])
    return left_fee + right_fee + 0.001 * (sum(segment) ** 1.5)

transaction_volumes = [1200, 800, 1500, 600, 950, 1300, 750]
segment_map = defaultdict(list)

for i, vol in enumerate(transaction_volumes):
    segment_map[i % 3].append(vol)

optimal_fee = 0.0
for segment_id in sorted(segment_map.keys()):
    segment_total = sum(segment_map[segment_id])
    if segment_total > 1000:
        fee = compute_segment_fee(segment_map[segment_id])
        optimal_fee = max(optimal_fee, fee)
    else:
        optimal_fee += segment_total * 0.02

print(f"Result: {round(optimal_fee, 4)}")