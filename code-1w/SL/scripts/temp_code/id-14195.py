def analyze_pattern(seq, limit):
    """Irrelevant helper function for pattern analysis (dead code path)."""
    count = 0
    for i in range(len(seq)):
        if seq[i] > limit:
            count += 1
    return count

thresholds = [0.85, 0.90, 0.75, 0.60]
diagnostic_map = {i: val * 100 for i, val in enumerate(thresholds)}

# Distractor: Unused complex list comprehension with slicing
shadow_scores = [x ** 2 for x in thresholds[1:3] if x < 0.8]

# Real data pipeline begins
raw_signals = [0.88, 0.92, 0.77, 0.65]
filter_mask = [True if x > 0.7 else False for x in raw_signals]

# Apply masking with zip and conditional logic
filtered_data = [sig for sig, mask in zip(raw_signals, filter_mask) if mask]

# Secondary distractor: Bitwise red herring
obfuscation_key = 0b1101
scrambled = [(int(sig * 100) ^ obfuscation_key) & 0xF for sig in filtered_data]

# Irrelevant combinatorics
from math import comb
possible_pairs = sum(comb(i + 1, 2) for i in range(3))  # evaluates to 4, unused

# Core transformation chain
normalized = [round(x * 1.08, 4) for x in filtered_data]  # Boost for calibration

# Destructuring assignment distraction
a, b, *rest = normalized
offset_adjustment = a * 0.1 - b * 0.05

# Conditional expression with enumerate side calculation
bonus_factor = 0
for idx, val in enumerate(normalized):
    bonus_factor += val * 0.1 if idx % 2 == 0 else val * 0.05

# Health scoring logic
health_data = []
for val in normalized:
    if val >= 0.85:
        health_data.append(4)
    elif val >= 0.77:
        health_data.append(3)
    elif val >= 0.70:
        health_data.append(2)
    else:
        health_data.append(1)

# Real processing function
def process_metrics(data, ref_thresholds):
    base_score = sum(data)
    # Complex adjustment using slicing and conditional logic
    adjustment = sum([ref_thresholds[i] * data[i] for i in range(len(data))])
    # Final nonlinear transformation
    final_score = base_score * (1 + adjustment) // 1
    # Another decoy: string-based distraction
    status_log = ''.join(['OK' if d > 2 else 'WARN' for d in data])
    # This line has no effect on output but distracts
    status_log = status_log[::-1]  # reverse string
    return int(final_score)

# Critical execution point
final_diagnostic = process_metrics(health_data, thresholds)

print(f"Result: {final_diagnostic}")