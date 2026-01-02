from itertools import combinations

def process_rankings(ranks, threshold):
    rank_set = set(ranks)
    filtered_ranks = {r for r in rank_set if r >= threshold}
    
    # Irrelevant distraction: unused variable (low interference)
    temp_result = [x * 2 for x in ranks]
    
    # Generate all pairs and compute average rank
    if len(filtered_ranks) < 2:
        return min(filtered_ranks, default=0)
    
    avg_pairs = []
    for pair in combinations(filtered_ranks, 2):
        avg_pairs.append((pair[0] + pair[1]) / 2.0)
    
    # Compute median-like central value
    sorted_avgs = sorted(avg_pairs)
    mid = len(sorted_avgs) // 2
    median_avg = sorted_avgs[mid] if len(sorted_avgs) % 2 == 1 else (sorted_avgs[mid-1] + sorted_avgs[mid]) / 2
    
    # Final transformation using integer division and case logic
    base_value = int(median_avg)
    adjustment = len(filtered_ranks) // 3
    final_score = base_value + adjustment
    return final_score

# Input data
rank_list = [85, 90, 78, 92, 88, 76]
cutoff = 80

# Key computation
final_score = process_rankings(rank_list, cutoff)
print(f"Target result: {final_score}")