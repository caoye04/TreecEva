import math

def analyze_signal(data, threshold=0.5):
    """Irrelevant function: simulates signal processing."""
    filtered = [x for x in data if abs(x) > threshold]
    normalized = [x / max(filtered) for x in filtered]
    return sum(normalized)


def evaluate_risk(profile):
    """Irrelevant function: evaluates risk based on profile."""
    age, income, score = profile
    if age < 30 and income > 70000:
        return 'high'
    elif score > 800:
        return 'low'
    else:
        return 'medium'


def transform_features(features):
    """Partially relevant: modifies feature set but only one output matters."""
    a, b, c = features
    temp_x = (a ** 2 + b ** 2) ** 0.5
    temp_y = abs(c - a)
    magnitude = int(temp_x // (temp_y + 1))
    category = 'A' if magnitude > 10 else 'B'
    return magnitude, category, temp_x  # Only magnitude used later


def compute_weights(values):
    """Distractor: computes weights not used in final path."""
    total = sum([v**2 for v in values])
    return [v**2 / total for v in values]


def integrate_feedback(results, adjustments):
    """Dead code path: never called."""
    return [r * (1 + adj) for r, adj in zip(results, adjustments)]

# Irrelevant global constants
data_stream = [0.1, -0.3, 0.7, 1.2, -0.9]
baseline_config = {'mode': 'alpha', 'version': 2.1}

# Key data structures
feature_set = (12, 5, 8)
score_flags = {True, False, True, False}
metric_history = [88, 92, 76, 85]

# Intermediate variables with misleading computations
raw_analysis = analyze_signal(data_stream)
risk_profile = (28, 75000, 820)
risk_level = evaluate_risk(risk_profile)

# Partially used transformation
extracted_magnitude, _, _ = transform_features(feature_set)

# Distractor list comprehension
weight_distribution = compute_weights([3, 4, 5])

# Complex conditional with red herring branches
if len(metric_history) > 3:
    avg_metric = sum(metric_history) / len(metric_history)
    adjusted_metrics = [m * 1.1 for m in metric_history if m > 80]
    if avg_metric >= 85:
        bonus_factor = 1.5
    else:
        bonus_factor = 1.2
        secondary_adjust = [m * 0.9 for m in metric_history]  # Unused
else:
    bonus_factor = 1.0

# Set operations with irrelevant transformations
flag_state = score_flags and {True, False}  # Results in mixed boolean set
flag_sum = sum([int(f) for f in flag_state])  # Computed but not critical

# Core logic embedded within noise
base_score = extracted_magnitude * 100
penalty = 0

if any(metric < 80 for metric in metric_history):
    penalty += 15

if len(flag_state) == 2:
    penalty -= 5  # Net effect: reduces penalty due to duplicate booleans

# Critical statement buried in context
final_score = process_outcome = lambda m, f: (
    base_score - penalty + 
    (50 if len(set(m)) > 2 else 30) + 
    (20 if all(f) else 0)
)(metric_history, score_flags)

print(f"Result: {final_score}")