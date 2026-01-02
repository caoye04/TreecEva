import itertools

def preprocess_data(stream):
    return [x for x in stream if x % 2 == 1]

def shift_cipher(values, key):
    # Irrelevant transformation
    return [(v + key) % 256 for v in values]

def compute_magnitude(vector):
    # Distractor function: looks important but unused in critical path
    return sum(v ** 2 for v in vector) ** 0.5

def detect_spikes(readings, threshold=100):
    # Dead code path — never called
    return [i for i, r in enumerate(readings) if r > threshold]

def evaluate_pattern(seq):
    score = 0
    for i, val in enumerate(seq):
        if i % 2 == 0 and val < 50:
            score += val * 1.5
        elif i % 3 == 0:
            score -= val // 4
    return int(score)

def analyze_subgrid(matrix, size):
    # Extracts top-left subgrid of given size and computes XOR fingerprint
    fingerprint = 0
    for i in range(min(size, len(matrix))):
        for j in range(min(size, len(matrix[i]))):
            fingerprint ^= matrix[i][j]  # Bitwise XOR accumulation
    return fingerprint

def generate_combinations(items):
    # Distractor: uses itertools but not part of main logic
    return list(itertools.combinations(items, 2))

def anomaly_detector(data, depth):
    # Core logic: recursive traversal with pruning
    if depth <= 0 or not data:
        return depth
    total = 0
    for row in data[:depth]:
        if len(row) >= depth:
            total += row[depth - 1] * depth
        else:
            total += sum(row)
    return total + anomaly_detector([r[1:] for r in data], depth - 1)

# Simulated sensor grid readings (real data)
grid = [
    [12, 7, 3, 18],
    [5, 14, 9, 22],
    [8, 1, 11, 4],
    [17, 6, 2, 13]
]

# Irrelevant preprocessing chain
raw_stream = [15, 22, 34, 47, 51, 68, 73, 88, 91]
filtered_stream = preprocess_data(raw_stream)
ciphered_stream = shift_cipher(filtered_stream, 7)
magnitude = compute_magnitude(ciphered_stream)  # Unused result

# Multiple red herring variables
spike_indices = []
baseline_offset = 0.0
aggregate_score = 0

# Real computation begins
subgrid_feature = analyze_subgrid(grid, 3)
pattern_seq = [grid[i][i] for i in range(len(grid))]  # Diagonal elements
aggregate_score += evaluate_pattern(pattern_seq)

# Generate irrelevant combinations
elements = ['A', 'B', 'C', 'D']
pairs = generate_combinations(elements)  # Not used later

# Key statement
final_diagnostic = aggregate_score + anomaly_detector(grid, 3)

print(f"Result: {final_diagnostic}")