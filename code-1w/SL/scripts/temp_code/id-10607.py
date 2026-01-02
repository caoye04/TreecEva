def analyze_efficiency(metrics):
    adjusted = []
    penalty_factor = 0.85
    for val in metrics:
        if val > 100:
            adjusted.append(val * 0.9)
        elif val < 50:
            adjusted.append(val * 1.1)  # Compensation for low values
        else:
            adjusted.append(val)
    return [x for x in adjusted if x > 0]  # Remove any potential negatives (none here)


def calculate_stability(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    stability_score = 100 - (variance / 10)
    return max(stability_score, 10)

# Simulate daily productivity metrics over a workweek
daily_output = [85, 102, 45, 93, 110]

# Apply efficiency analysis
efficiency_curve = analyze_efficiency(daily_output)

# Calculate baseline stability
baseline_stability = calculate_stability(efficiency_curve)

# Track cumulative progress with redundant tracking
progress_log = []
cumulative_total = 0
for day in efficiency_curve:
    cumulative_total += day
    progress_log.append(cumulative_total)

# Introduce irrelevant auxiliary computation (distractor)
temp_buffer = [x * 0.01 for x in progress_log]
scaling_constant = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0

# Define risk thresholds using set operations
productivity = set(efficiency_curve)
thresholds = {x for x in range(90, 120)}  # High-performance band
risk_set = productivity.symmetric_difference(thresholds)

# Secondary metric: volatility index (not used in final answer)
avg = sum(efficiency_curve) / len(efficiency_curve)
volatility_index = sum(abs(x - avg) for x in efficiency_curve) / avg

# Core evaluation logic
high_performers = productivity.intersection(thresholds)
consistency_bonus = len(high_performers) * 5

# Final performance scoring
base_performance = sum(efficiency_curve) / len(efficiency_curve)
stability_modifier = baseline_stability / 100

# Red herring: unused conditional adjustment
if len(risk_set) > 10:
    base_performance *= 0.9
elif len(risk_set) < 3:
    base_performance *= 1.05  # Not triggered

# Key statement
final_score = evaluate_performance(productivity, risk_set)

# Helper function defined after use (syntactically valid due to execution order)
def evaluate_performance(perf_set, risk):
    base = sum(perf_set)
    risk_penalty = len(risk) * 2
    safety_margin = 10 if len(perf_set.difference(risk)) > 4 else 5
    return int((base - risk_penalty) + safety_margin + consistency_bonus)

print(f"Result: {final_score}")