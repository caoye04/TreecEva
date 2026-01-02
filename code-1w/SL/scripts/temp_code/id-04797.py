def analyze_pattern(sequence):
    if not sequence:
        return 0
    
    # Irrelevant transformation (distractor)
    normalized = [x / (sum(sequence) + 1e-5) for x in sequence]
    entropy = 0.0
    for p in normalized:
        if p > 0:
            entropy -= p * __import__('math').log(p)
    
    # Semi-relevant preprocessing
    filtered = [x for x in sequence if x > sum(sequence) / len(sequence)]
    trend = sum(1 for i in range(1, len(filtered)) if filtered[i] > filtered[i-1])
    
    return len(filtered) + trend

# Misleading auxiliary function that isn't used in final path
def legacy_compatibility_mode(data):
    checksum = 0
    for item in data:
        if isinstance(item, str):
            checksum += len(item)
        else:
            checksum += item % 100
    return checksum

# Key processing function
def calculate_rating(converged, dataset):
    base = 0
    adjustment = 0
    
    # Simulate state tracking over iterations
    states = []
    for i in range(len(dataset)):
        if i % 3 == 0:
            base += dataset[i] // 2
        elif i % 3 == 1 and dataset[i] > 5:
            base += dataset[i] // 3
        else:
            adjustment += 1
    
    # Nested conditional with early exit
    if converged:
        temp_result = base * 2
        intermediate_flag = False
        
        for val in dataset:
            if val < 0:
                intermediate_flag = True
                break
        
        if intermediate_flag:
            temp_result -= 5
        else:
            temp_result += 3
        
        # Core computation path
        outlier_count = sum(1 for x in dataset if x > 15)
        penalty = outlier_count * 2
        return temp_result - penalty
    else:
        return base - adjustment

# Main execution block
data_points = [8, 12, 3, 9, 16, 5, 11, 2, 7]

# Distractor: unused but plausible variable
checksum_validation = legacy_compatibility_mode(['itemA','itemB','itemC'])

# Distractor: irrelevant string processing
config_tags = ['MODE_X', 'FLAG_Y', 'TEST_Z']
active_modes = [tag.lower() for tag in config_tags if 'X' in tag or 'Z' in tag]

convergence = True

# State-tracking variable with partial relevance
processing_log = []
for idx, val in enumerate(data_points):
    if val % 2 == 0:
        processing_log.append(f"even_{idx}")

pattern_metric = analyze_pattern(data_points)

# Critical assignment
final_score = calculate_rating(convergence, data_points)

print(f"Result: {final_score}")