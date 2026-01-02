def preprocess_signal(data_stream, threshold=0.75):
    filtered = [x for x in data_stream if abs(x) > threshold]
    normalized = [round(x / max(filtered), 4) for x in filtered]
    return normalized

signal_input = [-2.3, 0.1, 1.8, -0.9, 3.1, 0.05, -1.4, 2.7]
processed = preprocess_signal(signal_input)

# Irrelevant transformation (distractor)
decoy_stats = {"mean": sum(processed)/len(processed), "range": max(processed)-min(processed)}
summary_text = "Analysis complete: {} values processed".format(len(processed))

# Simulate bit-encoded state flags
state_flags = []
for val in processed:
    flag = 0
    if val > 0.5:
        flag |= 1 << 3
    if abs(val) < 1.0:
        flag |= 1 << 1
    if val == max(processed):
        flag |= 1 << 2
    state_flags.append(flag)

# Misleading entropy calculation (dead path)
temp_entropy = 0
for p in [0.25, 0.5, 0.25]:
    temp_entropy -= p * __import__('math').log2(p) if p > 0 else 0

# Core logic disguised among distractions
logic_core = set()
for i, v in enumerate(state_flags):
    if v & 8:  # Check if high amplitude
        logic_core.add(i % 7)

mask_sequence = []
xor_key = 14
for i in range(8):
    computed = (i ^ xor_key) % 5
    if computed != 0:
        mask_sequence.append(computed * 2)

# Decoy function that's never called
def evaluate_coherence(pattern):
    """Unused function - red herring"""
    return sum(p ** 2 for p in pattern) / len(pattern)

# Unused dictionary operations (distractor)
status_map = {0: 'idle', 1: 'active', 2: 'standby'}
status_counts = {status_map[k]: 0 for k in status_map}

# String-based control flow (irrelevant but plausible)
mode_selector = "priority_high"
if "high" in mode_selector:
    adjustment_factor = 1.5
else:
    adjustment_factor = 0.8

# Real computation buried in noise
def analyze_pattern(indices, masks):
    accumulator = 0
    shift_base = 3
    for idx in indices:
        for m in masks:
            if idx % 2 == 0:
                accumulator += (m ^ idx) >> 1
            else:
                accumulator -= (m + idx) % 4
    return accumulator * shift_base

final_diagnostic = analyze_pattern(logic_core, mask_sequence)
print(f"Result: {final_diagnostic}")