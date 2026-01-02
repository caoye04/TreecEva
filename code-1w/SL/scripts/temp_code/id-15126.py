import math

# Irrelevant helper function (dead code path)
def unused_transform(x):
    return [val ** 2 for val in x if val % 3 == 0]

# Distractor variables
temp_cache = [i * 2 + 1 for i in range(15)]
shadow_buffer = sum([i for i in temp_cache if i > 10])
flag_lookup = {i: (i % 4 == 0) for i in range(12)}

# Relevant data structure initialization
data_stream = [3, 7, -2, 8, 1, 4, 9, 6, 5]

# Misleading pre-processing (partially unused)
filtered_data = [x for x in data_stream if x > 0]
sorted_data = sorted(filtered_data, reverse=True)

# Bit manipulation decoy
bit_flags = [(x << 1) ^ 3 for x in sorted_data]
activation_mask = sum(bit_flags[:4]) & 0xFF

# Conditional slicing with red herring logic
if len(sorted_data) > 5:
    sliced_view = sorted_data[2:7:2]  # Uses slicing operation
else:
    sliced_view = sorted_data

# Decoy dictionary transformation
stats_summary = {
    'max_val': max(sliced_view),
    'min_val': min(sliced_view),
    'range': max(sliced_view) - min(sliced_view),
    'ignored_metric': sum([math.log(abs(x) + 1) for x in sliced_view])
}

# Unused recursive distraction
def bad_recursion(n):
    if n <= 1:
        return 1
    return n * bad_recursion(n - 2)

# Core processing pipeline (actually used)
def process_pipeline(input_seq):
    accumulator = 0
    threshold = 6
    
    # Loop with early break and conditional branches
    for val in input_seq:
        if val <= 0:
            continue
        squared = val * val
        root_val = math.sqrt(abs(val))
        
        # Key conditional logic
        if squared > 20:
            if root_val < 3:
                accumulator += val // 2
            else:
                accumulator -= val % 3
        else:
            accumulator += int(root_val)
            
        # Early exit red herring (never triggered due to data)
        if accumulator > 100:
            break  # Dead logic

    # Secondary transformation on accumulator
    intermediate = (accumulator * 3) ^ 7  # Bitwise XOR distraction
    intermediate = abs(intermediate)
    
    # Final adjustment using slice-derived value
    control_factor = sliced_view[1] if len(sliced_view) > 1 else 1
    final_adjusted = intermediate - control_factor
    
    # Injection of irrelevant dictionary lookup
    for k in flag_lookup:
        if k == control_factor:
            final_adjusted += 1  # Never hits due to value mismatch
            break
            
    return final_adjusted

# Execution point of interest
final_output = process_pipeline(data_stream)

print(f"Target result: {final_output}")