from collections import defaultdict

# Simulate developer contribution analysis with noise and side computations
def analyze_developer_activity(logs):
    activity_count = defaultdict(int)
    time_spent = 0
    idle_periods = 0

    for entry in logs:
        action, duration = entry['action'], entry['duration']
        activity_count[action] += 1
        time_spent += duration

        if duration > 100:
            idle_periods += 1

    # Irrelevant aggregation (distractor)
    total_actions = sum(activity_count.values())
    avg_duration = time_spent / len(logs) if logs else 0

    return dict(activity_count), time_spent

# Secondary function with misleading complexity
def compute_efficiency_metric(data, threshold=5):
    efficiency = 0
    overhead = 0

    for k, v in data.items():
        if len(k) % 2 == 0:
            efficiency += v * 0.1
        else:
            efficiency -= v * 0.05
        overhead += v * 0.01  # Unused variable

    # Fake normalization
    normalized = efficiency / (overhead + 1e-8) if overhead > 0 else efficiency
    return efficiency  # Only efficiency matters

# Core logic obscured by auxiliary steps
def calculate_rating(contributions, penalty_factor):
    base_rating = 0
    bonus_tracker = []
    temp_adjustment = 0

    # Real computation mixed with distractions
    for i, (contributor, lines) in enumerate(contributions.items()):
        if lines > 200:
            base_rating += 10
            bonus_tracker.append(i)
        elif lines > 100:
            base_rating += 5
        else:
            base_rating += 2

        # Distractor: unrelated adjustment
        if i % 3 == 0:
            temp_adjustment -= 1

    # Real penalty application
    if penalty_factor > 0:
        base_rating -= int(base_rating * penalty_factor)

    # Fake post-processing
    smoothing = sum(bonus_tracker) * 0.01
    final_value = base_rating - smoothing  # Smoothing has negligible effect

    return int(final_value)

# Main execution with red herrings
if __name__ == "__main__":
    # Input data
    dev_logs = [
        {'action': 'commit', 'duration': 45},
        {'action': 'push', 'duration': 120},
        {'action': 'edit', 'duration': 67},
        {'action': 'commit', 'duration': 33},
        {'action': 'review', 'duration': 89}
    ]

    # Step 1: Analyze logs (produces side results)
    actions, total_time = analyze_developer_activity(dev_logs)

    # Step 2: Compute irrelevant efficiency metric
    fake_metric = compute_efficiency_metric(actions)

    # Step 3: Prepare real input
    contributions = {
        'alice': 250,
        'bob': 150,
        'charlie': 300,
        'diana': 80
    }

    # Step 4: Introduce decoy calculation
    phantom_score = 0
    for val in contributions.values():
        if val % 25 == 0:
            phantom_score += 3
    phantom_score *= 0.5  # Not used

    # Step 5: Actual target computation
    penalty_factor = 0.2
    final_score = calculate_rating(contributions, penalty_factor)

    # Output result as required
    print(f"Result: {final_score}")