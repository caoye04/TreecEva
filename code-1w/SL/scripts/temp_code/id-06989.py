def analyze_pattern(sequence):
    if len(sequence) < 5:
        return False
    peaks = [i for i in range(1, len(sequence)-1) if sequence[i] > sequence[i-1] and sequence[i] > sequence[i+1]]
    return len(peaks) >= 2

# Irrelevant helper function (decoy)
def compute_entropy(data):
    from math import log
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

# Another irrelevant transformation
def mirror_sequence(arr):
    return arr + arr[::-1]

# Core logic disguised among distractions
def calculate_filtration(readings, limits):
    # Distractor: unused intermediate
    normalized = [max(0, min(100, x)) for x in readings]
    
    # Real logic begins: filter valid readings
    valid = [x for x in readings if limits[0] <= x <= limits[1]]
    
    # Distractor: dead code path (never executed due to prior filtering)
    if any(x < 0 for x in readings):
        valid = [x for x in valid if x >= 0]
    
    # Distractor: complex but unused computation
    rolling_avg = []
    window_size = 3
    for i in range(len(normalized) - window_size + 1):
        avg = sum(normalized[i:i+window_size]) / window_size
        rolling_avg.append(avg)
    
    # Distractor: misleading flag
    high_variance = len(rolling_avg) > 0 and max(rolling_avg) - min(rolling_avg) > 15
    
    # Key transformation: frequency analysis
    freq_map = {}
    for val in valid:
        freq_map[val] = freq_map.get(val, 0) + 1
    
    # Use enumerate and zip (required python features)
    indexed = list(enumerate(valid))
    paired = list(zip(valid, valid[1:]))
    
    # Distractor: set operation with no impact
    unique_pairs = set(paired)
    
    # Real scoring logic
    base_score = sum(freq_map.values())
    penalty = 0
    for k, v in freq_map.items():
        if v == 1:
            penalty += k // 10  # small penalty for rare values
    
    # Final score influenced by pattern detection
    if analyze_pattern(valid):
        base_score += 25
    
    result = base_score - penalty
    
    # Dead code branch (misleading)
    if high_variance and len(unique_pairs) > 10:
        result *= 0.9
        
    return int(result)

# Main execution
sensor_readings = [85, 92, 76, 88, 95, 70, 82, 90, 87, 83, 78, 94]
thresholds = (75, 95)

# Distractor variables
entropy_value = compute_entropy([1,2,2,3,3,3,4,4,4,4])
dummy_sequence = mirror_sequence([1,2,3])
shadow_copy = sensor_readings.copy()

# Noise: string processing (required feature)
data_tag = "sensor_log_2024"
formatted = data_tag.upper().replace("_", ":")
segments = formatted.split(":")
label_set = set(segments)  # required set operation

# Critical statement
filtration_score = calculate_filtration(sensor_readings, thresholds)

# Output result as required
print(f"Result: {filtration_score}")