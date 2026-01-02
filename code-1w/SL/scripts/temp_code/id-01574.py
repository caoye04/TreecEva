from collections import defaultdict, Counter

# Simulate cognitive load assessment in a multitasking environment
def analyze_workload(tasks, stress_threshold=7):
    load_map = defaultdict(int)
    complexity_weights = {"critical": 3, "high": 2, "medium": 1, "low": 0}
    feedback_levels = []

    for idx, (task, priority, duration) in enumerate(tasks):
        base_load = complexity_weights.get(priority, 0) * duration
        context_factor = (idx + 1) % 4 / 2.0
        adjusted_load = base_load + context_factor

        # Distractor: irrelevant tracking
        if duration > 5:
            load_map["long_tasks"] += 1

        # Real logic branch
        if adjusted_load > stress_threshold:
            feedback_levels.append(3)
        elif adjusted_load > 4:
            feedback_levels.append(2)
        else:
            feedback_levels.append(1)

        # Dead code path (never alters outcome)
        temp_snapshot = [x for x in load_map.values()]
        if len(temp_snapshot) > 10:
            break  # Unreachable due to input size

    return feedback_levels


def compute_entropy(values):
    # Irrelevant function - looks useful but not used in final path
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, misleading
    return round(entropy, 4)


def aggregate_performance(levels, scaling_factors):
    cumulative = 0
    history = []

    for i, (level, weight) in enumerate(zip(levels, scaling_factors)):
        contribution = level * weight
        adjustment = (i % 3) - 1  # [-1, 0, 1] cycle
        net_effect = contribution + adjustment

        # Only positive contributions are retained
        if net_effect > 0:
            cumulative += net_effect
        else:
            cumulative -= (-net_effect) * 0.5  # partial penalty

        history.append(cumulative)

    # Apply non-linear boost at the end
    if cumulative > 10:
        cumulative *= 1.25
    elif cumulative > 5:
        cumulative *= 1.1

    return int(cumulative)

# Main execution
if __name__ == "__main__":
    # Input data
    task_list = [
        ("debugger", "critical", 4),
        ("scheduler", "high", 6),
        ("validator", "medium", 3),
        ("parser", "critical", 5),
        ("analyzer", "high", 4)
    ]

    # Irrelevant preprocessing
    task_names = [t[0] for t in task_list]
    name_length_map = {name: len(name) for name in task_names}
    total_chars = sum(name_length_map.values())

    # Unused transformation
    reversed_pairs = list(zip(*reversed(list(enumerate(task_list)))))[1]

    # Real pipeline
    feedback = analyze_workload(task_list, stress_threshold=6.5)

    # Weight vector – aligned with feedback
    weights = [1.0, 1.8, 1.2, 2.0, 1.5]

    # Distractor: unused alternative weighting
    alt_weights = [w * 0.9 + (i % 2) * 0.3 for i, w in enumerate(weights)]

    # Key computation
    final_score = aggregate_performance(feedback, weights)

    # Additional red herring
    snapshot = sorted(feedback, reverse=True)
    peak = snapshot[0] if snapshot else 0
    decay_factor = sum(1 / (i + 1) for i in range(len(snapshot)))

    # Output result as required
    print(f"Result: {final_score}")