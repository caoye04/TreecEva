from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    trend_data = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend_data.append(1)
        elif sequence[i] < sequence[i-1]:
            trend_data.append(-1)
        else:
            trend_data.append(0)
    
    # Irrelevant accumulation (distractor)
    cumulative_drift = sum(trend_data)
    temp_analysis = [x for x in trend_data if x != 0]

    # Real logic: count ascending pairs
    for val in trend_data:
        if val == 1:
            count += 1
    return count

# Simulate sensor readings
sensor_readings = [23, 25, 25, 27, 30, 29, 31]

duplicate_tracker = {}
for val in sensor_readings:
    duplicate_tracker[val] = duplicate_tracker.get(val, 0) + 1

# Compute volatility (unused distractor)
volatility = sum(abs(a - b) for a, b in zip(sensor_readings, sensor_readings[1:]))

# Generate all 2-element increasing subsequences (distraction with no impact)
increasing_pairs = list(combinations([x for x in sensor_readings if x > 25], 2))
filtered_pairs = [p for p in increasing_pairs if p[1] - p[0] >= 3]

# Core state variables
base_trend = analyze_pattern(sensor_readings)
event_marker = len([x for x in sensor_readings if x % 2 == 1])

# Secondary derived metrics (some irrelevant)
redundant_metric_a = event_marker * 2 - 1
redundant_metric_b = volatility // 3 if volatility > 0 else 0

# Key intermediate transformation
adjusted_trend = base_trend + (event_marker // 2)

# Simulated weight adjustment (partially relevant)
weights = [1.0, 0.5, 0.7, 1.2]
scaling_factor = sum(w for w in weights if w >= 0.7)

# Final computation
raw_aggregate = adjusted_trend * scaling_factor
penalty = len(filtered_pairs)  # Minor correction based on distractor structure

# Final score calculation — this is the key statement
final_score = int(raw_aggregate - penalty)

Result: final_score