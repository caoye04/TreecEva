from collections import defaultdict

# Simulate network packet segments with priority levels and sizes
dataset = [
    ('A', 12, 'high'), ('B', 8, 'low'), ('C', 15, 'medium'),
    ('D', 23, 'high'), ('E', 5, 'low'), ('F', 17, 'medium'),
    ('G', 9, 'low'), ('H', 14, 'high'), ('I', 11, 'medium')
]

# Irrelevant statistic tracking (distractor)
total_packets = len(dataset)
size_distribution = defaultdict(int)
for _, size, _ in dataset:
    size_distribution[size] += 1

# Filter segments above minimum size threshold
min_size_threshold = 10
filtered_segments = [item for item in dataset if item[1] >= min_size_threshold]

# Misleading transformation: convert to string and back (no effect but adds noise)
str_data = [f'{x[0]}:{x[1]}:{x[2]}' for x in filtered_segments]
reconstructed = []
for entry in str_data:
    parts = entry.split(':')
    reconstructed.append((parts[0], int(parts[1]), parts[2]))

# Group by priority level (actual relevant logic starts here)
priority_groups = defaultdict(list)
for label, size, level in reconstructed:
    priority_groups[level].append(size)

# Compute average size per group (semi-relevant computation)
avg_per_priority = {lvl: sum(sizes) / len(sizes) for lvl, sizes in priority_groups.items()}

# Extract high-priority segment sizes for processing
high_priority_sizes = priority_groups['high']

# Secondary distractor: analyze variance (not used later)
mean_high = sum(high_priority_sizes) / len(high_priority_sizes)
variance_proxy = sum((x - mean_high) ** 2 for x in high_priority_sizes)

# Process segments: apply sliding window sum of size 2 (relevant)
processed_segments = []
for i in range(len(high_priority_sizes) - 1):
    window_sum = high_priority_sizes[i] + high_priority_sizes[i + 1]
    processed_segments.append(window_sum)

# Another distractor: reverse slicing that isn't used
reversed_tail = processed_segments[::-1][:2]

# Threshold based on medium-priority average (key dependency)
threshold = int(avg_per_priority['medium'])

# Core logic: count how many processed segments exceed threshold
qualified_count = sum(1 for val in processed_segments if val > threshold)

# Final allocation calculation: multiply count by base unit
base_unit = 12
intermediate_result = qualified_count * base_unit

# Additional misleading calculation (dead code path)
if len(processed_segments) > 10:
    backup_plan = sum(priority_groups['low'])
else:
    backup_plan = None  # unused

# Critical statement
final_capacity = optimize_allocation(processed_segments, threshold)

# Helper function definition (must appear before use)
def optimize_allocation(segments, limit):
    # Count valid allocations under constraint
    count = 0
    for seg in segments:
        if seg > limit:
            count += 1
    return count * 12  # Each valid segment contributes 12 units

# Print result as required
print(f"Result: {final_capacity}")