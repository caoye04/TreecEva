def analyze_user_behavior(raw_logs):
    parsed_data = []
    temp_buffer = []
    total_events = 0
    redundant_sum = 0  # distractor

    for log in raw_logs:
        if not log.get('active', True):
            continue
        action_type = log['type']
        timestamp = log['ts']
        payload = log['data']

        # Irrelevant filtering (distractor)
        if action_type == 'hover':
            redundant_sum += len(payload) % 7
            continue

        # Real processing path
        if action_type in ['click', 'submit']:
            duration = payload.get('duration', 0)
            confidence = 1 if duration > 50 else 0.5
            temp_buffer.append({'time': timestamp, 'conf': confidence})

        total_events += 1

    parsed_data = sorted(temp_buffer, key=lambda x: x['time'])
    return parsed_data


def compute_baseline_score(events):
    base = 0
    offset = 3  # red herring
    for e in events:
        base += int(e['conf'] * 10)
    scaling_factor = 0.95  # misleading comment: "used in final calc" (it's not)
    return base * 0.1


def evaluate_sequence(patterns):
    score = 0
    streak = 0
    for p in patterns:
        if p['conf'] == 1:
            streak += 1
            score += streak * 0.5
        else:
            streak = 0
    decayed = score * 0.8  # unused variable - dead end
    return score


def aggregate_performance(logs, weights):
    cleaned = analyze_user_behavior(logs)
    if not cleaned:
        return 0.0

    base_score = compute_baseline_score(cleaned)
    sequence_bonus = evaluate_sequence(cleaned)

    # Distractor variables
    phantom_weight = weights.get('rare_event', 0.1)
    dummy_offset = sum(1 for c in str(base_score) if c.isdigit()) % 5  # irrelevant

    # Actual calculation
    w1 = weights.get('primary', 1.2)
    w2 = weights.get('temporal', 0.8)
    intermediate = base_score * w1 + sequence_bonus * w2

    # Conditional expression (required feature)
    penalty = 5.0 if len(cleaned) < 3 else 2.0 if len(cleaned) < 6 else 0.0

    # Final logic step with slicing (required feature): use only last 4 entries for adjustment
    recent = cleaned[-4:]
    adjustment = sum(r['conf'] for r in recent) * 0.3

    final_score = intermediate - penalty + adjustment

    # Dead code path - never reached due to structure
    if False and dummy_offset > 10:
        final_score += phantom_weight * 100

    return final_score

# Main execution
log_entries = [
    {'type': 'hover', 'ts': 100, 'data': {'duration': 30}, 'active': True},
    {'type': 'click', 'ts': 105, 'data': {'duration': 65}, 'active': True},
    {'type': 'submit', 'ts': 110, 'data': {'duration': 40}, 'active': True},
    {'type': 'click', 'ts': 115, 'data': {'duration': 70}, 'active': True},
    {'type': 'click', 'ts': 120, 'data': {'duration': 80}, 'active': True},
    {'type': 'click', 'ts': 125, 'data': {'duration': 55}, 'active': True},
    {'type': 'click', 'ts': 130, 'data': {'duration': 90}, 'active': True}
]

user_weights = {
    'primary': 1.2,
    'temporal': 0.8,
    'rare_event': 0.5  # unused in real path
}

final_score = aggregate_performance(log_entries, user_weights)
print(f"Result: {final_score}")