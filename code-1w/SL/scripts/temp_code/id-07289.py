import math

# Irrelevant helper function (dead code path)
def unused_signal_processor(x):
    return [i ** 2 for i in x if i % 3 == 0]

# Distractor variable
temp_calibration = [math.sin(i) for i in range(10)]
scaling_factor = 0.987
offset_adjustment = sum(temp_calibration[:5]) * scaling_factor

# Simulated sensor data with noise
data_stream = [12, 45, 23, 67, 89, 34, 56, 78, 90, 11]

# Misleading intermediate transformation
noisy_envelope = list(map(lambda x: abs(x - 50) + 0.1 * x, data_stream))
decoy_aggregate = sum(noisy_envelope) / len(noisy_envelope) + offset_adjustment

# Actual relevant processing begins here
filtered_readings = [x for x in data_stream if x > 30]
squared_signals = [x * x for x in filtered_readings]

# Bit manipulation red herring
bitwise_mask = 0b101010
masked_values = [x & bitwise_mask for x in squared_signals]  # unused later

# Conditional expression with logical operations
threshold_func = lambda x: x > 2000 and (x % 2 == 0 or x < 5000)

# Another decoy structure
class DataObfuscator:
    def __init__(self, factor):
        self.factor = factor

    def transform(self, data):
        return [d * self.factor for d in data]

obfuscate = DataObfuscator(1.5)
phantom_data = obfuscate.transform(data_stream)  # never used

# Real signal transformation
transformed_data = [sq + 2 * idx for idx, sq in enumerate(squared_signals)]

# Red herring: complex but unused calculation
correlation_score = sum(
    transformed_data[i] * transformed_data[i+1] 
    for i in range(len(transformed_data)-1)
) / (sum(transformed_data) + 1)

# Core logic hidden among distractions
def analyze_pattern(seq, condition):
    count_valid = 0
    cumulative = 0
    for val in seq:
        # Nested conditional expressions
        adjusted_val = val if condition(val) else (val // 2 if val > 1000 else val * 3)
        cumulative += adjusted_val
        if adjusted_val > 2500:
            count_valid += 1
            # Additional distraction inside loop
            temp_shift = math.log(adjusted_val, 2) if adjusted_val > 0 else 0
    return cumulative - count_valid * 100

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold_func)

print(f"Result: {final_diagnostic}")