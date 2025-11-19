import math
from functools import wraps

def depth_tracker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.depth += 1
        result = func(*args, **kwargs)
        wrapper.depth -= 1
        return result
    wrapper.depth = 0
    return wrapper

def generate_modified_fibonacci(n, modifier_func):
    if n <= 0:
        return []
    elif n == 1:
        return [modifier_func(1)]
    elif n == 2:
        return [modifier_func(1), modifier_func(1)]
    
    sequence = [modifier_func(1), modifier_func(1)]
    for i in range(2, n):
        next_val = sequence[i-1] + sequence[i-2]
        sequence.append(modifier_func(next_val))
    return sequence

@depth_tracker
def backtrack_analyze(data, index, accumulator):
    if index >= len(data):
        return accumulator
    
    # Process current element with statistical weight
    weighted_value = data[index] * (index + 1)
    accumulator.append(weighted_value)
    
    # Recursive exploration with condition
    if data[index] % 2 == 0:
        return backtrack_analyze(data, index + 2, accumulator)
    else:
        return backtrack_analyze(data, index + 1, accumulator)

# Main processing pipeline
signal_modifier = lambda x: x * 2 if x % 3 == 0 else x + 1
raw_sequence = generate_modified_fibonacci(10, signal_modifier)
sorted_sequence = sorted(raw_sequence, reverse=True)

# Apply backtracking analysis
analysis_result = []
backtrack_analyze(sorted_sequence, 0, analysis_result)

# Statistical computations using lambda functions
mean_calculator = lambda lst: sum(lst) / len(lst) if lst else 0
variance_component = lambda lst, mean: sum((x - mean) ** 2 for x in lst) / len(lst) if lst else 0

computed_mean = mean_calculator(analysis_result)
processed_variance = round(variance_component(analysis_result, computed_mean))

print(f"Result: {processed_variance}")