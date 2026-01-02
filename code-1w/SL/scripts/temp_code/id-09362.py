def analyze_pattern(seq):
    """Irrelevant function analyzing character patterns."""
    freq = {}
    for char in seq:
        freq[char] = freq.get(char, 0) + 1
    return {k: v for k, v in freq.items() if v > 1}

# Irrelevant data structures
dummy_logs = ['error', 'info', 'debug', 'warning']
status_map = {'active': 1, 'paused': 0, 'closed': -1}

# Decoy weight configurations
weights_a = [0.1, 0.2, 0.7]
weights_b = [0.5, 0.3, 0.2]  # unused
weights_c = [0.4, 0.4, 0.2]  # unused

# Real weights used in computation
weights = [0.6, 0.3, 0.1]

# Sensor input data (simulated readings)
data = [850, 420, 120]

# Auxiliary transformation (distractor)
normalized = list(map(lambda x: round(x / max(data), 3), data))

# Misleading intermediate score
baseline_score = sum(data) / len(data)

# Complex data processing with red herrings
def adjust_for_bias(val, mode='standard'):
    if mode == 'high':
        return val * 1.1
    elif mode == 'low':
        return val * 0.9
    return val  # standard mode

# Unused adjustment functions
def legacy_adjust(x):
    return x * 0.95 + 10

def experimental_scale(x):
    return x ** 0.5 * 10

# Core processing logic with distractions
def compute_factor(a, b, c):
    temp = a * weights[0]
    
    # Distractor block - looks important but not used
    if temp > 500:
        adjustment = 1.05
    else:
        adjustment = 0.95
    
    # Actual relevant path
    result = temp + (b * weights[1])
    result += (c * weights[2])
    return result

# Secondary validation (irrelevant)
def validate_input(arr):
    return all(isinstance(x, int) and x >= 0 for x in arr)

# Data integrity check (unused)
data_checksum = sum(d % 10 for d in data)

# Main processing function with multiple concepts
def process_metrics(readings, w):
    # Unpack with enumerate for distraction
    indexed = [v for i, v in enumerate(readings)]
    
    # Apply bias correction (uses standard mode)
    corrected = [adjust_for_bias(v) for v in readings]
    
    # Use zip to pair values with weights (key step)
    paired = list(zip(corrected, w))
    
    # Compute weighted sum using lambda (core operation)
    weighted_sum = sum(map(lambda x: x[0] * x[1], paired))
    
    # Additional scaling based on threshold logic
    if weighted_sum > 700:
        scale_factor = 0.8
    elif weighted_sum > 500:
        scale_factor = 0.9
    else:
        scale_factor = 1.0
    
    # Final transformation
    final = weighted_sum * scale_factor
    
    # Dead code path - looks like post-processing
    if final < 0:
        final = abs(final) * 0.5
    
    return int(final)

# Execution point of interest
final_score = process_metrics(data, weights)

# Print result as required
print(f"Target result: {final_score}")