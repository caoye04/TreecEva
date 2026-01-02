import math

# Irrelevant constants (distractors)
GRAVITY_CONSTANT = 9.81
NOISE_FLOOR = 0.001
MAX_ITERATIONS = 1000
DUMMY_THRESHOLD = 42

# Sensor simulation data (real input)
sensor_readings = [12, 8, 15, 3, 9, 6, 14]

def preprocess(signal):
    # Distractor: unused normalization path
    normalize = lambda x: x / max(signal) if max(signal) != 0 else 0
    filtered = [x for x in signal if x > 5]  # Only values >5 matter
    return list(map(lambda x: x ** 2 - x, filtered))

def transform_dataset(data):
    # Complex but irrelevant transformation chain
    temp_a = [d * 1.5 for d in data]
    temp_b = [math.sin(x / 10) for x in temp_a]
    weighted = [a * b for a, b in zip(temp_a, temp_b)]
    return sum(weighted)  # Never actually used later

# Dead function – looks important but unused
def legacy_calibrate(values):
    adjustment = 0.95
    return [v * adjustment for v in values if v % 2 == 0]

# Core processing functions
adder_lambda = lambda a, b: a + b

# Accumulate relevant intermediate
processed_data = preprocess(sensor_readings)

# Misleading complex block (no effect on result)
if len(processed_data) > 3:
    dummy_var = 0
    for i in range(len(processed_data)):
        dummy_var += math.log(abs(processed_data[i]) + 1)
        for j in range(2):
            dummy_var = math.sqrt(dummy_var + j) if dummy_var > 0 else 0
            if dummy_var > 10:
                break

# Another red herring: matrix-like structure with no use
redundant_grid = [[i * j + 2 for j in range(4)] for i in range(4)]
summary_stats = {
    'mean': sum(redundant_grid[0]) / 4,
    'peak': max(max(row) for row in redundant_grid),
    'dummy_flag': True
}

# Real computation begins here — heavily obscured
intermediate_sum = 0
for val in processed_data:
    if val % 7 == 0:  # Only 14^2 - 14 = 182 qualifies
        intermediate_sum += val // 7
    elif val > 50:
        intermediate_sum += int(math.sqrt(val))

# Critical decoy: looks like it modifies but doesn't affect logic
shadow_copy = processed_data.copy()
shadow_copy.append(999)

# Final transformation using lambda and arithmetic
final_transform = lambda dataset: (
    intermediate_sum * 2 + 
    len([x for x in dataset if x < 100]) - 
    dataset.count(122)  # This is 0
)

# Key assignment statement
energy_output = final_transform(processed_data)

# Output required format
print(f"Target result: {energy_output}")