import math

def analyze_pattern(sequence, depth):
    if depth == 0:
        return sum([x ** 2 for x in sequence if x % 2 == 1])
    shifted = [(sequence[i] + sequence[(i+1) % len(sequence)]) // 2 for i in range(len(sequence))]
    return analyze_pattern(shifted, depth - 1)

def compute_entropy(data):
    total = sum(data)
    probabilities = [v / total for v in data if v > 0]
    return -sum(p * math.log(p) for p in probabilities)

def dummy_filter(values):
    # Irrelevant filtering function (dead code path)
    return [v for v in values if v > 5 and v < 100]

def process_signals(raw_signals):
    # Misleading signal processing chain
    filtered = [abs(x - 50) for x in raw_signals]
    normalized = [min(max(f, 0), 100) for f in filtered]
    envelope = [math.sin(math.pi * n / 50) * n for n in normalized]
    return envelope

def evaluate_performance(metrics, threshold):
    adjusted = [m * 1.5 if m < threshold else m * 0.8 for m in metrics]
    bonus_applied = []
    for val in adjusted:
        if val > threshold * 1.2:
            bonus_applied.append(val + 10)
        elif val < threshold * 0.8:
            bonus_applied.append(val - 5)
        else:
            bonus_applied.append(val)
    aggregate = sum(bonus_applied) / len(bonus_applied)
    penalty_factor = 0.9 if aggregate > 70 else 1.1
    final = aggregate * penalty_factor
    return int(final)

# Initialization of sensor data (red herring - not directly used)
raw_sensor_input = [32, 45, 67, 89, 12, 78, 91, 24, 56, 65]
envelope_data = process_signals(raw_sensor_input)

# Dummy statistical analysis (distractor computation)
dummy_stats = {
    'mean_deviation': sum(abs(x - 55) for x in raw_sensor_input) / len(raw_sensor_input),
    'peak_count': len([x for x in raw_sensor_input if x > 70]),
    'entropy': compute_entropy([x % 10 + 1 for x in raw_sensor_input])
}

# Core metric pipeline begins here
base_sequence = [8, 12, 15, 7, 20, 14]
recursion_depth = 2
processed_level = analyze_pattern(base_sequence, recursion_depth)

# Secondary transformation with list comprehension
transformed = [processed_level // 4]
for i in range(3):
    transformed.append((transformed[-1] * 3) % 25 + i)

# Add irrelevant noise vector (misleading intermediate)
noise_floor = [x ^ 15 for x in transformed if x % 2 == 0]

# Key data preparation
metric_data = [transformed[0] + 5, transformed[2], 68, 71, 60]
base_threshold = 65

# Critical execution point
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")