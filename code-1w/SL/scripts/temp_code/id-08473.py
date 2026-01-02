import math

# Irrelevant helper function (dead code path)
def unused_helper(data):
    return [x ** 2 for x in data if x % 3 == 0]

# Decoy transformation with misleading intermediate result
def decoy_transform(seq):
    temp = [int(math.sqrt(x)) if x > 0 else 0 for x in seq]
    scaling_factor = 7  # Misleading variable
    normalized = [round(v / scaling_factor, 2) for v in temp]
    return normalized  # Never actually used

# Real transformation function
transform_fn = lambda arr: [x * 2 + 1 for x in arr]

# Complex flag generation with red herring logic
def generate_flags(values):
    flags = []
    threshold = sum(v % 5 for v in values[:10]) // 2
    for i, val in enumerate(values):
        if i == 0:
            flags.append(val % 2 == 0)
        elif i % 3 == 0:
            # Complex but partially irrelevant condition
            parity_check = (val + i) % 4 < 2
            magnitude_check = val > threshold * 1.5
            flags.append(parity_check or magnitude_check)  # Some influence
        else:
            flags.append(False)
    # Dead assignment - looks important but unused
    final_flag_snapshot = flags.copy()
    return flags

# Main processing with nested logic
def process_data(data, control_flags):
    accumulator = 0
    temp_results = []
    
    for idx, (val, flag) in enumerate(zip(data, control_flags)):
        if not flag and idx % 2 == 1:
            continue  # Early skip - relevant control flow
        adjusted = val + int(math.log2(idx + 1)) if idx > 0 else val
        
        # Bit manipulation red herring
        binary_shift = (adjusted << 1) ^ 3
        decoy_value = binary_shift & 0xFF  # Looks cryptic but unused
        
        # Actual contribution
        if idx % 4 == 0:
            accumulator += adjusted * 3
        elif idx % 4 == 2:
            accumulator -= adjusted // 2
        else:
            accumulator += adjusted % 7
            
        temp_results.append(accumulator)
    
    # Final adjustment with hidden rule
    correction_factor = len([x for x in temp_results if x > 50])
    accumulator -= correction_factor * 2
    
    # Unused complex structure - distractor
    summary_stats = {
        'peak': max(temp_results, default=0),
        'variance_proxy': sum((x - accumulator) ** 2 for x in temp_results[-3:]) / 3 if len(temp_results) >= 3 else 0,
        'ignored_metric': math.atan2(correction_factor, accumulator)
    }
    
    return accumulator

# Irrelevant data initialization
dummy_cache = {i: math.factorial(i % 6) for i in range(15)}

# Core input sequence generation with subtle pattern
base_sequence = [i * i - 2*i + 3 for i in range(1, 17)]

# Apply real transformation
transformed = transform_fn(base_sequence)

# Generate control flags using original base, not transformed (important detail)
flags = generate_flags(base_sequence)

# Critical execution point
final_output = process_data(transformed, flags)

# Print result as required
print(f"Result: {final_output}")