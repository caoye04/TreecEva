def analyze_pattern(sequence):
    if len(sequence) < 2:
        return 0
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    return sum(diffs) * len(set(diffs))

# Irrelevant helper function (decoy)
def compute_entropy(data):
    from math import log
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

# Unused transformation path (dead code)
def transform_signal(signal):
    shifted = [(x << 1) & 255 for x in signal]
    return [x ^ 17 for x in shifted]

# Real processing chain begins
base_readings = [3, 5, 9, 15, 23]
offsets = [1, 1, 2, 3, 5]

adjusted = []
for i, val in enumerate(base_readings):
    adjusted.append(val + offsets[i])

# Generate signature with distractor logic
signature_pool = {1: 8, 2: 6, 3: 7, 4: 5, 5: 9}
signature_keys = sorted(signature_pool.keys())
health_signature = []
for k in signature_keys:
    health_signature.append(signature_pool[k] + (k % 3))

# Misleading combinatorics block (irrelevant)
count = 0
for i in range(len(health_signature)):
    for j in range(i+1, len(health_signature)):
        if health_signature[i] != health_signature[j]:
            count += 1
combinatorial_index = count * 2  # Dead end

# Core arithmetic manipulation
readings = []
for a, b in zip(adjusted, health_signature):
    readings.append((a * 2) - (b // 2))

# Another red herring: bit analysis (unused result)
binary_fingerprint = 0
for val in readings:
    binary_fingerprint ^= (val & 15) << 2

# Actual key computation
scaling_factor = analyze_pattern(readings[:3])
intermediate_score = 0
for idx, (r, s) in enumerate(zip(readings, health_signature)):
    intermediate_score += r - s + (idx * scaling_factor // 4)

# Final diagnostic depends on set intersection size and scaled score
diagnostic_set_a = set(health_signature)
diagnostic_set_b = set([x % 10 for x in base_readings])
diagnostic_overlap = len(diagnostic_set_a.intersection(diagnostic_set_b))

final_diagnostic = intermediate_score + (diagnostic_overlap * scaling_factor)

# Print required output
print(f"Result: {final_diagnostic}")