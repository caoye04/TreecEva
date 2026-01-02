from collections import defaultdict
from itertools import combinations

# Simulate user feedback analysis for a training module
feedback_data = [4, 5, 3, 4, 5, 2, 3, 4, 4, 5, 1, 2, 3, 4, 5]

def analyze_trends(data):
    trend_counter = defaultdict(int)
    increases = 0
    decreases = 0
    
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            increases += 1
            trend_counter['up'] += 1
        elif data[i] < data[i-1]:
            decreases += 1
            trend_counter['down'] += 1
        else:
            trend_counter['stable'] += 1
    
    # Distractor computation: calculate average fluctuation (not used later)
    total_fluctuation = sum(abs(data[i] - data[i-1]) for i in range(1, len(data)))
    avg_fluctuation = total_fluctuation / len(data) if data else 0
    
    return trend_counter, increases, decreases

def compute_diversity_score(data):
    freq = defaultdict(int)
    for val in data:
        freq[val] += 1
    
    # Shannon diversity index approximation
    diversity = 0.0
    total = len(data)
    for count in freq.values():
        p = count / total
        if p > 0:
            diversity -= p * p
    
    # Irrelevant transformation
    normalized_diversity = (diversity + 1) * 10
    return normalized_diversity

def generate_pairs(data):
    # Generate all possible pairs (unused in final logic)
    pair_list = list(combinations(data, 2))
    pair_sum_avg = sum(a + b for a, b in pair_list) / len(pair_list) if pair_list else 0
    return int(pair_sum_avg)

def evaluate_performance(feedback_sequence):
    # Core logic starts here
    trend_stats, up_count, down_count = analyze_trends(feedback_sequence)
    diversity_metric = compute_diversity_score(feedback_sequence)
    
    # Secondary distractor: unused deep analysis
    long_run_stable = 0
    current_run = 1
    for i in range(1, len(feedback_sequence)):
        if feedback_sequence[i] == feedback_sequence[i-1]:
            current_run += 1
        else:
            long_run_stable = max(long_run_stable, current_run)
            current_run = 1
    long_run_stable = max(long_run_stable, current_run)
    
    # Key calculation components
    improvement_ratio = up_count / (down_count + 1)
    consistency_bonus = 1 if trend_stats['stable'] > 3 else 0
    base_score = sum(feedback_sequence) / len(feedback_sequence)
    
    # Final performance score
    raw_score = base_score * improvement_ratio
    adjusted_score = raw_score + consistency_bonus + (diversity_metric * 0.1)
    
    # Apply arbitrary scaling and round
    final_score = int(adjusted_score * 10)
    
    # This print is required to expose the result
    print(f"Result: {final_score}")
    return final_score

# Execution entry point
final_score = evaluate_performance(feedback_data)