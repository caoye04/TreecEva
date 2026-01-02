def preprocess_signal(data):
    # Irrelevant preprocessing (dead path)
    if len(data) > 100:
        return [x * 0.9 for x in data]
    return data

# Simulated sensor readings (distraction)
sensor_readings = [2.1, 4.3, 5.6, 7.8, 9.2, 10.1, 12.5, 15.0, 18.3, 20.7]
filtered_data = preprocess_signal(sensor_readings)

# Unused transformation function (decoy)
def transform_basis(vec):
    return [sum(vec[:i+1]) for i in range(len(vec))]

# Core logic begins here — pattern analyzer with red herrings
def generate_sequence(n):
    seq = []
    a, b = 1, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b  # Fibonacci-like distraction
    return seq

# Misleading call to unrelated sequence
temp_seq = generate_sequence(10)

# Actual relevant data structure: binary decision tree simulation
logic_tree = [
    {'node': 1, 'left': 2, 'right': 3, 'value': 0},
    {'node': 2, 'left': 4, 'right': 5, 'value': 1},
    {'node': 3, 'left': 6, 'right': 7, 'value': 0},
    {'node': 4, 'left': None, 'right': None, 'value': 1},
    {'node': 5, 'left': None, 'right': None, 'value': 1},
    {'node': 6, 'left': None, 'right': None, 'value': 0},
    {'node': 7, 'left': None, 'right': None, 'value': 1}
]

# Traverse tree based on bit conditions (real logic)
def traverse_tree(tree, path_bits):
    result_bits = []
    for path in path_bits:
        node_idx = 0
        for direction in path:
            if direction == 1 and tree[node_idx]['right']:
                # Find right child index
                for idx, node in enumerate(tree):
                    if node['node'] == tree[node_idx]['right']:
                        node_idx = idx
                        break
            elif direction == 0 and tree[node_idx]['left']:
                for idx, node in enumerate(tree):
                    if node['node'] == tree[node_idx]['left']:
                        node_idx = idx
                        break
        result_bits.append(tree[node_idx]['value'])
    return result_bits

# Generate control paths using conditional expressions (key python feature)
path_configurations = [
    [0, 1] if i % 2 == 0 else [1, 0] for i in range(4)
]

# Execute traversal
traversal_results = traverse_tree(logic_tree, path_configurations)

# Accumulate results (summation)
accumulated_score = sum(traversal_results)

# Secondary transformation: simulate logic gate cascade (bit manipulation red herring)
shifted_mask = 0
for i in range(len(traversal_results)):
    shifted_mask |= (traversal_results[i] << i)

# Real computation hidden among distractions
logic_sequence = [int(x ** 0.5) for x in [4, 16, 36, 64]]  # yields [2,4,6,8]

threshold = 5

# Core analysis function with conditional expression
def analyze_pattern(seq, thresh):
    base = sum(x for x in seq if x < thresh)  # 2+4 = 6
    bonus = len([x for x in seq if x >= thresh]) * 2  # 2 elements → +4
    penalty = 0
    for i in range(1, len(seq)):
        if seq[i] - seq[i-1] > 2:
            penalty += 1
    # Conditional expression used here (required)
    adjustment = (penalty * -3) if base > bonus else (bonus * 2)
    return base + bonus + adjustment

# Critical execution point
final_diagnostic = analyze_pattern(logic_sequence, threshold)

# Print final result as required
print(f"Target result: {final_diagnostic}")