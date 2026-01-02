def preprocess_signal(raw_data):
    filtered = [x for x in raw_data if x > -50 and x < 50]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized


def encode_sequence(seq):
    base_encoding = {char: idx + 1 for idx, char in enumerate('ACGT')}
    return [base_encoding.get(char, 0) for char in seq]


def analyze_pattern(fragment):
    reversed_frag = fragment[::-1]
    palindromic_score = sum(1 for i in range(len(fragment)) if fragment[i] == reversed_frag[i])
    complexity_index = len(set(fragment)) ** 2 / (len(fragment) + 1)
    return palindromic_score, complexity_index

# Irrelevant helper (distractor)
def compute_entropy(data):
    from math import log2
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = -sum((count / total) * log2(count / total) for count in freq.values())
    return round(entropy, 4)

# Unused function (dead code path)
def legacy_transform(x):
    return (x << 2) ^ 0xAAAA

# Misleading intermediate calculation
temp_calibration = sum(i * (i % 7) for i in range(15)) // 3
offset_matrix = [[i * j for j in range(4)] for i in range(4)]

# Main pipeline
raw_input_signal = [-120, -45, 30, 60, 25, -33, 40, 100, -10]
processed = preprocess_signal(raw_input_signal)

nucleotide_seq = "ACGTCGTAGG"
encoded_bases = encode_sequence(nucleotide_seq)

# Character counting and string method usage (required feature)
seq_stats = {
    'length': len(nucleotide_seq),
    'g_count': nucleotide_seq.count('G'),
    'cg_ratio': (nucleotide_seq.count('C') + nucleotide_seq.count('G')) / len(nucleotide_seq),
    'has_motif': 'GT' in nucleotide_seq
}

# Simulate segmented encoding
segments = [encoded_bases[i:i+3] for i in range(0, len(encoded_bases), 3)]
encoded_segments = [sum(segment) * (idx + 1) for idx, segment in enumerate(segments)]

# Bitwise distraction (irrelevant)
magic_key = 0x1F
scrambled = [(val ^ magic_key) & 0xF for val in encoded_segments]

# Control flow with nested conditionals and comparisons
threshold = 6.5
activation_log = []
for val in processed:
    if val > 0:
        if val > threshold * 0.1:
            status = 2
        elif val > threshold * 0.05:
            status = 1
        else:
            status = 0
    else:
        status = -1
    activation_log.append(status)

# Weight assignment with min/max logic
weights = []
for i in range(len(encoded_segments)):
    weight = min(3.0, max(1.0, i * 0.8 + 0.5))
    weights.append(round(weight, 2))

# Core aggregation (key relevant logic)
def aggregate_metrics(values, w):
    adjusted = [v * w[i] for i, v in enumerate(values)]
    base_total = sum(adjusted)
    # Apply conditional bonus using bitwise AND on index pattern
    bonus = sum(adjusted[i] for i in range(len(adjusted)) if i & 1 and adjusted[i] > 4)
    penalty = len([x for x in adjusted if x < 2]) * 1.5
    return int(base_total + bonus - penalty)

# Decoy call (misleading)
decoy_result = aggregate_metrics([1, 1, 1], [0.5, 0.5, 0.5])

# Critical execution point
final_diagnostic = aggregate_metrics(encoded_segments, weights)

# Output result
print(f"Result: {final_diagnostic}")