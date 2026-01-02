import math

# Irrelevant helper function (dead code path)
def legacy_calculate(x):
    return (x ** 2 + 3 * x + 1) % 7

# Misleading transformation chain
temp_offset = 17
scaling_factor = 2.5
buffer_cache = [0] * 10

# Simulated sensor data with noise
data_stream = [i ^ 13 for i in range(15) if i % 3 != 0]

# Decoy processing steps (unused results)
filtered_data = [x for x in data_stream if x > 5]
scaled_data = [round(x * scaling_factor, 2) for x in filtered_data]
log_transform = [math.log(x) if x > 0 else 0 for x in scaled_data]

# Real processing path hidden among distractions
def transform_value(val):
    shifted = val << 1
    modded = shifted % 11
    return modded ^ 5

# Accumulation with conditional logic
def accumulate_series(values):
    total = 0
    for v in values:
        if v % 2 == 0:
            total += transform_value(v)
        else:
            total -= (v % 7)
    return total + temp_offset  # temp_offset is real dependency

# Secondary transformation (distractor)
def analyze_pattern(seq):
    pattern_score = 0
    for i in range(len(seq)):
        pattern_score += seq[i] & (i + 1)
    return pattern_score // 2

# Core pipeline function that actually determines result
def process_pipeline(stream):
    # Step 1: Apply bit manipulation via list comprehension
    stage1 = [transform_value(x) for x in stream]
    
    # Step 2: Filter and accumulate
    stage2 = [x for x in stage1 if x < 10]
    
    # Step 3: Sum with modular adjustment
    raw_sum = sum(stage2)
    mod_adjust = raw_sum % 8
    
    # Step 4: Combine with offset and secondary modifier
    modifier = len(stage1) - len(stage2)
    intermediate = raw_sum + mod_adjust * modifier
    
    # Step 5: Final adjustment using accumulation function (key dependency)
    final_component = accumulate_series(stage2)
    
    # Final computation
    result = intermediate - final_component
    return result

# Unused but plausible analysis functions
def validate_integrity(data):
    checksum = 0
    for item in data:
        checksum ^= item
    return checksum == 0

def generate_metadata():
    return {"version": 2.1, "active": True, "mode": "debug"}

# Execution point of interest
final_output = process_pipeline(data_stream)

# Red herring operation (looks important, unused)
buffer_cache[0] = analyze_pattern(data_stream)

print(f"Result: {final_output}")