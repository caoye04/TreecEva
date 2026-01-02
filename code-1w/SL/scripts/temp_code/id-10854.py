import math

# Irrelevant helper function (dead code path)
def unused_transform(x):
    return (x ** 2 + 3 * x + 1) % 100

# Misleading data processing chain
data_stream = [i * 3 + 2 for i in range(150) if i % 4 != 0]
decoys = [math.sin(math.radians(j)) for j in range(0, 360, 15)]  # Unused trigonometric noise
temp_shift = list(map(lambda x: x << 2, data_stream[:50]))  # Bit-shift red herring, not used later

# Actual signal embedded in noise
raw_checksum = 0
for val in data_stream:
    if val % 7 == 0:
        raw_checksum += val * 0.5

# Decoy accumulator with plausible but irrelevant logic
phantom_total = 0
for idx, num in enumerate(data_stream):
    if idx % 11 == 0 and num < 300:
        phantom_total += num

# Core logic buried under distractions
threshold = 42
scaling_factor = 1.25
offset_compensation = lambda a: a - int(a * 0.1)  # Unused compensation function

# Critical filtering operation
valid_entries = []
for item in data_stream:
    normalized = item // 3
    meets_criteria = (normalized > threshold) and ((normalized ^ 7) & 1 == 1)
    if meets_criteria:
        valid_entries.append(normalized)

# Secondary filter based on digit sum (real condition)
def digit_sum(n):
    return sum(int(d) for d in str(abs(n)))

valid_entries = [v for v in valid_entries if digit_sum(v) % 3 == 2]

# Accumulation step — this is where the answer is determined
filtered_sum = sum(valid_entries)

# More distraction: complex unused transformation
data_matrix = [[i + j * 10 for i in range(8)] for j in range(8)]
transformed_matrix = [
    [math.log(1 + abs(cell), 10) * scaling_factor for cell in row]
    for row in data_matrix
]

# Final output (must print the target result)
print(f"Result: {filtered_sum}")