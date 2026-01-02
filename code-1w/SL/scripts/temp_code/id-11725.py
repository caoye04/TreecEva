from itertools import compress, cycle
import math

def analyze_signal(data, threshold=0.5):
    # Irrelevant signal processing (distractor)
    filtered = [x for x in data if abs(x) > threshold]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-8) for x in filtered]
    return [math.sin(x) for x in normalized]

def generate_weights(n):
    # Generates weighted pattern using modular arithmetic and bit shifts (semi-relevant)
    base = [(i * 7 + 13) % 11 for i in range(n)]
    shifted = [(w << 1) ^ 3 for w in base]  # Bit manipulation distraction
    return [w / sum(shifted) for w in shifted]

def evaluate_performance(metrics, weights):
    # Core logic: weighted combination with conditional boosts
    raw_score = sum(m * w for m, w in zip(metrics, weights))
    
    # Conditional bonus based on logical conditions (relevant)
    above_threshold = [m > 0.7 for m in metrics]
    if all(above_threshold):
        raw_score *= 1.2
    elif any(above_threshold) and not all(above_threshold):
        raw_score *= 1.05
    
    # Bonus for symmetry pattern in metrics (rarely triggered, minor distractor)
    reversed_metrics = list(reversed(metrics))
    if metrics == reversed_metrics:
        raw_score += 0.05
    
    # Apply non-linear transformation (relevant)
    final_score = math.log(1 + raw_score) * 100
    
    # Dead code path - never executed due to prior constraints (distractor)
    if len(metrics) > 100:
        backup = list(compress(metrics, cycle([True, False])))
        final_score = max(final_score, sum(backup))
    
    return final_score

# Simulated sensor metrics from system diagnostics (real data)
data_stream = [0.81, 0.74, 0.89, 0.63, 0.91]
processed_signal = analyze_signal(data_stream)  # Unused side computation (distractor)

# Key variables
metrics = [0.85, 0.76, 0.88, 0.72, 0.90]  # Performance KPIs
weights = generate_weights(len(metrics))

# Critical execution point
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")