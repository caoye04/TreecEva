def transform_sequence(seq, offset):
    # Irrelevant transformation (dead logic path)
    return [x * 2 for x in seq if x % 2 == 0]


def compute_entropy(data):
    # Misleading function: looks important but unused in critical path
    result = 0
    for x in data:
        result += x ^ (x << 1)
    return result % 100


def shift_window(arr, window_size):
    # Distractor: complex-looking but unused in main logic
    windows = []
    for i in range(len(arr) - window_size + 1):
        windows.append(sum(arr[i:i+window_size]))
    return sorted(windows, reverse=True)


def recursive_fold(seq, depth):
    # Relevant recursive function used in actual computation
    if depth == 0 or len(seq) < 2:
        return seq[0] if seq else 1
    mid = len(seq) // 2
    left = recursive_fold(seq[:mid], depth - 1)
    right = recursive_fold(seq[mid:], depth - 1)
    return (left + right) * (depth % 4 + 1)


def analyze_pattern(signal):
    # Dead code: never called
    return sum(x ** 0.5 for x in signal if x > 0)


def process_phase(sequence, index):
    # Core logic with slicing and modular arithmetic
    segment = sequence[index:index+7]  # Slice of interest
    rotated = segment[3:] + segment[:3]  # Rotate by 3
    
    # Apply modular transforms
    mapped = [(val * 7 + 13) % 23 for val in rotated]
    
    # Bit manipulation red herring
    decoy_value = 0
    for val in mapped:
        decoy_value ^= (val << 2) | (val >> 1)
    
    # Real calculation uses recursion on transformed slice
    base_seq = [mapped[i] - i for i in range(len(mapped))]
    pivot = len(base_seq) // 2
    left_part = base_seq[:pivot]
    right_part = base_seq[pivot:]
    
    # Recursive folding determines final output
    fold_depth = (mapped[0] + mapped[-1]) % 5 + 2
    left_result = recursive_fold(left_part, fold_depth)
    right_result = recursive_fold(right_part, fold_depth)
    
    # Final computation
    final_score = (left_result * right_result) - (fold_depth ** 2)
    return final_score

# Initialization of various signals (many irrelevant)
signal_a = [1, 8, 15, 22, 4, 11, 18, 25, 7, 14]
signal_b = [x**2 % 19 for x in range(12)]
twist_sequence = [3, 7, 1, 9, 4, 8, 2, 6, 5, 10]

# Unused transformations (distractors)
entropy_probe = compute_entropy(signal_a)
filtered_seq = transform_sequence(twist_sequence, 3)
window_analysis = shift_window(signal_b, 4)

# Key index determined via modular arithmetic
pivot_index = (len(twist_sequence) * 17) % 11

# Critical execution point
phase_output = process_phase(twist_sequence, pivot_index)

# Additional red herring variables
diagnostic_flag = False
for i in range(5):
    diagnostic_flag = not diagnostic_flag

# Print only the target result
print(f"Target result: {phase_output}")