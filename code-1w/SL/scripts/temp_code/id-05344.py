def preprocess_signal(raw_data):
    filtered = [x for x in raw_data if x > 0]
    normalized = [x / max(filtered) for x in filtered]
    return normalized


def generate_reference(size):
    ref = []
    for i in range(size):
        ref.append((i * i + 3 * i + 7) % 10)
    return ref  # Dead function - never used in computation path

def shift_window(seq, offset):
    return seq[offset:] + seq[:offset]


def calculate_entropy(data):
    from math import log2
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 6)  # Distractor: looks important but unused


def recursive_reduce(n):
    if n <= 1:
        return 1
    return n - recursive_reduce(n - 2)


def analyze_pattern(seq, limit):
    temp = 0
    for i in range(len(seq)):
        if i % 2 == 0:
            temp += seq[i] * (i + 1)
        else:
            temp -= seq[i] // 2
    if temp > limit:
        temp = temp ^ 987  # Bitwise XOR red herring
    return abs(temp)  # Actual return used in final answer

# Irrelevant global constants
MAX_BUFFER = 1024
DEBUG_MODE = True
LOG_LEVEL = 'VERBOSE'

# Main execution
raw_input = [-3, -1, 4, 8, 2, 6, -5, 10, 1]
baseline = [1, 0, 1, 2, 3, 1, 2, 2, 0]  # Unused reference data

# Real signal processing chain
processed = preprocess_signal(raw_input)
scaled = [int(x * 10) for x in processed]  # Scale to integers
trimmed = scaled[1:8:2]  # Slice: elements at index 1,3,5,7 → [2,6,1,1]

augmented = []
for val in trimmed:
    augmented.append(val + recursive_reduce(val % 5))

# Inserting decoy logic
snapshot = augmented.copy()
augmented.reverse()  # Reversal has no effect on downstream
augmented.reverse()  # Undo - pure distraction

threshold = len(augmented) * 15

transformed_sequence = []
for idx, num in enumerate(augmented):
    if idx % 2 == 0:
        transformed_sequence.append(num | 3)  # OR with 3
    else:
        transformed_sequence.append(num & 7)  # AND with 7

# Key statement
final_diagnostic = analyze_pattern(transformed_sequence, threshold)

# Print result as required
print(f"Target result: {final_diagnostic}")