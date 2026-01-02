from collections import defaultdict
import math

def analyze_pattern(sequence):
    freq = defaultdict(int)
    for item in sequence:
        freq[item] += 1
    return dict(freq)

def validate_checksum(record):
    # Irrelevant validation not used in final logic
    checksum = 0
    for char in record:
        checksum += ord(char) % 7
    return checksum % 3 == 0

def transform_data(entries):
    transformed = []
    offset = len(entries) // 2
    for i, val in enumerate(entries):
        if i % 2 == 0:
            transformed.append(val ** 2 - offset)
        else:
            transformed.append(int(math.sqrt(abs(val) + 1)) + offset)
    return transformed

def compute_entropy(values):
    # Distractor function: calculated but not used
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 4)

def filter_outliers(nums, limit=3):
    mean_val = sum(nums) / len(nums)
    std_dev = (sum((x - mean_val) ** 2 for x in nums) / len(nums)) ** 0.5
    return [x for x in nums if abs(x - mean_val) <= limit * std_dev]

def process_metrics(raw_data, config):
    stage_one = transform_data(raw_data)
    
    # Semi-relevant processing
    filtered = filter_outliers(stage_one, config['sensitivity'])
    
    # Key computation path
    adjusted = [x + config['bias'] for x in filtered]
    
    # Use list comprehension with conditional logic
    scaled = [x * 1.5 for x in adjusted if x > 0]
    
    # Additional distraction: unused intermediate
    stats_summary = analyze_pattern([int(x % 10) for x in scaled])
    
    # Core logic determining final result
    base_score = sum(scaled)
    penalty = len([x for x in raw_data if x < 0]) * 2.5
    bonus = int(math.log2(len(raw_data) + 1)) * config['multiplier']
    
    final_score = int(base_score - penalty + bonus)
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Simulate input data
user_inputs = [3, -1, 4, 1, -5, 9, 2, 6]
detection_thresholds = {
    'sensitivity': 2,
    'bias': 4,
    'multiplier': 3
}

# Misleading pre-processing (dead-end)
dummy_copy = user_inputs.copy()
dummy_copy.reverse()
checksum_valid = validate_checksum("trace_2048")
entropy_value = compute_entropy(user_inputs)

# Main execution point
final_score = process_metrics(user_inputs, detection_thresholds)