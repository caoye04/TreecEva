import math

# Simulate sensor data processing with noise filtering and performance scoring
def collect_sensor_data():
    raw_values = [12, 15, 8, 23, 7, 14]
    filtered = [x for x in raw_values if x > 10]
    return filtered

def compute_entropy(data):
    total = sum(data)
    probabilities = [(x / total) for x in data]
    entropy = -sum(p * math.log(p) for p in probabilities if p > 0)
    return round(entropy, 4)

def generate_baseline(n):
    # Irrelevant helper: generates dummy sequence
    return [i**2 % 7 for i in range(n)]

def evaluate_performance(metrics, weights):
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    adjustment_factor = 1.0
    
    # Misleading conditional: looks important but doesn't affect final path
    if len(metrics) > 5:
        adjustment_factor = 0.95
    elif sum(metrics) < 30:
        adjustment_factor = 1.05
    else:
        adjustment_factor = 1.0  # Neutral case

    # Dummy combinatorics calculation (distractor)
    def count_pairs(arr):
        return len(arr) * (len(arr) - 1) // 2
    
    pair_count = count_pairs(metrics)  # Computed but unused
    
    # Real computation
    base_score = weighted_sum * adjustment_factor
    
    # Lambda-based transformation (required feature)
    apply_bonus = lambda x: x * 1.1 if x < 20 else x * 1.05
    enhanced_score = apply_bonus(base_score)
    
    # Additional red herring: recursive function that computes unused metric
    def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
    
    fib_offset = fibonacci(6)  # = 8, computed but not used
    
    # Final score computation
    final_score = int(round(enhanced_score - 5))  # Deterministic integer result
    
    return final_score

# Main execution flow
data = collect_sensor_data()  # [12, 15, 23, 14]

# Compute derived metrics
avg_val = sum(data) / len(data)
peak = max(data)
entropy = compute_entropy(data)

dummy_sequence = generate_baseline(10)  # Distractor variable

# Prepare evaluation inputs
metrics = [
    avg_val,           # ~16.0
    peak,              # 23
    entropy,           # ~1.365
    len(data)          # 4
]

weights = [0.4, 0.3, 0.2, 0.1]

# Key statement
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")