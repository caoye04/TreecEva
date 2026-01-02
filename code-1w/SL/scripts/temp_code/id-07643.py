from itertools import groupby

def calculate_final_score(ranks, data):
    # Remove duplicate ranks using set operations
    unique_ranks = set(ranks)
    sorted_ranks = sorted(unique_ranks, reverse=True)
    
    # Group performance data by value and compute average counts
    grouped_data = [list(group) for key, group in groupby(sorted(data))]
    avg_group_size = sum(len(g) for g in grouped_data) / len(grouped_data) if grouped_data else 0
    
    # Base score from top rank
    base_score = sorted_ranks[0] * 10 if sorted_ranks else 0
    
    # Bonus logic based on group density
    bonus = 5 if avg_group_size >= 3 else 2
    
    # Apply conditional expression to adjust score based on rank count
    adjustment = -3 if len(unique_ranks) < 3 else 0
    
    final_score = base_score + bonus + adjustment
    return final_score

# Input data
rank_set = [8, 5, 8, 3, 5, 9]
performance_data = [20, 20, 20, 15, 15, 10]

# Additional irrelevant variables (minimal distraction - intervention level 5)
baseline = 100
threshold = 4.5
placeholder_list = [x * 2 for x in range(5)]

final_score = calculate_final_score(rank_set, performance_data)
print(f"Result: {final_score}")