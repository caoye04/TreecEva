import math

# Simulate sensor readings with noise
data_stream = [3.2, 5.7, 1.4, 8.9, 2.6, 7.1, 4.3, 6.8, 9.5, 0.8]

# Irrelevant transformation (distractor)
weighted_sum = sum(x * 0.9 for x in data_stream)
scaled_values = [x * 1.1 for x in data_stream]

# Noise threshold and filtering logic
noise_floor = 2.0
filtered_values = [x for x in data_stream if x > noise_floor]

# Secondary filtering based on fractional part (semi-relevant but not used directly)
fractional_filtered = [x for x in filtered_values if math.modf(x)[0] > 0.2]

# Dummy aggregation function (dead code path)
def aggregate_signals(data):
    return sum(x ** 0.5 for x in data if x < 6.0)

# Core processing via lambda and conditional logic
transform_fn = lambda x: x ** 2 if x < 6.0 else math.log(x)

# Apply transformation
processed = [transform_fn(val) for val in filtered_values]

# Conditional sorting based on average (misleading computation)
avg_processed = sum(processed) / len(processed)
sorted_processed = sorted(processed, reverse=(avg_processed > 10))

# Another distraction: simulate calibration offset
offset = 0.0
for i in range(len(sorted_processed)):
    if i % 3 == 0:
        offset += 0.05

# Actual final processing function
def process_data(values):
    temp_result = 0.0
    for v in values:
        if v < 6.0:
            temp_result += v * 1.5
        elif v >= 6.0 and v < 8.0:
            temp_result += v * 0.8
        else:
            temp_result += math.sqrt(v)
    return int(temp_result)  # Final quantization step

# Key statement
final_output = process_data(filtered_values)

# Output result
print(f"Result: {final_output}")