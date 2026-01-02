from collections import defaultdict, Counter
import itertools

# Simulated sensor data preprocessing pipeline
def preprocess_sensor_readings(raw):    filtered = [x for x in raw if abs(x - 50) < 25]    normalized = [(x - 30) * 1.8 for x in filtered]    return [round(n) for n in normalized]

def generate_checksum(sequence):    checksum = 0    for i, val in enumerate(sequence):        checksum ^= (val + i) % 256    return checksum

def evaluate_thresholds(data):    stats = defaultdict(int)    for d in data:        if d > 60:            stats['high'] += 1        elif d > 40:            stats['medium'] += 1        else:            stats['low'] += 1    return dict(stats)

def compute_entropy(arr):    if len(arr) == 0:        return 0.0    counter = Counter(arr)    total = len(arr)    entropy = 0.0    for count in counter.values():        p = count / total        if p > 0:            entropy -= p * __import__('math').log2(p)    return round(entropy, 6)

def transform_sequence(seq):    # Irrelevant transformation chain    temp_a = [x * 2 + 1 for x in seq if x % 2 == 0]    temp_b = [y - 3 for y in temp_a if y > 10]    shifted = list(itertools.accumulate(temp_b, lambda a, b: a + (b % 7)))    # Decoy function call    _ = evaluate_thresholds(shifted)    # Actual relevant output    return [s % 100 for s in shifted]

def analyze_pattern(dataset):    # Misleading preliminary analysis    summary_stats = evaluate_thresholds(dataset)    _ = compute_entropy(dataset)  # Red herring computation
    
    # Core logic hidden among distractions    candidate_values = []    for i in range(len(dataset)):        if dataset[i] % 4 == 0 and i % 3 == 2:            candidate_values.append(dataset[i] * 3)
    
    # Dead code path - looks important but unused    alternate_route = False
    backup_result = 0
    if alternate_route:  # Never executed
        backup_result = sum(dataset) // len(dataset)
    
    # Key filtering with non-obvious condition    valid_candidates = [cv for cv in candidate_values if cv > 50]
    
    # Secondary distraction: checksum on unrelated sequence    decoy_sequence = [i**2 % 19 for i in range(1, 10)]
    _ = generate_checksum(decoy_sequence)
    
    # Final computation: sum of valid candidates with modular adjustment    intermediate_sum = sum(valid_candidates)
    final_score = intermediate_sum % 97321
    
    # Critical assignment
    final_diagnostic = final_score + 100
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Initial irrelevant setup
    base_signal = list(range(25, 76))
    calibration_offset = 7
    adjusted_signal = [x + calibration_offset for x in base_signal]
    
    # Real input generation
    raw_input = [x * 2 for x in adjusted_signal if x % 3 != 0]
    processed = preprocess_sensor_readings(raw_input)
    
    # Apply transformations with decoys
    transformed_data = transform_sequence(processed)
    
    # Additional red herring: unused statistical analysis
    _ = compute_entropy(transformed_data)
    _ = generate_checksum(transformed_data[:10])
    
    # Key statement
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Output result
    print(f"Result: {final_diagnostic}")