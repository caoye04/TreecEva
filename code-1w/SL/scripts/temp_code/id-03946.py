import math

def preprocess_records(raw_entries):
    cleaned = []
    temp_sum = 0
    outlier_count = 0

    for entry in raw_entries:
        if not isinstance(entry, dict) or 'value' not in entry:
            continue
        val = entry['value']
        if val < 0 or val > 1000:
            outlier_count += 1
            continue
        if val % 2 == 0:
            temp_sum += val * 0.1
        cleaned.append(val)

    adjustment_factor = math.log(temp_sum + 1) if temp_sum > 0 else 0
    adjusted = [x + adjustment_factor for x in cleaned]
    return adjusted, outlier_count

def analyze_distribution(data):
    mean_val = sum(data) / len(data) if data else 0
    variance = sum((x - mean_val) ** 2 for x in data) / len(data) if data else 0
    std_dev = math.sqrt(variance)
    skew = sum(((x - mean_val) / (std_dev + 1e-8)) ** 3 for x in data) / len(data) if data else 0
    
    # Distractor computations
    kurtosis = sum(((x - mean_val) / (std_dev + 1e-8)) ** 4 for x in data)
    noise_floor = abs(skew * kurtosis * 0.01)
    
    return {'mean': mean_val, 'std': std_dev, 'skew': skew, 'noise': noise_floor}

def calculate_final_score(dataset):
    processed, count = preprocess_records(dataset)
    stats = analyze_distribution(processed)
    
    # Irrelevant aggregation
    phantom_total = 0
    for i, val in enumerate(processed):
        if i % 3 == 0:
            phantom_total += math.sin(val)  # Dead-end computation
    
    base_score = stats['mean'] * 0.6
    penalty = stats['skew'] ** 2 * 5
    bonus = math.exp(-stats['noise']) * 2
    
    # Additional misleading logic
    threshold_adjustment = 0
    extremes = [x for x in processed if x > stats['mean'] + 2 * stats['std']]
    if len(extremes) > 3:
        threshold_adjustment -= 10
    
    # Final calculation
    final_score = base_score - penalty + bonus + threshold_adjustment
    
    # More red herring variables
    dummy_weight = len(processed) % 7
    shadow_factor = (phantom_total * dummy_weight) % 1

    return round(final_score, 4)

# Input data
raw_input = [
    {'value': 120}, {'value': 50}, {'value': 200}, {'value': 80},
    {'value': 999}, {'value': 45}, {'value': 73}, {'value': 612},
    {'value': 333}, {'value': 1001}, {'value': 55}, {'value': 77}
]

processed_data, _ = preprocess_records(raw_input)
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")