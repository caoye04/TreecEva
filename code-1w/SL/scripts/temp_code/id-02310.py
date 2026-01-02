import math

# Simulated sensor data with noise and redundant readings
data_set = [144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625]

# Irrelevant constants for electromagnetic interference simulation (distractors)
EMI_FACTOR = 0.87
NOISE_FLOOR = 12.4
calibration_offset = sum([EMI_FACTOR * i + NOISE_FLOOR for i in range(5)])  # Unused

# Threshold derived from statistical analysis
threshold = int(sum([math.sqrt(x) for x in data_set]) / len(data_set))  # Average root value

# Secondary dataset - looks important but unused in final calculation
auxiliary_data = [x ** 0.5 for x in data_set if x % 2 == 0]
filtered_aux = list(filter(lambda x: x > threshold * 0.5, auxiliary_data))

# Decoy function that appears relevant but is never called
def analyze_pattern(seq, mode='strict'):
    if mode == 'strict':
        return sum([i * seq[i] for i in range(len(seq)) if i % 3 == 0])
    else:
        return sum([seq[i] ** 2 for i in range(len(seq)) if seq[i] < 20])

# Set operations to validate data integrity (some distraction here)
expected_squares = {i**2 for i in range(12, 26)}
observed_set = set(data_set)
missing_entries = expected_squares - observed_set  # Computed but unused
extra_entries = observed_set - expected_squares  # Also unused

# Core processing function with conditional logic and modular arithmetic
def process_recordings(records, limit):
    valid_entries = []
    checksum = 0
    
    for idx, val in enumerate(records):
        root = int(math.sqrt(val))
        
        # Conditional expression determining validity
        status = 'valid' if root * root == val and val % 10 != 3 else 'invalid'
        
        if status == 'valid' and val > limit:
            # Apply modular transformation
            transformed = (val * 7 + 13) % 1000
            valid_entries.append(transformed)
            
            # Bit manipulation decoy - affects checksum but not result
            temp_flag = (transformed >> 4) ^ (idx & 0xF)
            checksum += temp_flag
    
    # Additional filtering using set intersection (distraction)
    unique_valid = list(set(valid_entries))
    sorted_results = sorted(unique_valid, reverse=True)
    
    # Red herring: entropy-like computation (not used in output)
    entropy_approx = sum([math.log(x) if x > 1 else 0 for x in sorted_results])
    
    return sorted_results

# Another decoy: recursive validation (never executed path)
def validate_hierarchy(arr, depth=0):
    if depth >= 3 or len(arr) == 0:
        return False
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid+1:]
    return (arr[mid] % 7 == 0) or validate_hierarchy(left, depth+1) or validate_hierarchy(right, depth+1)

# Primary scoring logic with multiple abstraction layers
def calculate_final_score(dataset, thresh):
    # Step 1: Filter and transform main data
    processed = process_recordings(dataset, thresh)
    
    # Step 2: Compute weighted accumulation
    accumulator = 0
    for i, v in enumerate(processed):
        weight = 1.0 if i % 2 == 0 else 0.5
        contribution = v * weight
        accumulator += contribution
    
    # Step 3: Apply conditional bonus based on count
    entry_count = len(processed)
    bonus = 50 if entry_count >= 6 else (25 if entry_count >= 4 else 0)
    
    # Step 4: Adjust using modular constraint
    mod_adjustment = (sum(processed) % 17) * 3
    
    # Step 5: Final composition
    raw_score = accumulator + bonus
    final_normalized = raw_score - mod_adjustment
    
    # Misleading intermediate: normalized relative score (unused)
    reference_peak = max(data_set)
    relative_ratio = final_normalized / reference_peak if reference_peak else 0  # Distractor
    
    # Critical assignment
    final_score = int(final_normalized)
    
    return final_score

# Execution point of interest
final_score = calculate_final_score(data_set, threshold)

# Output required format
print(f"Target result: {final_score}")