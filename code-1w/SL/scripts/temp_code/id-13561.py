import math

# System configuration constants (some are decoys)
MAX_BUFFER_SIZE = 1024
timeout_grace_period = 500
DEBUG_MODE = False
legacy_mode = True
CALIBRATION_OFFSET = 0.05
irrelevant_threshold = 888  # unused parameter

# Signal processing setup
pattern_buffer = [3, 7, 2, 8, 1, 9, 4, 6]
signal_weights = {i: w ** 0.5 for i, w in enumerate([4, 9, 1, 16, 0, 25, 1, 36])}
threshold_map = {'low': 3.5, 'high': 7.0, 'critical': 8.5}

# Misleading auxiliary data structures
auxiliary_cache = {(x, y): x ^ y for x in range(4) for y in range(4)}
decoy_sequence = list(reversed([x * 2 for x in pattern_buffer if x % 2 == 0]))
shadow_copy = pattern_buffer[:]

# Data transformation pipeline
processed_signal = []
for idx, val in enumerate(pattern_buffer):
    weighted_val = val * signal_weights[idx]
    if val > threshold_map['low']:
        processed_signal.append(int(weighted_val + CALIBRATION_OFFSET))
    elif val < threshold_map['high']:
        processed_signal.append(int(weighted_val - CALIBRATION_OFFSET))
    else:
        processed_signal.append(round(weighted_val))

# Secondary analysis with red herring computation
aggregated_metrics = []
for i in range(len(processed_signal)):
    temp_metric = processed_signal[i] + (i * 0.1)
    if i % 3 == 0:
        temp_metric = abs(temp_metric - 1)  # misleading branch
    aggregated_metrics.append(temp_metric)

# Dead code path - never executed due to DEBUG_MODE = False
if DEBUG_MODE and legacy_mode:
    for item in auxiliary_cache:
        print(f'Debug: {item}')  # unreachable

# Real-time filter simulation (distractor loop)
filter_state = 1
for _ in range(3):
    filter_state = (filter_state * 7 + 3) % 10
    if filter_state > 5:
        break

# String-based tag generation (uses string methods as required)
signal_tags = []
category_prefix = "SIG"
for val in pattern_buffer:
    tag = f"{category_prefix}_{val}".replace("3", "X")
    if val % 2 == 0:
        tag += "_EVEN"
    else:
        tag += "_ODD"
    signal_tags.append(tag.upper())

# Tuple unpacking and slicing distraction
tag_summary = tuple(tag[-4:] for tag in signal_tags)
mid_slice = tag_summary[2:6:2]  # uses slicing
index_pairs = list(enumerate(mid_slice))

# Bit manipulation decoy
bit_fiddling = 0
for tag in signal_tags:
    bit_fiddling ^= len(tag) & 7

# Actual critical function with nested logic
def analyze_signal(buffer, thresholds):
    score = 0
    high_count = 0
    cumulative = 0.0

    # Primary evaluation chain
    for i, x in enumerate(buffer):
        if x >= thresholds['high']:
            high_count += 1
            score += 3
        elif x <= thresholds['low']:
            score -= 1
        else:
            score += 1

        # Nested conditional with multiple concepts
        temp = x
        while temp > 1:
            if temp % 2 == 0:
                temp //= 2
            else:
                temp = 3 * temp + 1
            cumulative += math.log(temp + 1) if temp > 0 else 0

    # Use of sets and tuples
    unique_remainders = set(p % 4 for p in buffer)
    bonus_multiplier = len(unique_remainders.intersection({1, 2, 3}))

    # Final calculation - correct path
    final_score = score * bonus_multiplier
    adjustment = int(cumulative / len(buffer)) if buffer else 0
    return final_score + adjustment + high_count

# Irrelevant precomputation (dead end)
potential_outcome = sum(decoy_sequence) // 2

# Key execution point
final_diagnostic = analyze_signal(pattern_buffer, threshold_map)

# Another decoy using zip and enumerate (satisfies language feature requirement but irrelevant)
for i, (a, b) in enumerate(zip(shadow_copy, processed_signal)):
    if a != b:
        potential_outcome -= 1  # never reached due to prior logic

print(f'Result: {final_diagnostic}')