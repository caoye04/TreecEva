import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(v > 0 for v in x) if isinstance(x, list) else False

# Distractor variables
dummy_mask = [1, 0, 1, 1, 0]
placeholder_sum = 0
temp_buffer = {i: i**2 for i in range(10)}

# Logical operation with red herring intermediate
event_flag = True and not False or (1 == 0)
flag_weight = event_flag * 5.5  # Misleading float usage

# Bit manipulation decoy chain
bit_trail = 0
for shift in [1, 2, 4]:
    bit_trail |= (1 << shift)
bit_trail ^= 255  # Further obfuscation

# Actual data stream (slice-based processing)
data_stream = [3, 7, -2, 8, 1, 9, 4, 6][1:6]  # Slice: [7, -2, 8, 1, 9]

# Lambda-based transformation pipeline
transform_A = lambda x: x * 2 if x > 0 else x + 10
transform_B = lambda x: int(math.log(abs(x) + 1, 2))  # Stable mapping

# Dictionary-based state tracker (used later)
state_registry = {
    'level': 3,
    'mode': 'active',
    'threshold': 7
}

# Conditional data routing (short-circuit evaluation pattern)
routing_key = (state_registry['level'] > 2) and (state_registry['mode'] == 'active')
secondary_check = routing_key and bool(transform_A(-5))  # Always true

# Core processing function with nesting and slicing
def process_pipeline(stream):
    accumulator = 0
    history = []
    
    for index, val in enumerate(stream):
        # Nested condition with logical ops and bitwise distraction
        if val > 0:
            transformed = transform_A(val)
            if transformed >= state_registry['threshold']:
                # Apply secondary transform only on high values
                secondary = transform_B(transformed)
                
                # Bitwise mix (relevant step)
                mixed = secondary ^ (index | 3)  # XOR with OR-mask
                accumulator += mixed
                
                # Update history (tuple unpacking)
                history.append((index, mixed))
            else:
                accumulator += transformed % 4
        else:
            # Negative branch with decoy computation
            decoy_calc = (val * 100) >> 2  # Shift, never used
            accumulator += abs(val)
    
    # Post-processing with dictionary lookup and slicing
    cutoff = min(3, len(history))
    recent = history[-cutoff:] if history else []
    
    # Final adjustment using logical reduction
    bonus = 0
    for pos, entry in enumerate(recent):
        idx, val = entry  # Tuple unpacking
        bonus += val & (pos + 1)  # Bitwise AND with position
    
    return accumulator + bonus

# Unused alternate version (distractor)
def process_pipeline_v2(stream):
    return sum(x ** 0.5 for x in stream if x > 0)

# Key execution point
final_output = process_pipeline(data_stream)

# Output result
print(f"Result: {final_output}")