import math

# Irrelevant helper function (dead code path)
def unused_diagnostic(x):
    return sum([i ** 2 for i in x if i % 3 == 0])

# Distractor variables
diag_flag = True
buffer_cache = [0] * 100
offset_correction = 3.14159

# Real data stream with embedded signal
raw_signal = [18, 27, 36, 45, 54, 63]
noise_floor = list(map(lambda x: x % 10, raw_signal))  # Irrelevant transformation

# Key preprocessing chain
filtered = [x for x in raw_signal if x > 20]
scaled = [x // 9 for x in filtered]  # Integer division

# Bit manipulation red herring
twisted = 0
for val in scaled:
    twisted ^= (val << 2) | (val >> 1)

# Logical control flow with nested conditions
trigger_state = False
if len(scaled) > 3:
    if sum(scaled) % 2 == 0:
        trigger_state = True

# Decoy data structure
log_entry = {
    'timestamp': 1678886400,
    'status': 'OK',
    'diagnostics': [twisted, offset_correction],
    'payload_size': len(raw_signal)
}

# Core processing pipeline (relevant)
def transform(x):
    return (x + 1) * 2

def validate(x):
    return x % 3 == 0

# Higher-order function with lambda (required python feature)
processor_chain = [
    lambda arr: [transform(x) for x in arr],
    lambda arr: [x for x in arr if validate(x)],
    lambda arr: sorted(arr, reverse=True)
]

# Data transformation pipeline
intermediate_mask = [int(math.log2(x)) for x in scaled if x > 1]  # Partially irrelevant

# Main data flow
data_stream = [3, 5, 6, 7]

# Simulated pipeline execution
pipeline_state = data_stream.copy()
for stage in processor_chain:
    pipeline_state = stage(pipeline_state)

# Conditional mutation based on decoy logic
if trigger_state and diag_flag:
    pipeline_state = [x + 10 for x in pipeline_state]
else:
    pipeline_state = [x - 1 for x in pipeline_state]

# Final aggregation
aggregated = 0
for i, val in enumerate(pipeline_state):
    if i % 2 == 0:
        aggregated += val * 2
    else:
        aggregated -= val

# Critical assignment point
final_output = aggregated + len(log_entry['diagnostics'])

# Output result as required
print(f"Result: {final_output}")