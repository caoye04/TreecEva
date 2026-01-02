from collections import defaultdict
import math

# Simulate a benchmarking system for algorithm performance across test cases
def evaluate_algorithm(test_outputs, expected):
    score = 0
    penalties = 0
    temp_scores = []
    
    for i, (output, expect) in enumerate(zip(test_outputs, expected)):
        if output == expect:
            score += 10
            temp_scores.append(10)
        elif abs(output - expect) <= 2:
            score += 5
            penalties += 1
            temp_scores.append(5)
        else:
            temp_scores.append(0)
            
    # Distractor: unused smoothing logic
    smoothed = [temp_scores[0]]
    for j in range(1, len(temp_scores)):
        smoothed.append(int(0.7 * temp_scores[j] + 0.3 * smoothed[j-1]))
    
    return score, penalties

# Misleading helper function that isn't used in final computation
def legacy_scoring(raw_data):
    total = 0
    for x in raw_data:
        total += int(math.sqrt(x ** 2))
    return total // len(raw_data) if raw_data else 0

# Another red herring: tracking execution metadata that goes unused
def track_execution_time(start, end):
    duration = end - start
    overhead = duration * 0.05
    adjusted = duration - overhead
    return adjusted

# Core evaluation logic
benchmark_results = [
    [12, 15, 14, 16, 13],
    [10, 10, 10, 10, 10],
    [8, 12, 9, 11, 10]
]

expected_values = [12, 10, 10]

# Irrelevant intermediate transformation
transformed_data = defaultdict(lambda: 0)
for idx, series in enumerate(benchmark_results):
    transformed_data[f'series_{idx}'] = sum(x % 7 for x in series)

# Real processing begins here
raw_totals = list(map(sum, benchmark_results))

# Use lambda to filter high-performing runs
is_high_performer = lambda total: total > 50
high_runs = list(filter(is_high_performer, raw_totals))

# Compute base scores using evaluate_algorithm
individual_scores = []
for result_set, expected in zip(benchmark_results, expected_values):
    base_score, fault_count = evaluate_algorithm(result_set, [expected]*len(result_set))
    individual_scores.append(base_score)

# Introduce distraction: complex weighting that is not used
weights = [0.8, 1.2, 0.9]
weighted_distractor = sum(individual_scores[i] * weights[i] for i in range(len(weights)))

# Actual logic path
aggregate = sum(individual_scores)
average_base = aggregate / len(individual_scores)

# Apply non-linear adjustment using logarithmic scaling
adjusted_perf = math.log(aggregate + 1) * 10

# Final scoring with conditional bonus
bonus = 15 if len(high_runs) >= 2 else 5

final_score = 0
final_score += int(adjusted_perf)
final_score += bonus

# This print is required for answer extraction
target_variable_value = final_score
print(f"Target result: {target_variable_value}")