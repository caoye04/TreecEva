from collections import defaultdict, Counter
import math

def preprocess_signal(raw_samples):
    # Irrelevant preprocessing: applies noise filter that isn't used later
    filtered = [x for x in raw_samples if x > -50]
    stats = defaultdict(int)
    for val in filtered:
        stats['count'] += 1
        stats['sum'] += val
    return [x * 1.05 for x in raw_samples]  # Scaled but not actually needed

def compute_entropy(data):
    # Misleading function: computes entropy but result is ignored
    freqs = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in freqs.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 3)

def generate_sequence(n):
    # Dead code path: generates Fibonacci-like sequence never used
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def extract_features(dataset):
    # Extracts multiple features, only one of which is relevant
    lengths = defaultdict(int)
    max_val = max(dataset)
    min_val = min(dataset)
    lengths['high'] = len([x for x in dataset if x > 30])
    lengths['medium'] = len([x for x in dataset if 10 <= x <= 30])
    lengths['low'] = len([x for x in dataset if x < 10])
    
    # Decoy transformation
    normalized = [round((x - min_val) / (max_val - min_val + 1e-8), 4) for x in dataset]
    
    # Only this part is actually used later
    categorized = []
    for x in dataset:
        if x > 40: categorized.append('A')
        elif x > 25: categorized.append('B')
        elif x > 10: categorized.append('C')
        else: categorized.append('D')
    return categorized

def transform_sequence(pattern_list):
    # Maps string categories to numeric codes; crucial for final step
    mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    return [mapping[p] for p in pattern_list]

def validate_integrity(trace):
    # Distractor function: checks sum but is never called
    return sum(trace) % 7 == 0

def analyze_pattern(values, limit):
    # Core logic: cumulative product under condition
    accumulator = 1
    for v in values:
        if accumulator > limit:
            accumulator -= limit
        accumulator *= v
        # Simulated overflow guard (never triggers due to data)
        if accumulator > 1e6:
            accumulator = 1e6
    return int(accumulator)

# Main execution flow
raw_data_stream = [12, 45, 8, 33, 5, 41, 19, 27, 38, 4]
signal_checksum = sum(x**2 for x in raw_data_stream if x % 2 == 0)  # Red herring

# Step 1: Preprocess (returns scaled version, not used)
calibrated_input = preprocess_signal(raw_data_stream)

# Step 2: Compute entropy (stored but unused)
entropy_metric = compute_entropy(raw_data_stream)

# Step 3: Extract category pattern
categorized_diagnostics = extract_features(raw_data_stream)

# Step 4: Transform to numeric sequence
transformed_data = transform_sequence(categorized_diagnostics)

# Step 5: Set threshold based on decoy logic
estimated_depth = len(generate_sequence(12))  # Returns 12, unused in any real way
threshold = 12

# Step 6: Analyze pattern — THIS IS THE KEY STATEMENT
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Output result
print(f"Result: {final_diagnostic}")