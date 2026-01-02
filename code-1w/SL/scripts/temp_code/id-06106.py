import itertools

# Simulated sensor readings with noise and metadata
data_stream = [15, -8, 22, 44, -3, 9, 11, 7, 0, -12, 35, 28, 41]

# Irrelevant metadata (distractor)
sensor_ids = ['S1', 'S2', 'S3', 'S4']
location_map = {'S1': 'RoomA', 'S2': 'RoomB'}

# Noise filter threshold (red herring: not actually used in final logic)
noise_threshold = 5

# Extract only positive values using lambda (relevant)
positive_filter = lambda x: x > 0
positives = list(filter(positive_filter, data_stream))

# Additional irrelevant transformation chain
shifted_values = [x + 10 for x in data_stream if x % 2 == 0]
doubled_shifted = [v * 2 for v in shifted_values]

# Real processing begins: group consecutive even numbers (modular arithmetic)
even_groups = []
current_group = []
for val in data_stream:
    if val % 2 == 0:
        current_group.append(val)
    else:
        if len(current_group) >= 2:
            even_groups.append(current_group[:])
        current_group.clear()
if len(current_group) >= 2:
    even_groups.append(current_group)

# Compute group sums but only use later (decoy result)
group_sums = [sum(g) for g in even_groups]

duplicate_check = set()
duplicates_found = []
for item in data_stream:
    if item in duplicate_check:
        duplicates_found.append(item)
    else:
        duplicate_check.add(item)

decoy_aggregate = max(duplicates_found) if duplicates_found else 0

# Core logic: find all values divisible by 3 or 7 (relevant)
valid_candidates = [x for x in positives if x % 3 == 0 or x % 7 == 0]

# Sort and take every third element starting from index 1 (sorting + indexing)
sorted_candidates = sorted(valid_candidates)
strided_selection = []
for i in range(1, len(sorted_candidates), 3):
    strided_selection.append(sorted_candidates[i])

# Apply transformation using itertools.cycle to simulate pattern matching (itertools basics)
cycle_pattern = itertools.cycle([1, -1])
oscillated = [val + next(cycle_pattern) for val in strided_selection]

# Final filtering: keep only those above median of original positives (comparison + statistics)
if positives:
    median_positive = sorted(positives)[len(positives)//2]
else:
    median_positive = 0

# Critical assignment point
filtered_data = [x for x in oscillated if x > median_positive]

# Key computation
filtered_result = sum(filtered_data)

# Output the target result
print(f"Result: {filtered_result}")