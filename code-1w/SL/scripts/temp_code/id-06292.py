import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(i > 0 for i in x) if isinstance(x, list) else False

# Decoy transformation chain
def decoy_transform(sequence):
    temp = [math.sin(x) * 2.5 for x in sequence]
    adjusted = [round(t, 2) for t in temp]
    return [a + 1 for a in adjusted]  # Never used

# Real processing core
def entropy_score(values):
    total = sum(values)
    probs = [(v / total) for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

# Key lambda for dynamic filtering
even_filter = lambda seq, threshold: [x for x in seq if x % 2 == 0 and x > threshold]

# Dictionary-based operation router
operations = {
    'shift': lambda x: [i << 1 for i in x],
    'scale': lambda x: [int(i * 1.5) for i in x],
    'fold': lambda x: [abs(i - 10) for i in x]
}

# Misleading accumulation (red herring)
running_diagnostics = {
    'checksum': 0,
    'iterations': 0,
    'anomalies': []
}

# Fake recursive tracker (unused but looks important)
call_depth = [0]
def track_recursion(n):
    call_depth[0] += 1
    if n <= 1:
        return 1
    return track_recursion(n - 2) + 1

# Real data processor with layered logic
def process_chunk(chunk, mode):
    if mode == 'A':
        return operations['shift'](chunk)
    elif mode == 'B':
        filtered = even_filter(chunk, 3)
        return operations['scale'](filtered)
    else:
        folded = operations['fold'](chunk)
        return [f + 2 for f in folded]

# Main pipeline with conditional routing
def process_pipeline(stream, config):
    intermediate = []
    for segment in stream:
        key = list(config.keys())[0]
        if config[key] > len(segment):
            processed = process_chunk(segment, 'A')
        elif config[key] == len(segment):
            processed = process_chunk(segment, 'B')
        else:
            processed = process_chunk(segment, 'C')
        intermediate.extend(processed)
    
    # Redundant smoothing pass (looks important but doesn't affect outcome)
    smoothed = [int((intermediate[i] + intermediate[i-1]) / 2) if i > 0 else intermediate[0] for i in range(len(intermediate))]
    
    # Critical computation hidden among distractions
    entropy = entropy_score(intermediate)
    
    # Decoy summation with misleading name
    diagnostic_sum = sum(smoothed) + len(smoothed)  # Unused
    
    # Actual answer derivation
    magnitude = sum(1 for x in intermediate if x > 8)
    final_value = int(entropy * magnitude * 10)
    
    # The target variable
    final_output = final_value
    
    # Print required output
    print(f"Result: {final_output}")
    return final_output

# Simulated input data
data_stream = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

config = {'threshold': 3}

# Execution point of interest
final_output = process_pipeline(data_stream, config)