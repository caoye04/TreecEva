from itertools import combinations

def preprocess_records(raw_entries):
    # Irrelevant transformation (distractor)
    normalized = [x * 0.95 for x in raw_entries if x > 0]
    filtered = [x for x in normalized if x < 500]
    return filtered

def analyze_pairs(values):
    # Semi-relevant: computes pair products but only max is used
    all_pairs = list(combinations(values, 2))
    pair_products = [a * b for a, b in all_pairs]
    avg_product = sum(pair_products) / len(pair_products) if pair_products else 0
    max_product = max(pair_products) if pair_products else 0
    return max_product, avg_product  # Only max_product is used later

def calculate_final_score(data_chunk):
    temp_offset = sum([x % 7 for x in data_chunk])  # Minor adjustment factor
    base_total = sum(data_chunk)
    
    # Red herring computation
    shadow_sum = 0
    for i in range(len(data_chunk)):
        if i % 3 == 0:
            shadow_sum += data_chunk[i] * 1.5
    
    # Key logic hidden among distractions
    adjustment_factor = len(list(filter(lambda x: x > 100, data_chunk)))
    bonus = 10 if any(x > 400 for x in data_chunk) else 0
    
    intermediate = base_total + adjustment_factor * 5 + bonus
    
    # Use of lambda in non-critical path (distractor)
    scaling_fn = lambda x: x * 1.1 if x < 200 else x * 0.9
    scaled_values = [scaling_fn(val) for val in data_chunk]
    
    # Critical execution point
    final_score = int(intermediate - temp_offset // 2)
    
    return final_score

# Main execution flow
raw_data = [120, 150, 300, 450, 50, 25, 420]
processed_data = preprocess_records(raw_data)

# Extraneous analysis (not affecting final result)
dummy_analysis = analyze_pairs(raw_data)
dummy_analysis = analyze_pairs(processed_data)

# Additional irrelevant variables
timestamp_log = [1690000000 + i*100 for i in range(len(raw_data))]
weight_map = {i: v * 0.1 for i, v in enumerate(raw_data)}

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")