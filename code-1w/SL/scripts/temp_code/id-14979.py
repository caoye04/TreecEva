import math

# Irrelevant helper function (dead code path)
def legacy_calculate(x):
    return (x ** 2 + 3 * x + 1) % 100

# Misleading transformation chain
def transform_segment(segment):
    a = segment ^ 0xFF
    b = (a >> 3) & 0x0F
    c = math.log(b + 1) if b > 0 else 0
    d = int(c * 100)
    return d

# Unused but plausible-looking utility
temp_buffer = [0] * 256
def populate_buffer(value):
    for i in range(len(temp_buffer)):
        temp_buffer[i] = (value * i) % 255

# Core data processing pipeline
mapper = lambda x: x if x < 500 else 999 - x

initial_seed = 17
offset_lookup = {i: (i * 7) % 137 for i in range(15)}

# Simulated sensor data segments (real input)
data_segments = [18, 22, 41, 13, 9, 37]

# Distractor: fake checksum that's never used
current_checksum = 0
for val in data_segments:
    current_checksum ^= (val * 3) % 251

# Auxiliary state with red herring variables
state_flags = {'active': True, 'mode': 'legacy', 'priority': 7}
shadow_stack = []
for i in range(3):
    shadow_stack.append((i * initial_seed) % 43)

# Real processing begins here
filtered_data = list(map(mapper, data_segments))
sliced_view = filtered_data[1:-1]  # Use of slicing

# Complex nested logic with early termination
intermediate_results = []
for val in sliced_view:
    acc = 0
    for shift in offset_lookup.values():
        if shift > 100:
            break  # Early break (rarely triggered)
        temp_val = (val << 2) ^ shift
n        if temp_val % 7 == 0:
            acc += 1
        else:
            acc -= (temp_val % 5)
    intermediate_results.append(acc)
    if acc > 20:
        state_flags['mode'] = 'turbo'
        break

# Secondary transformation using lambda and tuple unpacking
total_pairs = []
for idx, res in enumerate(intermediate_results):
    total_pairs.append((idx, res * 3))

# Final reduction with distractor conditionals
aggregated = 0
threshold_met = False
for index, score in total_pairs:
    if index % 2 == 0:
        aggregated += score
    else:
        if score > 10:
            threshold_met = True
        aggregated -= (score // 2)

# Key computation: optimization based on aggregated flow
def process_pipeline(segments):
    base = sum(segments)
    adjustment = len(intermediate_results) * 4
    penalty = 0
    for s in segments:
        if s > 30:
            penalty += s // 10
    result = base + adjustment - penalty
    # Final twist: apply log scaling only if threshold was met (it wasn't)
    if threshold_met:
        result = math.floor(result * math.log(result))
    return result

# Critical execution point
optimized_flow = process_pipeline(data_segments)

# Output the target result
print(f"Result: {optimized_flow}")