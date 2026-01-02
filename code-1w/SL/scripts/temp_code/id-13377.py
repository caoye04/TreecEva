def analyze_efficiency(metrics):
    base = sum(m * (i + 1) for i, m in enumerate(metrics))
    adjusted = base * 0.9 if len(metrics) > 5 else base * 1.1
    return adjusted


def extract_signals(log_data):
    segments = log_data.split(',')
    values = [int(s.strip()[2:]) for s in segments if s.startswith('S:')]
    return [v for v in values if v % 2 == 1]  # Keep only odd values


def assess_stability(readings):
    normalized = [r / max(readings) for r in readings]
    trend = sum(1 for a, b in zip(normalized, normalized[1:]) if b > a)
    volatility = sum(abs(a - b) for a, b in zip(normalized, normalized[1:]))
    return trend - volatility * 0.5


def evaluate_performance(output, risk):
    efficiency = output * 0.8
    penalty = risk * 2.3
    score = efficiency - penalty
    return int(score) if score > 0 else 0

# Simulated sensor log input
log_input = "S:44, S:23, S:67, S:12, S:89, S:35, S:76"

# Extract and process signal data
signal_values = extract_signals(log_input)
dummy_calc_1 = [x ** 2 for x in signal_values if x < 50]  # Irrelevant computation

# Analyze system efficiency from derived metrics
metrics_data = [len(signal_values), sum(signal_values), max(signal_values), min(signal_values)]
efficiency_score = analyze_efficiency(metrics_data)

# Assess operational stability
stability_readings = [efficiency_score / 100.0, 0.67, 0.54, 0.89, 0.45]
dummy_calc_2 = ''.join([str(int(r * 10)) for r in stability_readings])  # Misleading string operation
stability_index = assess_stability(stability_readings)

# Compute composite performance factors
productivity = efficiency_score + stability_index * 10
temp_tracker = tuple((i, val) for i, val in enumerate(stability_readings))  # Dead code path
risk_factor = len(dummy_calc_1) * 3.7

# Critical evaluation point
final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")