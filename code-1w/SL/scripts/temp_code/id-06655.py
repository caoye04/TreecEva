from collections import defaultdict

# Simulate developer contribution analysis with noise and side computations
def analyze_developer_activity(events):
    action_count = defaultdict(int)
    timestamps = []
    total_actions = 0

    for event in events:
        action = event['type']
        action_count[action] += 1
        total_actions += 1
        if 'timestamp' in event:
            timestamps.append(event['timestamp'])

    # Irrelevant timing statistics (distractor)
    avg_interval = (timestamps[-1] - timestamps[0]) / len(timestamps) if len(timestamps) > 1 else 0
    peak_hour = max(timestamps, default=0) % 24

    return action_count, total_actions, avg_interval, peak_hour

def calculate_complexity_score(lines_of_code, churn_rate):
    # Secondary computation not directly used but plausible
    if lines_of_code == 0:
        return 0.0
    base = (lines_of_code ** 0.5) * (1 + churn_rate)
    adjustment = 1 + (churn_rate > 0.3)
    return round(base / adjustment, 3)

def calculate_rating(contributions, penalty_factor):
    # Core logic embedded in multiple steps
    weights = {'commit': 3, 'pr_review': 2, 'issue': 1, 'doc_update': 1}
    raw_score = 0
    
    for action, count in contributions.items():
        raw_score += weights.get(action, 0) * count
    
    # Apply non-linear bonus for high activity
    bonus = 10 if raw_score > 50 else (5 if raw_score > 30 else 0)
    adjusted_score = raw_score + bonus
    
    # Apply penalty factor from external heuristic
    final_rating = adjusted_score * (1 - penalty_factor)
    
    # Additional distracting state
    normalized = final_rating / (raw_score + 1) if raw_score else 0
    efficiency_metric = (adjusted_score - raw_score) / (final_rating + 1e-5)
    
    return int(round(final_rating))

# Main execution
if __name__ == "__main__":
    # Real input data
    dev_events = [
        {'type': 'commit', 'timestamp': 1712050000},
        {'type': 'commit', 'timestamp': 1712050100},
        {'type': 'pr_review', 'timestamp': 1712050150},
        {'type': 'commit', 'timestamp': 1712050200},
        {'type': 'issue', 'timestamp': 1712050300},
        {'type': 'commit', 'timestamp': 1712050400},
        {'type': 'pr_review', 'timestamp': 1712050500},
        {'type': 'doc_update', 'timestamp': 1712050600},
        {'type': 'commit', 'timestamp': 1712050700},
        {'type': 'commit', 'timestamp': 1712050800},
        {'type': 'issue', 'timestamp': 1712050900}
    ]

    # Extract contribution counts
    actions, total, interval_stat, hour = analyze_developer_activity(dev_events)
    
    # Simulated codebase metrics (some used, some not)
    loc_changes = 1250
    churn = 0.28
    complexity = calculate_complexity_score(loc_changes, churn)  # Computed but not used in final score
    
    # Heuristic penalty based on churn
    penalty_factor = 0.15 if churn > 0.25 else 0.05
    
    # Critical statement
    final_score = calculate_rating(actions, penalty_factor)
    
    # Distractor: secondary evaluation
    if total > 10:
        scaling_factor = 1.1
    elif complexity > 50:
        scaling_factor = 1.05
    else:
        scaling_factor = 1.0  # Unused path
    
    # Output target result
    print(f"Result: {final_score}")