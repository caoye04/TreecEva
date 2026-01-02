import math

# Irrelevant helper function (dead code path)
def legacy_calculate(x):
    return (x ** 2 + 3 * x + 1) % 100

# Misleading transformation chain
def transform_signal(values):
    temp_result = [v * 1.5 for v in values if v % 2 == 0]
    shifted = [(t + 42) % 256 for t in temp_result]
    return [math.sin(s * math.pi / 180) for s in shifted]

# Unused data structure (distractor)
error_log = {
    'codes': [404, 500, 403],
    'count': 0,
    'active': False
}

# Core processing pipeline
def evaluate_constraints(seq):
    valid = []
    for i, val in enumerate(seq):
        if i % 3 == 0 and val > 0:
            valid.append(abs(val) ** 0.5)
    return valid

# Auxiliary calculation with decoy intermediate results
def compute_entropy(arr):
    total = sum(arr)
    norm = [x / total for x in arr if total != 0]
    entropy = 0
    for p in norm:
        if p > 0:
            entropy -= p * math.log(p)
    return entropy * 100  # scaled for distraction

# Real computation buried in abstraction
def filter_and_aggregate(data):
    # Step 1: Extract every second element
    subset = [x for i, x in enumerate(data) if i % 2 == 1]
    
    # Step 2: Apply conditional modification
    adjusted = []
    for item in subset:
        if item < 0:
            adjusted.append(item ** 2)
        else:
            adjusted.append(item + 1)
    
    # Step 3: Pairwise summation via zip
    paired = [a + b for a, b in zip(adjusted, adjusted[1:])]
    
    # Step 4: Accumulate final sum
    accumulator = 0
    for num in paired:
        accumulator += int(num) % 97
    
    return accumulator

# Higher-order orchestrator with red herring logic
def analyze_pattern(stream):
    # This looks important but is unused in final result
    stats = {
        'mean': sum(stream) / len(stream),
        'peak': max(stream),
        'triggers': [i for i, x in enumerate(stream) if x > 50]
    }
    
    # Actual relevant transformation
    modified = [x - 1 for x in stream if x % 4 == 0]
    return len(modified) > 0  # boolean side result

# Main processing function
def process_pipeline(input_seq):
    # Key manipulation steps
    base_mod = [x for x in input_seq if x % 2 == 0]  # Keep evens
    
    # Add offset using enumeration
    offset_data = [val + idx for idx, val in enumerate(base_mod)]
    
    # Introduce bitwise distraction
    masked = []
    for num in offset_data:
        mask = (num ^ 255) & 0xFF  # bit flip and truncate
        if mask > 100:
            masked.append(mask)
    
    # Real accumulation hidden among distractions
    running_sum = 0
    for i, m in enumerate(masked):
        if i % 2 == 0:
            running_sum += m // (i + 1)
        else:
            running_sum -= m % 7
    
    # Final aggregation step (this feeds into answer)
    secondary = filter_and_aggregate(input_seq)
    
    # Critical combination point
    final_value = running_sum + secondary - len(masked)
    
    # Output variable
    final_output = final_value
    
    # Decoy print statements (not executed)
    # print(f'Debug: {stats}')
    # print(f'Entropy score: {compute_entropy(base_mod)}')
    
    return final_output

# Input data stream (meaningful pattern)
data_stream = [12, -8, 33, 4, 19, 16, 44, 7, -2, 64, 51, 28]

# Execute main logic
final_output = process_pipeline(data_stream)

# Output result as required
print(f"Target result: {final_output}")