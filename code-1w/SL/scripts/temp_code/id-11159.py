def analyze_text_patterns(text_data):
    char_freq = {}
    for c in text_data:
        char_freq[c] = char_freq.get(c, 0) + 1
    unique_chars = len(char_freq)
    total_chars = len(text_data)
    redundancy_factor = (total_chars - unique_chars) / total_chars if total_chars > 0 else 0
    return redundancy_factor


def compute_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * log2(p)
    return entropy

# Irrelevant helper function (dead code path)
def unused_similarity_score(seq1, seq2):
    set1, set2 = set(seq1), set(seq2)
    return len(set1 & set2) / len(set1 | set2)

# Decoy data structures
decoys = {
    'mask_1': [x**2 for x in range(10)],
    'mask_2': {i: chr(i+97) for i in range(8)},
    'junk_flag': True,
    'temp_result': None
}

# Mock dataset with no impact on final result
temporary_aggregates = [
    {'type': 'A', 'value': 42},
    {'type': 'B', 'value': 17},
    {'type': 'C', 'value': 99}
]

# Real input data
input_stream = "abacabadabacaba"

# Step 1: Compute character redundancy (used later)
redundancy = analyze_text_patterns(input_stream)

# Step 2: Generate frequency map again (redundant but obscures focus)
freq_map = {}
for ch in input_stream:
    freq_map[ch] = freq_map.get(ch, 0) + 1

distinct_count = len(freq_map)

# Step 3: Build metric components
raw_counts = list(freq_map.values())
entropy_metric = compute_entropy(raw_counts)
symbol_density = distinct_count / len(input_stream) if input_stream else 0

# Step 4: Simulate multi-layer processing using lambda and dict ops
transform = lambda x, w: round(x * w, 3)
weights = {'entropy': 3.5, 'density': 2.0, 'redundancy': 1.8}

processed_metrics = {
    'entropy': transform(entropy_metric, weights['entropy']),
    'density': transform(symbol_density, weights['density']),
    'redundancy': transform(redundancy, weights['redundancy'])
}

# Step 5: Add irrelevant transformations
_ = [transform(x, 0.5) for x in raw_counts if x % 2 == 0]  # dead computation

# Step 6: Create misleading conditional block
if len(decoys['mask_1']) > 5 and decoys['junk_flag']:
    decoys['temp_result'] = "intermediate_false_positive"
    temp_value = sum([len(v) if isinstance(v, str) else 0 for v in decoys.values()])  # red herring

# Step 7: Benchmark reference (fixed)
benchmark = [0.85, 0.72, 0.63]

# Step 8: Define evaluation logic
metrics = [processed_metrics['entropy'], processed_metrics['density'], processed_metrics['redundancy']]

# Step 9: Core comparison logic using set operations (distraction)
available_keys = set(processed_metrics.keys())
expected_keys = {'entropy', 'density', 'redundancy'}
valid_profile = available_keys >= expected_keys  # always true

# Step 10: Actual performance evaluator
def evaluate_performance(mets, bench):
    if not mets or len(mets) != len(bench):
        return -1
    score = 0.0
    for i in range(len(mets)):
        deviation = abs(mets[i] - bench[i])
        contribution = 1 / (1 + deviation)  # higher similarity = higher contribution
        score += contribution
    # Final transformation
    return round(score * 100, 4)

# Step 11: Compute final score
final_score = evaluate_performance(metrics, benchmark)

# Step 12: Print result
print(f"Result: {final_score}")