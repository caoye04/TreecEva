from collections import defaultdict, Counter

# Simulate user engagement analytics with scoring logic
def analyze_engagement(log_entries):
    event_count = defaultdict(int)
    session_lengths = []
    total_actions = 0

    for entry in log_entries:
        event_type = entry['event']
        duration = entry.get('duration', 1)
        event_count[event_type] += 1
        session_lengths.append(duration)
        total_actions += 1

    avg_duration = sum(session_lengths) / len(session_lengths) if session_lengths else 0
    return event_count, avg_duration, total_actions

def calculate_risk_factor(events):
    # Irrelevant risk calculation (distractor)
    counts = Counter(events)
    high_risk_events = counts.get('error', 0) + counts.get('timeout', 0)
    return high_risk_events * 0.5

def calculate_final_score(data, flags):
    base_score = 0
    multiplier = 1

    # Real scoring logic
    for rank, users in data.items():
        if rank == 'gold' and flags['premium_award']:
            base_score += len(users) * 10
        elif rank == 'silver' and flags['active_bonus']:
            base_score += len(users) * 5
        else:
            base_score += len(users) * 2

    # Conditional expression affecting multiplier
    multiplier += 1 if flags['premium_award'] and sum(len(u) for u in data.values()) > 5 else 0
    multiplier = multiplier * 1.5 if 'boost' in flags and flags['boost'] else multiplier

    # Dummy computation - misleading but not used
    temp_score = base_score * 0.1
    adjustment_log = []
    for i in range(3):
        adjustment_log.append(temp_score / (i + 1) if i > 0 else temp_score)

    # Final score computed here
    final_score = int(base_score * multiplier)

    # Unused dead code path (distractor)
    if False:
        fallback = sum(adjustment_log)
        final_score = int(fallback)

    return final_score

# Main execution
log_data = [
    {'event': 'click', 'duration': 2},
    {'event': 'view', 'duration': 5},
    {'event': 'click', 'duration': 1},
    {'event': 'scroll', 'duration': 3},
    {'event': 'hover', 'duration': 2}
]

# Extract analytics (some used, some not)
event_freq, average_time, actions = analyze_engagement(log_data)
risk_level = calculate_risk_factor(event_freq.keys())  # Distractor call

# User rank data - core input
rank_data = {
    'gold': ['u1', 'u2'],
    'silver': ['u3', 'u4', 'u5'],
    'bronze': ['u6', 'u7', 'u8', 'u9', 'u10']
}

# Bonus flags with mixed relevance
bonus_flags = {
    'premium_award': True,
    'active_bonus': False,
    'boost': True,
    'debug_mode': True  # Unused flag
}

# Misleading intermediate calculation
baseline_metric = sum(len(users) for rank, users in rank_data.items() if rank != 'bronze')
decay_factor = 0.95 ** baseline_metric
projected_growth = baseline_metric * (1 + decay_factor)  # Not used later

# Key statement: final_score assignment
temp_result = calculate_final_score(rank_data, bonus_flags)
shadow_copy = temp_result * 0.9  # Red herring
final_score = temp_result  # Final answer source

# Print result as required
print(f"Result: {final_score}")