from collections import defaultdict, Counter

# Simulated user interaction logs with noise and irrelevant fields
timestamps = [1623456780, 1623456789, 1623456800, 1623456815, 1623456830]
user_actions = ['click', 'hover', 'click', 'scroll', 'click']
duration_ms = [120, 45, 300, 800, 150]

# Irrelevant telemetry data (distractor)
sensor_readings = [0.12, 0.34, 0.25, 0.67, 0.89]
device_ids = ['dev_A', 'dev_B', 'dev_C', 'dev_D', 'dev_E']

# Core data structures for processing
action_count = defaultdict(int)
duration_by_action = defaultdict(list)
action_sequence = []

# Populate action counts and durations
for i, action in enumerate(user_actions):
    action_count[action] += 1
    duration_by_action[action].append(duration_ms[i])
    if action == 'click':
        action_sequence.append(i)

# Dead code path - never used (red herring)
def analyze_sensor_patterns(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return {'average': avg, 'variance': variance}

sensor_analysis = analyze_sensor_patterns(sensor_readings)  # Unused result

# Misleading intermediate computation (decoy)
event_rhythm = 0
for t in range(1, len(timestamps)):
    delta = timestamps[t] - timestamps[t-1]
    event_rhythm += (delta % 2) * (t + 1)

# Real logic begins: extract click burst patterns
click_intervals = [timestamps[action_sequence[i]] - timestamps[action_sequence[i-1]] 
                   for i in range(1, len(action_sequence))]

# Compute burst score: inverse of average interval between clicks
burst_score = 0
if click_intervals:
    avg_interval = sum(click_intervals) / len(click_intervals)
    burst_score = round(1000 / (avg_interval + 1), 4)

# Secondary metric: consistency of click durations
click_durations = duration_by_action['click']
mean_duration = sum(click_durations) / len(click_durations)
variance = sum((x - mean_duration) ** 2 for x in click_durations) / len(click_durations)
duration_consistency = 100 / (1 + variance)  # Higher is more consistent

# Tertiary signal: pattern in action sequence using slicing
seq_pattern = action_sequence[::2]  # Every other click index
pattern_sum = sum(seq_pattern)

# Combine metrics into final score
base_weight = action_count['click'] * 10
temporal_factor = burst_score * 0.7
consistency_factor = duration_consistency * 0.3

# Final aggregation with conditional adjustment
adjustment = 1.1 if len(click_intervals) >= 2 else 0.95

final_score = int(
    (base_weight + temporal_factor + consistency_factor) * adjustment + pattern_sum
)

# Noise injection via unused bitwise operation chain (irrelevant)
key = 0b101010
for d in duration_ms:
    key ^= d
    key = (key << 1) | (key >> 7)  # Rotate and mix

# Output the target variable
print(f"Result: {final_score}")