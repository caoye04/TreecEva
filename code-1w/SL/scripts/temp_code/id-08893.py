def preprocess_signal(raw_readings):
    # Irrelevant transformation (dead path)
    normalized = [x / max(raw_readings) for x in raw_readings]
    filtered = [x for x in raw_readings if x > sum(raw_readings) / len(raw_readings)]
    return [x * 2 + 1 for x in filtered]  # Only this line matters

# Misleading data structure
audit_log = {'entries': 0, 'status': 'pending', 'checksum': None}
def update_log(entry):
    audit_log['entries'] += 1
    audit_log['checksum'] = hash(str(audit_log['entries']))

# Decoy function with no real impact
compute_entropy = lambda data: sum([x * x for x in data]) / len(data) if data else 0

# Core logic disguised among distractors
def transform_sequence(seq, mode='advanced'):
    temp_result = []
    for i, val in enumerate(seq):
        if i % 3 == 0:
            temp_result.append(val ** 2)
        elif i % 3 == 1:
            temp_result.append(val + 5)
        else:
            temp_result.append(abs(val - 10))
    if mode == 'advanced':
        # Real computation path
        shifted = [temp_result[i] - temp_result[i-1] for i in range(1, len(temp_result))]
        return shifted + [sum(temp_result)]
    return temp_result

def analyze_pattern(data, threshold):
    count_valid = 0
    rolling_sum = 0
    pattern_signature = set()
    
    for x in data:
        if x > threshold:
            count_valid += 1
            rolling_sum += x
        # Distractor operation
        if x % 4 == 0:
            pattern_signature.add(x // 4)
    
    # Secondary check with red herring variables
    avg_contribution = rolling_sum / count_valid if count_valid > 0 else 0
    size_factor = len(pattern_signature) * 2
    
    # Final diagnostic combines actual logic and decoy
    result = rolling_sum + size_factor - count_valid
    
    # This print is just to mislead about importance
    debug_info = {'count': count_valid, 'sum': rolling_sum, 'factor': size_factor}
    
    return int(result)

# Initialization with plausible but partially irrelevant data
base_input = [3, 7, 12, 4, 9, 11, 6, 8]
scaled_data = [x * 3 for x in base_input]
processed_batch = preprocess_signal(scaled_data)

# Apply complex transformation
transformed_data = transform_sequence(processed_batch, mode='advanced')

# Introduce unused intermediate calculation (distractor)
entropy_value = compute_entropy(transformed_data)
key_threshold = len(transformed_data) * 2  # Threshold derived from length

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, key_threshold)

# Output result as required
print(f"Result: {final_diagnostic}")