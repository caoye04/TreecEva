from collections import defaultdict

# Simulate developer contribution analysis with noise and side computations
def analyze_developer_activity(events):
    activity_counts = defaultdict(int)
    event_types = ['commit', 'review', 'merge', 'issue']
    
    for event in events:
        if event in event_types:
            activity_counts[event] += 1

    # Irrelevant transformation (distractor)
    normalized = {k: v / (sum(activity_counts.values()) + 1e-5) for k, v in activity_counts.items()}
    
    return activity_counts

def compute_volatility(data):
    # Dummy volatility calculation (not used in final logic)
    if len(data) < 2:
        return 0.0
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    return sum(diffs) / len(diffs) if diffs else 0.0

def calculate_rating(contributions, penalty_factor):
    base_score = 0
    weights = {'commit': 3, 'review': 2, 'merge': 4, 'issue': 1}
    
    for ctype, count in contributions.items():
        base_score += weights.get(ctype, 0) * count
    
    # Apply penalty factor based on artificial metric
    spike_count = 0
    values = list(contributions.values())
    for i in range(1, len(values)):
        if values[i] > 2 * (values[i-1] + 1):
            spike_count += 1
    
    adjustment = spike_count * penalty_factor
    raw_rating = base_score - adjustment
    
    # Additional irrelevant smoothing (distractor)
    smoothed = raw_rating * 0.95 + 5
    
    # Final constrained score
    final_score = max(10, min(100, int(raw_rating)))
    
    return final_score

# Main execution block
if __name__ == "__main__":
    dev_events = [
        'commit', 'commit', 'review', 'commit', 'merge',
        'issue', 'review', 'commit', 'merge', 'merge',
        'commit', 'issue', 'review', 'commit'
    ]
    
    # Step 1: Analyze raw contributions
    contributions = analyze_developer_activity(dev_events)
    
    # Step 2: Compute unused volatility metric (distraction)
    counts_list = list(contributions.values())
    volatility = compute_volatility(counts_list)
    
    # Step 3: Introduce side calculation with string processing (distractor)
    event_log = " -> ".join(dev_events)
    fragment_length = len(event_log.split(' -> ')[5:10])
    
    # Step 4: Calculate auxiliary statistic (irrelevant)
    total_actions = sum(contributions.values())
    avg_per_type = total_actions / len(contributions) if contributions else 0
    
    # Step 5: Determine penalty factor from artificial rule
    penalty_factor = 3 if volatility > 0.5 else 2
    
    # Step 6: Critical statement - compute final rating
    final_score = calculate_rating(contributions, penalty_factor)
    
    # Output result
    print(f"Result: {final_score}")