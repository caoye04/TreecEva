import math

# Irrelevant helper function (dead code path)
def unused_signal_filter(x):
    return [v for v in x if v % 3 == 0]

# Decoy transformation with misleading intermediate results
def decoy_enhance(seq):
    shifted = [(v << 2) ^ 5 for v in seq]
    normalized = [abs(s) % 100 for s in shifted]  # Not actually used later
    return normalized

# Real data transformation chain
def transform_input(raw):
    processed = []
    for item in raw:
        if item < 0:
            processed.append(abs(item) * 3)
        elif item % 2 == 0:
            processed.append(item + 7)
        else:
            processed.append(item ** 2)
    return processed

# Core pattern analyzer (uses lambda abstraction)
analyze_pattern = lambda data: sum(
    math.floor(math.sin(x) * 100) if x % 4 == 0 else 
    math.ceil(math.cos(x) * 50) if x > 50 else 
    x // 7 for x in data
)

# Misleading diagnostic chain (distractor)
def false_diagnosis(seq):
    score = 0
    for v in seq:
        score += (v & 7) ^ 3
        if score > 100:
            score -= 80
    return score * 2  # Never called but looks important

# Unused complex structure
class DataInspector:
    def __init__(self, values):
        self.values = values
        self.checksum = sum(v % 11 for v in values)

    def validate(self):
        return self.checksum % 7 == 0

# Simulated sensor readings (initial input)
sensor_readings = [ -4, 12, 5, 8, 13, 21, 16 ]

# Apply real transformation
transformed_data = transform_input(sensor_readings)

# Irrelevant list comprehension (red herring)
filtered_diagnostics = [x for x in transformed_data if x > 10 and (x & 1) == 0]

# Secondary fake processing that computes but doesn't affect result
shadow_buffer = [math.log(v + 10) for v in transformed_data if v < 30]

# Key computational step with meaningful nesting and logic
intermediate_flags = []
for i, val in enumerate(transformed_data):
    if i % 3 == 0:
        flag = (val + i) ^ 7
    elif val > 25:
        flag = val >> 1
    else:
        flag = val * 2 + (i & 3)
    intermediate_flags.append(flag)

# Dummy bit manipulation chain (decoy logic)
bit_accumulator = 0
for f in intermediate_flags:
    bit_accumulator ^= (f << 1) | 1
    bit_accumulator %= 97

# Final analysis using lambda function (critical execution point)
final_diagnostic = analyze_pattern(transformed_data)

# Print result as required
print(f"Target result: {final_diagnostic}")