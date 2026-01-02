def analyze_system_stability(readings):
    base_threshold = 75
    adjustment_factor = 1.2
    temp_buffer = []
    stability_scores = []

    for reading in readings:
        raw_value = reading * adjustment_factor
        if raw_value > 100:
            raw_value = 100
        temp_buffer.append(raw_value)

    # Compute rolling average for smoothing
    for i in range(len(temp_buffer)):
        window = temp_buffer[max(0, i-2):i+1]
        avg = sum(window) / len(window)
        stability_scores.append(round(avg, 1))

    # Misleading computation: unused derived metric
    derived_trend = 0
    for i in range(1, len(stability_scores)):
        derived_trend += stability_scores[i] - stability_scores[i-1]
    derived_trend = round(derived_trend, 2)

    # Add padding to avoid edge effects (simulates signal processing)
    stability_scores = [stability_scores[0]] + stability_scores + [stability_scores[-1]]

    # Key statement: extract peak from interior region
    peak_stability = max(stability_scores[1:-1])

    # Dead code path: never executed under current logic
    if False:
        fallback = sum(stability_scores) / len(stability_scores)
        peak_stability = max(peak_stability, fallback)

    # Irrelevant normalization
    total_norm = sum(s**2 for s in stability_scores)**0.5
    normalized_peak = peak_stability / total_norm if total_norm != 0 else 0

    return peak_stability

# Simulated sensor readings
sensor_data = [60, 68, 70, 72, 67, 75, 73, 69]
result = analyze_system_stability(sensor_data)
print(f"Result: {result}")