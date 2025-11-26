import itertools

def compute_ranking_score(data_points):
    # Distractor: unnecessary tuple operations
    redundant_tuples = [(x, x*2) for x in range(5, 15)]
    misleading_sum = sum(x[1] for x in redundant_tuples)
    
    # Main logic: process data with conditional expressions
    filtered_data = [x if x % 3 != 0 else x // 2 for x in data_points]
    sorted_data = sorted(filtered_data, reverse=True)
    
    # Distractor: dead code path with string operations
    fake_metrics = "score:85,rank:3,tier:gold"
    parsed_metrics = fake_metrics.split(',')
    unused_score = int(parsed_metrics[0].split(':')[1])  # Dead code
    
    # Key computation: combinatorics with filtering
    combinations = list(itertools.combinations(sorted_data[:4], 2))
    valid_pairs = [pair for pair in combinations if abs(pair[0] - pair[1]) > 5]
    
    # Distractor: misleading intermediate calculation
    distraction_value = len(valid_pairs) * misleading_sum // 10
    
    # Final score calculation
    base_score = sum(sorted_data[:3])
    bonus = len(valid_pairs) * 7
    penalty = sum(1 for x in data_points if x % 4 == 0) * 3
    
    return base_score + bonus - penalty

# Main execution
raw_data = [12, 8, 25, 17, 9, 31, 6, 19, 14, 27]

# Distractor: irrelevant data processing
processed_data = [x + 2 if x > 15 else x - 1 for x in raw_data]
unused_calc = sum(processed_data[::2])  # Dead variable

# Target computation
final_score = compute_ranking_score(processed_data)
print(f"Result: {final_score}")