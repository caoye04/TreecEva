def process_results(data, limits):
    # Irrelevant transformation (distractor)
    normalized = [round((x - min(data)) / (max(data) - min(data)) * 100) for x in data]
    
    # Semi-relevant filtering (some values used later)
    filtered = [x for x in data if x > sum(data) // len(data)]
    
    # Red herring computation
    outlier_check = [x for x in data if abs(x - sum(data)/len(data)) > 2 * (max(data)-min(data))/len(data)]
    anomaly_count = len(outlier_check)  # Not actually used

    # Key slicing operation to extract evaluation window
    window = data[1:-1]  # Exclude first and last

    # Core logic: count how many exceed each threshold, then combine
    high_performers = 0
    for val in window:
        for limit in limits:
            if val >= limit:
                high_performers += 1
                break  # Count once per value
    
    # Secondary metric (distraction)
    avg_normalized_top = sum(normalized[:5]) / len(normalized[:5]) if len(normalized) > 5 else 0

    # Final scoring logic
    base_score = len([x for x in filtered if x % 2 == 1])  # odd numbers in above-average group
    bonus = len(limits) * 2
    penalty = len([x for x in data if x < limits[0]]) // 2
    
    final_score = base_score + bonus - penalty + high_performers

    return final_score

# Input data
assessment_data = [85, 92, 78, 96, 88, 70, 91, 87]
thresholds = [80, 90, 95]

# Execution point
final_score = process_results(assessment_data, thresholds)
print(f"Result: {final_score}")