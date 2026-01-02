import math

def analyze_pattern(seq):
    # Irrelevant function: analyzes sequence symmetry (dead end)
    return sum(1 for i in range(len(seq)) if seq[i] == seq[-(i+1)])

def dummy_transform(x):
    # Distractor: unused transformation
    return (x ** 2 + 3 * x + 1) % 107

def evaluate_stability(ratio):
    # Misleading intermediate calculation
    if ratio < 0.5:
        return math.log(1 / ratio)
    else:
        return math.exp(-ratio)

# Unused data structures acting as red herrings
trend_data = [0.1, 0.4, 0.8, 1.2, 1.6]
config_map = {'alpha': 0.7, 'beta': 1.3, 'gamma': 0.9}
flag_lookup = {k: (v > 1) for k, v in config_map.items()}

# Core logic disguised among noise
primes = [2, 3, 5, 7, 11, 13, 17]
shift_key = len(primes) * 2  # Red herring value

offset_table = {i: (primes[i] * shift_key) % 25 for i in range(len(primes))}

# Lambda-based filtering (partially relevant)
valid_filter = lambda x: x > 0 and (x % 2 == 1 or x % 3 == 0)

data = [84, -12, 18, 27, 36, 45, 13]
weights = [0.1, 0.3, 0.15, 0.05, 0.2, 0.1, 0.1]

# Decoy accumulation with misleading comments
running_total = 0
for val in trend_data:
    running_total += math.sin(val)  # Irrelevant trigonometric accumulation

# Real processing buried in complexity
def process_metrics(values, scales):
    filtered = [v for v in values if valid_filter(abs(v))]  # Use of lambda
    adjusted = []
    index = 0
    
    while index < len(filtered):
        item = filtered[index]
        # Conditional expression with modular arithmetic
        transformed = item * scales[index % len(scales)] if item % 2 == 0 else (item + 1) * scales[index % len(scales)]
        adjusted.append(transformed)
        index += 1
    
    # Bit manipulation decoy
    mask = 0b1101
    masked_sum = sum(adjusted) ^ mask  # XOR distraction
    
    # Actual result computation
    base_result = sum(adjusted)  # This contributes to final answer
    
    # Short-circuit evaluation pattern (distractor)
    fallback = base_result > 100 and evaluate_stability(0.8) or -1.0
    
    # Dictionary operation that looks important but isn't used directly
    stats = {
        'count': len(adjusted),
        'sum': base_result,
        'special': analyze_pattern(primes)  # Calls dead-end function
    }
    
    # Final computation chain
    temp = stats['sum'] * 1.1
    correction = math.floor(temp / 10) * 0.5
    return int(temp - correction)

# Early termination decoy
if len(data) > 10:
    final_score = -999
else:
    final_score = process_metrics(data, weights)

# Additional irrelevant bit shifting
checksum = 0
for p in primes:
    checksum ^= (p << 2) >> 1

# Output the target variable
print(f"Result: {final_score}")