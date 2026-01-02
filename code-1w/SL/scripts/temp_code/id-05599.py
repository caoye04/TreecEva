from collections import defaultdict
from itertools import permutations

# Simulate system performance metrics
def analyze_throughput(data_points):
    total = sum(data_points)
    average = total / len(data_points)
    variance = sum((x - average) ** 2 for x in data_points) / len(data_points)
    return average, variance

def count_transitions(sequence):
    transitions = 0
    state_log = []
    for i in range(len(sequence) - 1):
        if sequence[i] != sequence[i + 1]:
            transitions += 1
            state_log.append((sequence[i], sequence[i + 1]))
    # Irrelevant computation (distractor)
    unused_entropy = len(state_log) * 1.5 if state_log else 0
    return transitions

def evaluate_performance(efficiency, errors):
    base = efficiency * 100
    penalty = errors * 5
    adjustment = 10 if efficiency > 0.8 else 0
    final_score = base - penalty + adjustment
    return int(final_score)

# Main execution
if __name__ == "__main__":
    # Input data
    raw_metrics = [0.78, 0.82, 0.85, 0.79, 0.81]
    error_count = 3
    status_sequence = [1, 1, 0, 0, 1, 1, 1, 0]

    # Step 1: Analyze throughput (used)
    avg_efficiency, var = analyze_throughput(raw_metrics)

    # Step 2: Count state transitions (semi-relevant, used for distraction)
    switch_count = count_transitions(status_sequence)

    # Step 3: Prepare efficiency metric (used)
    normalized_efficiency = avg_efficiency / 1.0  # Identity op (distractor)

    # Step 4: Simulate load distribution (dead code path - distractor)
    load_profile = defaultdict(int)
    for perm in permutations([1, 2, 3], 3):
        load_profile[perm[0]] += 1
    total_load = sum(load_profile.values())  # Computed but unused

    # Step 5: Compute auxiliary statistic (irrelevant)
    cumulative_shift = 0
    for i in range(5):
        cumulative_shift += (i * 2) >> 1  # Bit shift distraction

    # Step 6: Key logic - determine final score (answer point)
    efficiency = avg_efficiency
    final_score = evaluate_performance(efficiency, error_count)

    # Output result
    print(f"Result: {final_score}")