from itertools import combinations

def process_ratings(ratings, base):
    adjusted = [round((r + base) / 1.5) for r in ratings]
    pairs = list(combinations(adjusted, 2))
    valid_pairs = {pair for pair in pairs if abs(pair[0] - pair[1]) <= 3}
    
    # Irrelevant distraction: unused variable (minimal interference)
    max_pair_sum = max(sum(p) for p in pairs)  
    
    count = len(valid_pairs)
    total = sum(adjusted)
    final_score = total - count
    return final_score

# Main execution
baseline = 2
user_ratings = [4, 5, 3, 7, 5]
final_score = process_ratings(user_ratings, baseline)
print(f"Result: {final_score}")