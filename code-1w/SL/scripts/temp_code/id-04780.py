def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if x > -50 and x < 50]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized


def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq


def compute_entropy(values):
    from math import log2
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * log2(count / total) for count in freq_map.values())
    return round(entropy, 4)


def shift_window(data, size=3):
    windows = []
    for i in range(len(data) - size + 1):
        windows.append(data[i:i+size])
    return windows


def evaluate_symmetry(block):
    return block == block[::-1]


def analyze_pattern(dataset, criteria):
    temp_results = []
    for i, segment in enumerate(dataset):
        if len(segment) % 2 == 0 and sum(segment) in criteria:
            temp_results.append(i * sum(segment))
        else:
            temp_results.append(0)
    
    # Irrelevant transformation
    decoy_analysis = [x * 2 for x in temp_results if x > 10]
    mask = {i for i in range(len(temp_results)) if temp_results[i] > 0}
    masked = [temp_results[i] for i in sorted(mask)]
    
    # Red herring: unused recursive function
    def recursive_weight(acc, depth):
        if depth == 0:
            return acc
        return recursive_weight(acc * 0.9 + 1, depth - 1)
    
    # Distractor: complex but unused calculation
    phantom_score = sum([len(str(x)) * (i+1) for i, x in enumerate(temp_results)])
    
    # Core logic disguised among distractions
    valid_count = sum(1 for x in temp_results if x != 0)
    adjustment_factor = len(criteria.intersection({x % 7 for x in temp_results if x}))
    
    # Final computation buried in noise
    result = valid_count * 137 + adjustment_factor * 19
    
    # Decoy output variables
    debug_trace = {'entries': len(temp_results), 'nonzero': valid_count, 'phantom': phantom_score}
    return result

# Main execution with realistic context: signal pattern diagnosis
raw_sensor_data = list(range(-60, 70, 3))

# Step 1: Signal preprocessing
processed_signal = preprocess_signal(raw_sensor_data)

# Step 2: Generate auxiliary sequence (distractor)
fibonacci_guide = generate_sequence(12)

# Step 3: Compute entropy (seemingly important but unused later)
signal_entropy = compute_entropy(processed_signal)

# Step 4: Windowing operation
windowed_frames = shift_window(processed_signal, 4)

# Step 5: Create threshold set using set operations and slicing
base_thresholds = {x for x in fibonacci_guide if x % 2 == 1}
offset_set = {x + 10 for x in base_thresholds}
threshold_set = base_thresholds.union(offset_set).difference({1, 11})

# Step 6: Transform data using symmetry evaluation (generates list of lists)
transformed_data = []
for frame in windowed_frames:
    if evaluate_symmetry([int(x * 10) % 3 for x in frame]):
        transformed_data.append([int(x * 5) for x in frame])
    else:
        transformed_data.append([int(abs(x) * 2) for x in frame[::2]])  # slicing used

# Step 7: Misleading intermediate analysis
dummy_diagnostics = [analyze_pattern([w], threshold_set) for w in windowed_frames[:3]]

# Step 8: Critical statement
final_diagnostic = analyze_pattern(transformed_data, threshold_set)

print(f"Result: {final_diagnostic}")