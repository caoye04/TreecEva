from itertools import combinations

# Simulate system performance metrics under varying load conditions
def generate_metrics(base_load, stress_factor):
    linear_component = base_load * 1.5
    nonlinear_component = int((stress_factor ** 0.5) * 10)
    overhead = 7  # constant system overhead
    total = linear_component + nonlinear_component + overhead
    return {
        'latency': total + 3,
        'throughput': total - 12,
        'error_rate': max(0.01, 100.0 / (total + 1)),
        'energy': total * 0.8
    }

def calculate_weighted_sum(data, weights):
    # Redundant helper that isn't used in final logic
    weighted = 0
    for i, key in enumerate(data.keys()):
        weighted += data[key] * weights[i]
    return weighted

def find_optimal_pair(values):
    # Distractor function — never called
    best = (0, 0)
    max_product = 0
    for a, b in combinations(values, 2):
        if a * b > max_product:
            max_product = a * b
            best = (a, b)
    return best

def normalize_scores(raw):
    total = sum(raw.values())
    return {k: v / total for k, v in raw.items()}

def evaluate_performance(metrics, weights):
    norm = normalize_scores(metrics)
    score = 0
    # Key calculation uses only latency, throughput, error_rate
    relevant_keys = ['latency', 'throughput', 'error_rate']
    temp_debug_log = []
    
    for key in norm.keys():
        if key in relevant_keys:
            contribution = norm[key] * weights[key]
            score += contribution
            temp_debug_log.append(contribution)  # logged but not used
        else:
            # energy metric skipped intentionally
            pass
    
    # Additional distraction: irrelevant adjustment
    adjustment_counter = 0
    for _ in range(3):
        adjustment_counter += 1  # does nothing meaningful
    
    # Final transformation
    score *= 100  # scale to percentage-like score
    rounded_score = round(score, 2)
    
    # Dead code branch (never reached due to structure)
    if adjustment_counter > 10:
        rounded_score += 5
    
    return rounded_score

# Main execution flow
base_load = 40
stress_factor = 9

# Generate performance metrics
metrics = generate_metrics(base_load, stress_factor)

# Define weighting scheme
weights = {
    'latency': 0.3,
    'throughput': 0.4,
    'error_rate': 0.3,
    'energy': 0.0  # explicitly zero-weighted
}

# Irrelevant precomputation
baseline_avg = sum(metrics.values()) / len(metrics)
dummy_pairs = list(combinations([1, 2, 3, 4], 2))  # unused later

# Core evaluation
final_score = evaluate_performance(metrics, weights)

# Output result
print(f"Result: {final_score}")