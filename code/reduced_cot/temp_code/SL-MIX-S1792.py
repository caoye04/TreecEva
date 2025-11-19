from collections import defaultdict

def compute_optimal_hub():
    # District efficiency mapping
    district_parcels = {'A': 120, 'B': 85, 'C': 145, 'D': 95, 'E': 160}
    base_scores = {'A': 75, 'B': 80, 'C': 70, 'D': 85, 'E': 65}
    
    # Dynamic programming storage
    dp_scores = defaultdict(int)
    
    # Compute adjusted scores using ternary logic
    for district, parcels in district_parcels.items():
        threshold = 100
        adjusted = base_scores[district] + 10 if parcels >= threshold else base_scores[district] - 5
        dp_scores[district] = max(dp_scores[district], adjusted)
    
    # Convert to sorted list for binary search
    sorted_scores = sorted(dp_scores.values())
    
    # Binary search for optimal hub (closest to average score)
    target = sum(sorted_scores) // len(sorted_scores)
    left, right = 0, len(sorted_scores) - 1
    optimal_index = 0
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_scores[mid] <= target:
            optimal_index = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return optimal_index

hub_index = compute_optimal_hub()
print(f"Result: {hub_index}")