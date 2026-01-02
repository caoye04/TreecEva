from collections import defaultdict
from itertools import combinations

# Simulate sensor readings with noise and valid data
raw_readings = [102, 98, 100, 101, 99, 250, 97, 103, 300, 95]

# Irrelevant transformation: create reversed mapping (not used in final logic)
reversed_indices = {i: len(raw_readings) - i for i in range(len(raw_readings))}
offset_map = defaultdict(lambda: 0)
for i, val in enumerate(raw_readings):
    if val < 200:  # Filter out obvious outliers for offset tracking
        offset_map[i % 4] += 1

# Step 1: Filter outliers using simple threshold
filtered_readings = [x for x in raw_readings if x < 200]

# Step 2: Compute moving average of window size 2 (with overlap)
smoothed = []
for i in range(len(filtered_readings) - 1):
    smoothed.append((filtered_readings[i] + filtered_readings[i + 1]) / 2)

# Distractor: Generate all pairs for no reason
all_pairs = list(combinations(smoothed, 2))
total_pairs = sum(1 for _ in all_pairs)  # Unused metric

# Step 3: Normalize values around mean
mean_val = sum(smoothed) / len(smoothed)
normalized = [round(x - mean_val, 2) for x in smoothed]

# Step 4: Apply weighting based on position (higher weight to later entries)
weighted_devs = []
for idx, dev in enumerate(normalized):
    weight = 1 + (idx * 0.1)  # Increasing weight
    weighted_devs.append(dev * weight)

# Step 5: Aggregate total deviation magnitude
aggregate_deviation = sum(abs(w) for w in weighted_devs)

# Step 6: Count stability transitions (sign changes in normalized diffs)
stability_changes = 0
for i in range(1, len(normalized)):
    if normalized[i] * normalized[i - 1] < 0:  # Sign change
        stability_changes += 1

# Step 7: Calculate final score using composite formula
base_score = len(filtered_readings) * 10
penalty = aggregate_deviation * 1.5
bonus = max(0, 50 - (stability_changes * 5))

# Critical statement
final_score = calculate_final_score(processed_data)

# Dummy function to obscure logic slightly
def calculate_final_score(data):
    return base_score - penalty + bonus

# Inject actual values into function via closure
processed_data = normalized  # Meaningful but indirect reference

# Print result as required
Result: {final_score}