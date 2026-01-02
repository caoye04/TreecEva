from collections import defaultdict, Counter
import math

# Simulated system performance metrics
def generate_metrics():
    raw_data = [78, 85, 92, 67, 88, 95, 70, 82, 90, 73]
    metrics = defaultdict(float)
    for i, val in enumerate(raw_data):
        metrics[f'entry_{i}'] = round(math.log(val) * math.sin(i + 1), 3)
    return metrics

def analyze_trends(data):
    trends = []
    for k, v in data.items():
        if 'entry_' in k:
            trends.append(v > 0)
    return sum(trends)

def compute_entropy(values):
    # Irrelevant entropy calculation (dead path)
    freq = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def filter_outliers(data, threshold=0.5):
    # Distractor function: not used in final computation
    cleaned = {}
    for k, v in data.items():
        if abs(v) >= threshold:
            cleaned[k] = v * 1.1
    return cleaned

def calculate_baseline(data):
    # Computes a misleading intermediate value
    temp_vals = [v ** 2 for k, v in data.items() if int(k.split('_')[-1]) % 2 == 0]
    baseline = sum(temp_vals) / len(temp_vals)
    adjustment = math.cos(len(data))
    return baseline + adjustment

def derive_weights(n):
    # Generates unused weights (red herring)
    return [round(math.exp(-i * 0.2), 3) for i in range(n)]

def evaluate_performance(metrics, base):
    # Core logic hidden among distractors
    valid_entries = [v for k, v in metrics.items() if int(k.split('_')[-1]) % 3 == 0]
    
    # Misleading transformation
    transformed = [abs(x) * 2.5 for x in valid_entries]
    
    # Real computation begins here
    adjusted = [t - base for t in transformed]
    clamped = [max(0, min(100, x)) for x in adjusted]  # Clamp to 0-100 scale
    
    # Final aggregation
    raw_total = sum(clamped)
    count_factor = len(clamped) or 1
    final_score = int((raw_total / count_factor) * 1.75)  # Scale and convert
    
    # Decoy assignment (looks important but unused)
    final_score += int(math.sqrt(base) * 0.5)
    
    return final_score

# Main execution flow
metric_data = generate_metrics()
base_threshold = calculate_baseline(metric_data)  # This returns ~4.3, used as base

# Dead code path: entropy analysis (never called in logic)
# entropy_value = compute_entropy(list(metric_data.values()))

# Unused filtering
# filtered_data = filter_outliers(metric_data)

# Derive weights for no reason (distractor)
weights = derive_weights(10)

# Key statement
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")