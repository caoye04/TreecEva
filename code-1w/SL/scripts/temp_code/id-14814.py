def analyze_efficiency(data, threshold=0.75):
    above_threshold = list(filter(lambda x: x > threshold, data))
    return len(above_threshold) / len(data) if data else 0

# Simulate sensor readings from three subsystems
data_stream_a = [0.82, 0.67, 0.91, 0.73, 0.88]
data_stream_b = [0.76, 0.81, 0.69, 0.93]
data_stream_c = [0.54, 0.77, 0.85, 0.68, 0.92, 0.79]

# Misleading normalization (not used in final result)
normalized_a = [round(x * 100) for x in data_stream_a]
dummy_sum = sum(normalized_a)

# Evaluate each subsystem's compliance rate
compliance_a = analyze_efficiency(data_stream_a)
compliance_b = analyze_efficiency(data_stream_b)
compliance_c = analyze_efficiency(data_stream_c)

# Weighted importance of each subsystem (calibration factors)
weights = [0.4, 0.35, 0.25]

# Track auxiliary stats (distractor variables)
average_compliance = (compliance_a + compliance_b + compliance_c) / 3
variance_proxy = (compliance_a - average_compliance)**2 + (compliance_b - average_compliance)**2 + (compliance_c - average_compliance)**2

# Key metrics in order: A, B, C
metrics = [compliance_a, compliance_b, compliance_c]

# Secondary processing chain (some steps irrelevant)
processing_steps = []
for i, (m, w) in enumerate(zip(metrics, weights)):
    adjusted = m * w
    squared_dev = (m - 0.8) ** 2  # unused distraction
    processing_steps.append(adjusted)

# Unused intermediate transformation
temp_results = list(map(lambda x: x + 0.1, processing_steps))

# Core aggregation function
def aggregate_performance(mets, wts):
    total = 0.0
    for idx in range(len(mets)):
        total += mets[idx] * wts[idx]
    return round(total * 100, 2)  # Return percentage score

# Final computation step
calibration_offset = 5.0  # red herring, not applied
final_score = aggregate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")