from collections import Counter, defaultdict

# Simulate user interaction logs with redundant and irrelevant metrics
def analyze_user_engagement(logs):
    event_count = Counter()
    temporal_gaps = []
    total_actions = 0
    idle_time = 0  # Distractor: not used later

    for entry in logs:
        event_count[entry['action']] += 1
        total_actions += 1

    # Irrelevant computation (dead-end)
    avg_frequency = total_actions / (len(event_count) or 1)
    normalized_bias = sum([v ** 0.5 for v in event_count.values()]) if event_count else 0

    return event_count

# Assess system responsiveness — partially relevant but mostly distraction
def measure_latency(events):
    response_times = []
    latency_summary = defaultdict(int)

    for e in events:
        if 'response_ms' in e:
            response_times.append(e['response_ms'])

    if response_times:
        latency_summary['mean'] = sum(response_times) / len(response_times)
        latency_summary['peak'] = max(response_times)
        latency_summary['optimized_count'] = sum(1 for t in response_times if t < 100)

    # Unused derived values (distractors)
    improvement_factor = latency_summary['mean'] * 0.85 if latency_summary else 0
    stability_index = len(response_times) - latency_summary.get('peak', 0) // 10

    return latency_summary  # Not actually used

# Core logic disguised among noise
def evaluate_performance(feedback, rating):
    base = sum(feedback.values())
    penalty = 0

    # Conditional penalties based on feedback types
    if feedback.get('error', 0) > 5:
        penalty += 15
    if feedback.get('timeout', 0) > 3:
        penalty += 10
    if feedback.get('retry', 0) == 0:
        penalty -= 5  # Reward for no retries

    score = base - penalty

    # Additional conditional adjustment
    if rating > 80:
        score += 10
    elif rating < 50:
        score -= 20
    else:
        score += 5

    return int(score)

# Main execution flow
if __name__ == '__main__':
    # Simulated raw data input
    raw_logs = [
        {'action': 'click', 'timestamp': 100},
        {'action': 'error', 'timestamp': 105},
        {'action': 'retry', 'timestamp': 110},
        {'action': 'submit', 'timestamp': 120},
        {'action': 'error', 'timestamp': 125},
        {'action': 'navigate', 'timestamp': 130},
        {'action': 'click', 'timestamp': 135},
        {'action': 'timeout', 'timestamp': 140},
        {'action': 'click', 'timestamp': 145}
    ]

    # Extract engagement insights (uses Counter)
    feedback_counter = analyze_user_engagement(raw_logs)

    # Simulate secondary system metric (uses defaultdict, irrelevant)
    system_events = [
        {'type': 'api_call', 'response_ms': 120},
        {'type': 'query', 'response_ms': 95},
        {'type': 'update', 'response_ms': 200},
        {'type': 'fetch', 'response_ms': 80}
    ]
    performance_metrics = measure_latency(system_events)  # Computed but unused

    # Derived rating from logs — semi-relevant preprocessing
    total_interactions = sum(feedback_counter.values())
    error_count = feedback_counter.get('error', 0) + feedback_counter.get('timeout', 0)
    success_rate = (total_interactions - error_count) / total_interactions if total_interactions else 0
    efficiency_rating = int(success_rate * 100)

    # Key statement containing target variable
    final_score = evaluate_performance(feedback_counter, efficiency_rating)

    print(f"Result: {final_score}")