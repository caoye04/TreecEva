def analyze_efficiency(raw_metrics):
    # Irrelevant transformation - distractor
    adjusted = [x * 1.05 for x in raw_metrics if x > 0]
    baseline = sum(adjusted) / len(adjusted) if adjusted else 0

    # Red herring computation with unused result
    volatility = sum((x - baseline) ** 2 for x in adjusted) ** 0.5 if adjusted else 0

    # Real processing path begins here
    filtered = [x for x in raw_metrics if x >= 50]  # Only values >= 50 matter
    capped = [min(x, 95) for x in filtered]  # Cap at 95
    return capped


def normalize_data(values):
    if not values:
        return [0]
    max_val = max(values)
    return [round(v / max_val * 100, 2) for v in values] if max_val != 0 else [0] * len(values)

# Decoy function - never called
def compute_risk_factor(data):
    risk = 0
    for i in range(len(data)):
        if i % 3 == 0:
            risk += data[i] * 0.1
    return round(risk, 3)

# Another decoy - looks important but unused
system_thresholds = {"level1": 45, "level2": 70, "level3": 85}
active_modes = ["diagnostic", "standard", "enhanced"]
mode_multiplier = {"diagnostic": 0.9, "standard": 1.0, "enhanced": 1.1}

# Core logic variables
metric_weights = [0.2, 0.3, 0.15, 0.25, 0.1]
raw_input_metrics = [88, 72, 94, 63, 47, 91, 68, 55]

# Distractor list comprehension with side effect-like appearance (but unused)
processed_pairs = [(a, b) for a in raw_input_metrics for b in metric_weights if a * b > 20]

# Real data flow starts here
focused_metrics = analyze_efficiency(raw_input_metrics)

# This normalization is actually used
normalized_contributions = normalize_data(focused_metrics)

# Dead code branch - misleading control flow
if len(normalized_contributions) > 10:
    scaling_factor = 1.2
else:
    scaling_factor = None  # Never used

# Key computation: weighted sum using only first five elements (padding if needed)
while len(normalized_contributions) < len(metric_weights):
    normalized_contributions.append(0)

# Final evaluation function
def evaluate_performance(weights, contributions):
    total = 0.0
    for i in range(len(weights)):
        total += weights[i] * contributions[i]
    return round(total, 4)

# Critical statement
final_score = evaluate_performance(metric_weights, normalized_contributions)

# Output result as required
print(f"Result: {final_score}")