import math

# Simulated system telemetry (irrelevant data)
technical_metrics = {
    'latency': [120, 150, 130, 180],
    'bandwidth': [85.5, 90.2, 87.1, 88.3],
    'jitter': [5, 8, 6, 10]
}

# Core evaluation parameters
metric_data = {
    'accuracy': 0.92,
    'complexity_weight': 3.5,
    'iterations': 144,
    'threshold': 0.85,
    'penalty_factor': 0.9,
    'base_offset': 17
}

# Decoy function - looks important but unused
def analyze_bandwidth(data):
    avg = sum(data['bandwidth']) / len(data['bandwidth'])
    return avg * 0.01

# Auxiliary transformation (distractor)
transformed = list(map(lambda x: round(x ** 0.5, 2), technical_metrics['latency']))

# Dummy counters (misleading intermediate values)
alert_count = 0
warning_level = 0
for val in technical_metrics['jitter']:
    if val > 7:
        alert_count += 1
        warning_level += val // 2

# Real processing begins here
def compute_adjustment(iterations, weight):
    if iterations <= 100:
        return iterations * 0.7
    else:
        # Complex adjustment with nested logic
        temp = iterations // (weight + 1)
        temp = temp if temp % 2 == 0 else temp + 1
        return int(math.log(temp + 10, 2) * weight)

# Scoring engine with red herrings
def evaluate_performance(metrics):
    score = 0

    # Primary contribution
    if metrics['accuracy'] > metrics['threshold']:
        base = metrics['accuracy'] * 100
        adjustment = compute_adjustment(metrics['iterations'], metrics['complexity_weight'])
        score += base + adjustment

        # Conditional penalty application
        if metrics['accuracy'] < 0.95:
            score *= metrics['penalty_factor']

    # Irrelevant branch (never executes due to data)
    if metrics['accuracy'] > 1.0:
        score += 50  # Impossible condition

    # Destructive unpacking distraction
    try:
        values = [10, 20, 30, 40]
        a, b, *rest = values
        c = rest[0] * 0.1  # Computed but not used
    except:
        c = 0

    # Final offset addition (key step)
    score += metrics['base_offset']

    # Dead code path
    debug_trace = []
    for i in range(3):
        debug_trace.append(f"Step {i}")  # Unused list

    return int(round(score))

# Spurious dictionary operation (looks like it modifies something)
diag_report = {k: f"{v}_diag" for k, v in metric_data.items()}

# Key execution point
final_score = evaluate_performance(metric_data)

# Output result
print(f"Result: {final_score}")