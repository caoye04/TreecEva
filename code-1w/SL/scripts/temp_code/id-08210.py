def analyze_events(event_list):
    event_counts = {}
    for event in event_list:
        if event not in event_counts:
            event_counts[event] = 0
        event_counts[event] += 1
    return event_counts

# Simulated sensor data with noise
timestamps = [101, 102, 103, 104, 105, 106, 107, 108]
sensor_readings = [23.1, 24.5, 24.5, 25.0, 23.1, 26.3, 25.0, 24.5]
reading_pairs = list(zip(timestamps, sensor_readings))

# Track state changes
state_changes = []
prev = None
for ts, val in reading_pairs:
    if prev is not None and abs(val - prev) > 1.0:
        state_changes.append(ts)
    prev = val

# Misleading computation: average gap (not used later)
avg_gap = 0
if len(state_changes) > 1:
    gaps = [state_changes[i] - state_changes[i-1] for i in range(1, len(state_changes))]
    avg_gap = sum(gaps) / len(gaps) if gaps else 0

# Core data log for scoring
data_log = ['motion', 'idle', 'motion', 'motion', 'idle', 'motion', 'motion', 'idle']
event_freq = analyze_events(data_log)

# Weight mapping for score calculation
weights = {'motion': 3, 'idle': -1, 'alert': 5}

# Red herring: unused transformation
distinct_values = set(sensor_readings)
scaled_values = [round(v * 1.05, 2) for v in distinct_values]
value_histogram = {v: sensor_readings.count(v) for v in distinct_values}

# Another distraction: character analysis from fake labels
labels = ['M', 'I', 'M', 'M', 'I', 'M', 'M', 'I']
label_map = {k: v for k, v in enumerate(labels)}
char_count = {}
for label in labels:
    char = label.lower()
    char_count[char] = char_count.get(char, 0) + 1

# Actual scoring logic
def calculate_final_score(log, weight_dict):
    base_score = 0
    bonus_trigger = 0
    
    for event, count in log.items():
        if event in weight_dict:
            contribution = count * weight_dict[event]
            base_score += contribution
            if event == 'motion' and count >= 3:
                bonus_trigger += 1
    
    # Apply bonus if conditions met
    final = base_score
    if bonus_trigger > 0:
        final += 10  # achievement bonus
    
    # Irrelevant loop (dead code path, never reached in this case)
    temp_debug = []
    for k, v in weight_dict.items():
        if v > 4:
            temp_debug.append(k)
    
    return final

# Execute main logic
interim_result = analyze_events(data_log)
count_motion = interim_result.get('motion', 0)
count_idle = interim_result.get('idle', 0)

# Key execution point
total_actions = count_motion + count_idle
motion_ratio = count_motion / total_actions if total_actions else 0

final_score = calculate_final_score(data_log, weights)
print(f"Result: {final_score}")