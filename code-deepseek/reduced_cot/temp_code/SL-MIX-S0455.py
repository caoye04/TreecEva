from itertools import combinations

# Analyze overlapping customer segments
segment_a = {12, 25, 38, 42, 55}
segment_b = {25, 42, 67, 89, 91}
segment_c = {38, 42, 55, 77, 89}

# Find overlapping customers
overlap_ab = segment_a & segment_b
overlap_bc = segment_b & segment_c
overlap_ac = segment_a & segment_c

# Calculate metrics
unique_customers = segment_a | segment_b | segment_c
unique_count = len(unique_customers)
overlap_sum = len(overlap_ab) + len(overlap_bc) + len(overlap_ac)
combined_sum = len(segment_a) + len(segment_b) + len(segment_c)

# Final calculation
final_result = combined_sum - unique_count
print(f"Result: {final_result}")