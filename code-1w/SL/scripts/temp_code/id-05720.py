def calculate_performance(base, data):
    adjustments = []
    penalty_factor = 0.85
    bonus_threshold = base * 1.1
    warning_threshold = base * 0.9
    cumulative_deviation = 0
    peak_anomaly = 0
    trend_stability = 0

    for i, value in enumerate(data):
        deviation = value - base
        cumulative_deviation += abs(deviation)

        if value > bonus_threshold:
            adjustments.append(1.2)
        elif value < warning_threshold:
            adjustments.append(0.88)
        else:
            adjustments.append(1.0)

        # Track largest anomaly
        if abs(deviation) > peak_anomaly:
            peak_anomaly = abs(deviation)

        # Simulate trend smoothing (irrelevant to final score)
        if i > 0:
            delta = data[i] - data[i-1]
            trend_stability += abs(delta)

    # Irrelevant secondary calculation (distractor)
    avg_adjustment = sum(adjustments) / len(adjustments) if adjustments else 1.0
    total_penalty = cumulative_deviation * 0.01

    # Actual scoring logic
    performance_multiplier = sum(1.0 if adj > 1.0 else 0.5 for adj in adjustments)
    
    # Key statement
    final_score = int((performance_multiplier * avg_adjustment * 10) - total_penalty + (42 if peak_anomaly < 20 else 0))

    return final_score

# Baseline and sensor readings from system diagnostics
baseline = 95
readings = [90, 98, 102, 89, 96, 105, 87, 94]

# Dead code path - never executed but adds cognitive load
if __name__ != "__main__":
    debug_log = [f"Raw: {x}" for x in readings]
    normalized = [x / max(readings) for x in readings]

# Core execution
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")