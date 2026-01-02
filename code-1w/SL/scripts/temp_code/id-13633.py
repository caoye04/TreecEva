from collections import defaultdict, Counter

# Simulated user interaction log with noise
event_stream = [
    ('click', 1), ('hover', 2), ('scroll', 3), ('click', 4),
    ('keypress', 5), ('click', 6), ('hover', 7), ('scroll', 8),
    ('click', 9), ('hover', 10), ('invalid_event', 11), ('click', 12)
]

# Irrelevant statistical counters (distractors)
stat_summary = defaultdict(int)
duplicate_tracker = set()
noise_filter = [x for x in range(1, len(event_stream) + 5) if x % 4 == 0]

# Process events but with red herring logic
processed_events = []
temp_buffer = []
for event_type, timestamp in event_stream:
    if event_type == 'invalid_event':
        continue
    if 'hover' in event_type and timestamp % 2 == 0:
        stat_summary['even_hover'] += 1
    elif 'scroll' in event_type:
        temp_buffer.append(timestamp)
        stat_summary['scroll_count'] += 1  # Distractor
    processed_events.append((event_type, timestamp))

# Fake aggregation path (dead code path - never used later)
aggregated = {}
for typ, ts in processed_events:
    if typ not in aggregated:
        aggregated[typ] = 0
    aggregated[typ] += ts % 3

# Real data transformation begins here
action_sequence = [t for t, _ in processed_events]
frequency_map = Counter(action_sequence)

# Misleading intermediate calculation
phantom_score = 0
for k, v in frequency_map.items():
    phantom_score += hash(k) % 10 * v
phantom_score = phantom_score % 100

# Actual relevant logic hidden among distractions
def compute_engagement(events):
    score = 0
    streak = 0
    last_was_click = False
    for e, _ in events:
        if e == 'click':
            score += 3
            if last_was_click:
                streak += 1
            else:
                streak = 1
            last_was_click = True
        elif e == 'keypress':
            score += 2
            streak = 0
            last_was_click = False
        elif e == 'hover':
            score += 1
            if streak > 0:
                streak -= 1
            last_was_click = False
    return score + streak  # Final adjustment

# Another decoy function that looks important
def predict_next_event(seq):
    if not seq:
        return 'unknown'
    c = Counter(seq)
    return max(c, key=c.get)

# Hidden dependency: feedback log is a slice of original data
feedback_log = action_sequence[1:10:2]  # Slicing operation used (required feature)

# Threshold derived from irrelevant stats
threshold = stat_summary['even_hover'] + 1

# Core analysis function — looks complex due to distractors
# But only uses frequency_map and feedback_log meaningfully
def analyze_performance(log, thresh):
    base = 0
    freq_weights = {'click': 5, 'hover': 2, 'keypress': 4}
    for action in log:
        if action in freq_weights:
            base += freq_weights[action]
    # Conditional twist based on length and threshold
    if len(log) >= thresh:
        anomaly_detector = sum(1 for a in log if a == 'hover') % 2
        if anomaly_detector:
            base *= 2
    return base + len(log)  # Final formula

# Critical execution point
final_score = analyze_performance(feedback_log, threshold)

# Print result as required
print(f"Target result: {final_score}")