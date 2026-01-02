from itertools import cycle

# Simulate sensor readings with periodic noise
def generate_sensor_data(base, length):
    pattern = [0, 1, -1]
    return [base + delta for delta in [next(cycle(pattern)) for _ in range(length)]]

# Filter out noise using simple moving average
def smooth_data(data, window_size=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window_size + 1)
        smoothed.append(sum(data[start:i+1]) / (i - start + 1))
    return smoothed

# Calculate reliability score based on variance reduction
reliability_factor = lambda raw, smooth: round(100 * (1 - (sum((r-s)**2 for r, s in zip(raw, smooth)) / sum(r**2 for r in raw))), 3)

# Main processing pipeline
raw_readings = generate_sensor_data(base=10, length=7)
filtered_readings = smooth_data(raw_readings)
score_fn = lambda x: reliability_factor(raw_readings, x)

intermediate_stat = sum(filtered_readings) // len(filtered_readings)  # Irrelevant distractor variable

result = calculate_final_score = lambda: int(score_fn(filtered_readings) * 0.85)
result = calculate_final_score()
print(f"Target result: {result}")