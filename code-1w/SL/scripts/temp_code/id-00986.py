import math

# Simulated sensor data processing with performance evaluation
raw_readings = [0.85, 0.92, 0.78, 0.63, 0.91]
decoy_readings = [x ** 2 for x in raw_readings]  # Irrelevant transformation
temp_buffer = list(map(lambda x: math.log(x + 1), raw_readings))

# Data normalization (relevant)
normalized = [(x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) for x in raw_readings]

# Threshold filtering (partially relevant)
effective_signals = [x for x in normalized if x > 0.5]
useless_signals = [x for x in normalized if x <= 0.3]  # Dead-end collection

# Weight initialization (mix of relevant and irrelevant)
metric_weights = {
    'accuracy': 0.4,
    'stability': 0.3,
    'response': 0.2,
    'fallback': 0.1,
    'dummy_metric': 0.0  # Will be ignored in logic
}

# Outcome computation with red herrings
raw_outcomes = {}
raw_outcomes['accuracy'] = sum(effective_signals) / len(raw_readings)
raw_outcomes['stability'] = abs(normalized[0] - normalized[-1])
raw_outcomes['response'] = math.exp(-temp_buffer[2])  # Misleading use of temp_buffer
raw_outcomes['fallback'] = 0.5  # Constant override
raw_outcomes['phantom'] = 999  # Decoy key

# Auxiliary function that looks important but is unused
def compute_robustness(data):
    return sum(x ** 3 for x in data if x > 0.7)

# Another unused helper with complex logic
calculate_resilience = lambda seq: sum(1 for a, b in zip(seq, seq[1:]) if b >= a) / len(seq) if seq else 0
decoy_result = calculate_resilience(decoy_readings)  # Dead path

# Core evaluation logic (critical path)
def evaluate_performance(weights, outcomes):
    score = 0.0
    for key in weights:
        if key in outcomes and weights[key] > 0:  # Skip dummy and phantom
            if key == 'response':
                # Special nonlinear adjustment
                adjusted = 1 / (1 + math.exp(-outcomes[key] * 10))  # Sigmoid transform
            else:
                adjusted = outcomes[key]
            score += weights[key] * adjusted
    return round(score * 100, 4)  # Scale to percentage-like score

# Secondary function that simulates alternative path (never called)
def legacy_evaluation(sig_list):
    total = 0
    for i in range(len(sig_list)):
        total += sig_list[i] * (0.9 ** i)
    return total * 10

intermediate_diag = evaluate_performance({'accuracy': 1.0}, raw_outcomes)  # Distractor call

# Critical execution point
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Output result
print(f"Result: {final_score}")