import math

# Irrelevant helper function (dead code path)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v]

# Misleading performance metric that isn't used
def legacy_scorer(data):
    return sum(d * 0.7 for d in data) % 100

# Core transformation pipeline with red herrings
def transform_input(raw_data, mode='advanced'):
    if mode == 'basic':
        return [x * 2 for x in raw_data if x > 5]
    elif mode == 'advanced':
        # Complex transformation with distractors
        temp_result = []
        shift_val = 3
        for i, val in enumerate(raw_data):
            shifted = val << 1  # Bit manipulation red herring
            masked = shifted & 7                   # Decoy bitwise logic
            if i % 2 == 0:
                temp_result.append(val ** 0.5)
            else:
                temp_result.append(val / (i + 1))
        return [round(t, 3) for t in temp_result]
    return []

# Unused but plausible alternative weighting
ALTERNATIVE_WEIGHTS = [0.1, 0.3, 0.4, 0.2]

# Critical lambda: maps raw metrics to normalized influence
influence_model = lambda x, w: sum(a * b for a, b in zip(x, w)) ** 1.25

# Secondary adjustment with conditional branching
def apply_adjustment(base_value, category):
    adjustments = {
        'alpha': 0.95,
        'beta': 1.05,
        'gamma': 1.0
    }
    adj = adjustments.get(category, 1.0)
    intermediate = base_value * adj
    
    # Distractor block: looks important but unused
    if intermediate > 100:
        capped = 100
        penalty = (intermediate - 100) * 0.1
        intermediate = capped  # Never actually used
    
    # Actual adjustment logic
    if base_value < 80:
        intermediate += 8
    elif base_value > 120:
        intermediate -= 5
    
    return intermediate

# Main evaluation logic buried among distractions
def evaluate_performance(metrics, weights):
    # Step 1: Transform inputs using non-default path
    processed = transform_input(metrics, mode='advanced')
    
    # Step 2: Apply influence model via lambda
    raw_influence = influence_model(processed, weights)
    
    # Step 3: Adjust based on synthetic category
    category = 'beta'
    adjusted = apply_adjustment(raw_influence, category)
    
    # Step 4: Final nonlinear scaling
    noise_component = 0.0  # Placeholder for potential randomness (unused)
    final_value = math.log(adjusted ** 2 + 1, 10) * 4.2
    
    # Irrelevant diagnostic print (simulates debugging noise)
    # print(f'Diagnostic: {len(processed)} elements processed')
    
    return final_value

# Decoy global variables
current_epoch = 2024
scaling_factor = 0.88
temp_cache = {f'key_{i}': i * 1.5 for i in range(10)}

# Input data with meaningful names
system_metrics = [16, 9, 25, 4]  # e.g., response times, error rates, throughput, latency
weight_distribution = [0.4, 0.1, 0.3, 0.2]  # Allocated importance per metric

# Key execution point
final_score = evaluate_performance(system_metrics, weight_distribution)

# Result output (required format)
print(f"Target result: {final_score}")