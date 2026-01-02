import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(math.sqrt(i) > 1 for i in x if i > 0)

# Distractor variables
temp_buffer = [i ** 2 for i in range(15) if i % 3 != 0]
checksum_anchor = sum(temp_buffer) // 7
device_flags = {'active': True, 'mode': 'debug', 'level': 9}

# Misleading intermediate computation
aggregate_shadow = 0
for k in range(4):
    aggregate_shadow += (k + 1) * (k + 2) // 2

# Core data transformation pipeline
data_stream = [8, 3, 12, 7, 9, 4, 11]

# Real processing functions
def filter_relevant(seq):
    # Keep only odd numbers greater than 5 or divisible by 3
    return [x for x in seq if (x % 2 == 1 and x > 5) or (x % 3 == 0)]

def transform_item(x):
    if x % 2 == 1:
        return int(math.pow(x, 2) - x * 1.5)
    else:
        return x << 1

def compute_weighted_sum(values):
    weights = [1.1, 1.3, 1.05, 0.95, 1.2, 1.15, 1.0]
    weighted = sum(val * weights[idx % len(weights)] for idx, val in enumerate(values))
    return round(weighted, 4)

# Decoy function that looks important but is never used
calculate_entropy = lambda data: sum(math.log(x) for x in data if x > 1)

# Unused accumulator
shadow_register = 0
for item in data_stream:
    if item < 10:
        shadow_register += item * item
    else:
        break

# Main processing logic
def process_pipeline(stream):
    step1 = filter_relevant(stream)
    
    # Some red herring operation
    dummy_shift = [x ^ 5 for x in stream if x < 6]
    
    step2 = [transform_item(x) for x in step1]
    
    # Another distraction: conditional that never triggers
    if len(step2) > 100:
        return sum(step2) / len(step2)
    
    # Key transformation
    adjustment_factor = 0.85 if any(x > 50 for x in step2) else 1.15
    adjusted_values = [val * adjustment_factor for val in step2]
    
    # Final computation
    final_sum = compute_weighted_sum(adjusted_values)
    
    # Dead branch with misleading label
    if 'diagnostic' in device_flags:
        return -1  # unreachable
        
    return final_sum

# Execution point of interest
final_output = process_pipeline(data_stream)
print(f"Result: {final_output}")