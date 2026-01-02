import math

# Simulated sensor data processing with embedded logic analysis
raw_signals = [0.1, 0.4, 0.9, 1.3, 1.8, 2.0, 2.5, 3.0, 3.2, 3.8]
decoy_accumulator = 0
irrelevant_buffer = []

# Irrelevant transformation chain 1
for x in raw_signals:
    if x > 1.5:
        decoy_accumulator += math.log(x) * 0.3

# Fake filter that looks important but isn't used in final result
def apply_noise_filter(data, level=0.1):
    return [d + level * math.sin(i) for i, d in enumerate(data)]

filtered_data = apply_noise_filter(raw_signals, 0.15)

# Real processing begins: extract binary pattern based on threshold
binary_mask = [1 if s >= 2.0 else 0 for s in raw_signals]

# Decoy statistical summary (not used later)
mean_signal = sum(raw_signals) / len(raw_signals)
std_deviation = (sum((x - mean_signal)**2 for x in raw_signals) / len(raw_signals))**0.5

# Red herring: complex-looking but unused frequency analysis
frequency_map = {}
for i in range(len(raw_signals) - 1):
    delta = round(raw_signals[i+1] - raw_signals[i], 1)
    frequency_map[delta] = frequency_map.get(delta, 0) + 1

# Actual logic sequence derived from binary mask transitions
def detect_transitions(bits):
    transitions = []
    for i in range(len(bits) - 1):
        if bits[i] == 0 and bits[i+1] == 1:
            transitions.append(1)  # rising edge
        elif bits[i] == 1 and bits[i+1] == 0:
            transitions.append(-1)  # falling edge
        else:
            transitions.append(0)
    return transitions

logic_sequence = detect_transitions(binary_mask)

# Unused recursive checksum (dead path)
def recursive_checksum(seq, depth=0):
    if depth >= 3 or len(seq) == 0:
        return 0
    return seq[0] ** 2 + recursive_checksum(seq[1:], depth + 1)

# Distractor: string-based encoding of signals (misleading)
signal_labels = [''.join(['S', str(i), ':', ('HIGH' if b else 'LOW')]) for i, b in enumerate(binary_mask)]
label_lengths = list(map(lambda lbl: len(lbl), signal_labels))
aggregate_length = sum(label_lengths)

# Core diagnostic engine
valid_pairs = set()
for i in range(len(logic_sequence)):
    if logic_sequence[i] == 1:
        for j in range(i + 1, len(logic_sequence)):
            if logic_sequence[j] == -1:
                width = j - i
                valid_pairs.add(width)
                break

# Secondary pattern weight calculation
pattern_weights = []
for idx, val in enumerate(logic_sequence):
    weight = 0
    if val == 1:
        weight = (idx + 1) * 0.5
    elif val == -1:
        weight = -(idx + 1) * 0.3
    else:
        weight = 0.1 * math.cos(idx)
    pattern_weights.append(round(weight, 3))

# Real answer computation hidden among noise
weighted_sum = sum(pattern_weights)
transition_count = sum(1 for x in logic_sequence if x != 0)

# Final analysis function using closure and lambda
analyze_pattern = lambda seq, threshold: (lambda w, c: round(w * threshold) if c > 0 else 0)(weighted_sum, transition_count)

# Key execution point
final_diagnostic = analyze_pattern(logic_sequence, threshold=0.7)

# Output requirement
print(f"Target result: {final_diagnostic}")