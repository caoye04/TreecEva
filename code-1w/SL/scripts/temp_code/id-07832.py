import math

# Simulated sensor data ingestion
raw_signals = ["1011", "1100", "1010", "0111", "1111"]
timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800]
location_grid = [(0, 0), (1, 0), (2, 1), (1, 2), (0, 1)]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_X = 0.987
CALIBRATION_FACTOR_Y = 1.013
BASELINE_OFFSET = -0.05
MAX_SENSORS = 10

# Signal preprocessing
bit_weights = {i: 2 ** i for i in range(4)}

# Misleading transformation chain (dead path)
def legacy_transform(signal):
    reversed_bits = signal[::-1]
    return sum(int(reversed_bits[i]) * bit_weights[i] for i in range(len(reversed_bits)))

# Unused function - red herring
def compute_entropy(data_list):
    from collections import Counter
    counts = Counter(data_list)
    total = len(data_list)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return entropy

# Another decoy function with plausible but unused logic
def validate_checksum(signal_str):
    ones_count = signal_str.count('1')
    return ones_count % 2 == 0

# Real processing begins here
processed_data = []
for raw in raw_signals:
    # Convert binary string to numeric value (MSB first)
    val = sum(int(raw[i]) * (2 ** (3 - i)) for i in range(4))
    processed_data.append(val)

# Distractor list comprehension with side effect-free computation
extended_diagnostics = [x * x + 2 * x + 1 for x in processed_data if x > 5]
decoy_aggregate = sum([x for x in extended_diagnostics if x % 3 == 0])

# Threshold configuration map (actually used later)
threshold_map = {
    'low': 3,
    'medium': 7,
    'critical': 12
}

# Spurious data structure with redundant info (distraction)
signal_metadata = [
    {"id": i, "raw": raw_signals[i], "zone": loc} 
    for i, loc in enumerate(location_grid)
]

# Fake filter that looks important but isn't used
filtered_by_time = [
    ts for ts in timestamps 
    if ts - timestamps[0] < 30
]

# Core analysis function that uses threshold_map and processed_data
def analyze_signal(data_sequence, thresholds):
    cumulative_score = 0
    history_log = []
    
    for idx, value in enumerate(data_sequence):
        # Bit manipulation red herring
        shifted = value << 1
        inverted = shifted ^ 0b11111
        adjusted = inverted & 0b1111  # Clamp to 4 bits
        
        # Real logic starts here
        if value < thresholds['low']:
            contribution = value * 2
        elif value < thresholds['medium']:
            contribution = value * 3
        elif value <= thresholds['critical']:
            contribution = value * 5
        else:
            contribution = value * 8  # High severity multiplier
        
        # Accumulate with index-based weighting
        weighted_contribution = contribution * (idx + 1)
        cumulative_score += weighted_contribution
        
        # String method distractor
        bin_rep = bin(value)[2:].zfill(4)
        parity_check = bin_rep.count('1') % 2
        history_log.append({'step': idx, 'parity': parity_check})
    
    # Final adjustment using a seemingly complex but deterministic formula
    adjustment_factor = len(history_log) / (thresholds['medium'] - thresholds['low'])
    final_result = int(cumulative_score / adjustment_factor)
    
    # Dead code branch (never reached due to return above)
    if final_result < 0:
        final_result = abs(final_result)
    
    return final_result

# Execution point of interest
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print required result
print(f"Result: {final_diagnostic}")