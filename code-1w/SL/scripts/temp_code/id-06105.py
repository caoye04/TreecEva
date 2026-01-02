from itertools import compress, cycle

def analyze_trends(data):
    trends = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trends.append(1)
        elif data[i] < data[i-1]:
            trends.append(-1)
        else:
            trends.append(0)
    return trends

def smooth_signal(signal):
    smoothed = [signal[0]]
    for i in range(1, len(signal)-1):
        smoothed.append(sum(signal[i-1:i+2]) / 3)
    smoothed.append(signal[-1])
    return smoothed

def calculate_baseline(deviations):
    # Irrelevant helper function (dead logic path)
    return sum(abs(d) for d in deviations) / len(deviations) if deviations else 0

def evaluate_performance(metrics, weights):
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    adjustment = 0.1 * metrics[2]  # Bonus based on consistency
    return int(weighted_sum + adjustment)

# Simulated sensor data over time
raw_readings = [104, 102, 105, 107, 106, 108, 110, 109, 111, 113]

# Step 1: Detect trend directions
movement_trends = analyze_trends(raw_readings)

# Step 2: Smooth raw signal for noise reduction (distractor computation)
filtered_readings = smooth_signal(raw_readings)
smoothed_avg = sum(filtered_readings) / len(filtered_readings)

# Step 3: Compute various performance indicators (some irrelevant)
volatility = sum(1 for t in movement_trends if t != 0)
drift = movement_trends.count(1)
stability = movement_trends.count(0)
consistency = movement_trends.count(-1)

# Hidden baseline calculation (not used, distractor)
baseline_deviation = calculate_baseline([x - 105 for x in raw_readings])

# Generate auxiliary flags using list comprehension and itertools
anomaly_flags = [1 if x > 108 else 0 for x in raw_readings]
signal_parity = list(compress(movement_trends, anomaly_flags))

# Construct final evaluation metrics (only first three used in answer)
metrics = [
    volatility * 2,           # responsiveness
    drift + stability,          # directional strength
    max(consistency, 5),        # floor applied
    len(signal_parity)          # redundant metric
]

# Weight vector for scoring (only first three matter)
weights = [0.4, 0.35, 0.25, 0.1]

# Key statement
final_score = evaluate_performance(metrics, weights)

# Print result
print(f"Result: {final_score}")