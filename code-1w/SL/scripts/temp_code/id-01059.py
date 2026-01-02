import math

# Simulated sensor fusion system for environmental pattern detection
def collect_readings(start, count):
    readings = []
    for i in range(count):
        val = (start * (i + 1)) % 97
        if val % 3 == 0:
            readings.append(val + 2)
        elif val % 5 == 0:
            readings.append(val * 2)
        else:
            readings.append(val)
    return readings

# Irrelevant helper: computes entropy (not used in final result)
def compute_entropy(data):
    freq_map = {}
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    total = len(data)
    entropy = 0
    for freq in freq_map.values():
        p = freq / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Signal normalization with red herring transformations
def normalize_signal(raw_data):
    offset = 5
    normalized = [((x + offset) * 1.5) for x in raw_data]
    # Decoy transformation branch
    if sum(normalized) > 1000:
        normalized = [x / 2 for x in normalized]
    # This next block is dead code - never reached due to prior logic
    for i in range(len(normalized)):
        if i % 7 == 0:  # Practically unreachable given input size
            normalized[i] = math.sin(normalized[i])
    return [int(x) for x in normalized]

# Threshold mapping with set operations (key python feature)
def generate_threshold_map(config_level):
    base_set = {x for x in range(10, 100, 3)}
    adjustment_set = {x for x in range(15, 80, 5)}
    # Real logic: symmetric difference drives thresholds
    core_zones = base_set ^ adjustment_set  # XOR: elements in either but not both
    safety_buffer = {x + 1 for x in adjustment_set if x % 4 == 0}
    # Final map uses intersection to filter relevant zones
    active_thresholds = core_zones & safety_buffer
    return {k: k * config_level for k in sorted(active_thresholds)}

# Data filtering with misleading short-circuiting
def filter_anomalies(signal, limits):
    clean = []
    decoy_count = 0  # Unused counter - distraction
    for x in signal:
        # Complex condition with apparent significance
        if x <= min(limits.keys()) or x >= max(limits.keys()) and any(x % t == 0 for t in limits):
            continue
        # Real filter: only those within dynamic bounds
        valid_range = sum(limits.values()) // len(limits)
        if abs(x - valid_range) < 150:
            clean.append(x)
    return clean

# Core analysis function that combines multiple concepts
def analyze_pattern(sequence, t_map):
    # Initialize working variables
    accumulator = 0
    history = set()
    peak_magnitude = float('-inf')
    
    # Critical processing loop
    for idx, val in enumerate(sequence):
        history.add(val)
        if val in t_map:
            scaled = val * (t_map[val] // 10)
            if scaled > 500:
                accumulator += int(math.sqrt(scaled))
            else:
                accumulator += scaled % 17
        else:
            # Bit manipulation red herring
            transformed = (val << 1) ^ 255
            if transformed > 0:  # Always true
                accumulator -= transformed % 9
        
        # Track peak for decoy logic
        temp_peak = abs(val * math.log(abs(val) + 1))
        if temp_peak > peak_magnitude:
            peak_magnitude = temp_peak
    
    # Final computation using set-derived values
    relevant_keys = set(t_map.keys())
    key_sum = sum(relevant_keys)
    adjustment_factor = len(history) * (key_sum % 23)
    
    # Actual answer derivation
    final_score = accumulator + adjustment_factor
    
    # Dead code: complex averaging logic never used
    if final_score < 0:
        backup = []
        for k, v in t_map.items():
            if k in history:
                backup.append(v / (k + 1))
        final_score = sum(backup) / len(backup) if backup else 0
    
    return int(final_score)

# --- Main Execution with Distractors ---

def main():
    # Generate primary signal data
    raw_sensor_data = collect_readings(13, 42)
    
    # Irrelevant statistical summary
    mean_val = sum(raw_sensor_data) / len(raw_sensor_data)
    variance = sum((x - mean_val) ** 2 for x in raw_sensor_data) / len(raw_sensor_data)
    std_dev = math.sqrt(variance)
    
    # Normalize signal (used in real path)
    signal_sequence = normalize_signal(raw_sensor_data)
    
    # Generate threshold map using set logic (critical path)
    threshold_map = generate_threshold_map(3)
    
    # Filter anomalies (modifies data meaningfully)
    filtered_sequence = filter_anomalies(signal_sequence, threshold_map)
    
    # Analyze the pattern - key statement
    final_diagnostic = analyze_pattern(filtered_sequence, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()