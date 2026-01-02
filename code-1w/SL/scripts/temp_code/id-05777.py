import math

# Irrelevant helper function (dead code path)
def calculate_thermal_output(energy):
    return energy * 0.87 + 23

def transform_signal(data, threshold=100):
    # Complex transformation with red herring logic
    filtered = [x for x in data if x > threshold // 2]
    shifted = [(x << 1) ^ 3 for x in filtered]  # Bit manipulation distraction
    return list(map(lambda y: y if y % 4 == 0 else y + 1, shifted))

# Unused but plausible-looking processing chain
def analyze_pattern(sequence):
    accumulator = 0
    for i, val in enumerate(sequence):
        if i % 3 == 0:
            accumulator += math.sin(val / 10) * 100
    return int(accumulator)

# Core data generation with hidden logic
raw_input = tuple(range(15, 25))

# Distractor variables (irrelevant computations)
bogus_sum = sum([i ** 2 for i in range(7)])
scaling_factor = math.log(81, 3)  # Evaluates to 4, but looks complex
offset_table = {i: (i * scaling_factor) % 7 for i in range(10)}

# Real processing begins — nested transformations
intermediate = tuple(math.ceil((x * 1.5) - 8) for x in raw_input)
processed_a = transform_signal(intermediate, threshold=20)

# Decoy branching logic (never executed)
if len(processed_a) < 5:
    processed_a = [x + 100 for x in processed_a]
elif sum(processed_a) % 2 == 0:
    processed_a = [x ^ 15 for x in processed_a]  # XOR distraction
else:
    pass  # Dead end

# Actual relevant computation buried in noise
adjusted = [x - 5 for x in processed_a if x > 10]

# Key function containing final answer derivation
def harvest_results(data):
    base = 1
    for i, val in enumerate(data):
        if i % 2 == 0 and val > 20:
            base *= (val // 4)
        elif i % 2 == 1:
            base += (val % 7)
    return base * 3

# Critical statement — target of evaluation
final_yield = harvest_results(adjusted)

# Print result as required
print(f"Target result: {final_yield}")