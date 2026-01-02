import itertools

# Irrelevant helper function (decoy)
def calculate_entropy(values):
    from math import log2
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * log2(p)
    return entropy

# Misleading data transformation chain
def transform_sequence(seq):
    result = []
    for i in range(len(seq)):
        if i % 2 == 0:
            result.append(seq[i] ** 2)
        else:
            result.append(seq[i] + 1)
    return [x for x in result if x % 3 != 0]  # Filtering distraction

# Unused but plausible-looking utility
def validate_checksum(arr):
    checksum = 0
    for val in arr:
        checksum = (checksum + val) % 257
    return checksum == 131

# Core processing function with embedded logic and distractions
def process_metrics(data, config):
    # Irrelevant slicing that looks important
    window = data[3:10][::-1]
    
    # Distractor: unused intermediate calculation
    avg_outlier = sum(window[:4]) / len(window[:4]) if len(window) >= 4 else 0
    threshold = config.get('threshold', 50) * 0.8

    # Real work begins: count significant fluctuations
    fluctuations = 0
    recent_values = data[1:-1]  # Exclude edges
    for i in range(1, len(recent_values)):
        diff = abs(recent_values[i] - recent_values[i-1])
        if diff > threshold:
            fluctuations += 1

    # Bit manipulation red herring
    magic_mask = 0b101010
    masked_fluctuations = fluctuations ^ magic_mask & 0b1111  # Limited impact

    # Dictionary-based state tracking (partially relevant)
    status_log = {}
    for idx, val in enumerate(data):
        key = f"item_{idx % 4}"
        if key not in status_log:
            status_log[key] = 0
        status_log[key] += val % 7

    # Extract only one field from dict that matters
    base_score = status_log.get('item_2', 0) * 13

    # Conditional logic with misleading branch
    adjustment = 0
    if base_score > 40:
        adjustment = 7
    elif len(data) > 5:
        temp = [x for x in data if x > 20]
        if len(temp) > 3:
            adjustment = 5
        else:
            adjustment = -3  # Dead end due to outer condition
    else:
        adjustment = 0

    # Real adjustment is here, hidden in short-circuit logic
    multiplier = config.get('active', False) and config.get('mode', 0) > 0 or False
    scale = (multiplier and 2.5) or 1.8  # Ternary via short-circuit

    # Critical computation path
    raw_metric = base_score + fluctuations * 4 - abs(masked_fluctuations - 10)
    final_score = int(raw_metric * scale + adjustment)

    # Dead code path (never reached due to return above)
    if final_score < 0:
        final_score = 0

    return final_score

# Auxiliary distraction: complex iterator that isn't used
unused_combinations = list(itertools.combinations([1, 2, 3, 4], 3))
filtered_perms = [p for p in itertools.permutations([1, 1, 0], 2) if sum(p) > 1]

# Input setup with plausible decoys
data = [12, 15, 23, 45, 19, 8, 31, 52, 27, 14, 11]
config = {
    'threshold': 25,
    'active': True,
    'mode': 0,  # Important: prevents multiplier activation despite 'active'
    'debug': True,
    'version': '2.1-beta'
}

# Trigger execution
final_score = process_metrics(data, config)
print(f"Target result: {final_score}")