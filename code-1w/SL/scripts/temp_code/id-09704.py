import math

def analyze_pattern(sequence):
    # Irrelevant helper function (dead code path)
    return [x ** 2 for x in sequence if x % 3 == 0]

def validate_input(data):
    if not isinstance(data, list) or len(data) == 0:
        return False
    return all(isinstance(x, (int, float)) for x in data)

def compute_checksum(arr):
    # Distractor computation with modular arithmetic
    checksum = 0
    for i, val in enumerate(arr):
        checksum += (val * (i + 1)) % 7
    return checksum

def transform_values(raw):
    # Real transformation used later
    return [abs(x - 10) if x > 5 else x + 2 for x in raw]

def filter_outliers(values, threshold=3.5):
    # Misleading intermediate processing
    mean_val = sum(values) / len(values)
    filtered = [v for v in values if abs(v - mean_val) < threshold]
    return filtered if len(filtered) > 2 else values

def aggregate_data(snapshot):
    temp_result = []
    for item in snapshot:
        if item < 0:
            temp_result.append(item ** 2)
        elif item == 0:
            temp_result.append(1)
        else:
            temp_result.append(int(math.sqrt(item)) if item >= 1 else item)
    return temp_result

def calculate_entropy(weights):
    # Decoy function: looks important but unused in final logic
    entropy = 0.0
    total = sum(weights)
    for w in weights:
        if w > 0:
            p = w / total
            entropy -= p * math.log(p)
    return round(entropy, 6)

def normalize_vector(vec):
    norm = math.sqrt(sum(x * x for x in vec))
    return [round(x / norm, 6) for x in vec] if norm > 0 else vec

def process_metrics(data, config):
    # Core logic embedded in distractions
    
    # Irrelevant variables
    temp_cache = {}
    debug_log = []
    max_iteration = 10
    
    # Step 1: Transform input data
    transformed = transform_values(data)
    
    # Step 2: Checksum as red herring (not used later)
    integrity_sum = compute_checksum(transformed)
    
    # Step 3: Filter based on statistical threshold (partially affects outcome)
    cleaned = filter_outliers(transformed, threshold=4.0)
    
    # Step 4: Aggregate using conditional logic
    aggregated = aggregate_data(cleaned)
    
    # Step 5: Apply weight scaling (uses config)
    scaled = [a * b for a, b in zip(aggregated, config[:len(aggregated)])]
    
    # Step 6: Normalize vector (but only use sum)
    normalized = normalize_vector(scaled)
    
    # Step 7: String-based flag check (distractor)
    status_flag = "READY"
    if sum(normalized) > 10:
        status_flag = "OVERLOAD"
    
    # Step 8: Final scoring logic
    base_score = sum(normalized)
    penalty = 0
    
    # Additional distraction: early return that won't trigger
    if len(data) > 20:
        return -999  # Dead path
    
    # Actual key logic
    for i, val in enumerate(scaled):
        if val > 5 and i % 2 == 1:
            penalty += 1.5

    final_score = round(base_score - penalty, 6)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data with meaningful structure
    sensor_readings = [12, 3, 7, 0, 9, 11, 2]
    
    # Weight configuration (used in actual logic)
    fusion_weights = [0.8, 1.2, 1.0, 0.5, 1.1, 0.9, 1.3]
    
    # Irrelevant precomputations
    avg_reading = sum(sensor_readings) / len(sensor_readings)
    peak_value = max(sensor_readings)
    reading_labels = [f"R{i}" for i in range(len(sensor_readings))]
    labeled_dict = {k: v for k, v in zip(reading_labels, sensor_readings)}
    
    # Call target function
    final_score = process_metrics(sensor_readings, fusion_weights)
