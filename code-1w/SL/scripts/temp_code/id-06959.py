import math

# Simulated sensor data processing with diagnostic analysis
def collect_readings():
    raw_signals = [i * 0.5 + (i % 7) for i in range(15)]
    offset = 3.14159
    calibrated = [round(x - offset + 2.5, 3) for x in raw_signals]
    return calibrated

# Irrelevant auxiliary function - dead code path
def deprecated_filter(data):
    return [x for x in data if x > 1.0]  # Unused in execution

# Data transformation with red herring operations
def transform_signal(data):
    shifted = [(x * 1.1) + 0.05 for x in data]
    inverted = [-1.0 * val for val in shifted if val > 0]  # Partial use, some values filtered
    augmented = shifted + [sum(shifted[:3]), math.sqrt(55), len(shifted)]
    return augmented

# Decoy analysis function with misleading intermediate results
def compute_entropy(arr):
    total = 0.0
    for x in arr:
        if x != 0:
            total += x * math.log(abs(x))
    return round(total, 4)

# Core pattern analyzer with conditional branching and lambda
analyze_pattern = lambda seq, threshold: sum(
    int(x > threshold) * (2 if x < threshold * 2 else 3)
    for x in seq if isinstance(x, (int, float))
)

# Secondary distraction: unused statistical summary
def generate_summary(data_list):
    stats = {}
    stats['peak'] = max(data_list)
    stats['trough'] = min(data_list)
    stats['median_approx'] = sorted(data_list)[len(data_list)//2]
    stats['checksum'] = sum(x * (i+1) for i, x in enumerate(data_list))
    return stats

# Main execution flow
if __name__ == "__main__":
    # Step 1: Collect sensor readings
    sensor_data = collect_readings()  # Produces deterministic list
    
    # Step 2: Apply transformation (including decoy values)
    transformed_data = transform_signal(sensor_data)
    
    # Step 3: Compute irrelevant entropy (distractor)
    entropy_value = compute_entropy(transformed_data)  # Not used later
    
    # Step 4: Generate unused summary report
    report = generate_summary(transformed_data)  # Dead code result
    
    # Step 5: Define key threshold based on obscure rule
    base_ref = math.floor(sum(transformed_data[:5]))
    key_threshold = (base_ref / 4.0) if base_ref % 2 == 0 else (base_ref / 3.5)
    
    # Step 6: Analyze pattern using lambda function (critical step)
    final_diagnostic = analyze_pattern(transformed_data, key_threshold)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")