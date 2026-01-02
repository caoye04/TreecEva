def analyze_readings(readings):
    cumulative = 0
    trend_flags = []
    for i, val in enumerate(readings):
        if i == 0:
            prev = val
            continue
        diff = val - prev
        trend_flags.append(1 if diff > 0 else (-1 if diff < 0 else 0))
        cumulative += abs(diff)
        prev = val
    return cumulative, trend_flags

# Irrelevant auxiliary function (decoy)
def calculate_entropy(data):
    from math import log2
    freq = {}
    total = len(data)
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

# Unused transformation path
def transform_signal(signal):
    transformed = []
    phase = 0
    for s in signal:
        transformed.append(s * (phase % 3 + 1))
        phase += 1
    return transformed

# Core processing function
def process_metrics(data, limits):
    baseline = sum(data[:5]) // 5 if len(data) >= 5 else data[0]
    adjusted_values = [((x + baseline) // 2) for x in data if x % 2 == 1]
    
    # Distractor: complex but unused bitwise cascade
    decoy_state = 0b101010
    for x in data:
        decoy_state ^= (x << 2) & 0b111111
        decoy_state |= (x ^ 5)
    decoy_state = (decoy_state >> 1) ^ 0b1100
    
    # Real logic begins: filtering and aggregation
    valid_entries = []
    for idx, value in enumerate(data):
        if idx % 2 == 1:  # Only odd indices
            capped = min(value, limits['upper'])
            floored = max(capped, limits['lower'])
            valid_entries.append(floored)
    
    # Secondary filter based on conditional expression
    refined = [v if v > baseline else (v + baseline) // 2 for v in valid_entries]
    
    # Tertiary transformation using zip and enumerate together
    shift_offsets = [1, -2, 3, -1, 2]
    aligned = []
    for i, (val, offset) in enumerate(zip(refined, shift_offsets)):
        aligned.append(val + offset)
    
    # Final aggregation with conditional fallback
    aggregate = sum(aligned) if len(aligned) > 3 else sum(refined) * 2
    
    # Misleading intermediate
    diagnostic_score = aggregate * 3 - 127
    
    # Actual answer path
    normalization_factor = len(aligned) or 1
    final_diagnostic = (aggregate + baseline) // normalization_factor
    
    # Dead code branch (never executed due to logic)
    if False and diagnostic_score < 0:
        correction = calculate_entropy(data)
        final_diagnostic = int(final_diagnostic * correction)
    
    return final_diagnostic

# Simulated sensor data (real input)
health_data = [89, 94, 87, 91, 85, 88, 96, 84, 90, 93]

# Threshold configuration
thresholds = {
    'upper': 95,
    'lower': 85
}

# Unused alternate data set
legacy_data = [76, 81, 79, 85, 82, 80, 78]

# Phantom control flag
DEBUG_MODE = False
LOGGING_INTERVAL = 7

# Critical execution point
final_diagnostic = process_metrics(health_data, thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")