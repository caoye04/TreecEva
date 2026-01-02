from collections import defaultdict

def analyze_user_behavior(data):
    # Simulate processing of user interaction logs
    total_events = 0
    session_count = 0
    idle_time = 0
    temp_sum = 0

    event_types = defaultdict(int)
    latency_samples = []

    for session in data:
        session_count += 1
        local_events = 0
        max_gap = 0
        prev_timestamp = 0

        for i, (ts, evt, dur) in enumerate(session):
            total_events += 1
            local_events += 1
            event_types[evt] += 1
            latency_samples.append(dur)

            if i > 0:
                gap = ts - prev_timestamp
                if gap > max_gap:
                    max_gap = gap
            prev_timestamp = ts

        if local_events < 3:
            idle_time += 1
        temp_sum += local_events ** 0.5

    avg_latency = sum(latency_samples) / len(latency_samples) if latency_samples else 0
    high_latency = sum(1 for x in latency_samples if x > 500)

    # Irrelevant aggregation
    dummy_agg = sum(v * (k.count('click') + 1) for k, v in event_types.items())

    engagement = total_events / session_count if session_count else 0
    penalty_factor = idle_time * 0.5

    return engagement, avg_latency, penalty_factor, high_latency


def process_metrics(e, l):
    base = e * 10
    if l < 200:
        modifier = 1.5
    elif l < 400:
        modifier = 1.2
    else:
        modifier = 0.8

    # Distractor calculation
    debug_value = (e + l) / (l + 1)
    extra_boost = 0
    if e > 15 and l < 300:
        extra_boost = 5

    result = base * modifier + extra_boost
    return int(result)

# Main execution
user_sessions = [
    [(100, 'view', 150), (200, 'click', 300), (250, 'hover', 100)],
    [(100, 'click', 600), (300, 'view', 200), (400, 'click', 180), (600, 'submit', 900)],
    [(50, 'view', 100), (150, 'click', 250)],
    [(100, 'view', 800), (500, 'click', 700), (700, 'scroll', 120)]
]

engagement, latency, _, _ = analyze_user_behavior(user_sessions)

# Key computation point
final_score = process_metrics(engagement, latency)

print(f"Result: {final_score}")