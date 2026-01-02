from collections import defaultdict
import math

# Simulated sensor node metadata (irrelevant to final result)
node_registry = {
    'A1': {'type': 'input', 'status': 'active'},
    'B2': {'type': 'output', 'status': 'standby'},
    'C3': {'type': 'compute', 'status': 'active'}
}

# Irrelevant transformation function (dead code path)
def legacy_normalize(x):
    return [val / max(x) for val in x if val > 0]

# Unused helper that looks important
def compute_entropy(seq):
    freq = defaultdict(int)
    for item in seq:
        freq[item] += 1
    return -sum(p * math.log2(p) for p in (f / len(seq) for f in freq.values()))

# Decoy data structure with misleading values
decoy_matrix = [
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 1, 0]
]
decoy_sum = sum(sum(row) for row in decoy_matrix)  # Red herring computation

# Actual signal data (simulated input)
signal_buffer = [5, 3, 8, 3, 9, 5, 7, 3, 8, 5]

# Transform function using slicing and lambda
transformed_data = list(map(lambda x: (x ** 2) % 7, signal_buffer[::2]))  # Use only even indices

# Another irrelevant calculation on original buffer
smoothed = [sum(signal_buffer[i:i+3]) / 3 for i in range(len(signal_buffer) - 2)]
avg_smooth = sum(smoothed) / len(smoothed)

# Threshold map built with defaultdict (relevant)
threshold_map = defaultdict(lambda: 3)
for i, val in enumerate(transformed_data):
    threshold_map[i] = val % 4 + 1

# Auxiliary function that appears critical but is unused
def validate_coherence(data, thresholds):
    return all(data[i] >= thresholds[i] for i in range(len(data)))

# Core analysis function with nested logic
def analyze_pattern(seq, thresh):
    accumulator = 0
    history = []
    
    for i in range(len(seq)):
        # Bit manipulation mixed with arithmetic
        temp_val = (seq[i] ^ thresh[i]) + (i & 1)  # XOR and bitwise AND
        
        # Conditional accumulation with short-circuit logic
        if i > 0 and history and (temp_val > history[-1] or not (temp_val < 2 and i < 5)):
            accumulator += temp_val * 2
        else:
            accumulator += temp_val // 2 + 1
            
        # List mutation that looks important but only last value matters
        history.append(temp_val)
    
    # Final adjustment using sum and modular arithmetic
    core_metric = (accumulator * 3) % 19
    
    # Complex but deterministic mapping
    adjustment = 0
    for j in range(core_metric):
        if j % 4 == 0:
            adjustment += 1
        elif j % 3 == 0:
            adjustment -= 1
    
    return core_metric + adjustment

# Execution point of interest
core_flux = analyze_pattern(transformed_data, threshold_map)

# Distractor: another variable that looks like the answer
final_output = (core_flux + decoy_sum) * 2  

# Irrelevant print statements (not executed in logic)
# print(f'Signal integrity: {avg_smooth:.2f}')
# print(f'Decoy entropy: {compute_entropy([1,2,2,3])}')

# Correct output
print(f"Result: {core_flux}")