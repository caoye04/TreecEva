import math

# Simulated sensor data processing with diagnostic analysis
def preprocess_segment(segment, factor):
    return [x * factor for x in segment if x > 0]

def compute_entropy(values):
    total = 0
    for v in values:
        if v > 0:
            total += v * math.log(v)
    return -total if total != 0 else 0.0

def shift_window(data, offset):
    return data[offset:] + data[:offset]

def evaluate_peak(sequence):
    peak = max(sequence)
    avg = sum(sequence) / len(sequence)
    return peak - avg

# Irrelevant helper - dead code path (never called)
def deprecated_filter(arr):
    return [x for x in arr if x % 2 == 1]

# Unused transformation function
def mirror_array(arr):
    return arr + arr[::-1]

# Misleading intermediate diagnostic (not used in final result)
def false_diagnostic(signal):
    temp_score = 0
    for i in range(len(signal)):
        if signal[i] > 50:
            temp_score += 1
    temp_score *= 3.7
    return int(temp_score // 2)

# Core logic: pattern analysis with slicing and mapping
def extract_features(raw_data, window_size=4):
    features = []
    for i in range(0, len(raw_data) - window_size + 1, 2):
        window = raw_data[i:i + window_size]
        smoothed = [sum(window[j:j+2]) / 2 for j in range(0, len(window), 2)]
        entropy = compute_entropy(smoothed)
        features.append(round(entropy, 3))
    return features

def generate_threshold_map(levels):
    # Creates a dictionary of thresholds by severity level
    return {lvl: 10 * (lvl ** 1.5) for lvl in levels}

# Signal analyzer using multiple concepts
def analyze_signal(buffer, thresh_map):
    # Step 1: Preprocess buffer with amplification
    amplified = preprocess_segment(buffer, 1.2)
    
    # Step 2: Extract time-series features using sliding windows
    feature_vector = extract_features(amplified)
    
    # Step 3: Apply circular shift (bitwise-inspired but on data)
    shifted = shift_window(feature_vector, 2)
    
    # Step 4: Calculate deviation from expected entropy baseline
    baseline = sum(shifted) / len(shifted)
    deviations = [abs(x - baseline) for x in shifted]
    
    # Step 5: Use slicing to isolate critical anomalies
    critical_slice = deviations[1:4]  # Middle section only
    
    # Step 6: Map deviations to severity levels
    levels = []
    for d in critical_slice:
        assigned = None
        for level, thresh in sorted(thresh_map.items()):
            if d >= thresh:
                assigned = level
        levels.append(assigned if assigned is not None else 0)
    
    # Step 7: Aggregate final score
    aggregate = 0
    for i, lev in enumerate(levels):
        if lev > 0:
            aggregate += lev * (i + 1) * 100
    
    # Step 8: Apply final adjustment based on pattern symmetry
    rev_sum = sum(critical_slice)
    forward_sum = sum(critical_slice[::-1])
    if abs(rev_sum - forward_sum) < 0.001:
        aggregate -= 50
    
    # Final diagnostic value
    return aggregate

# --- Simulation Setup ---

# Simulated sensor readings (e.g., neural activity patterns)
pattern_buffer = [12, 45, 67, 23, 89, 34, 78, 56]

# Decoy data structures (distractors)
signal_log = {'entry_1': [12, 45], 'entry_2': [67, 23]}
diagnostic_cache = {(1,2): 0.5, (3,4): 0.9}

# Threshold configuration by severity (1-5 scale)
threshold_config = generate_threshold_map([1, 2, 3, 4, 5])

# Spurious computation on decoy variables
if len(signal_log) > 2:
    cached_value = diagnostic_cache.get((1,2), 0) * 1000
else:
    cached_value = 0

# Unused slicing operation (red herring)
fragment = pattern_buffer[::2]  # every second element

# Misleading intermediate call (no effect on output)
phantom_score = false_diagnostic(pattern_buffer)

# Main execution path
processed_main = preprocess_segment(pattern_buffer, 1)
feature_set = extract_features(processed_main)

# Key statement
final_diagnostic = analyze_signal(pattern_buffer, threshold_config)

# Output the target result
print(f"Result: {final_diagnostic}")