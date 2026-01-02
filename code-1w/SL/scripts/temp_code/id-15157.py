import math

# Irrelevant helper function (dead code path)
def legacy_calculate(x):
    return (x ** 2 + 3 * x + 1) % 7

# Misleading transformation chain
temp_buffer = [i * 1.5 for i in range(8)]
scaling_factor = sum(temp_buffer) / len(temp_buffer)
decoys = {f"key_{i}": i * scaling_factor for i in range(5)}

# Actual data source
raw_data = [12, -4, 8, 16, 24]

# Distractor: unused but plausible-looking filter
even_mask = list(map(lambda x: x % 2 == 0, raw_data))

# Real preprocessing step
filtered_data = [x for x in raw_data if x > 0]

# Bit manipulation red herring
dummy_flags = 0b1010
for val in filtered_data:
    dummy_flags ^= (val & 0b111)

# Conditional expression with distractors
status_flag = 'active' if sum(filtered_data) > 30 else 'inactive'
mode_offset = 2 if status_flag == 'active' else -1

# Set operations (relevant)
available_ids = {1, 2, 3, 4, 5, 6}
blacklisted = {3, 5}
valid_ids = available_ids - blacklisted

# Data stream construction with decoy values
data_stream = []
for i, val in enumerate(filtered_data):
    # Complex but partially irrelevant transformation
    transformed = int((val + mode_offset) * (1 + 0.1 * i))
    if i % 2 == 0:
        transformed = int(math.log2(transformed)) if transformed > 0 else 0
    data_stream.append({'id': valid_ids.pop() if valid_ids else 0, 'value': transformed})
    valid_ids.add(i)  # Restore to keep set operations misleading

# Unused sorting (distractor)
sorted_decoy = sorted(data_stream, key=lambda x: x['value'], reverse=True)

# Core processing pipeline (lambda and conditional expressions)
def process_value(item):
    base = item['value']
    # Simulated multi-step logic
    adj = base >> 1 if base > 10 else base << 1
    adj = adj ^ 3 if item['id'] in blacklisted else adj
    return adj + (5 if base % 4 == 0 else 0)

# Real pipeline function
process_pipeline = lambda stream: sum(
    process_value(entry) 
    for entry in stream 
    if entry['id'] % 2 == 1  # Only odd IDs contribute
)

# Final computation
final_output = process_pipeline(data_stream)

# Print result as required
print(f"Target result: {final_output}")