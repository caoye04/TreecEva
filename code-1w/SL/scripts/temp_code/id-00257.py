from itertools import accumulate

# Simulate sensor readings with small drift
def preprocess_signal(readings):
    bias_correction = lambda x: x - 0.1
    corrected = [bias_correction(x) for x in readings]
    return list(accumulate(corrected))

# Apply transformation to detect cumulative trend
def transform_data(signal):
    processed = preprocess_signal(signal)
    trend_factor = sum(1 for x in processed if x > 5)
    return int(sum(processed) * 0.1) + trend_factor

values = [1.2, 1.1, 1.3, 1.5, 1.8, 2.0, 2.2, 2.4]
result = transform_data(values)
print(f"Result: {result}")