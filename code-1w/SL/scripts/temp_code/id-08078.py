import math

# Simulated sensor array diagnostics with embedded logic chain
def collect_readings():
    base_values = [i * 1.5 for i in range(10)]
    offset = sum([v % 2 for v in base_values])  # Irrelevant: counts odd remainders
    readings = [round(math.sin(v) * 100, 2) for v in base_values]
    return readings

# Auxiliary function – looks important but unused in critical path
def deprecated_filter(data, limit=50):
    return [x for x in data if abs(x) > limit]

# Signal conditioning with red herring operations
def preprocess_signal(raw_data):
    filtered = [val for val in raw_data if val != 0]
    normalization_factor = sum(abs(v) for v in filtered) / len(filtered)
    normalized = [round(val / normalization_factor, 3) for val in filtered]

    # Dead code path — visually significant but not used
    if len(normalized) > 10:
        scaled = [v * 1.2 for v in normalized]
    else:
        temp_flags = [1 if v > 0 else -1 for v in normalized]  # Misleading intermediate
        adjusted = [v + 0.1 * temp_flags[i] for i, v in enumerate(normalized)]

    # Actual relevant transformation (obscured)
    categorized = []
    for v in normalized:
        if v < -0.5:
            categorized.append(-2)
        elif v < 0:
            categorized.append(-1)
        elif v < 0.5:
            categorized.append(1)
        else:
            categorized.append(2)
    return categorized

# Threshold mapping with set operations (required feature)
def build_threshold_map(config_level):
    defaults = {"low": -0.6, "mid": 0.0, "high": 0.7}
    overrides = {"debug": True, "low": -0.4, "active": False}
    merged = {**defaults, **overrides}  # Dictionary merge distractor

    # Set operation (required) — appears to affect logic but doesn't alter final path
    valid_keys = set(defaults.keys()) & set(merged.keys()) | {"calibrated"}
    calibrated_thresholds = {k: merged.get(k, 0.0) for k in valid_keys}

    # Real threshold subset used later
    return {"A": calibrated_thresholds["low"], "B": calibrated_thresholds["high"]}

# Core analysis with conditional expressions and nesting
def evaluate_stability(pattern):
    if not pattern:
        return 0

    balance = 0
    transitions = 0
    prev = pattern[0]

    for curr in pattern[1:]:
        if prev < 0 and curr > 0:
            transitions += 1
        balance += curr
        prev = curr

    # Complex conditional expression (required)
    status = "stable" if transitions == 0 else ("volatile" if balance < 0 else "fluctuating")
    
    # Nested decision tree with decoy branches
    if len(pattern) > 15:
        score = balance * 2
    elif transitions > 3:
        adjustment = -5 if status == "volatile" else 5
        score = balance + adjustment
    else:
        # This branch is actually taken
        base_score = sum(p ** 2 for p in pattern if p in {-2, 2})
        penalty = transitions * 3
        score = base_score - penalty  # Key calculation
    return score

# Main diagnostic analyzer
def analyze_pattern(sequence, thresholds):
    # Bit manipulation red herring
    magic_seed = 0b1010 ^ len(sequence) & 0xFF
    checksum = sum([magic_seed ^ i for i in range(3)])  # Fixed result, irrelevant

    # Conditional data transformation
    processed_seq = [
        x * 2 if x >= thresholds["B"] else \
        (x * -1 if x <= thresholds["A"] else x)
        for x in sequence
    ]

    # Another dead-end structure
    history_log = []
    for idx, val in enumerate(processed_seq):
        entry = {
            "index": idx,
            "value": val,
            "flag": "critical" if abs(val) == 4 else "normal"  # Decoy flag
        }
        history_log.append(entry)

    # Final computation — depends only on transformed values and stability
    net_sum = sum(processed_seq)
    stability_index = evaluate_stability(processed_seq)
    
    # Critical fusion point
    final_diagnostic = net_sum + stability_index  # Answer derived here
    return final_diagnostic

# Orchestration block
if __name__ == "__main__":
    raw_signal = collect_readings()
    signal_sequence = preprocess_signal(raw_signal)
    threshold_map = build_threshold_map(config_level=9)
    final_diagnostic = analyze_pattern(signal_sequence, threshold_map)
    print(f"Result: {final_diagnostic}")