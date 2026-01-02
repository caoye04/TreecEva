from collections import defaultdict, Counter

# Simulate log analysis for user activity scoring
def analyze_user_behavior(log_entries):
    event_count = defaultdict(int)
    duration_sum = defaultdict(float)
    action_magnitude = {}

    # Irrelevant preprocessing: normalize text (distractor)
    normalized_logs = []
    for entry in log_entries:
        parts = entry.strip().split(',')
        action = parts[0].lower().strip()
        time_spent = float(parts[1])
        severity = len(action) % 3  # Unused computation (red herring)

        normalized_logs.append(f'{action},{time_spent}')
        event_count[action] += 1
        duration_sum[action] += time_spent

        # Semi-relevant transformation
        if 'click' in action:
            action_magnitude[action] = time_spent * 1.5
        elif 'scroll' in action:
            action_magnitude[action] = time_spent * 0.8
        else:
            action_magnitude[action] = time_spent * 1.0

    return event_count, duration_sum, action_magnitude


def compute_engagement_index(counts, durations):
    base_index = 0
    penalty = 0

    for action, count in counts.items():
        base_index += count * (len(action) % 4)  # Minor influence
        if count > 2:
            penalty += 1

    total_duration = sum(durations.values())
    # Distraction: complex weight not fully used
    weighted_duration = sum(d ** 0.5 for d in durations.values() if d > 1)

    return base_index - penalty + (total_duration // 10)


def calculate_final_score(data):
    counts, durations, magnitudes = data
    
    # Core logic
    raw_score = 0
    adjustment = 0
    
    freq_counter = Counter(counts.values())
    mode_freq = freq_counter.most_common(1)[0][1] if freq_counter else 0
    
    for action, mag in magnitudes.items():
        if 'click' in action:
            raw_score += mag * 2
        elif 'scroll' in action:
            raw_score += mag * 1
        else:
            raw_score += mag * 0.5
    
    # Adjustment based on frequency pattern (semi-independent path)
    high_freq_actions = [a for a, c in counts.items() if c >= 3]
    if len(high_freq_actions) >= 2:
        adjustment = 5
    
    # Dead computation: unused statistical check
    avg_duration = sum(durations.values()) / len(durations) if durations else 0
    duration_variance = sum((d - avg_duration) ** 2 for d in durations.values()) / len(durations) if durations else 0
    
    # Final score calculation — only raw_score and adjustment matter
    final_score = int(raw_score + adjustment)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Main execution
log_data = [
    "click_button,4.5",
    "scroll_page,3.2",
    "hover_menu,2.1",
    "click_link,5.0",
    "scroll_page,2.8",
    "click_button,3.7",
    "click_link,4.1",
    "scroll_page,3.5",
    "keystroke_field,1.9"
]

event_counts, duration_totals, action_values = analyze_user_behavior(log_data)
engagement = compute_engagement_index(event_counts, duration_totals)
processed_data = (event_counts, duration_totals, action_values)
final_score = calculate_final_score(processed_data)