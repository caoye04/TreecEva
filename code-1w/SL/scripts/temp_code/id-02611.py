from itertools import combinations

# System parameters for device compatibility analysis
device_frequencies = [3.2, 3.5, 3.8, 4.0, 4.2]
base_threshold = 3.6
penalty_factor = 0.75

# Irrelevant auxiliary variable (minimal distraction)
placeholder_data = [0, 1, 1, 0]

# Calculate pairwise compatibility scores based on frequency alignment
compatibility_scores = []
for freq1, freq2 in combinations(device_frequencies, 2):
    if freq1 >= base_threshold and freq2 >= base_threshold:
        score = (freq1 + freq2) * 0.5
    else:
        score = (freq1 + freq2) * penalty_factor
    compatibility_scores.append(round(score, 3))

# Final aggregation step
total_harmony = sum(compatibility_scores)

# Output result
print(f"Target result: {total_harmony}")