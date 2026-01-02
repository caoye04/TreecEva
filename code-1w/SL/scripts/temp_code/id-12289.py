from collections import defaultdict, Counter

def analyze_performance(logs):
    # Track user attempts and outcomes
    attempts = defaultdict(int)
    successes = defaultdict(int)
    failure_modes = Counter()

    # Irrelevant intermediate statistics
    total_events = 0
    redundant_sum = 0
    temporal_weights = [1.0, 0.9, 0.8]  # Unused decay factors

    for log in logs:
        user = log['user']
        action = log['action']
        result = log['result']
        timestamp = log.get('ts', 0)

        attempts[user] += 1
        total_events += 1

        if action == 'submit_solution':
            if result == 'correct':
                successes[user] += 1
            else:
                failures = log.get('errors', [])
                for err in failures:
                    failure_modes[err] += 1

        # Distractor block: computes but doesn't impact final score
        if result == 'timeout':
            redundant_sum += len(action) * 2

    # Secondary metric with no downstream use
    avg_attempt_count = sum(attempts.values()) / len(attempts) if attempts else 0

    return attempts, successes, failure_modes


def compute_final_score(user_data, baseline_ref=None):
    raw_scores = {}
    penalty_adjustments = {}
    auxiliary_metric = 0

    for user, attempts in user_data.items():
        base_score = 100
        timeout_penalties = 0
        complexity_bonus = 0

        # Simulate historical adjustment (unused)
        legacy_factor = 0.95

        for attempt in range(attempts):
            if attempt > 2:
                timeout_penalties += 5
            if attempt % 3 == 0:
                complexity_bonus += 2

        adjusted_score = base_score - timeout_penalties + complexity_bonus
        raw_scores[user] = adjusted_score

        # Dead code path — never accessed
        if baseline_ref and user in baseline_ref:
            delta = adjusted_score - baseline_ref[user]
            auxiliary_metric += abs(delta)

    # Real computation for final score
    valid_scores = [score for score in raw_scores.values() if score >= 60]
    if not valid_scores:
        return 0

    mean_valid = sum(valid_scores) / len(valid_scores)
    outlier_threshold = mean_valid * 0.75
    filtered = [s for s in valid_scores if s >= outlier_threshold]

    final_score = int(round(sum(filtered) / len(filtered)))

    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Main execution
if __name__ == "__main__":
    log_data = [
        {'user': 'alice', 'action': 'compile_code', 'result': 'success'},
        {'user': 'alice', 'action': 'submit_solution', 'result': 'correct'},
        {'user': 'bob', 'action': 'submit_solution', 'result': 'error', 'errors': ['logic_error']},
        {'user': 'bob', 'action': 'submit_solution', 'result': 'timeout'},
        {'user': 'bob', 'action': 'submit_solution', 'result': 'timeout'},
        {'user': 'charlie', 'action': 'submit_solution', 'result': 'correct'},
        {'user': 'charlie', 'action': 'submit_solution', 'result': 'correct'},
        {'user': 'charlie', 'action': 'submit_solution', 'result': 'correct'},
        {'user': 'diana', 'action': 'submit_solution', 'result': 'error', 'errors': ['syntax_error']},
        {'user': 'diana', 'action': 'submit_solution', 'result': 'error', 'errors': ['logic_error']},
        {'user': 'diana', 'action': 'submit_solution', 'result': 'error', 'errors': ['runtime_error']},
        {'user': 'diana', 'action': 'submit_solution', 'result': 'timeout'}
    ]

    # Extract data using analysis function
    attempts_map, successes_map, failures_counter = analyze_performance(log_data)

    # Compute final score based on attempt counts
    final_score = compute_final_score(attempts_map)
