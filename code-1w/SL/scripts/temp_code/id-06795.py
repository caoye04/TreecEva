def analyze_performance(observations):
    raw_data = [x for x in observations if x > 0]
    filtered = list(filter(lambda x: x % 2 == 1, raw_data))
    counts = {i: raw_data.count(i) for i in set(raw_data)}
    temp_factor = sum([v * v for k, v in counts.items() if k < 5])
    return [x * 1.5 for x in filtered] + [temp_factor]


def normalize(values):
    max_val = max(values)
    return [round(v / max_val, 4) for v in values]


def compute_aggregate(metrics, weights):
    adjusted = [m * w for m, w in zip(metrics, weights)]
    penalty = 0
    for i, val in enumerate(adjusted):
        if val > 3.0:
            penalty += 0.5
    aggregate = sum(adjusted) - penalty
    return round(aggregate, 4)

# Simulated sensor readings
readings = [2, 3, 5, 3, 7, 2, 9, 5]

# Step 1: Analyze performance with sensor data
processed = analyze_performance(readings)

# Irrelevant intermediate computation (distractor)
disruption_signal = [x ** 0.5 for x in readings if x % 3 == 0]
distraction_sum = sum(disruption_signal) * 0.1  # Unused beyond this point

# Step 2: Normalize the processed metrics
norm_metrics = normalize(processed)

# Step 3: Define weighting scheme for final evaluation
weights = [0.8, 0.6, 0.9, 0.7, 0.5]

# Step 4: Extend normalized metrics to match weight length (critical alignment)
while len(norm_metrics) < len(weights):
    norm_metrics.append(min(norm_metrics))

# Key statement
final_score = compute_aggregate(norm_metrics, weights)

print(f"Target result: {final_score}")