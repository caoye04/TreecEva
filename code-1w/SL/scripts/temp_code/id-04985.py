def process_metrics(entries, limit):
    filtered = [x for x in entries if x > limit]
    squared = [x ** 2 for x in filtered]
    sum_sq = sum(squared)
    
    # Distractor: irrelevant transformation on strings
    labels = ['item_' + str(i) for i in range(len(entries))]
    upper_labels = [label.upper() for label in labels]
    sliced_labels = upper_labels[::2]  # unused

    # Red herring computation
    temp_avg = sum(entries) / len(entries) if entries else 0
    adjusted = [x - temp_avg for x in squared]  # partially used but not critical
    
    # Conditional expression affecting final result
    penalty = len(entries) > 5 else 0
    penalty_factor = 10 if penalty else 0

    # Actual key logic
    base_score = sum_sq // (len(filtered) or 1)
    secondary_correction = len(sliced_labels) * 3  # misleading, but named similarly
    correction = len(filtered) * 2  # relevant

    # String method used idiomatically but not central
    debug_info = "Metrics computed: " + "_".join(sliced_labels).replace("ITEM", "DEBUG")

    # Final computation
    final_score = base_score - penalty_factor + correction
    return final_score

# Main execution
raw_data = [3, 7, 2, 9, 4, 8]
threshold = 5
data_points = sorted(raw_data, reverse=True)

# Simulate intermediate inspection point
snapshot = data_points[:3]
size_hint = len(snapshot) * 100  # unused distractor

final_score = process_metrics(data_points, threshold)
print(f"Result: {final_score}")