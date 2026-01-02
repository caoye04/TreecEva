from collections import defaultdict, Counter
import math

def preprocess_signal(raw_samples):
    # Irrelevant preprocessing: applies noise filter that isn't used later
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return normalized

def generate_checksum(sequence):
    # Dead function: looks important but never called in critical path
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= int(val * 100) + i
    return checksum

def compute_entropy(data):
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def shift_window(arr, k):
    # Unused helper: part of a decoy algorithm
    return arr[-k:] + arr[:-k]

def transform_sequence(seq, key_offset):
    # Applies transformation but includes red herring operations
    temp_result = []
    cumulative = 0
    for i, val in enumerate(seq):
        adjusted = val + key_offset
        if adjusted % 2 == 0:
            cumulative += adjusted ** 2
        else:
            cumulative -= abs(adjusted)
        temp_result.append(cumulative)
    
    # Distractor: modifies data in a way that seems significant
    inverted = [max(temp_result) - x for x in temp_result]
    smoothed = [sum(inverted[i:i+3]) / 3 for i in range(len(inverted) - 2)] if len(inverted) > 2 else inverted
    
    # Actual relevant output is the sum of smoothed values
    return sum(smoothed)

def analyze_pattern(dataset, limit):
    # Core logic hidden among distractions
    stats = defaultdict(int)
    for item in dataset:
        if isinstance(item, float) and item > limit:
            stats['valid'] += 1
        elif item < 0:
            stats['negative'] += 1
        else:
            stats['other'] += 1
    
    # Misleading intermediate calculation
    dummy_score = (stats['valid'] * 1.5) + (stats['negative'] ** 0.5)
    
    # Critical decision point
    if stats['valid'] >= 3:
        return int(math.floor(dummy_score * 2))
    else:
        return -int(sum(dataset) // 10)

# Main execution with irrelevant setup
raw_input_data = [12, -5, 8, 14, -3, 19, 7, 21]
decoy_labels = ['A', 'B', 'C', 'D']

# Real pipeline starts here
processed_meta = {label: idx for idx, label in enumerate(decoy_labels)}
transformed_data = []
for val in raw_input_data:
    # Complex transformation chain
    temp_val = val * 3 + 2
    temp_val = temp_val ^ 5  # Bitwise red herring
    transformed_data.append(temp_val)

# Add more distraction: unused transformation branch
alt_path = [x for x in transformed_data if x % 4 == 0]
sorted_path = sorted(alt_path, reverse=True)

# Another decoy: string-based distraction using python feature
status_log = "System boot: OK | Data load: FAILED | Retry: SUCCESS"
log_parts = status_log.split('|')
health_flags = [part.strip().endswith('SUCCESS') for part in log_parts]

# Key computation step
entropy_metric = compute_entropy(transformed_data)
threshold = 10

# Final analysis with decisive statement
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Output result as required
print(f"Target result: {final_diagnostic}")