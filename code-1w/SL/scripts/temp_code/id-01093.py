from collections import defaultdict, Counter
import math

# Irrelevant utility function (dead code)
def unused_checksum(data):
    return sum(len(str(x)) for x in data) % 7

# Misleading transformation chain
def decoy_transform(sequence):
    temp = [x * 1.5 for x in sequence if x % 2 == 0]
    return [int(y) for y in temp]

# Unused statistical helper
def get_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Core data preprocessing (relevant)
def preprocess_signal(raw_input, mask):
    filtered = []
    for i, val in enumerate(raw_input):
        if i % 3 == 0 and val > 0:
            filtered.append(val ^ mask)  # Bitwise red herring
    return filtered[::-1]  # Reverse slicing

# Data enrichment with distractor logic
def augment_dataset(base, context):
    result = []
    lookup = defaultdict(int)
    for i, b in enumerate(base):
        lookup[b] += 1
        offset = context[i % len(context)]
        computed = (b + offset) * 2
        if computed > 50:  # Dead branch due to data range
            computed //= 3
        result.append(computed)
    # Irrelevant side computation
    magnitude = sum(lookup.values()) * 0.5
    return result

# Real transformation used in execution
def transform_sequence(elements):
    shifted = [e << 1 for e in elements]  # Left bit shift
    modified = [s + 5 for s in shifted]
    return modified[1:-1]  # Slicing out first and last

# Core analysis function (relevant)
def analyze_pattern(dataset, reference):
    diff_set = set(dataset) - set(reference)
    intersect = set(dataset) & set(reference)
    
    # Distractor: complex but unused calculation
    anomaly_score = 0
    for d in diff_set:
        if d % 4 == 0:
            anomaly_score += (d // 4) ** 2
    
    # Actual computation path
    base_total = sum(intersect)
    adjustment = len(diff_set) * 3
    if len(intersect) > 4:
        adjustment += 8
    else:
        adjustment -= 2
    
    # Key intermediate result (misleading)
    pseudo_metric = (base_total * adjustment) / (len(dataset) or 1)
    
    # Final relevant logic
    valid_entries = [x for x in dataset if x in reference]
    correction_factor = len(valid_entries) - len(diff_set)
    final_value = base_total + correction_factor
    
    return int(final_value)

# --- Execution Block ---
if __name__ == "__main__":
    # Initial data (real input)
    sensor_readings = [12, 7, 18, 3, 22, 9, 4, 11]
    filter_mask = 5
    
    # Irrelevant dataset
    auxiliary_stream = [17, 23, 8, 14, 6, 19, 1]
    
    # Step 1: Preprocess signal (relevant)
    processed_signal = preprocess_signal(sensor_readings, filter_mask)
    
    # Step 2: Decoy call (unused result)
    fake_output = decoy_transform(auxiliary_stream)
    
    # Step 3: Transform sequence (relevant)
    transformed_data = transform_sequence(processed_signal)
    
    # Step 4: Build baseline (relevant)
    baseline_reference = []
    for i in range(8):
        item = (i * 7) % 25
        if item not in [0, 5, 10]:
            baseline_reference.append(item)
    
    # Step 5: Augment with irrelevant context
    context_vector = [3, 1, 4, 2]
    enriched_data = augment_dataset(transformed_data, context_vector)  # Unused
    
    # Step 6: Analyze pattern (critical execution point)
    final_diagnostic = analyze_pattern(transformed_data, baseline_reference)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")