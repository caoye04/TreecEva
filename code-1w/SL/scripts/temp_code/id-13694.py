from collections import Counter, defaultdict

# Simulate user interaction logs with action types and timestamps
timestamps = [10, 20, 35, 40, 50, 60, 75, 80, 90, 100]
actions = ['click', 'scroll', 'click', 'hover', 'click', 'scroll', 'click', 'hover', 'scroll', 'click']

# Track frequency of actions
action_counter = Counter(actions)

click_count = action_counter['click']
scroll_count = action_counter['scroll']
hover_count = action_counter['hover']

# Misleading distraction: session duration calculation (not used in final score)
session_start = timestamps[0]
session_end = timestamps[-1]
session_duration = session_end - session_start
average_interval = session_duration / (len(timestamps) - 1) if len(timestamps) > 1 else 0

# Process data: find bursts of activity within time windows
burst_threshold = 15
activity_bursts = 0
for i in range(1, len(timestamps)):
    if timestamps[i] - timestamps[i-1] < burst_threshold:
        activity_bursts += 1

# Distractor variables: simulate engagement metrics not directly used
engagement_ratio = (click_count + scroll_count) / (hover_count + 1)
distraction_metric_1 = engagement_ratio * average_interval
distraction_metric_2 = sum([t // 10 for t in timestamps if t % 5 == 0])

# Prepare processed data using defaultdict for robustness
data_store = defaultdict(int)
data_store['clicks'] = click_count
data_store['bursts'] = activity_bursts
data_store['base_score'] = click_count * 2 + activity_bursts * 3

# Secondary distraction: unused alternative scoring logic
if data_store['clicks'] > 5:
    alt_score = data_store['clicks'] * 1.5
else:
    alt_score = data_store['clicks'] + data_store['bursts']

# Core logic: calculate final score based on weighted components
def calculate_final_score(data):
    base = data['base_score']
    bonus = 0
    
    # Conditional bonus logic
    if data['clicks'] >= 5:
        bonus += 10
    if data['bursts'] >= 3:
        bonus += 7
    
    # Apply decay for low hover (irrelevant but included for confusion)
    decay = 0
    if hover_count < 2:
        decay = 3  # Not actually subtracted - red herring
    
    return int(base + bonus)  # Final integer score

# Execute main computation
processed_data = dict(data_store)
final_score = calculate_final_score(processed_data)

# Print result as required
print(f"Target result: {final_score}")