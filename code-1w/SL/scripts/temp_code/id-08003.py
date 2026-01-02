from itertools import groupby

def analyze_trends(data, threshold=3):
    trends = []
    for key, group in groupby(data, lambda x: x > threshold):
        count = len(list(group))
        trends.append((key, count))
    return trends

# Simulate sensor readings over time
readings = [2, 2, 3, 5, 5, 5, 4, 4, 7, 7, 7, 7, 1, 1]

# Irrelevant transformation - distractor
transformed = [x ** 2 - x for x in readings if x % 2 == 0]
dummy_sum = sum(transformed) // (len(transformed) or 1)

# Track state across phases
phase_changes = 0
prev_was_high = False
for val in readings:
    current_high = val > 4
    if current_high and not prev_was_high:
        phase_changes += 1
    prev_was_high = current_high

# Core analysis using enumerate and zip
indices = [i for i, x in enumerate(readings) if x >= 5]
windows = list(zip(indices, indices[1:], indices[2:]))
valid_windows = [w for w in windows if w[2] - w[0] <= 4]

# Secondary metric - distracted computation
spike_pairs = 0
for i in range(len(readings) - 1):
    if readings[i] < 4 and readings[i+1] >= 6:
        spike_pairs += 1

# Calculate baseline stats
high_readings = [r for r in readings if r >= 5]
avg_high = sum(high_readings) / len(high_readings) if high_readings else 0

# Misleading clustering attempt
clusters = []
current_cluster = []
for r in readings:
    if r >= 5:
        current_cluster.append(r)
    else:
        if current_cluster:
            clusters.append(current_cluster)
            current_cluster = []
if current_cluster:
    clusters.append(current_cluster)

cluster_sizes = [len(c) for c in clusters]
max_cluster_size = max(cluster_sizes) if cluster_sizes else 0

# Main performance calculation function
def calculate_performance(raw_data):
    # Use of enumerate and list comprehension
    critical_points = [i for i, v in enumerate(raw_data) if v >= 6]
    
    # Use of zip to pair consecutive critical points
    if len(critical_points) < 2:
        return len(raw_data) % 100
    
    intervals = [b - a for a, b in zip(critical_points, critical_points[1:])]
    stability_score = sum(1 for x in intervals if x <= 3)
    
    # Real logic path
    base = len(critical_points) * 10
    penalty = 0
    for i, interval in enumerate(intervals):
        if interval > 4:
            penalty += 3
    
    # Dummy recursive call (unused but looks important)
    def _helper(n):
        return n if n <= 1 else _helper(n-1) + _helper(n-2)
    
    return base - penalty + stability_score

# Key statement
final_score = calculate_performance(readings)
print(f"Result: {final_score}")