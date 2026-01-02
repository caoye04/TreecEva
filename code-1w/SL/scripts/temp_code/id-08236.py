import math

# Simulated sensor data processing with diagnostic analysis
def collect_sensor_readings():
    raw_readings = [127, 255, 98, 64, 201, 150, 73]
    scale_factor = 0.76
    calibrated = [r * scale_factor for r in raw_readings]
    return calibrated

# Irrelevant helper: computes entropy (not used in final path)
def compute_entropy(data):
    total = sum(data)
    probabilities = [d / total for d in data]
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return entropy

# Distraction function: operates on strings, never called
def decode_signature(sig):
    reversed_sig = ''.join(reversed(sig))
    return reversed_sig.encode('utf-8').hex()

# Core transformation pipeline
def transform_signal(seq):
    shifted = [int(x) & 127 for x in seq]  # bitmask to simulate noise filtering
    adjusted = [x - 10 for x in shifted]
    return adjusted

# Set-based anomaly detection (uses set operations)
def detect_anomalies(values):
    base_set = set(range(50, 100))
    input_set = set(values)
    anomalies = input_set - base_set
    return len(anomalies)

# Data enrichment with red herring fields
def enrich_dataset(data):
    enriched = []
    for val in data:
        entry = {
            'raw': val,
            'squared': val ** 2,
            'is_critical': val > 100,
            'checksum': (val * 3) ^ 255,  # bit manipulation distraction
            'category': 'LEVEL_2'
        }
        enriched.append(entry)
    return enriched

# Main analysis logic
def analyze_sequence(dataset):
    # Extract numeric values from enriched entries
    numerics = [entry['raw'] for entry in dataset]
    
    # Compute multiple distractor metrics
    avg_val = sum(numerics) / len(numerics)
    squared_sum = sum(entry['squared'] for entry in dataset)
    critical_count = sum(1 for e in dataset if e['is_critical'])
    
    # Real computation path starts here
    filtered = [n for n in numerics if n > 30]
    
    # Apply mathematical transformations
    processed = []
    for num in filtered:
        temp = num
        if num % 2 == 0:
            temp = int(math.sqrt(num))
        else:
            temp = int(math.log(num + 10) * 3)
        processed.append(temp)
    
    # Use set operation to remove duplicates and intersect with valid range
    unique_vals = set(processed)
    valid_range = set(range(0, 25))
    pruned = list(unique_vals & valid_range)
    
    # Final calculation
    cumulative = 0
    for i, v in enumerate(pruned):
        cumulative += v * (i + 1)  # weighted sum by position
    
    # Key assignment - this is the target result
    final_diagnostic = cumulative + 500
    
    # Dead code path: unreachable under normal execution
    if False:
        backup = sum(pruned) * 2
        final_diagnostic = backup
    
    return final_diagnostic

# Orchestration with misleading intermediate steps
if __name__ == '__main__':
    # Step 1: Collect raw data
    readings = collect_sensor_readings()
    
    # Step 2: Transform signal (relevant)
    transformed_data = transform_signal(readings)
    
    # Step 3: Enrich data (partially relevant, adds required 'raw' field)
    enriched_data = enrich_dataset(transformed_data)
    
    # Step 4: Compute irrelevant diagnostics
    _ = compute_entropy(transformed_data[:4])
    _ = detect_anomalies(transformed_data)
    
    # Step 5: Perform final analysis - key statement
    final_diagnostic = analyze_sequence(enriched_data)
    
    # Output result
    print(f"Target result: {final_diagnostic}")