def preprocess_data(raw):
    # Irrelevant preprocessing steps (distractors)
    cleaned = [x for x in raw if x > 0]
    stats = {'sum': sum(cleaned), 'len': len(cleaned)}
    normalized = [x / stats['sum'] for x in cleaned]  # Not actually used
    return cleaned

# Decoy function that looks important but isn't used
def compute_entropy(values):
    from math import log
    total = sum(values)
    entropy = 0
    for v in values:
        p = v / total
        entropy -= p * log(p)
    return entropy

# Another decoy: complex bit manipulation with no impact
def mask_outliers(arr, threshold=4):
    result = []
    mask = (1 << threshold) - 1
    for x in arr:
        masked = x & mask
        if masked < threshold:
            result.append(x)
    return result  # Never called

# Real logic buried among distractions
def transform_sequence(seq):
    # Step 1: filter multiples of 3
    seq = [x for x in seq if x % 3 == 0]
    
    # Step 2: map using modular arithmetic
    seq = [(x * 2 + 1) % 17 for x in seq]
    
    # Step 3: reverse and shift
    seq = seq[::-1]
    shifted = [seq[i] - i for i in range(len(seq))]
    
    # Step 4: conditional accumulation
    acc = 0
    for val in shifted:
        acc += val if val > 0 else 0  # Ignore negatives
    
    return acc

# Core calculation function
def calculate_final_score(raw_input):
    # Distractor: unused statistical variables
    mean_val = sum(raw_input) / len(raw_input)
    variance_proxy = sum((x - mean_val) ** 2 for x in raw_input)
    outlier_flag = variance_proxy > 100
    
    # Actual data flow
    filtered_data = preprocess_data(raw_input)
    
    # More distraction: fake validation check
    is_valid = all(x < 100 for x in filtered_data)
    checksum = sum(filtered_data[i] * (i+1) for i in range(len(filtered_data))) % 19
    
    # Key transformation
    intermediate = transform_sequence(filtered_data)
    
    # Conditional expression (required Python feature)
    adjustment = 15 if len(filtered_data) > 5 else 7
    
    # Final computation
    base_score = intermediate * 3
    final_score = base_score + adjustment - checksum
    
    # Critical point: this is the answer variable
    return final_score

# Simulated dataset with meaningful name
network_latency_samples = [12, -5, 18, 21, 0, 24, 9, 33, -2, 6, 39]

# Execution entry point
processed = preprocess_data(network_latency_samples)
data = [x for x in network_latency_samples if x > 0]  # Redundant but misleading
final_score = calculate_final_score(data)
print(f"Result: {final_score}")