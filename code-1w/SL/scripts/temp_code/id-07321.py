import itertools

def preprocess_sensor(stream):
    offset = 5
    return [x + offset for x in stream if x > -270]

def calculate_optimal_yield(temp_stream, press_stream):
    # Misleading intermediate calculations
    baseline = sum(press_stream) / len(press_stream)
    adjusted_temps = [t * 1.8 + 32 for t in temp_stream]  # Convert to Fahrenheit (unused path)
    filtered_pairs = [(t, p) for t, p in zip(temp_stream, press_stream) if t >= 0]

    # Distractor: complex-looking but unused lambda
    anomaly_detector = lambda x: (x[0] > 100 and x[1] < baseline)
    anomalies = list(filter(anomaly_detector, filtered_pairs))

    # Actual relevant logic begins here
    scaled_pressure = [p * 0.01 for p in press_stream]
    composite_index = []
    for i, t in enumerate(temp_stream):
        if i % 2 == 0:
            idx = t * scaled_pressure[i % len(scaled_pressure)]
            composite_index.append(idx)
        else:
            # This branch contributes nothing due to filtering later
            composite_index.append(0)

    # Key computation
    valid_indices = [idx for idx in composite_index if idx > 0]
    average_effect = sum(valid_indices) / len(valid_indices) if valid_indices else 0

    # Secondary transformation with distractor variables
    peak = max(temp_stream)
    noise_floor = 0.05 * peak  # Unused variable
    damping_factor = 0.9 if peak > 50 else 0.95

    final_yield = average_effect * damping_factor * 10

    # Dead code path - never executed due to logic
    if len(anomalies) > 100:
        final_yield *= 0.5

    return final_yield

# Simulated sensor data
raw_temperature = [-20, 45, 60, -5, 80, 30]
temperature_data = preprocess_sensor(raw_temperature)
pressure_data = [1000, 950, 1050, 900, 1100, 980]

# Execute main logic
final_yield = calculate_optimal_yield(temperature_data, pressure_data)
print(f"Result: {final_yield}")