from collections import defaultdict, Counter
import math

# Simulated sensor array preprocessing (distractor: not actually used)
raw_sensors = [127, 255, 64, 192, 31, 158, 93]
noise_floor = sum(raw_sensors) / len(raw_sensors)
adjusted_readings = [x - noise_floor + 10 for x in raw_sensors]

# Irrelevant transformation chain
temp_buffer = []
for val in adjusted_readings:
    if val > 100:
        temp_buffer.append(int(math.sqrt(val) * 3))
    else:
        temp_buffer.append(val // 2)

# Core data structure: water quality sample timeline (relevant)
sample_timeline = [
    {'timestamp': 1623, 'purity': 87, 'turbidity': 3.2, 'ph': 7.1},
    {'timestamp': 1624, 'purity': 91, 'turbidity': 2.8, 'ph': 7.3},
    {'timestamp': 1625, 'purity': 85, 'turbidity': 3.5, 'ph': 6.9},
    {'timestamp': 1626, 'purity': 94, 'turbidity': 2.1, 'ph': 7.4},
    {'timestamp': 1627, 'purity': 88, 'turbidity': 3.0, 'ph': 7.0}
]

# Decoy function - looks important but unused
def analyze_resistivity(data):
    base = 0
    for item in data:
        base ^= int(item['ph'] * 10)
    return base << 2

# Unused statistical helper
def compute_rolling_kurtosis(seq):
    mean_val = sum(seq) / len(seq)
    variance = sum((x - mean_val) ** 2 for x in seq) / len(seq)
    if variance == 0:
        return 0
    kurtosis = sum((x - mean_val) ** 4 for x in seq) / (len(seq) * variance ** 2)
    return kurtosis - 3

# Real processing functions

def segment_data():
    # Extract purity values and apply bitwise smoothing
    purities = [entry['purity'] for entry in sample_timeline]
    smoothed = []
    for i in range(len(purities)):
        left = purities[i-1] if i > 0 else purities[i]
        right = purities[i+1] if i < len(purities)-1 else purities[i]
        # Bitwise averaging using XOR and AND for noise reduction
        avg_raw = (left + purities[i] + right) // 3
        bit_correction = (left ^ right) & 0x0F  # Use lower nibble diff
        corrected = (avg_raw ^ bit_correction) + (bit_correction >> 2)
        smoothed.append(corrected & 0xFF)  # Clamp to byte
    return smoothed


def process_sequence(purity_list):
    # Apply decay-based weighting using integer division
    weights = [max(0, 5 - abs(i - len(purity_list)//2)) for i in range(len(purity_list))]
    weighted_sum = sum(p * w for p, w in zip(purity_list, weights))
    total_weight = sum(weights)
    
    # Add decoy logic with dead branch
    if len(purity_list) > 10:  # Never true
        backup_estimator = math.log(sum(purity_list))
        return int(backup_estimator)
        
    base_estimate = weighted_sum // total_weight if total_weight else 0
    
    # Augment with turbidity cross-reference (irrelevant here, but plausible)
    turbidity_map = defaultdict(lambda: 0)
    for entry in sample_timeline:
        key = entry['purity'] // 10
        turbidity_map[key] += entry['turbidity']
    
    # This looks like it matters but doesn't affect output
    phantom_offset = int(sum(turbidity_map.values()) * 0.7) % 7
    
    return base_estimate - (phantom_offset // 2)  # Minimal impact


def validate_purity(estimation):
    # Critical validation with logical operations and thresholds
    is_accurate = estimation > 80
    is_stable = estimation < 95
    has_consistency = estimation % 2 == 1  # Oddness heuristic
    
    # Short-circuit logic with misleading intermediate
    confidence_factor = 1.0
    if is_accurate and is_stable:
        confidence_factor *= 1.1
    if has_consistency or (estimation > 85):
        confidence_factor *= 1.05
    
    # Final score computation
    raw_score = estimation * confidence_factor
    
    # Red herring: entropy-like calculation (unused)
    test_bits = [estimation >> i & 1 for i in range(8)]
    run_entropy = sum(1 for a, b in zip(test_bits, test_bits[1:]) if a != b)
    
    # Actual return (only raw_score matters)
    return int(round(raw_score))

# Dead code path - unreachable
MAX_ITER = 15
def legacy_calibrate(seq, depth=0):
    if depth >= MAX_ITER:
        return sum(seq) >> 1
    return legacy_calibrate([x >> 1 for x in seq], depth + 1)

# Key execution point
data_chunk = segment_data()
processed_est = process_sequence(data_chunk)
filtration_score = validate_purity(processed_est)

# Distractor print (not the answer)
# print(f"Diagnostics: {analyze_resistivity(sample_timeline)}")

Result: filtration_score