from itertools import combinations

# Simulate sensor data with noise filtering and ranking logic
def preprocess_ranks(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    sorted_vals = sorted(filtered, reverse=True)
    return [val - 10 for val in sorted_vals if val % 2 == 0]

# Misleading auxiliary function (not directly used in final score)
def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Core scoring logic with distractors
def calculate_final_score(ranks, penalties):
    base_total = sum(ranks)
    
    # Irrelevant statistical computation (distractor)
    avg_rank = sum(ranks) / len(ranks) if ranks else 0
    outlier_count = len([r for r in ranks if r > avg_rank * 1.5])
    
    # Real logic: apply penalty map
    penalty_sum = 0
    for i, rank in enumerate(ranks):
        key = i % 4
        if key in penalties:
            penalty_sum += penalties[key]
    
    # Additional distraction: unused combination analysis
    pair_sums = [sum(pair) for pair in combinations(ranks, 2)]
    high_pairs = [p for p in pair_sums if p > 50]
    
    # Final computation
    adjustment = len(high_pairs) - outlier_count  # minor influence via adjustment
    final_score = base_total - penalty_sum + adjustment
    
    return final_score

# Main execution
raw_sensor_data = [15, 22, 8, 94, 67, 88, 73, 102, 44, 55, 96]
dropped_readings = [x for x in raw_sensor_data if x < 10 or x > 100]  # irrelevant tracking

rank_data = preprocess_ranks(raw_sensor_data)
penalty_map = {0: 5, 1: 3, 2: 8, 3: 1}

# Dead code path (never executed)
if False:
    fallback = sum(dropped_readings) // 10

final_score = calculate_final_score(rank_data, penalty_map)
print(f"Result: {final_score}")