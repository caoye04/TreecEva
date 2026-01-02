from itertools import compress, count
import math

# Simulate sensor data stream with noise and redundant readings
data_stream = [14, 18, 22, 25, 27, 30, 33, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45]

# Irrelevant baseline calibration (red herring)
calibration_offset = sum([x % 3 for x in range(15)]) / 7
offset_adjusted = [x - calibration_offset for x in data_stream]

# Noise filter mask using prime detection (complex distractor)
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))
valid_indices = [is_prime(i) for i in range(len(data_stream))]
filtered_readings = list(compress(data_stream, valid_indices))  # Only positions at prime indices

# Secondary filtering based on growth rate (misleading path)
growth_rates = [(data_stream[i] - data_stream[i-1]) / data_stream[i-1] for i in range(1, len(data_stream))]
stable_growth_mask = [rate < 0.1 for rate in growth_rates]
adjusted_length = min(len(stable_growth_mask), len(data_stream))

# Decoy function: appears important but unused
def analyze_variance(sequence):
    mean_val = sum(sequence) / len(sequence)
    return sum((x - mean_val) ** 2 for x in sequence) / len(sequence)

# Destructuring assignment with irrelevant components
primary_signal, *background_noise = data_stream[::3]  # Pick every 3rd element

# Accumulate relevant metrics using lambda-based reducer
accumulator = lambda acc, val: acc + (val ** 1.5 if val % 2 == 0 else val ** 0.8)
aggregated_value = 0
for val in filtered_readings:
    aggregated_value = accumulator(aggregated_value, val)

# Complex conditional processing chain
if len(filtered_readings) > 5:
    adjustment_factor = 0.88
else:
    adjustment_factor = 1.12

threshold_func = lambda x: int(x ** 0.5) % 2 == 0

# Data transformation via zip and count (distractor)
indexed_pairs = list(zip(count(start=1), offset_adjusted))
decay_weights = [math.exp(-i * 0.1) for i in range(len(indexed_pairs))]
weighted_sum = sum(val * weight for (_, val), weight in zip(indexed_pairs, decay_weights))

# Real computation begins here — aggregate using filtered data
aggregated_data = []
for idx, value in enumerate(filtered_readings):
    if idx % 2 == 0:
        transformed = int(math.log(value + 10) * 100)
    else:
        transformed = int(value / math.pi)
    aggregated_data.append(transformed)

# Finalize processing: this is where the answer is determined
finalize_processing = lambda data, func: sum(x for x in data if func(x)) - sum(x for x in data if not func(x))
filtration_score = finalize_processing(aggregated_data, threshold_func)

# Dead code branch — never executed (decoy control flow)
if __debug__:
    debug_info = analyze_variance(background_noise)

# Output result
print(f"Result: {filtration_score}")