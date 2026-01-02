import math

# Simulated sensor data with noise and metadata
data_stream = [
    (0.5, 1.2, 'active'), (1.8, 0.9, 'idle'), (2.3, 1.7, 'active'),
    (0.1, 0.3, 'error'), (3.0, 2.5, 'active'), (1.1, 0.8, 'idle'),
    (2.7, 1.9, 'active'), (0.6, 0.7, 'active'), (1.4, 1.1, 'idle')
]

# Irrelevant constants (distractors)
CALIBRATION_OFFSET = 0.042
MAX_BUFFER_SIZE = 1024
TEMPORAL_WINDOW = 5
THRESHOLD_SQUARED = 6.25
EPSILON = 1e-5

# Decoy function - looks important but unused in critical path
def calibrate_signal(x, y):
    return (x + CALIBRATION_OFFSET) ** 2, (y - CALIBRATION_OFFSET) * 1.1

# Another decoy: complex transformation not actually used for final result
def generate_diagnostic_report(data):
    total_entries = len(data)
    status_count = {}
    for _, _, status in data:
        status_count[status] = status_count.get(status, 0) + 1
    return {"total": total_entries, "breakdown": status_count}

# Misleading intermediate computation (dead end)
preliminary_stats = {
    'avg_x': sum([x for x, _, _ in data_stream]) / len(data_stream),
    'avg_y': sum([y for _, y, _ in data_stream]) / len(data_stream),
    'modes': [s for _, _, s in data_stream if s != 'error']
}

# Real processing begins here — filtering active signals
filtered_data = [(x, y) for x, y, status in data_stream if status == 'active']

# Secondary filter based on magnitude threshold (relevance starts here)
filtered_data = [(x, y) for x, y in filtered_data if (x**2 + y**2) <= THRESHOLD_SQUARED]

# Auxiliary calculation that seems related but isn't directly used later
vector_norms = [math.sqrt(x*x + y*y) for x, y in filtered_data]
angle_radians = [math.atan2(y, x) for x, y in filtered_data]

# Bit manipulation red herring: simulates signal encoding
encoded_flags = []
for i, (x, y) in enumerate(filtered_data):
    flag = (i & 7) ^ int(x * 10) | int(y * 5) << 2
    encoded_flags.append(flag % 256)

# Now begin actual recursive processing chain
def integrate_component(values, idx=0, acc=0.0, depth=0):
    if idx >= len(values) or depth > 10:
        return acc
    # Only every second element contributes meaningfully
    if idx % 2 == 0:
        acc += values[idx] * (depth + 1)
    else:
        acc -= values[idx] * 0.1  # minor penalty
    return integrate_component(values, idx + 1, acc, depth + 1)

# Apply recursion on norm-like transformed values (but not raw norms)
transformed_inputs = [
    abs(x - y) + math.log(1 + x * y) for x, y in filtered_data
]

intermediate_sum = integrate_component(transformed_inputs)

# More distraction: zipping unrelated lists
paired_diagnostics = list(zip(vector_norms, angle_radians, encoded_flags))
decoded_summary = 0
for norm, angle, code in paired_diagnostics:
    if norm > 1.0:
        decoded_summary += code & 15  # extract nibble — irrelevant

# Real logic resumes: use enumerate to conditionally scale values
scaling_factor = 1.0
for i, val in enumerate(transformed_inputs):
    if i == 0:
        scaling_factor *= 1.5
    elif val > 1.0:
        scaling_factor += 0.1 * i

adjusted_sum = intermediate_sum * scaling_factor

# Final processing step: simulate multi-stage output validation
validation_seeds = [7, 3, 9]
current_hash = 0
for seed in validation_seeds:
    current_hash ^= int(adjusted_sum) & seed

# Core answer derivation — only this matters
def process_signals(signal_list):
    base = 0.0
    for x, y in signal_list:
        base += x ** 2 - y ** 2  # difference of squares
    return base + math.sin(math.pi / 3) * len(signal_list)

final_output = process_signals(filtered_data)

# Output must be printed exactly like this
print(f"Target result: {final_output}")