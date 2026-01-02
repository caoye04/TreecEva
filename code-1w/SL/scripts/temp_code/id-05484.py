import math

def preprocess_records(raw_entries):
    filtered = [x for x in raw_entries if x > 0]
    adjusted = list(map(lambda val: val * 1.5 if val < 50 else val * 0.9, filtered))
    return adjusted

def validate_sequence(seq):
    """Irrelevant validation function that isn't used in final computation"""
    return all(a <= b for a, b in zip(seq, seq[1:]))

def calculate_entropy(values):
    """Dead code path - not used but adds distraction"""
    total = sum(values)
    probs = [v / total for v in values]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def calculate_efficiency(dataset):
    size = len(dataset)
    if size == 0:
        return 0
    
    # Core logic begins
    squared_sum = sum(x ** 2 for x in dataset)
    mean_val = sum(dataset) / size
    variance = squared_sum / size - mean_val ** 2
    
    # Intermediate distractor variables
    temp_buffer = [math.sqrt(abs(x)) for x in dataset if x > 10]
    buffer_sum = sum(temp_buffer)  # Used nowhere important
    
    # Simulated system thresholds
    threshold_map = {k: k * 0.85 for k in range(10, 100, 10)}
    adjustment_factor = threshold_map.get(round(mean_val), 1.0)
    
    # Actual efficiency formula
    raw_efficiency = (mean_val * (1 + math.exp(-variance / 100)))
    normalized = raw_efficiency * adjustment_factor
    
    # Red herring conditional with no impact
    status_flags = []
    for i in range(3):
        if normalized > 50 + i * 10:
            status_flags.append(f"high_{i}")
        else:
            status_flags.append(f"low_{i}")
    
    # Final adjustment based on tuple unpacking logic
    base, modifier = divmod(normalized, 7)
    final_modifier = modifier if modifier > 3 else modifier * 1.25
    efficiency_score = base + final_modifier
    
    return efficiency_score

# Main execution flow
raw_data = [12, 45, 67, 23, 89, 34, 56]
distorted_copy = [x * 1.1 for x in raw_data]  # Unused duplicate
checksum = sum(distorted_copy)  # Irrelevant metric

processed_data = preprocess_records(raw_data)

# Extraneous set operations for distraction
unique_values = set(processed_data)
overlap_check = unique_values.intersection({40, 50, 60})

entropy_metric = calculate_entropy(processed_data)  # Computed but unused

# Key statement
efficiency_score = calculate_efficiency(processed_data)

print(f"Result: {efficiency_score}")