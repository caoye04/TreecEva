import itertools

# System load simulation with optimization
base_load = [34, 56, 23, 78, 45, 89, 12, 67]
thresholds = [40, 60, 80]

# Distractor: Historical data not used in final computation
daily_avg_loads = [45, 48, 52, 55, 53, 50, 47]
peak_history = {day: max(base_load) - day * 2 for day in range(7)}

# Irrelevant transformation chain
temp_weights = [x * 0.9 + 5 for x in base_load]
scaled_weights = [w / sum(temp_weights) for w in temp_weights]
weighted_sum = sum(w * i for i, w in enumerate(scaled_weights))

# Real logic begins: categorize and redistribute load
load_categories = []
for val in base_load:
    category = 0
    for t in thresholds:
        if val >= t:
            category += 1
    load_categories.append(category)

# Use of zip and enumerate (required Python features)
categorized_pairs = list(zip(base_load, load_categories))
indexed_adjustments = []
for idx, (val, cat) in enumerate(categorized_pairs):
    adjustment_factor = 1 + (cat * 0.1)
    adjusted = val * adjustment_factor
    # Introduce minor distractor computation
    _ = adjusted * 0.95  # unused
    indexed_adjustments.append(adjusted)

# Secondary processing using itertools.groupby
sorted_pairs = sorted(categorized_pairs, key=lambda x: x[1])
grouped_by_category = [
    list(group) for k, group in itertools.groupby(sorted_pairs, key=lambda x: x[1])
]

category_averages = {
    group[0][1]: sum(item[0] for item in group) / len(group)
    for group in grouped_by_category
}

# Optimization function with embedded distractor variables
def optimize_distribution(load, thres):
    total = sum(load)
    count = len(load)
    
    # Unused statistical measures
    mean = total / count
    variance_proxy = sum((x - mean) ** 2 for x in load) / count
    entropy_shadow = -sum((x/total) * ((x/total)+1e-9) for x in load)
    
    # Core logic: apply threshold-based scaling
    scaled_load = []
    for x in load:
        level = 0
        for t in thres:
            if x > t:
                level += 1
        scale = 1 + (level * 0.05)
        scaled_load.append(x * scale)
    
    # Final aggregation with rounding
    aggregated = sum(scaled_load)
    normalized = round(aggregated / 1.15, 2)  # arbitrary normalization factor
    
    # Distractor: unused branching
    if normalized > 1000:
        flag_override = True
        result = normalized - 100
    else:
        flag_override = False
        result = normalized  # actual path taken
    
    return int(result)

# Key execution point
final_load = optimize_distribution(base_load, thresholds)
print(f"Result: {final_load}")