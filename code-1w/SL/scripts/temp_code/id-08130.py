import itertools

# System health monitoring simulation with diagnostic interference

def analyze_pattern(seq):
    return sum(a * b for a, b in zip(seq, seq[1:]))

def generate_baseline(n):
    return [i ** 2 % 7 for i in range(n)]

def evaluate_stability(ring_buffer):
    pivot = len(ring_buffer) // 2
    left_score = sum(ring_buffer[:pivot])
    right_score = sum(x ** 0.5 for x in ring_buffer[pivot:] if x > 0)
    return abs(left_score - right_score)

def filter_artifacts(data_stream, threshold=3):
    # Irrelevant filtering function (dead code path)
    return [x for x in data_stream if x % threshold != 0]

def compute_entropy(signal):
    from math import log2
    freq = {}
    for s in signal:
        freq[s] = freq.get(s, 0) + 1
    entropy = 0
    total = len(signal)
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def aggregate_metrics(chain, references):
    # Core computation disguised among distractions
    base = sum(references) * 0.5
    modifier = 0
    
    # Distractor: complex but unused transformation
    transformed = [sum(pair) for pair in itertools.pairwise(references)]
    derived_keys = list(itertools.accumulate(references, lambda a, b: (a + b) % 4))
    temp_grid = [[i + j for j in derived_keys] for i in transformed]
    
    # Relevant logic chain begins
    for i, segment in enumerate(chain):
        if i % 2 == 0:
            # Conditional expression with side relevance
            modifier += analyze_pattern(segment) if evaluate_stability(segment) < 5 else -2
        else:
            # Another valid branch
            modifier += len(segment) // 2
    
    # Red herring: entropy computed but not used in final result
    decoy_entropy = compute_entropy([val for seg in chain for val in seg])
    dummy_offset = int(decoy_entropy * 10)  # Misleading intermediate
    
    # Actual answer depends only on base and controlled modifier
    final_diagnostic = int(base + modifier * 3)
    return final_diagnostic

# Simulated sensor processing chain (data)
processing_chain = [
    [1, 3, 2, 3, 1],
    [4, 1, 5],
    [2, 2, 1, 4, 3],
    [6, 1]
]

# Baseline calibration signals
baseline_signals = generate_baseline(10)

# Dead variables and irrelevant operations (distractors)
corrupted_flag = False
diagnostic_log = {f'step_{i}': 0 for i in range(5)}
buffer_snapshot = processing_chain[0][:]
shadow_copy = [row[:] for row in processing_chain]

# Unused complex structure
lookup_cube = [[[i*j*k for k in range(3)] for j in range(3)] for i in range(3)]

# Key execution point
final_diagnostic = aggregate_metrics(processing_chain, baseline_signals)

# Output result
print(f"Result: {final_diagnostic}")