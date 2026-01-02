def analyze_pattern(sequence):
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Distractor: irrelevant pattern analysis
    flat_segments = [i for i in range(len(trend)) if trend[i] == 0]
    oscillations = sum(1 for i in range(1, len(trend)) if trend[i] != trend[i-1])

    return trend

# Simulated sensor readings
data_stream = [23.1, 24.5, 24.5, 26.8, 25.9, 27.3, 27.3, 28.0]

# Preprocessing: extract integer parts (distractor step)
integer_caps = [int(x) for x in data_stream]
avg_int = sum(integer_caps) / len(integer_caps)

# Compute moving difference (relevant)
deltas = [round(data_stream[i] - data_stream[i-1], 2) for i in range(1, len(data_stream))]

# Flag anomalies above threshold (semi-relevant)
anomaly_flags = [abs(d) > 1.0 for d in deltas]
corrected_deltas = [d if abs(d) <= 1.4 else round(d * 0.5, 2) for d in deltas]  # partial correction

# Accumulate corrected changes
net_drift = round(sum(corrected_deltas), 2)

# Simulate system health score (mostly distractor)
base_health = 95
latency_jitter = 0.17
health_penalty = 0
for flag in anomaly_flags:
    if flag:
        health_penalty += 2

adjusted_health = max(0, base_health - health_penalty)
system_stability = adjusted_health + net_drift  # misleading combination

# Core logic: performance rating based on trend persistence
raw_trend = analyze_pattern([int(x*2) for x in data_stream])  # scale to amplify changes

positive_trends = sum(1 for t in raw_trend if t == 1)
negative_trends = sum(1 for t in raw_trend if t == -1)
neutral_trends = len(raw_trend) - positive_trends - negative_trends

# Weighted scoring with distractor coefficients
w1, w2, w3 = 1.1, 0.8, 0.3  # weights (some irrelevant)
trend_score = w1 * positive_trends - w2 * negative_trends + w3 * neutral_trends

# Secondary adjustment using delta statistics
valid_increases = sum(1 for d in deltas if d > 0)
valid_decreases = sum(1 for d in deltas if d < 0)
consistency_factor = valid_increases - valid_decreases

# Final calculation (key statement)
final_score = int(round(trend_score * 10 + consistency_factor * 2 + net_drift))

# Output result as required
print(f"Result: {final_score}")