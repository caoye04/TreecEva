import math

# Simulated sensor fusion system for environmental monitoring
base_readings = [0.87, 0.92, 0.76, 0.88, 0.94, 0.65, 0.81]
duplicate_buffer = [x * 2 for x in base_readings]  # Irrelevant: duplicated and scaled
offset_correction = sum([abs(b - 0.8) for b in base_readings]) / len(base_readings)

def apply_noise_filter(data, level=1.0):
    """Irrelevant function: simulates noise reduction but not used in main logic"""
    return [d * (1 + level * 0.01) for d in data]

def generate_baseline_reference():
    """Dead code path: generates reference but never called"""
    return {f'node_{i}': math.sin(i) + 0.5 for i in range(7)}

# Historical thresholds (unused legacy data)
historical_caps = {
    'max_temp': 0.95,
    'min_temp': 0.6,
    'spike_tolerance': 0.1
}

# Data transformation chain
filtered = [x for x in base_readings if x > 0.75]  # Keep only high-confidence readings
adjusted = [math.log(x) + 0.5 for x in filtered]

# Weight configuration for evaluation metrics
metric_weights = {
    'accuracy': 0.4,
    'stability': 0.3,
    'response_time': 0.2,
    'redundancy': 0.1
}

# Raw performance outcomes across test scenarios
raw_outcomes = [
    {'accuracy': 0.88, 'stability': 0.82, 'response_time': 0.76, 'redundancy': 0.94},
    {'accuracy': 0.91, 'stability': 0.85, 'response_time': 0.79, 'redundancy': 0.87},
    {'accuracy': 0.85, 'stability': 0.79, 'response_time': 0.72, 'redundancy': 0.91}
]

# Auxiliary calculation with misleading intermediate
normalization_factor = math.sqrt(sum([w**2 for w in metric_weights.values()]))
scaled_weights = {k: v / normalization_factor for k, v in metric_weights.items()}

# Decoy aggregation (never used)
avg_outcome_snapshot = {
    key: round(sum(d[key] for d in raw_outcomes) / len(raw_outcomes), 4)
    for key in raw_outcomes[0].keys()
}

# Core evaluation logic
aggregated_scores = []
for outcome in raw_outcomes:
    score = 0.0
    for metric, weight in metric_weights.items():
        score += weight * outcome[metric] * 100  # Scale to percentage contribution
    aggregated_scores.append(score)

# Secondary adjustment using transformed data
bonus_eligibility = [adj > 0.3 for adj in adjusted]
eligible_count = sum(bonus_eligibility)
performance_bonus = eligible_count * 2.5 if len(aggregated_scores) > 2 else 0

# Final computation
base_performance = sum(aggregated_scores) / len(aggregated_scores)

# Critical statement
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Supporting function defined after use (misdirection)
def evaluate_performance(weights, outcomes):
    """Evaluates weighted performance score across multiple test runs"""
    total = 0.0
    for outcome in outcomes:
        for k, v in weights.items():
            total += v * outcome[k] * 100
    average = total / len(outcomes)
    bonus = len([x for x in base_readings if x > 0.75]) * 2.5  # Bonus per valid reading
    return average + bonus

# Print result
print(f"Result: {final_score}")