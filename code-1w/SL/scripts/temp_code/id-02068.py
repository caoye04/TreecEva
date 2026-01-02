from collections import defaultdict, Counter
import math

# Simulated sensor data stream with noise and redundant fields
data_stream = [
    {'id': 1, 'val': 3.5, 'type': 'A', 'seq': 1, 'corrupted': False, 'meta': 'X'},
    {'id': 2, 'val': 2.1, 'type': 'B', 'seq': 2, 'corrupted': True, 'meta': 'Y'},
    {'id': 3, 'val': 3.5, 'type': 'A', 'seq': 3, 'corrupted': False, 'meta': 'X'},
    {'id': 4, 'val': 5.8, 'type': 'C', 'seq': 4, 'corrupted': False, 'meta': 'Z'},
    {'id': 5, 'val': 2.1, 'type': 'B', 'seq': 5, 'corrupted': False, 'meta': 'Y'},
    {'id': 6, 'val': 7.2, 'type': 'A', 'seq': 6, 'corrupted': False, 'meta': 'X'},
    {'id': 7, 'val': 5.8, 'type': 'C', 'seq': 7, 'corrupted': False, 'meta': 'Z'},
    {'id': 8, 'val': 3.5, 'type': 'A', 'seq': 8, 'corrupted': False, 'meta': 'X'},
]

# Irrelevant statistical counters (distractor)
stat_summary = defaultdict(int)
for entry in data_stream:
    stat_summary[entry['type']] += 1
    stat_summary['total'] += 1

# Filter out corrupted entries (actually not used later — red herring)
clean_data = [e for e in data_stream if not e['corrupted']]

# Transform: extract values and types, but also inject irrelevant transformations
types_map = {'A': 1, 'B': 2, 'C': 3}
raw_values = [d['val'] for d in data_stream]
sorted_pairs = sorted([(d['val'], types_map[d['type']]) for d in data_stream], reverse=True)

# Misleading normalization path (unused)
normalized = [v / max(raw_values) for v in raw_values]
scaling_factor = 100
rescaled = [int(n * scaling_factor) for n in normalized]

# Actual relevant transformation: group by value frequency and apply function
duplicates = [item for item, count in Counter(raw_values).items() if count > 1]
transformed_data = []
for val in raw_values:
    freq = Counter(raw_values)[val]
    # Apply non-linear transformation only on repeated values
    if val in duplicates:
        transformed_data.append(math.log(val ** freq + 1))
    else:
        transformed_data.append(math.sqrt(val))

# Decoy analysis function that looks important but isn't called
def legacy_analysis(data):
    acc = 1.0
    for x in data:
        acc *= x + 1
        if acc > 1000:
            acc /= 10
    return acc % 100

# Real analysis function
def analyze_patterns(data, threshold):
    # Count how many transformed values exceed threshold
    count_above = sum(1 for x in data if x > threshold)
    # Use list comprehension with filtering and indexing
    indices = [i for i, x in enumerate(data) if x > threshold]
    # Compute weighted influence score
    influence = 0.0
    for i, val in enumerate(data):
        if i in indices:
            influence += val * (i + 1)
    # Combine metrics
    if count_above == 0:
        return 0.0
    base_score = influence / count_above
    adjustment = math.sin(len(indices) * math.pi / 4)
    final_score = base_score + adjustment
    return round(final_score, 6)

# Secondary decoy logic: graph-like structure (dead code path)
graph_nodes = defaultdict(list)
for i in range(len(data_stream) - 1):
    graph_nodes[data_stream[i]['type']].append(data_stream[i+1]['id'])

traversal_stack = []
visited = set()
for node in graph_nodes:
    if node == 'A':
        traversal_stack.extend(graph_nodes[node])

# Another distraction: bit manipulation on ids (irrelevant)
bit_encoded = 0
for d in data_stream:
    bit_encoded ^= d['id'] << 1
    bit_encoded |= int(d['val'])

# Key threshold derived from non-obvious pattern
key_threshold = sum(math.floor(x) for x in raw_values if x > 3.0) / len(raw_values)

# Critical execution point
final_diagnostic = analyze_patterns(transformed_data, key_threshold)

# Print result
print(f"Target result: {final_diagnostic}")