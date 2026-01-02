def analyze_trend(data, threshold=0.5):
    moving_avg = [sum(data[i:i+3]) / 3 for i in range(len(data) - 2)]
    deviations = [(x - moving_avg[0]) for x in data[2:]]
    volatility = sum(abs(d) for d in deviations) / len(deviations) if deviations else 0
    return volatility > threshold

# Simulated sensor metrics over time
sensor_readings = [0.4, 0.6, 0.5, 0.7, 0.8, 0.65, 0.72, 0.68]

# Irrelevant transformation - distractor
transformed_data = list(map(lambda x: x ** 2 + 0.1, sensor_readings))
buffer_slice = transformed_data[2:6]
offset_correction = sum(buffer_slice) / 4

# Core metric computation with slicing and filtering
cleaned = [x for x in sensor_readings if 0.45 < x < 0.75]
efficiency_peaks = [i for i, x in enumerate(sensor_readings) if x > 0.7 and i % 2 == 0]

# Weight assignment using conditional logic
base_weights = [0.2, 0.3, 0.25, 0.15]
temporal_bias = [1.0, 1.05, 0.95, 1.1]  # unused but plausible
weights = [w * 1.0 for w in base_weights]  # neutral scaling (distractor)

# Secondary analysis - misleading path
outlier_count = 0
for val in sensor_readings:
    if abs(val - 0.6) > 0.15:
        outlier_count += 1
adjustment_factor = outlier_count * 0.05  # computed but unused

# Key state variables
metrics = [
    len(cleaned),                    # count of valid readings
    len(efficiency_peaks),            # number of even-indexed peaks
    int(analyze_trend(sensor_readings)), # trend stability (0 or 1)
    sum(cleaned) / len(cleaned) if cleaned else 0  # average of clean data
]

# Red herring: complex-looking but unused structure
summary_matrix = [[m * w for w in weights] for m in metrics]

# Critical computation step
final_score = aggregate_performance = lambda m, w: sum(m[i] * w[i] for i in range(len(m)))
final_score = aggregate_performance(metrics, weights)

# Debug print removed - only final result output
print(f"Result: {final_score}")