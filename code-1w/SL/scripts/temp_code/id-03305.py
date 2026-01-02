from itertools import combinations
from math import log

# Simulate system performance metrics from various subsystems
def collect_metrics(base_load, efficiency_factor):
    raw_data = [base_load * (1.2 ** i) for i in range(5)]
    normalized = [x / sum(raw_data) for x in raw_data]
    adjusted = [x * efficiency_factor + 0.1 for x in normalized]
    return [round(x, 4) for x in adjusted]

def calculate_entropy(values):
    """Irrelevant helper: computes entropy but not used in final path"""
    return -sum(x * log(x) for x in values if x > 0)

def generate_weights(n):
    # Generates exponential decay weights
    return [0.9 ** i for i in range(n)]

def validate_stability(metrics):
    # Dummy validation that returns a boolean; distractor logic
    return all(m < 0.8 for m in metrics) and len(metrics) == 5

def smooth_data(data, factor=0.1):
    # Smoothing function not ultimately used
    return [d + factor * (-1)**i for i, d in enumerate(data)]

def evaluate_performance(metrics, weights):
    # Core calculation: weighted harmonic mean with filtering
    filtered_metrics = [m for m in metrics if m > 0.15]
    
    # Distractor: complex combination analysis
    comb_pairs = list(combinations(filtered_metrics, 2))
    avg_product = sum(a * b for a, b in comb_pairs) / len(comb_pairs) if comb_pairs else 0
    
    # More irrelevant computation
    lambda_offset = (lambda x: x ** 0.5)(avg_product * 2) if avg_product > 0 else 0
    
    # Actual relevant logic starts here
    weighted_inv_sum = sum(weights[i] / metrics[i] for i in range(len(metrics)))
    weight_sum = sum(weights[:len(metrics)])
    harmonic_baseline = weight_sum / weighted_inv_sum
    
    # Apply conditional bonus based on string pattern in debug mode
    debug_flag = "perf_check_enabled"
    case_transformed = debug_flag.upper().replace("_", "").lower()
    bonus = 10 if 'enabled' in case_transformed else 0
    
    # Final score computation
    stability = validate_stability(metrics)  # Called but result not directly used
    temp_result = harmonic_baseline * 100 + bonus
    
    # Dead code path - looks important but doesn't affect outcome
    if temp_result > 200:
        temp_result = temp_result % 97
    elif temp_result < 50:
        temp_result = temp_result * 1.5
    
    # This is the actual assignment
    final_score = int(temp_result)  # Truncate to integer
    
    return final_score

# Main execution flow
base = 150
factor = 0.65

# Collect performance data
metrics = collect_metrics(base, factor)

# Generate weighting scheme
weights = generate_weights(5)

# Perform evaluation
dummy_entropy = calculate_entropy(metrics)  # Irrelevant call
smoothed = smooth_data(metrics)  # Unused result

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")