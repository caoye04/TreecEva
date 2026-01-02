from functools import reduce
import math

# Simulate user interaction sequences and performance scoring
def analyze_user_flow():
    raw_events = [1, 2, 2, 3, 4, 4, 4, 5]
    event_count = {}
    for e in raw_events:
        event_count[e] = event_count.get(e, 0) + 1

    # Extract unique ranks based on frequency
    rank_set = {k for k, v in event_count.items() if v >= 2}

    # Irrelevant: Compute entropy (not used in final score)
    total = sum(event_count.values())
    entropy = sum(-(v/total) * math.log2(v/total) for v in event_count.values())

    # Weight assignment per rank (distraction: some weights are unused)
    all_weights = {1: 0.5, 2: 1.5, 3: 2.0, 4: 3.0, 5: 1.0}
    log_weights = {k: math.log(v + 1) for k, v in all_weights.items()}

    # Misleading intermediate: transform via lambda (unused)
    transform = lambda x, w: x ** w if x > 1 else 0
    dummy_scores = [transform(k, log_weights.get(k, 1)) for k in event_count.keys()]

    # State tracker with red herring counters
    state_log = []
    temp_sum = 0
    for i in range(3):
        temp_sum += i * 2
        state_log.append(temp_sum)

    # Core evaluation logic
    def evaluate_performance(ranks, weights):
        base = 10
        adjustment = 0
        for r in ranks:
            if r in weights:
                adjustment += weights[r] * r
        return int(base + adjustment)  # deterministic integer result

    # Key statement
    final_score = evaluate_performance(rank_set, log_weights)

    # Distractor: another function defined but not called
    def calculate_efficiency(seq):
        return reduce(lambda a, b: a * b % 100, seq, 1)

    # Output the required result
    print(f"Result: {final_score}")

    return final_score

# Execute
analyze_user_flow()