import math

# Simulated sensor fusion system for environmental monitoring
def acquire_raw_data():
    return [144, 25, 73, 9, 169, 4, 58, 36]

def filter_outliers(data, threshold=50):
    # Irrelevant filtering (not used in final computation path)
    return [x for x in data if x <= threshold]

def transform_basis(x):
    return int(math.sqrt(x)) if math.sqrt(x).is_integer() else x // 2

def decode_frame(frame):
    # Complex but partially irrelevant transformation chain
    shifted = [(val >> 2) + (val << 1) & 15 for val in frame]
    mapped = list(map(lambda x: (x * 3) % 17, shifted))
    return [mapped[i] for i in range(len(mapped)) if i % 2 == 0]

# Extraneous helper with dead logic
def validate_checksum(arr):
    checksum = sum(arr) % 11
    return checksum == 7

def generate_reference_map(base_values):
    # Distractor: builds unused reference grid
    ref_map = {}
    for i, v in enumerate(base_values):
        ref_map[f'node_{i}'] = {
            'raw': v,
            'phase': (v % 7) * 1.5,
            'flagged': v & 1 == 1
        }
    return ref_map  # Never used

def accumulate_momenta(values):
    # Real computation begins here
    momenta = []
    for v in values:
        if v > 10:
            momenta.append(v ** 0.5)
    return momenta

def compute_entropy(seq):
    total = sum(seq)
    entropy = 0.0
    for x in seq:
        if x > 0 and total > 0:
            p = x / total
            entropy -= p * math.log(p) if p > 0 else 0
    return round(entropy, 6)

def integrate_levels(moments):
    level_stack = []
    for m in moments:
        if len(level_stack) == 0:
            level_stack.append(m)
        elif m > level_stack[-1]:
            level_stack.append(m * 0.9)
        else:
            level_stack.append(level_stack[-1] * 1.1)
    return [round(x, 3) for x in level_stack]

def assess_coherence(levels):
    coherence_score = 0
    for i in range(1, len(levels)):
        diff = abs(levels[i] - levels[i-1])
        coherence_score += 1 if diff < 1.0 else 0
    return coherence_score

def finalize_diagnostic(score, size, base):
    # Final mapping using composite logic
    adjustment = (base // 10) & 7
    return (score * size) + adjustment - (base % 5)

# Key data flow pipeline
raw_signal = acquire_raw_data()

# Irrelevant branch: dead code path
if len(raw_signal) > 10:
    sanitized = filter_outliers(raw_signal)
elif raw_signal[0] < 100:
    sanitized = [x for x in raw_signal if x % 2 == 0]
else:
    sanitized = raw_signal[:]  # This executes, but only partial use later

# Apply real transformation
processed_candidates = [transform_basis(x) for x in raw_signal]

# Decoy processing chain
encoded_frame = decode_frame(processed_candidates)
_ = generate_reference_map(encoded_frame)  # Unused result
valid = validate_checksum(encoded_frame)  # Computed but not used

# Core analysis starts here — actual signal path
filtered_active = [x for x in processed_candidates if x > 10]
momenta = accumulate_momenta(filtered_active)
entropy_metric = compute_entropy(momenta)
integrated_levels = integrate_levels(momenta)
coherence_index = assess_coherence(integrated_levels)

# Secondary diagnostic from entropy
primary_size = len(integrated_levels)
base_anchor = processed_candidates[0]  # 12, since sqrt(144)=12

# Critical statement
final_diagnostic = finalize_diagnostic(coherence_index, primary_size, base_anchor)

print(f"Result: {final_diagnostic}")