from collections import defaultdict

# Simulate user interaction logs with action counts
def generate_metrics():
    metrics = defaultdict(int)
    actions = ['click', 'hover', 'scroll', 'click', 'click', 'keypress', 'scroll', 'hover']
    for action in actions:
        metrics[action] += 1
    return metrics

# Determine bonus based on specific interaction patterns
def evaluate_engagement(metrics):
    bonus_flags = {}
    bonus_flags['high_clicks'] = metrics['click'] > 2
    bonus_flags['engaged_scroller'] = metrics['scroll'] >= 2
    bonus_flags['passive'] = metrics['hover'] == 2 and metrics['keypress'] < 1
    return bonus_flags

# Calculate final performance score based on flags and metric values
def calculate_performance(bonus_flags, metrics):
    base = metrics['click'] * 2 + metrics['scroll']
    if bonus_flags['high_clicks']:
        base += 5
    if bonus_flags['engaged_scroller']:
        base += 3
    if bonus_flags['passive']:
        base -= 4
    return base

# Irrelevant utility function (minor distraction)
def unused_helper():
    return "This does nothing important"

# Main execution flow
metrics = generate_metrics()
bonus_flags = evaluate_engagement(metrics)
final_score = calculate_performance(bonus_flags, metrics)

# Print result for verification
print(f"Result: {final_score}")