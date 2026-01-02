import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return (x ** 2 + 3 * x + 1) % 7

# Misleading transformation chain
def decoy_transform(sequence):
    temp = [i * 2 for i in sequence if i % 2 == 0]
    return sorted(temp, reverse=True)

# Auxiliary function with red herring logic
def side_calc(values):
    accumulator = 0
    for v in values:
        if v > 5:
            accumulator += v ^ 3  # Bitwise XOR distraction
    return accumulator * 0.5  # Never used but looks important

# Core processing pipeline
def process_pipeline(chunk):
    # Step 1: Filter and transform relevant data
    filtered = [x for x in chunk if x % 3 == 0]
    
    # Step 2: Apply conditional exponentiation
    processed = [
        val ** 2 if val > 0 else abs(val) + 1
        for val in filtered
    ]
    
    # Step 3: Compute running sum with offset
    running_sum = sum(processed) + 17
    
    # Step 4: Conditional logic determining final branch
    threshold = 100
    adjustment = (running_sum > threshold) \n        and (len(processed) % 2 == 0) \n        or (running_sum % 7 == 0)
    
    # Step 5: Key branching decision (only this affects output)
    if adjustment:
        result = running_sum // 2
    else:
        result = int(math.sqrt(running_sum))
    
    # Step 6: Final bitwise refinement
    result ^= 13  # XOR mask applied unconditionally
    
    # Step 7: Redundant check (distractor)
    if all(x < 50 for x in chunk):
        result -= 999  # Dead path — never reached due to input
    
    # Step 8: Return final computed value
    return result

# Irrelevant global constants
data_snapshot = [1, 4, 6, 8, 10]
backup_buffer = list(reversed(data_snapshot))

# Decoy data structure
analysis_report = {
    'status': 'complete',
    'metrics': {'p1': 0.91, 'p2': 0.76},
    'payload': side_calc([4, 8, 12])
}

# Actual input data (carefully chosen to follow correct path)
data_chunk = [9, -3, 6, 12, 15, 3]  # All divisible by 3; positive dominant

# Execution point of interest
final_output = process_pipeline(data_chunk)

# Print target result
print(f"Target result: {final_output}")