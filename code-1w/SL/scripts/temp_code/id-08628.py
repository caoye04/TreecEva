from itertools import compress

# System configuration for distributed task scheduling
core_counts = [4, 8, 6, 12, 16]
frequency_levels = [3.2, 2.8, 3.5, 2.4, 3.0]
overclocked_flags = [True, False, True, False, True]

# Calculate performance score per core
performance_scores = []
for i, (count, freq) in enumerate(zip(core_counts, frequency_levels)):
    base_score = count * freq
    if overclocked_flags[i]:
        base_score *= 1.2
    performance_scores.append(base_score)

# Determine viable cores based on minimum performance threshold
efficiency_mask = [score >= 10.0 for score in performance_scores]
optimized_slots = list(compress(core_counts, efficiency_mask))

# Final aggregation step
total_capacity = sum(optimized_slots)
print(f"Result: {total_capacity}")