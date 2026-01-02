def analyze_trends(data, threshold=5.0):
    trends = []
    for i in range(1, len(data)):
        change = data[i] - data[i-1]
        trend_label = 'up' if change > 0 else 'down'
        if abs(change) > threshold:
            trends.append((i, change, trend_label))
    return trends

# Simulated sensor readings over time
readings = [23.5, 24.1, 23.8, 25.6, 26.2, 25.9, 27.8, 28.0, 27.3, 29.1]

# Misleading secondary analysis with dead-end logic
outlier_flags = []
for val in readings:
    deviation = abs(val - sum(readings)/len(readings))
    is_outlier = deviation > 1.5
    if is_outlier and val > 27:  # Conditional that rarely triggers
        outlier_flags.append(True)
    else:
        outlier_flags.append(False)

# Red herring: unused transformation
transformed = [round(x ** 0.5, 3) for x in readings if x > 25]

# Core processing pipeline
baseline = readings[0]
adjusted_readings = [x - baseline for x in readings]

# Detect significant upward movements
movement_log = analyze_trends(adjusted_readings, threshold=1.0)

# Accumulate performance score based on sustained upward trends
streak = 0
score = 0
for idx, delta, direction in movement_log:
    if direction == 'up':
        streak += 1
        score += delta * streak  # Reward longer streaks
    else:
        streak = 0

# Secondary scoring using slicing and conditional expressions
recent_trend = adjusted_readings[-4:]
score_boost = sum([x * 1.5 if x > 2.0 else x * 0.5 for x in recent_trend])

# Final aggregation with tuple unpacking
raw_metrics = (score, score_boost, len(movement_log))
base_score, boost, event_count = raw_metrics

# Final calculation obscured by intermediate scaling
scaling_factor = 1.2 if event_count >= 3 else 0.8
intermediate_result = (base_score + boost) * scaling_factor

# Key statement
final_score = int(intermediate_result // 1)  # Truncate to integer

# Distractor: unused function call placeholder
unused_buffer = [0]*5
for i in range(len(unused_buffer)):
    unused_buffer[i] = i * 2  # Irrelevant computation

print(f"Result: {final_score}")