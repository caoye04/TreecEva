from collections import defaultdict
import itertools

# Simulate a scenario where employee performance is evaluated across multiple metrics
# Some computations are distractions (e.g., normalization_history, auxiliary_score)

def preprocess_metrics(raw_data):
    normalized = {}
    history = []
    for k, v in raw_data.items():
        shifted = v + 0.1
        corrected = max(shifted, 0.5)
        normalized[k] = round(corrected, 2)
        history.append(shifted)  # stored but not used later
    return normalized


def calculate_baseline(scores):
    total = 0
    count = 0
    for val in scores.values():
        if val > 0.7:
            total += val * 1.2
        else:
            total += val * 0.8
        count += 1
    return total / count if count else 0


def generate_combinations(metrics):
    # Distractor function: generates combinations but only length is used
    keys = list(metrics.keys())
    combs = list(itertools.combinations(keys, 2))
    return len(combs)


def evaluate_performance(weights, outcomes):
    # Main logic begins here
    processed_weights = preprocess_metrics(weights)
    baseline = calculate_baseline(processed_weights)
    
    # Distraction: irrelevant combination logic
    comb_count = generate_combinations(outcomes)
    adjustment_factor = comb_count * 0.05 if comb_count > 4 else 0.1
    
    # Core scoring logic
    raw_score = 0
    for key in outcomes:
        if key in processed_weights:
            raw_score += outcomes[key] * processed_weights[key]
    
    # Secondary distraction: unused auxiliary computation
    auxiliary_score = 0
    temp_acc = defaultdict(float)
    for k, v in outcomes.items():
        temp_acc[k] += v * 0.1
        auxiliary_score += temp_acc[k]
    
    # Final calculation
    adjusted_score = raw_score * (1 + adjustment_factor)
    normalized_final = min(adjusted_score, 100)
    
    # This variable is critical
    final_score = int(round(normalized_final))
    
    return final_score

# Input data
metric_weights = {
    'accuracy': 0.8,
    'speed': 0.6,
    'consistency': 0.9,
    'adaptability': 0.5,
    'collaboration': 0.7
}

raw_outcomes = {
    'accuracy': 85,
    'speed': 70,
    'consistency': 90,
    'adaptability': 60,
    'collaboration': 75
}

# Execution point of interest
final_score = evaluate_performance(metric_weights, raw_outcomes)
print(f"Result: {final_score}")