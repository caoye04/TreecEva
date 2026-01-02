def transform_signal(raw_values, scale):
    """Apply non-linear transformation to sensor signal (distractor function)"""
    transformed = []
    accumulator = 0
    for val in raw_values:
        if val > 0:
            accumulator += (val ** 0.5) * scale
        else:
            accumulator -= (abs(val) ** 0.3)
        transformed.append(round(accumulator, 3))
    return transformed


def filter_outliers(data_stream, limit):
    """Remove extreme values beyond limit (partially relevant but not used in final path)"""
    filtered = []
    for reading in data_stream:
        if abs(reading - sum(data_stream) / len(data_stream)) < limit:
            filtered.append(reading)
    return filtered if filtered else data_stream


def compute_checksum(sequence):
    """Calculate XOR checksum of integer sequence (red herring)"""
    checksum = 0
    for item in sequence:
        checksum ^= int(abs(item)) % 256
    return checksum


def generate_triplets(count):
    """Produce Pythagorean triplets (irrelevant computation)"""
    triplets = []
    for m in range(2, count + 2):
        for n in range(1, m):
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            triplets.append((a, b, c))
            if len(triplets) >= count:
                return triplets
    return triplets


def recursive_reduce(value, depth):
    """Recursive bit manipulation with decay (decoy recursion)"""
    if depth <= 0 or value < 1:
        return value
    shifted = (value >> 1) ^ (value << 1)
    return recursive_reduce(shifted % 1000, depth - 1)


def integrate_readings(readings):
    """Compute cumulative integral of sensor readings"""
    integral = 0
    steps = len(readings)
    for i in range(steps - 1):
        integral += (readings[i] + readings[i+1]) * 0.5
    return round(integral, 4)


def classify_pattern(seq):
    """Classify sequence pattern using set logic (core relevant function)"""
    evens = {x for x in seq if x % 2 == 0}
    odds = {x for x in seq if x % 2 == 1}
    positives = {x for x in seq if x > 0}
    negatives = {x for x in seq if x < 0}
    
    # Distractor transformations
    offset_evens = {x + 10 for x in evens}
    scaled_odds = {x * 2 for x in odds if x < 50}
    
    symmetry_score = len(odds & {x + 1 for x in evens})
    balance = len(positives) - len(negatives)
    
    # Key intermediate result
    base_value = len(evens | odds) * (symmetry_score + 1)
    
    return base_value, balance > -3


def analyze_readings(dataset, criteria_set):
    """Main analysis using set operations and arithmetic logic"""
    total_weight = 0
    
    # Simulated preprocessing (with red herrings)
    temp_store = []
    debug_flags = [False, True, False]
    
    for idx, record in enumerate(dataset):
        if idx % 3 == 0:
            temp_store.append(record * 1.1)
        
        # Core processing branch
        if len(record) > 2:
            first_moment = sum(record) / len(record)
            second_moment = sum(x*x for x in record) / len(record)
            variance = second_moment - (first_moment ** 2)
            
            # Critical set construction
            record_set = {int(x) for x in record}
            intersection_with_threshold = record_set & criteria_set
            
            contribution = len(intersection_with_threshold) * variance
            total_weight += contribution
    
    # Secondary validation path (dead code - never executed due to prior condition)
    if len(temp_store) > 100:
        avg_temp = sum(temp_store) / len(temp_store)
        total_weight += avg_temp // 10

    # Final classification using helper function
    pattern_value, meets_condition = classify_pattern([int(total_weight), 42, 88, -5, 7])
    
    # Misleading floating point adjustment
    adjustment = (total_weight * 0.001) ** 2
    adjusted_weight = total_weight - adjustment
    
    # Final decision logic (key statement)
    if meets_condition and adjusted_weight > 50:
        final_score = pattern_value * 7 + int(adjusted_weight)
    else:
        final_score = pattern_value - int(adjusted_weight)
    
    return int(final_score)

# --- Main Execution ---
if __name__ == '__main__':
    # Sensor input simulation (real data source)
    raw_sensor_data = [
        [1.2, 3.4, 5.6, 7.8],
        [2.1, 4.3, 6.5],
        [8.0, 9.2, 10.1, 11.3, 12.5],
        [13.4, 14.6],
        [15.7, 16.8, 17.9, 18.0, 19.1, 20.2]
    ]

    # Irrelevant constants (distractors)
    CALIBRATION_FACTOR = 0.987
    MAX_ITERATIONS = 500
    TIMEOUT_DELAY = 15.6
    BUFFER_SIZE = 2048
    
    # Threshold configuration (used in main logic)
    threshold_set = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    
    # Unused data structures (misdirection)
    legacy_mappings = {'A': 1, 'B': 4, 'C': 9}
    deprecated_list = [x**3 for x in range(1, 8)]
    
    # Signal transformation (distractor pipeline)
    transformed_signal = transform_signal([1.1, -2.2, 3.3, -4.4, 5.5], 1.5)
    
    # Outlier filtering (called but result unused)
    filtered_data = filter_outliers([1, 2, 3, 100, 5, 6], 10)
    
    # Checksum calculation (red herring)
    chk = compute_checksum([7, 14, 21, 28, 35])
    
    # Generate mathematical artifacts (irrelevant)
    triples = generate_triplets(3)
    
    # Recursive operation (unused)
    tail_result = recursive_reduce(123, 5)
    
    # Data integration (core preprocessing)
    processed_deltas = []
    for series in raw_sensor_data:
        integral_value = integrate_readings(series)
        processed_deltas.append([integral_value, integral_value + 1.1, integral_value * 0.9])
    
    # Final diagnostic assessment (key statement)
    final_diagnostic = analyze_readings(processed_deltas, threshold_set)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")