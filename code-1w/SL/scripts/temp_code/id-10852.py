from collections import defaultdict, Counter

# Simulate user interaction logs with redundant tracking
def generate_logs():
    actions = ['click', 'scroll', 'hover', 'click', 'scroll', 'click', 'keystroke', 'click']
    timestamps = [100, 150, 200, 250, 300, 350, 400, 450]
    log_entries = []
    for i in range(len(actions)):
        log_entries.append({'action': actions[i], 'ts': timestamps[i]})
    return log_entries

# Extraneous helper to compute time gaps (some irrelevant)
def compute_deltas(logs):
    deltas = []
    cumulative_offset = 0
    for i in range(1, len(logs)):
        delta = logs[i]['ts'] - logs[i-1]['ts']
        cumulative_offset += delta // 10  # Fake aggregation
        deltas.append(delta)
    avg_gap = sum(deltas) / len(deltas) if deltas else 0
    return deltas, avg_gap, cumulative_offset

# Misleading analysis function that tracks hover but doesn't impact final score
def analyze_engagement_type(logs):
    counts = defaultdict(int)
    for entry in logs:
        counts[entry['action']] += 1
    
    # Red herring: hover_ratio has no effect on final result
    total = len(logs)
    hover_ratio = counts['hover'] / total if total else 0
    keystroke_ratio = counts['keystroke'] / total if total else 0
    
    # Dummy transformation
    engagement_vector = [counts['click'], counts['scroll'], int(hover_ratio * 100)]
    return counts, engagement_vector

# Core logic obscured by noise
def calculate_performance_rating():
    logs = generate_logs()
    
    # Irrelevant computation branch
    _, avg_time_gap, _ = compute_deltas(logs)
    action_counts, _ = analyze_engagement_type(logs)
    
    # Fake normalization step (distraction)
    normalized_clicks = (action_counts['click'] * 100) // len(logs) if logs else 0
    
    # Actual signal: weighted score based on click density and scroll frequency
    click_weight = 7
    scroll_weight = 3
    base_score = action_counts['click'] * click_weight + action_counts['scroll'] * scroll_weight
    
    # Conditional adjustment based on presence of keystroke (only one)
    has_keystroke = any(log['action'] == 'keystroke' for log in logs)
    bonus_multiplier = 1.25 if has_keystroke else 1.0
    
    # Apply bonus (this affects final score)
    adjusted_score = base_score * bonus_multiplier
    
    # Dead code path - never executed but adds confusion
    if len(logs) > 100:
        adjusted_score *= 0.9  # This won't run
    
    # Final transformation: take floor after scaling
    import math
    final_score = math.floor(adjusted_score + avg_time_gap * 0.1)  # Minor influence from avg_time_gap
    
    # Print required output format
    print(f"Target result: {final_score}")
    return final_score

# Key execution point
final_score = calculate_performance_rating()