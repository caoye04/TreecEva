import math

# Irrelevant helper function (dead code path)
def unused_transform(x):
    return [val ** 2 for val in x if val % 3 == 0]

# Decoy statistical analyzer (never called in execution path)
class StatsAnalyzer:
    def __init__(self, values):
        self.values = sorted(values)
    
    def get_median(self):
        n = len(self.values)
        mid = n // 2
        return self.values[mid] if n % 2 else (self.values[mid-1] + self.values[mid]) / 2

# Misleading intermediate computation with decoy result
temp_buffer = [i * 1.5 for i in range(10)]
decoys = {f'key_{i}': temp_buffer[i] * math.sin(i) for i in range(len(temp_buffer))}

# Core logic disguised among distractions
data_stream = [
    14, 28, 42, 56, 70,  # Multiples of 14
    99, 105, 111         # Non-multiples (red herring group)
]

# Lambda-based filtering function (actually used)
effective_filter = lambda seq, base: list(filter(lambda x: x % base == 0, seq))

# Conditional branching with nested logic
if len(data_stream) > 5:
    filtered_data = effective_filter(data_stream, 14)
else:
    filtered_data = data_stream

# Bit manipulation red herring
bitmask_results = []
for i in range(3):
    shifted = (255 << i) & 1023
    bitmask_results.append(shifted ^ 7)  # Computationally irrelevant

# String processing distraction
status_log = "event:START|step:INIT|mode:DEBUG"
log_parts = status_log.split('|')
context_map = dict(part.split(':') for part in log_parts)

# Real transformation chain
scaling_factor = 3
scaled_filtered = [elem * scaling_factor for elem in filtered_data]

# Conditional data augmentation (only some elements qualify)
augmented_data = []
for val in scaled_filtered:
    if val > 50:
        augmented_data.append(val + (val // 10))
    elif val == 42:
        augmented_data.append(val * 2)
    else:
        augmented_data.append(val)

# Final pipeline processing with closure
def process_pipeline(stream):
    offset = len(stream) * 2
    
    def apply_correction(value):
        return value + offset if value % 5 != 0 else value
    
    corrected = [apply_correction(x) for x in stream]
    
    # Another decoy operation
    _ = [math.log(x + 1) for x in corrected if x < 30]
    
    # Actual aggregation
    aggregate = 0
    for idx, num in enumerate(corrected):
        weight = 1 + (idx * 0.1)
        aggregate += num * weight
    
    # Final adjustment based on bitwise property
    if aggregate & 1:
        aggregate -= 5
    else:
        aggregate += 2
        
    return int(aggregate)

# Execution point of interest
final_output = process_pipeline(augmented_data)

# Output required format
print(f"Result: {final_output}")