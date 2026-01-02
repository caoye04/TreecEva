from collections import defaultdict
import math

# Simulate system performance metrics over time
raw_data = [120, 150, 130, 160, 145, 155, 138, 142]

def preprocess(data):
    # Normalize data using moving average (irrelevant for final result)
    smoothed = []
    for i in range(len(data)):
        window = data[max(0, i-2):i+1]
        smoothed.append(sum(window) / len(window))
    return smoothed

def calculate_efficiency(x):
    # Dummy efficiency function with side effect
    if x > 140:
        return x * 0.9
    else:
        return x * 1.1

# Preprocess step (distraction)
processed = preprocess(raw_data)

# Initialize tracking structure (semi-relevant)
metrics = defaultdict(float)
for i, val in enumerate(raw_data):
    key = f"metric_{i % 3}"
    metrics[key] += val

# Apply transformation with lambda (relevant)
transform = lambda x: math.floor(x ** 0.5)
transformed_metrics = {k: transform(v) for k, v in metrics.items()}

# Weight configuration (critical)
weights = {'metric_0': 0.5, 'metric_1': 0.3, 'metric_2': 0.2}

# Extraneous computation: simulate load test (distractor)
cpu_loads = [calculate_efficiency(x) for x in raw_data]
energy_consumption = sum([x * 0.05 for x in cpu_loads])

# Core evaluation logic
def evaluate_performance(mets, wts):
    base = 0
    adjustment = 0
    
    # Key logic steps (5-8 steps with interdependencies)
    for key in mets:
        temp_val = mets[key] * wts[key]
        if temp_val > 25:
            adjustment += 2
        base += temp_val
    
    # Nested condition and bitwise operation (relevant)
    if base > 100:
        base = base ^ 15  # XOR to alter final value
        adjustment = adjustment << 1  # Left shift
    
    # Final composition
    score = int(base + adjustment)
    
    # Dead code path (distractor)
    if score < 0:
        score = abs(score)
        
    return score

# Execute critical statement
final_score = evaluate_performance(transformed_metrics, weights)

# Print result as required
print(f"Result: {final_score}")